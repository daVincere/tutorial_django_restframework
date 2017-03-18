# 
# For returning the status
from rest_framework import status

from rest_framework.decorators import api_view

from rest_framework.response import Response

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
	# 
	# Lists all the snippets together
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return Response(serializer.data)

	elif request.method=='POST':
		# 
		# data consists of every type of data
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):

	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method=='GET':
		serializer = SnippetSerializer(snippet)
		return Response(serializer.data)

	elif request.method=='PUT':
		serializer = SnippetSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	elif request.method=='DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

"""
With the use of request.data, we no longer have to specify the content type
for our requests/responses
"""

"""
To enable the support for format suffixes, we write

def generalView(request, some paramenters, format = None)

to our fn view declarations


In the urls.py file, we add 

urlpatterns = format_suffix_patterns(urlpatterns)
"""