# coding: utf-8
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from api import views as api_view
from web.views import IndexView


router = DefaultRouter()
router.register(r'api', api_view.SnippetViewSet)

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^', include(router.urls)),
)