
from django.contrib import admin
from django.urls import path, include
from .views import home_page
from api.views import companyviewset
from rest_framework import routers



router = routers.DefaultRouter()
router.register = (r'companies', companyviewset)

urlpatterns = [
    path('', include(routers.urls))
    

]
