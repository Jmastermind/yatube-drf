from rest_framework import mixins, viewsets


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet for model creation and list view"""
