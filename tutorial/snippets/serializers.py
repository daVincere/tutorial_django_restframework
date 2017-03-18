from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

"""
class SnippetSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required= False, allow_blank=True, max_length=100)
	code = serializers.CharField(style={'base_template': 'textarea.html'})
	lineos = serializers.BooleanField(required=False)
	language= serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

	def create(self, validated_data):
		
		//create and return a new 'snippet' instance, given the validated data
		
		return Snippet.objects.create(**validated_data)

	def update(self, instance, validated_data):
		
		// Update and return an existing "snippet" instance
		// given the validated data
		
		instance.title = validated_data.GET('title', instance.title)
		instance.code = validated_data.GET('code', instance.code)
		instance.lineos = validated_data.GET('lineos', instance.lineos)
		instance.language = validated_data.GET('language', instance.language)
		instance.style = validated_data.GET('style', instance.style)
		instance.save()

		return instance

"""

# Equivalent of what's written above

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

	"""
	ModelSerializer classes assist in the following ways:
		1) automatic determination of fields
		2) simple default implementation of create() and update() methods
	"""

"""
Serializer class in Django is very similar to the form class, and includes
various validation flags on the various fields, such as 
required, max_length and default etc
"""

