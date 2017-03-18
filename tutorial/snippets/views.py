from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
# why this?
from django.views.decorators.csrf import csrf_exempt

# For JSON rendering
from rest_framework.renderers import JSONRenderer
# For JSON parsing
from rest_framework.parsers import JSONParser

from .models import Snippet
from .serializers import SnippetSerializer

# 
# We want the clients without the csrf token to be able to POST to this view. 
# csrf_exempt decorator allows for that.
# -- not recommended --
@csrf_exempt
def snippet_list(request):
	# 
	# List of all code snippets, or create a new snippet (Obviously)
	# 
	if request.method == 'GET':
		# 
		# snippets store all the objects corresponding to the Snippet Object 
		snippets = Snippet.objects.all()
		# 
		# Serializer serializers the data coming into snippets
		serializer = SnippetSerializer(snippets, many=True)

		# 
		# returns the serializer data in the form of a JSON
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		# 
		# If the data is getting posted by the user, we'd want to parse it
		# Obviously!

		data = JSONParser.parse(request)
		serializer = SnippetSerializer(data=data)

		# 
		# How will it check if the serailizer is valid?
		if serializer.is_valid():
			serializer.save()

			return JsonResponse(serializer.data, status=201)
			# Status 201 why?

		# 
		# Incase the serializer isn't valid, return erros
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
	# 
	# Retrieve, update or delete a code snippet

	# 
	# Gets the snippet object when asked for otherwise a 404
	# Why not use get_object_or_404 here?
	try:
		snippet = Snippet.objects.get(pk=pk)
	except SnippetDoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(snippet, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		snippet.delete()
		return HttpResponse(status=204)
		