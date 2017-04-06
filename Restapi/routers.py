from rest_framework import routers
from animals.views import KittenViewSet

router = routers.SimpleRouter()
router.register(r'kitten', KittenViewSet)
