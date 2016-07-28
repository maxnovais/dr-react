# coding: utf-8
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from api.models import Snippet
from api.serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.
    The `highlight` field presents a hyperlink to the highlighted HTML
    representation of the code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    @detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
