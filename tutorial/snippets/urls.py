from django.conf.urls import url
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns

"""
For function based views

urlpatterns = [
	url('^snippets/$', views.snippet_list),
	url('^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
"""


urlpatterns = [
	url(r'^snippets/$', views.SnippetList.as_view()),
	url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),	
]
urlpatterns = format_suffix_patterns(urlpatterns)