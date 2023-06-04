from rest_framework import viewsets

from reviews.models import Review, Tag
from reviews.serializers import ReviewSerializer, TagSerializer

class ReviewViewsets(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        place_id = self.request.query_params.get('place_id', None)
        if place_id is not None:
            queryset = queryset.filter(place_id=place_id)
        return queryset


class TagViewSets(viewsets.ModelViewSet):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer