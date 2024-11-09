from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class HistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view.'})


class CustomLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # You can add custom logic here (e.g., logging, failed attempts, etc.)
        response = super().post(request, *args, **kwargs)
        # Customize the response if needed
        return Response({
            'message': "login successfully",
            'user': {
                'access_token': response.data['access'],
                'refresh_token': response.data['refresh'],
                'username': request.user.username,
                'email': request.user.email,
                # Add other user-related data if needed
            }
        }, status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Register endpoint accessed")  # Add logging to confirm the endpoint is being accessed

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                data={
                    'user': serializer.data,
                    'auth': {
                        'refresh': str(refresh),
                        'access': str(refresh.token),
                    }

                }
                , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
