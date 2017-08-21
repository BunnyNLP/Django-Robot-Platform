from django.shortcuts import render
# Create your views here. 
from django.shortcuts import render
from Transducer.models import Snippet
from Transducer.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from Transducer.serializers import UserSerializer
from rest_framework import permissions
from Transducer.permissions import IsOwnerOrReadOnly
#User view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
#Humi_Transducer
from Transducer.models import Humi_Transducer
from Transducer.serializers import Humi_TransducerSerializer
#Temp_Transducer
from Transducer.models import Temp_Transducer
from Transducer.serializers import Temp_TransducerSerializer
#Infr_Transducer
from Transducer.models import Infr_Transducer
from Transducer.serializers import Infr_TransducerSerializer
#Smok_Transducer
from Transducer.models import Smok_Transducer
from Transducer.serializers import Smok_TransducerSerializer
#Image
from Transducer.models import Image
from Transducer.serializers import ImageSerializer
#Media
from Transducer.models import Media
from Transducer.serializers import MediaSerializer
#Showhumidity
from django.core import serializers
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect


@api_view(['GET'])
def api_root(request,format=None):
	return Response({
	'users':reverse('user-list',request=request,format=format),
	'snippets':reverse('snippet-list',request=request,format=format),
	'humidity':reverse('humidity-list',request=request,format=format),
	'temperature':reverse('temperature-list',request=request,format=format),
	'infrared':reverse('infrared-list',request=request,format=format),
	'smoke':reverse('smoke-list',request=request,format=format),
	'image':reverse('image-list',request=request,format=format),
	'media':reverse('media-list',request=request,format=format),
	

})


'''
class UserList(generics.ListAPIView):
	queryset =User.objects.all()
	serializer_class =UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset =User.objects.all()
	serializer_class =UserSerializer
'''
#Use Viewset
from rest_framework import viewsets
from rest_framework.decorators import detail_route
class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset=User.objects.all()
	serializer_class=UserSerializer
'''
class SnippetList(generics.ListCreateAPIView):
	queryset =Snippet.objects.all()
	serializer_class =SnippetSerializer
	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Snippet.objects.all()
	serializer_class =SnippetSerializer
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
'''

class SnippetViewSet(viewsets.ModelViewSet):
	queryset=Snippet.objects.all()
	serializer_class =SnippetSerializer
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)

#Humidity Transducer
class Humi_TransducerViewSet(viewsets.ModelViewSet):
	queryset=Humi_Transducer.objects.all()
	serializer_class =Humi_TransducerSerializer
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)
#Temperature Transducer
class Temp_TransducerViewSet(viewsets.ModelViewSet):
	queryset=Temp_Transducer.objects.all()
	serializer_class =Temp_TransducerSerializer
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)
#Infrared Transducer
class Infr_TransducerViewSet(viewsets.ModelViewSet):
	queryset=Infr_Transducer.objects.all()
	serializer_class =Infr_TransducerSerializer
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)

#Smoke Transducer
class Smok_TransducerViewSet(viewsets.ModelViewSet):
	queryset=Smok_Transducer.objects.all()
	serializer_class =Smok_TransducerSerializer
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)
#Image
class ImageViewSet(viewsets.ModelViewSet):
	queryset=Image.objects.all()
	serializer_class =ImageSerializer
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)
#Media
class MediaViewSet(viewsets.ModelViewSet):
	queryset=Media.objects.all()
	serializer_class =ImageSerializer
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)

#Put the date of humidity model to the HTML template
def showhumidity(request):
	'''
	lists=Transducer.objects.all().values('id','humidity')#Return a queryset
	data=json.dumps(list(lists))#Convert to str
	humidity_list=eval(data)#Convert to list and humidity[i] is a dict
	dic={}
	for l in humidity_list:
		dic['x%s' %(l.get('id'))]=l.get('humidity')#To make up a dict,such as dict[x0]=80.0
	return render(request,'test.html',dic)
	#return render_to_response('test.html',locals())#The locals put all of the args to the template
	'''
	obj=Humi_Transducer.objects.all().values('id','humidity')
	x=[]
	y=[]
	for i in obj:
		x.append(i.get('id')) 
	for i in obj:
		y.append(i.get('humidity'))
	return render(request,'test.html',{"x":x,"y":y,})


from django.contrib.auth.decorators import login_required
@login_required
def ultrasonic(request):
	obj=Infr_Transducer.objects.all().values('time','distance')
	x=[]
	y=[]
	for i in obj:
		x.append(i.get('time')) 
	for i in obj:
		y.append(i.get('distance'))
	return render(request,"ultrasonic.html",{"arr0":x,"arr1":y})
@login_required
def gps(request):
	return render(request,"gps.html",locals())
@login_required
def humidity(request):
	return render(request,"humidity.html",locals())
@login_required
def temperature(request):
	return render(request,"temperature.html",locals())
@login_required
def video(request):
	return render(request,"video.html",locals())
@login_required
def smog(request):
	return render(request,"smog.html",locals())
@login_required
def ifream(request):
	return render(request,"ifream.html",locals())
def login(request):
	return render(request,"login.html",locals())
#Login and Logout
from django.contrib import auth 
def login_action(request):
	if request.method  == 'POST':
		username= request.POST.get('username','')
		password= request.POST.get('password','')
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			request.session['user']=username
			response=HttpResponseRedirect('/index')
			return response
		else:
			  return render_to_response('login.html', {'error':'登陆名或密码错误！'})
@login_required
def logout(request):
	auth.logout(request)
	response =HttpResponseRedirect('/login')
	return response


def test(request):
	return render(request,"ajax.html",locals())
