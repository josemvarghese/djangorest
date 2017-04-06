from rest_framework.serializers import ModelSerializer
from animals.models import Kitten


class KittenSerialzer(ModelSerializer):
    class Meta:
        model= Kitten