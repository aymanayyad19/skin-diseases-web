from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from SkinDiseaseApp.models import SkinDisease
from skin_diseases import settings
from .serializers import ImageUploadSerializer, HistorySerializer
from .models import ImageUpload, History, Hospital
from PIL import Image
from keras._tf_keras.keras.preprocessing import image

import os
import numpy as np
from inference_sdk import InferenceHTTPClient
from keras._tf_keras.keras.models import load_model


class SearchByImageView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def ditect_Image(self, image_file):
        model_path = os.path.join(settings.BASE_DIR, "skin_deseases_model", "model.h5")
        image_name = image_file.replace("/media/uploads/", "")
        print(image_file)

        model = load_model(model_path)
        img_path = os.path.join(settings.BASE_DIR, "media", "uploads", image_name)
        print(f"base dir path {settings.BASE_DIR} ==> uploaded file path {img_path}")

        img = image.load_img(img_path, target_size=(256, 256, 3))  # Adjust size based on model input
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to match model input

        # Predict the class
        class_num = model.predict(img_array)

        # Get the class name
        class_num = np.argmax(class_num, axis=1)  # Get the class with the highest probability
        print(f"class_num == > {class_num[0]} ")

        if len(class_num) > 0:
            return class_num[0]
        else:
            return -1

    def testApi(self, your_image):
        CLIENT = InferenceHTTPClient(api_url="https://detect.roboflow.com", api_key="kdNkkbxsyXcEBKoX4JYO")
        result = CLIENT.infer(your_image, model_id="yolov8-skin-disease-detection/1")

        return result

    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)

        # Validate the uploaded data
        if serializer.is_valid():
            # Save the image to the server
            serializer.save()

            # Access the uploaded image file path
            image_path = serializer.data['image']
            image_full_path = os.path.join('media', image_path)  # Adjust your media root path if necessary

            # Detect disease based on image
            detect_result_class_num = self.ditect_Image(image_full_path)  # Call detection function once

            # Get the current user
            user = request.user

            try:
                # Retrieve the SkinDisease instance based on detected class number
                skin_disease = SkinDisease.objects.get(model_class_num=detect_result_class_num)
            except SkinDisease.DoesNotExist:
                return Response({'error': 'No skin disease found for the given class number.'},
                                status=status.HTTP_404_NOT_FOUND)

            try:
                # Retrieve the Hospital based on user's city (using exact city matching, adjust as necessary)
                hospital = Hospital.objects.get(city__iexact=user.city)
            except Hospital.DoesNotExist:
                return Response({'error': 'No hospital found for the user\'s city.'}, status=status.HTTP_404_NOT_FOUND)
            full_media_url = request.build_absolute_uri(image_full_path)

            # Create a History record
            history = History(
                image_url=full_media_url,
                hospital=hospital,
                user=user,
                skin_diseases=skin_disease  # Assign the SkinDisease instance
            )

            # Save the history record
            history.save()

            # Serialize the created history object
            history_serializer = HistorySerializer(history)

            # Return success response with relevant data
            return Response({
                'history': history_serializer.data,
                'message': 'Image uploaded and processed successfully!',
            }, status=status.HTTP_201_CREATED)

        # If the serializer is not valid, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserHistoryView(APIView):
    def get(self, request):
        user = request.user
        history_list = History.objects.filter(user=user)
        serializer = HistorySerializer(history_list, many=True)
        return Response(serializer.data)
