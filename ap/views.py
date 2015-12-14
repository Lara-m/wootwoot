from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.core import serializers
import models

def index(request):
    return render_to_response("ap/index.html", 
    	context_instance=RequestContext(request)) 

@csrf_exempt
def icall(request):
	n	= request.POST['n']
	u	= request.POST['u'] 

	#print request.body
	#print json.dumps(request.body) #turns shit into string

	print "name = " + n
	print "url = " + u


	obj = models.URLPost(name=n, body=u)
	print "b = " + obj.body
	obj.save()

	print "models.URLPost.objects.all = "
	print models.URLPost.objects.all()

	data = serializers.serialize('json',models.URLPost.objects.all())
	
	return HttpResponse(data)
