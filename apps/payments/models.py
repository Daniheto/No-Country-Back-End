from django.db import models
from django.contrib.auth.models import User
from apps.courses.models import Course


class Payments(models.Model):
    METHOD_CHOICES = [
        ('paypal', 'Paypal'),
        ('transfer', 'Transfer'),
        ('credit card', 'Credit Card'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=METHOD_CHOICES, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=False)