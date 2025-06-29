from django.urls import path,include
from rest_framework import routers
from .views import CountryViewSet

router=routers.DefaultRouter()
router.register(r'Country',CountryViewSet)


urlpatterns=[
    path('api/',include(router.urls))
]