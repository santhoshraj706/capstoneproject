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
    class Meta:
        model = CarDealer
        fields = '__all__'


class DealerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerReview
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
