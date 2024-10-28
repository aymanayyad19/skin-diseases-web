from rest_framework import serializers
from .models import ImageUpload, History

from rest_framework import serializers
from .models import SkinDisease, Hospital, User  # Import related models if needed

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ['image', 'uploaded_at']



from rest_framework import serializers
from .models import SkinDisease, Hospital, User, History  # Import your models

# Serializer for SkinDisease
class SkinDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinDisease
        fields = ['id', 'name', 'description','symptoms','risk_factors','coping_with','advices']  # Include all fields you want to expose

# Serializer for Hospital
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'address', 'city','contact_number','lat','lon',]  # Include relevant fields

# Serializer for User (you can adjust fields as per your custom user model)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number','address','dob',"city"]  # Include relevant fields

# Serializer for YourModel (including related models)
class HistorySerializer(serializers.ModelSerializer):
    skin_diseases = SkinDiseaseSerializer(read_only=True)  # Nested serializer for SkinDisease
    hospital = HospitalSerializer(read_only=True)  # Nested serializer for Hospital
    user = UserSerializer(read_only=True)  # Nested serializer for User

    class Meta:
        model = History  # Replace with your actual model name
        fields = ['id', 'skin_diseases', 'hospital', 'user', 'image_url']  # Include all the fields of YourModel
