from rest_framework import serializers
from .models import CarMake, CarModel, CarDealer, DealerReview
from django.contrib.auth.models import User


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarDealerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='dealer_id', read_only=True)

    class Meta:
        model = CarDealer
        fields = ['id', 'full_name', 'short_name', 'city', 'state', 'zip', 'address', 'lat', 'long']


class DealerReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        model = DealerReview
        fields = ['id', 'dealership', 'name', 'review', 'purchase', 'purchase_date', 'car_make', 'car_model', 'car_year']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CarMakeModelSerializer(serializers.ModelSerializer):
    CarModels = serializers.SerializerMethodField()

    class Meta:
        model = CarMake
        fields = ['id', 'name', 'CarModels']

    def get_CarModels(self, obj):
        car_models = CarModel.objects.filter(car_make=obj)
        return [{'id': m.id, 'name': m.name, 'car_type': m.car_type, 'year': m.year.year, 'price': str(m.price)} for m in car_models]
