
from django.conf.urls import include, url
from django.contrib import admin
from angular_ui_router.views import HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^templates/(?P<folder>\w+)/(?P<template>[^/]+)$', 
        'angular_ui_router.views.partials', 
        name='angular_ui_router_views_partials'
    ),
]
