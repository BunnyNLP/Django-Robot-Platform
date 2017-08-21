from rest_framework import serializers
from Transducer.models import Snippet,Humi_Transducer,Temp_Transducer,Infr_Transducer,Smok_Transducer,Image,Media
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True,view_name='snippet-detail',read_only=True)

	class Meta:
		model = User
		fields =('url','username','snippets')


	
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	owner=serializers.ReadOnlyField(source = 'owner.username')
	class Meta:
		model = Snippet
		fields =('url','owner','title','code','linenos','language','style')

		



class Humi_TransducerSerializer(serializers.HyperlinkedModelSerializer):
	owner=serializers.ReadOnlyField(source = 'humidity')
	class Meta:
		model =Humi_Transducer
		fields=('owner','humidity','time')

class Temp_TransducerSerializer(serializers.HyperlinkedModelSerializer):
	owner=serializers.ReadOnlyField(source = 'temperature')
	class Meta:
		model =Temp_Transducer
		fields=('owner','temperature','time')

class Infr_TransducerSerializer(serializers.HyperlinkedModelSerializer):
	owner=serializers.ReadOnlyField(source = 'infrared')
	class Meta:
		model =Infr_Transducer
		fields=('owner','distance','time')

class Smok_TransducerSerializer(serializers.HyperlinkedModelSerializer):
	owner=serializers.ReadOnlyField(source = 'smoke')
	class Meta:
		model =Smok_Transducer
		fields=('owner','smoke','time')

class Temp_TransducerSerializer(serializers.HyperlinkedModelSerializer):
	owner=serializers.ReadOnlyField(source = 'temperature')
	class Meta:
		model =Temp_Transducer
		fields=('owner','temperature','time')

class ImageSerializer(serializers.HyperlinkedModelSerializer):
	owner=serializers.ReadOnlyField(source = 'image')
	class Meta:
		model =Image
		fields=('owner','image','time')

class MediaSerializer(serializers.HyperlinkedModelSerializer):
	owner=serializers.ReadOnlyField(source = 'media')
	class Meta:
		model =Media
		fields=('owner','media','time')



