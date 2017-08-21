from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter


LEXERS=[item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES =sorted([(item[1][0],item[0]) for item in LEXERS])
STYLE_CHOICES=sorted((item,item) for item in get_all_styles())

class Snippet(models.Model):
	owner= models.ForeignKey('auth.User',related_name='snippets')
	created =models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length =100,blank=True,default='')
	code=models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(choices=LANGUAGE_CHOICES,default='python',max_length=100)
	style = models.CharField(choices=STYLE_CHOICES,default='friendly',max_length=100)

	
	class Meta:
		ordering=('created',)
	def save(self, *args,  **kwargs):
		lexer=get_lexer_by_name(self.language)
		linenos = self.linenos and 'table' or False
		options=self.title and {'title':self.title} or {}
		formatter = HtmlFormatter(style=self.style,linenos=linenos,full=True,**options)
		self.highlighted = highlight(self.code,lexer,formatter)
		super(Snippet,self).save( *args, **kwargs)


class Humi_Transducer(models.Model):
	owner= models.ForeignKey('auth.User',related_name='humidity')
	time=models.TimeField(auto_now=True,blank=True)
	humidity=models.FloatField()
	#class Meta:
		#ordering=('owner','humidity','time')

class Temp_Transducer(models.Model):
	owner= models.ForeignKey('auth.User',related_name='temperature')
	time=models.TimeField(auto_now=True,blank=True)
	temperature=models.FloatField()
	#class Meta:
		#ordering=('owner','temperature','time')

class Infr_Transducer(models.Model):
	owner= models.ForeignKey('auth.User',related_name='infrared')
	time=models.TimeField(auto_now=True,blank=True)
	distance=models.FloatField()
	#class Meta:
		#ordering=('owner','distance','time')

class Smok_Transducer(models.Model):
	owner= models.ForeignKey('auth.User',related_name='smoke')
	time=models.TimeField(auto_now=True,blank=True)
	smoke=models.FloatField()
	#class Meta:
		#ordering=('owner','smoke','time')

class Image(models.Model):
	owner= models.ForeignKey('auth.User',related_name='image')
	time=models.TimeField(auto_now=True,blank=True)
	image=models.ImageField()
	#class Meta:
		#ordering=('owner','image','time')

class Media(models.Model):
	owner= models.ForeignKey('auth.User',related_name='media')
	time=models.TimeField(auto_now=True,blank=True)
	media=models.FileField()
	#class Meta:
		#ordering=('owner','media','time')



