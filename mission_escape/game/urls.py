
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('profile',ProfileViewSet)
router.register('room',RoomViewSet)
router.register('escmap',EscmapViewSet)
router.register('access',AccessViewSet)


urlpatterns = router.urls
