from django.db import models


class Tag(models.Model):
    name=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Review(models.Model):
    place_id=models.PositiveIntegerField(primary_key=True, editable=True)
    content=models.TextField()
    rate=models.FloatField()
    tags=models.ManyToManyField(Tag, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

