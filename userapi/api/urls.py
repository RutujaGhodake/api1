from django.contrib import admin
from django.urls import path,include
from api.views import userviewset,postviewset,likeviewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'users',userviewset)
router.register(r'posts',postviewset)
router.register(r'likes',likeviewset)


urlpatterns = [
    path('',include(router.urls))
]