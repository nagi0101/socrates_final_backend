from rest_framework import viewsets

from reviews.models import Review, Tag
from reviews.serializers import ReviewSerializer, TagSerializer

class ReviewViewsets(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer

class TagViewSets(viewsets.ModelViewSet):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer