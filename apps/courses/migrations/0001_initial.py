# Generated by Django 5.1.1 on 2024-10-17 16:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('duration', models.PositiveIntegerField()),
                ('category', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('review', 'Review'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='draft', max_length=20)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('video', 'Video'), ('pdf', 'PDF'), ('other', 'Other')], max_length=20)),
                ('url', models.URLField(blank=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='courses.course')),
            ],
        ),
    ]