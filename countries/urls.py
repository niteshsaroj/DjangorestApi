from django.urls import path,include
from rest_framework import routers
from .views import CountryViewSet,StateViewset

router=routers.DefaultRouter()
router.register(r'Country',CountryViewSet)
router.register(r'States',StateViewset)


urlpatterns=[
    path('api/',include(router.urls))
]