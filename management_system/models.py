from django.db import models
from accounts.models import User

class Resident(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    flat = models.CharField(max_length=100)
    vehicle_no = models.CharField(blank=True ,max_length=100)
    reason = models.CharField(max_length=200)
    reg = models.DateTimeField(auto_now_add=True)
    cameback = models.DateTimeField(null=True, blank=True)
    corona_screening_positive = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class visitor(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    flat_vis = models.CharField(max_length=100)
    reason = models.CharField(max_length=200)
    vis_time = models.DateTimeField(auto_now_add=True)
    vis_returned_time = models.DateTimeField(null=True, blank=True)
    family = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
