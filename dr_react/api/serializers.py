# coding: utf-8
from rest_framework import serializers
from api.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'title', 'code', 'linenos', 'language', 'style')
