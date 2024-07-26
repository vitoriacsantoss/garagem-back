from rest_framework.serializers import ModelSerializer
from core.models import Veiculo

class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 2

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"