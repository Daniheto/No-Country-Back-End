from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.utils import timezone
from .serializers import UserValidationSerializer, UserResponseSerializer
from datetime import timedelta


# Endpoint para el registro de usuario
@api_view(['POST'])
def sign_up(request):
    # Serializa los datos
    user_validation_serializer = UserValidationSerializer(data=request.data)

    # Verifica que los datos son válidos
    if user_validation_serializer.is_valid():
        # Guarda al nuevo usuario
        user = user_validation_serializer.save()

        # Crea un token de autenticación para el usuario
        token = Token.objects.create(user=user)

        # Serializa los datos del usuario
        user_response_serializer = UserResponseSerializer(user)

        # Respuesta exitosa desde el endpoint
        return Response({
            'status': 'success',
            'message': 'User registered successfully.',
            'data': {
                'token': {
                    'token_key': token.key
                },
                'user': user_response_serializer.data
            }
        }, status=status.HTTP_201_CREATED)
    
    # Respuesta erronea desde el endpoint
    return Response({
        'status': 'error',
        'message': 'Errors in data validation.',
        'errors': user_validation_serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Endpoint para el inicio de sesión del usuario
@api_view(['POST'])
def sign_in(request):
    # Obtiene los datos del usuario
    username = request.data.get('username')
    password = request.data.get('password')

    # Auntentica al usuario
    user = authenticate(request, username=username, password=password)

    # Verifica la autenticación del usuario
    if user is None:
        # Respuesta erronea desde el endpoint
        return Response({
            'status': 'error',
            'message': 'Authentication failed.',
            'errors': {
                'non_field_errors': ['Invalid username or password']
            }
        }, status=status.HTTP_401_UNAUTHORIZED)

    # Crea o actualiza el token del usuario
    token, created = Token.objects.get_or_create(user=user)

    # Configura el tiempo de expiración del token
    token_expiration = timezone.now() + timedelta(days=3)

    # Serializa los datos del usuario
    user_response_serializer = UserResponseSerializer(user)

    # Respuesta exitosa desde el endpoint
    return Response({
        'status': 'success',
        'message': 'User logged in successfully.',
        'data': {
            'token': {
                'token_key': token.key,
                'token_expiration': token_expiration.isoformat()
            },
            'user': user_response_serializer.data
        }
    }, status=status.HTTP_200_OK)


# Endpoint para el cierre de sesión del usuario
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sign_out(request):
    try:
        # Elimina el token del usuario autenticado
        request.user.auth_token.delete()
        return Response({
            'status': 'success',
            'message': 'User logged out successfully.'
        }, status=status.HTTP_200_OK)
    except (AttributeError, Token.DoesNotExist):
        return Response({
            'status': 'error',
            'message': 'User is not logged in.'
        }, status=status.HTTP_400_BAD_REQUEST)


# Endpoint para actualización del usuario
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_user(request):
    # Obtiene el usuario autenticado
    user = request.user

    # Serializa los datos
    user_validation_serializer = UserValidationSerializer(user, data=request.data, partial=True)

    # Verifica que los datos son válidos
    if user_validation_serializer.is_valid():
        # Guarda los cambios en el usuario
        user = user_validation_serializer.save()

        # Serializa los datos del usuario
        user_response_serializer = UserResponseSerializer(user)

        # Respuesta exitosa desde el endpoint
        return Response({
            'status': 'success',
            'message': 'User profile updated successfully.',
            'data': user_response_serializer.data
        }, status=status.HTTP_200_OK)

    # Respuesta erronea desde el endpoint
    return Response({
        'status': 'error',
        'message': 'Errors in data validation.',
        'errors': user_validation_serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Endpoint para eliminación del usuario
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request):
    try:
        # Elimina el token del usuario autenticado
        request.user.auth_token.delete()

        # Elimina el usuario autenticado
        request.user.delete()

        return Response({
            'status': 'success',
            'message': 'User deleted successfully.'
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'status': 'error',
            'message': 'Error deleting user.',
            'errors': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
