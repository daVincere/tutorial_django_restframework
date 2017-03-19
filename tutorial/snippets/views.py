from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
	# The ListCreateAPIView is an already mixed-in generic view of ListModel mixin and CreateModel mixin

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	# Same here, 
	# RetieveModel , UpdateModel and DestroyModel mixin are mixed-in in this genreic view
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer