# coding: utf-8
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register(r'api', views.SnippetViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)