from rest_framework import routers
from animals.views import KittenViewSet
from animals.views import PuppyView

router = routers.SimpleRouter()
router.register(r'kitten', KittenViewSet)
router.register(r'puppy', PuppyView)
