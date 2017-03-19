from .models import Snippet
from .serializers import SnippetSerializer

from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
	mixins.CreateModelMixin, generics.GenericAPIView):
	
	# We are creating our app using the genericAPIView

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)
		# .list() comes from ListModelMixin

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
		# .create() comes from CreateModelMixin

# mixins have ModelMixins respective to the CRUD processes
class SnippetDetail(mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin, mixins.DestroyModelMixin,
	generics.GenericAPIView):
	
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def update(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)