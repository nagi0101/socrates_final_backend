from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Tag(models.Model):
    name=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Review(models.Model):
    place_id=models.PositiveIntegerField()
    place_name=models.TextField()
    content=models.TextField()
    rate=models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
    )
    tags=models.ManyToManyField(Tag, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

