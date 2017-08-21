"""Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#Original
'''
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
'''

#v4.10
'''
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include
from snippets.views import showhumidity

'''

'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^users/$',views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
	url(r'^snippets/$',views.SnippetList.as_view()),
	url(r'^snippets/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view()),
	url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
	url(r'^$',views.api_root),
	url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',views.SnippetHighlight.as_view()),

]
urlpatterns =format_suffix_patterns(urlpatterns)


'''
'''
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


from django.conf.urls.static import static
from django.conf import settings

from snippets.views import SnippetViewSet,UserViewSet,Humi_TransducerViewSet,Temp_TransducerViewSet,Infr_TransducerViewSet,ImageViewSet,MediaViewSet
from rest_framework import renderers
#Snippet
snippet_list=SnippetViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
snippet_detail = SnippetViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})
#User
user_list =UserViewSet.as_view({
	'get':'list'
})
user_detail=UserViewSet.as_view({
	'get':'retrieve'
})


#Humi_Transducer
Humi_Transducer_list=Humi_TransducerViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
Humi_Transducer_detail =Humi_TransducerViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})



#Temp_Transducer
Temp_Transducer_list=Temp_TransducerViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
Temp_Transducer_detail =Temp_TransducerViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})


#Infr_Transducer
Infr_Transducer_list=Infr_TransducerViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
Infr_Transducer_detail =Infr_TransducerViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})

#Image
Image_list=ImageViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
Image_detail =ImageViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})
#Media
Media_list=MediaViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
Media_detail =MediaViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})




#API endpoints
'''

'''
urlpatterns =format_suffix_patterns([
	url(r'^admin/', admin.site.urls),
	url(r'^$',views.api_root),
	url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
	url(r'^snippets/$',views.SnippetList.as_view(),name='snippet-list'),
	url(r'^snippets/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view(),name='snippet-detail'),
	url(r'^users/$',views.UserList.as_view(),name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),name='user-detail'),
	url(r'^transducer/$',views.TransducerList.as_view(),name='transducer-list'),
	url(r'^transducer/(?P<pk>[0-9]+)/$',views.TransducerDetail.as_view(),name='transducer-detail'),

	url(r'^humidity/$',views.showhumidity),
	#url( r'^static/(?P<path>.*)$', include('django.views.static.serve'),{ 'document_root': settings.STATIC_URL }), 
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT))


'''


'''
#Use Routers
from rest_framework.routers import DefaultRouter
#Creat a router and register our viewsets with it
router=DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)
router.register(r'humidity',views.Humi_TransducerViewSet)
router.register(r'temperature',views.Temp_TransducerViewSet)
router.register(r'infrared',views.Infr_TransducerViewSet)
router.register(r'image',views.ImageViewSet)
router.register(r'media',views.MediaViewSet)


#The API URLs ate now determined automatically by the router
#Additionally,we include the login URLs for the browsable API.
urlpatterns =[
	url(r'^admin/', admin.site.urls),
	url(r'^',include(router.urls)),
	url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))


]

'''



#v4.12
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()
from rest_framework.urlpatterns import format_suffix_patterns
from Transducer import views
from django.conf.urls import include
from Transducer.views import showhumidity
from rest_framework.routers import DefaultRouter
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns



from django.conf.urls.static import static
from django.conf import settings

from Transducer.views import SnippetViewSet,UserViewSet,Humi_TransducerViewSet,Temp_TransducerViewSet,Infr_TransducerViewSet,Smok_TransducerViewSet,ImageViewSet,MediaViewSet
from rest_framework import renderers

#Snippet
snippet_list=SnippetViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
snippet_detail = SnippetViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})
#User
user_list =UserViewSet.as_view({
	'get':'list'
})
user_detail=UserViewSet.as_view({
	'get':'retrieve'
})


#Humi_Transducer
Humi_Transducer_list=Humi_TransducerViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
Humi_Transducer_detail =Humi_TransducerViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})



#Temp_Transducer
Temp_Transducer_list=Temp_TransducerViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
Temp_Transducer_detail =Temp_TransducerViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})


#Infr_Transducer
Infr_Transducer_list=Infr_TransducerViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
Infr_Transducer_detail =Infr_TransducerViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})

#Smok_Transducer
Smok_Transducer_list=Smok_TransducerViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
Smok_Transducer_detail =Smok_TransducerViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})

#Image
Image_list=ImageViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
Image_detail =ImageViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})
#Media
Media_list=MediaViewSet.as_view({
	'get':'retrieve',
	'post':'creat'
})
Media_detail =MediaViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})

#API endpoints
#Use Routers
#Creat a router and register our viewsets with it
router=DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)
router.register(r'humidity',views.Humi_TransducerViewSet)
router.register(r'temperature',views.Temp_TransducerViewSet)
router.register(r'infrared',views.Infr_TransducerViewSet)
router.register(r'smoke',views.Smok_TransducerViewSet)
router.register(r'image',views.ImageViewSet)
router.register(r'media',views.MediaViewSet)


#The API URLs ate now determined automatically by the router
#Additionally,we include the login URLs for the browsable API.
urlpatterns =[
	url(r'^admin/', admin.site.urls),
	url(r'^',include(router.urls)),
	url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
	url(r'^showhumidity/',views.showhumidity),
	url(r'^login$',views.login),
	url(r'^ifream',views.ifream),
	url(r'^index$',views.ultrasonic),
	url(r'^gps$',views.gps),
	url(r'^humidities$',views.humidity),
	url(r'^temperatures$',views.temperature),
	url(r'^video$',views.video),
	url(r'^smog$',views.smog),
	url(r'^login_action/$',views.login_action),
	url(r'^accounts/login/$',views.login),
	url(r'^logout$',views.logout),
	url(r'^test$',views.test),
]

