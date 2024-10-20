from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Course, Inscripcion
from .serializers import CourseValidationSerializer, CourseResponseSerializer, InscripcionSerializer


# Endpoint para crear un curso
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_course(request):
    # Serializa los datos
    course_validation_serializer = CourseValidationSerializer(
        data=request.data)

    # Verifica que los datos san válidos
    if course_validation_serializer.is_valid():
        # Guarda el nuevo curso
        course = course_validation_serializer.save(instructor=request.user)

        # Serializa los datos del curso
        course_response_serializer = CourseResponseSerializer(course)

        # Respuesta exitosa del endpoint
        return Response({
            'status': 'success',
            'message': 'Course created successfully',
            'data': {
                'course': course_response_serializer.data
            }
        }, status=status.HTTP_201_CREATED)

    # Respuesta erronea del endpoint
    return Response({
        'status': 'error',
        'message': 'Errors in data validation.',
        'errors': course_validation_serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Endpoint para obtener todos los cursos
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_courses(request):
    # Obtiene todos los cursos
    courses = Course.objects.all().order_by('id')

    # Serializa los datos de los cursos
    course_response_serializer = CourseResponseSerializer(courses, many=True)

    # Respuesta exitosa del endpoint
    return Response({
        'status': 'success',
        'message': 'Successfully earned courses',
        'data': {
            'courses': course_response_serializer.data
        }
    }, status=status.HTTP_200_OK)


# Endpoint para actualizar un curso
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_course(request, course_id):
    try:
        # Obiene un curso por su ID
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        # Respuesta erronea del endpoint
        return Response({
            'status': 'error',
            'message': 'Course not found'
        }, status=status.HTTP_404_NOT_FOUND)

    # Verifica si el usuario autenticado es el propietario del curso
    if course.instructor != request.user:
        return Response({
            'status': 'error',
            'message': 'You do not have permission to update this course.'
        }, status=status.HTTP_403_FORBIDDEN)

    # Serializa los datos del curso
    course_validation_serializer = CourseValidationSerializer(
        course, data=request.data, partial=True)

    # Verifica que los datos sean válidos
    if course_validation_serializer.is_valid():
        # Guarda el curso con los nuevos datos
        course_validation_serializer.save()

        # Serializa los datos del curso
        course_response_serializer = CourseResponseSerializer(course)

        # Respuesta exitosa del endpoint
        return Response({
            'status': 'success',
            'message': 'Course updated successfully',
            'data': {
                'course': course_response_serializer.data
            }
        }, status=status.HTTP_200_OK)

    # Respuesta erronea del endpoint
    return Response({
        'status': 'error',
        'message': 'Errors in data validation.',
        'errors': course_validation_serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Endpoint para eliminar un curso
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_course(request, course_id):
    try:
        # Obtiene el curso por su ID
        course = Course.objects.get(id=course_id)

        # Verifica si el usuario autenticado es el propietario del curso
        if course.instructor != request.user:
            return Response({
                'status': 'error',
                'message': 'You do not have permission to delete this course.'
            }, status=status.HTTP_403_FORBIDDEN)

        # Elimina el curso
        course.delete()

        # Respuesta exitosa del endpoint
        return Response({
            'status': 'success',
            'message': 'Successfully deleted course',
        }, status=status.HTTP_204_NO_CONTENT)
    except Course.DoesNotExist:
        # Respuesta erronea del endpoint
        return Response({
            'status': 'error',
            'message': 'Course not found'
        }, status=status.HTTP_404_NOT_FOUND)


class InscripcionCreateView(generics.CreateAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
    permission_classes = [IsAuthenticated]


class InscripcionListView(generics.ListAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
    permission_classes = [IsAuthenticated]
