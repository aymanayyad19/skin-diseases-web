from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'dob', 'city', 'address', 'phone_number', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            dob=validated_data['dob'],
            city=validated_data['city'],
            address=validated_data['address'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password']
        )
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims to the token if necessary
        token['email'] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add the user data to the response
        data['user'] = {
            'id': self.user.id,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'dob': self.user.dob,
            'city': self.user.city,
            'address': self.user.address,
            'phone_number': self.user.phone_number
        }
        return data