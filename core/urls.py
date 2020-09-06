from django.urls import path, include


from . import views as core_views

app_name='core'

urlpatterns = [
	path('', core_views.index, name='index'),
	path('search-word/', core_views.search_word, name="search_word"),
]