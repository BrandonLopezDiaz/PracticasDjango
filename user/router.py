from rest_framework.routers import DefaultRouter
from user.views import UserModelViewSet

router_user = DefaultRouter()
router_user.register(r'Users', basename='user', viewset=UserModelViewSet)
