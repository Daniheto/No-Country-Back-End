from rest_framework import serializers
from .models import Course, Material, Inscripcion
from django.contrib.auth.models import User


class CourseValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'level',
            'price',
            'duration',
            'category',
            'status',
            'date_creation'
        ]
        read_only_fields = ['id', 'date_creation', 'instructor']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'type', 'url', 'title', 'description']


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CourseResponseSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True)
    instructor = InstructorSerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'level',
            'price',
            'duration',
            'category',
            'status',
            'date_creation',
            'materials',
            'instructor'
        ]
        read_only_fields = ['date_creation', 'materials', 'instructor']


class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = ['curso', 'estudiante', 'fecha_inscripcion']
