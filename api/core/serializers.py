from rest_framework import serializers

class ProdutosSerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.CharField()
    price = serializers.CharField()
    images = serializers.CharField(source="images.default")
    marca =  serializers.CharField(source="details.marca")
    # description = serializers.CharField()
    status = serializers.CharField()