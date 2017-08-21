from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Transducer.models import Snippet,Humi_Transducer,Temp_Transducer,Infr_Transducer,Smok_Transducer,Image,Media
class SnippetAdmin(admin.ModelAdmin):
	search_fields=('owner','title','language','style')
	list_display=('owner','created','title','code','linenos','language','style')
	list_filter=('owner','title','language','style')

class Humi_TransducerAdmin(admin.ModelAdmin):
	serch_fields=('owner')
	list_display=('owner','time','humidity')
	list_filter=('owner',)
class Temp_TransducerAdmin(admin.ModelAdmin):
	serch_fields=('owner')
	list_display=('owner','time','temperature')
	list_filter=('owner',)
class Infr_TransducerAdmin(admin.ModelAdmin):
	serch_fields=('owner')
	list_display=('owner','time','distance')
	list_filter=('owner',)
class Smok_TransducerAdmin(admin.ModelAdmin):
	serch_fields=('owner')
	list_display=('owner','time','smoke')
	list_filter=('owner',)
class ImageAdmin(admin.ModelAdmin):
	serch_fields=('owner')
	list_display=('owner','time','image')
	list_filter=('owner',)
class MediaAdmin(admin.ModelAdmin):
	serch_fields=('owner')
	list_display=('owner','time','media')
	list_filter=('owner',)
admin.site.register(Snippet,SnippetAdmin)
admin.site.register(Humi_Transducer,Humi_TransducerAdmin)
admin.site.register(Temp_Transducer,Temp_TransducerAdmin)
admin.site.register(Infr_Transducer,Infr_TransducerAdmin)
admin.site.register(Smok_Transducer,Smok_TransducerAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Media, MediaAdmin)
