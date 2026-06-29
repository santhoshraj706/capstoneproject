import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import CarMake, CarModel, CarDealer, DealerReview
from .serializers import CarMakeSerializer, CarModelSerializer, CarDealerSerializer, DealerReviewSerializer, UserSerializer, CarMakeModelSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_car_makes(request):
    makes = CarMake.objects.all()
    serializer = CarMakeSerializer(makes, many=True)
    data = []
    for make in serializer.data:
        models = CarModel.objects.filter(car_make_id=make['id'])
        model_serializer = CarModelSerializer(models, many=True)
        make['models'] = model_serializer.data
        data.append(make)
    return JsonResponse(data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_cars(request):
    makes = CarMake.objects.all()
    serializer = CarMakeModelSerializer(makes, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    data = json.loads(request.body)
    username = data.get('userName', '')
    password = data.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({
            'userName': username,
            'status': 'Authenticated'
        })
    return JsonResponse({'error': 'Invalid credentials'}, status=401)


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return JsonResponse({
        'userName': ''
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealers(request):
    all_dealers = CarDealer.objects.all()
    serializer = CarDealerSerializer(all_dealers, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetch_dealers(request):
    all_dealers = CarDealer.objects.all()
    serializer = CarDealerSerializer(all_dealers, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealer_by_id(request, dealer_id):
    try:
        dealer = CarDealer.objects.get(dealer_id=dealer_id)
        serializer = CarDealerSerializer(dealer)
        return JsonResponse(serializer.data)
    except CarDealer.DoesNotExist:
        return JsonResponse({'error': 'Dealer not found'}, status=404)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetch_dealer(request, dealer_id):
    try:
        dealer = CarDealer.objects.get(dealer_id=dealer_id)
        serializer = CarDealerSerializer(dealer)
        return JsonResponse(serializer.data)
    except CarDealer.DoesNotExist:
        return JsonResponse({'error': 'Dealer not found'}, status=404)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealers_by_state(request, state):
    dealers = CarDealer.objects.filter(state__iexact=state)
    serializer = CarDealerSerializer(dealers, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def dealer_reviews(request, dealer_id):
    if request.method == 'GET':
        try:
            dealer = CarDealer.objects.get(dealer_id=dealer_id)
        except CarDealer.DoesNotExist:
            return JsonResponse({'error': 'Dealer not found'}, status=404)
        reviews = DealerReview.objects.filter(dealership=dealer)
        serializer = DealerReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            dealer = CarDealer.objects.get(dealer_id=dealer_id)
        except CarDealer.DoesNotExist:
            return JsonResponse({'error': 'Dealer not found'}, status=404)
        review = DealerReview.objects.create(
            dealership=dealer,
            name=data.get('name', ''),
            purchase=data.get('purchase', False),
            review=data.get('review', ''),
            purchase_date=data.get('purchase_date', None),
            car_make=data.get('car_make', ''),
            car_model=data.get('car_model', ''),
            car_year=data.get('car_year', None),
        )
        sentiment_result = analyze_review_sentiment(review.review)
        review.sentiment = sentiment_result
        review.save()
        serializer = DealerReviewSerializer(review)
        return JsonResponse(serializer.data, status=201)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetch_reviews(request, dealer_id):
    try:
        dealer = CarDealer.objects.get(dealer_id=dealer_id)
    except CarDealer.DoesNotExist:
        return JsonResponse({'error': 'Dealer not found'}, status=404)
    reviews = DealerReview.objects.filter(dealership=dealer)
    serializer = DealerReviewSerializer(reviews, many=True)
    return JsonResponse(serializer.data, safe=False)


def analyze_review_sentiment(review_text):
    positive_words = ['excellent', 'great', 'good', 'fantastic', 'amazing', 'wonderful', 'best',
                      'love', 'awesome', 'satisfied', 'happy', 'pleased', 'outstanding', 'perfect',
                      'fantastic services']
    negative_words = ['bad', 'poor', 'terrible', 'awful', 'worst', 'hate', 'disappointed',
                      'horrible', 'mediocre', 'ugly', 'slow', 'broken']
    text_lower = review_text.lower()
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    if positive_count > negative_count:
        return 'positive'
    elif negative_count > positive_count:
        return 'negative'
    return 'neutral'


@api_view(['GET'])
@permission_classes([AllowAny])
def analyze_review(request):
    review_text = request.GET.get('review', '')
    sentiment = analyze_review_sentiment(review_text)
    return JsonResponse({'sentiment': sentiment, 'review': review_text})
