from rest_framework.serializers import ModelSerializer
from core.models import Modelo

class ModeloDetailSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
        depth = 1

class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"