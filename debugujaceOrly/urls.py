from rest_framework import routers
from django.urls import include, path
from .views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
