from rest_framework import serializers

from viewer.models import Movie


class MovieReadModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieCreateModelSerializers(serializers.ModelSerializer):
    class Meta :
        model = Movie
        exlude = ['created']

class MovieCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)


    def validated_data(self,attrs):
        pass

    def validate_title(self,):
        pass

