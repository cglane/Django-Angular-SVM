from rest_framework import serializers
# from photos.models import Photo, LANGUAGE_CHOICES, STYLE_CHOICES
from files.models import csvFile


# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = csvFile
#         fields = ('id', 'title', 'comment','created')
class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = csvFile
        fields = ('id', 'title', 'comment','created','csvFile')
