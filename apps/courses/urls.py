from django.urls import path
from . import views


# Urls para los endpoint de courses
urlpatterns = [
    path('courses/create', views.create_course, name='create_course'),
    path('courses/get_all', views.get_all_courses, name='get_all_courses'),
    path('courses/update/<int:course_id>', views.update_course, name='update_course'),
    path('courses/delete/<int:course_id>', views.delete_course, name='delete_course'),
]