from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import Bookmark

# Create your views here.

#bookmark_mainlist.html
class BookmarkMainlistView(ListView):
    model = Bookmark
    template_name_suffix = '_mainlist'


#bookmark_create.html
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'target_url'] #Fields to be saved
    success_url = reverse_lazy('mainlist') #after completion add bookmark, it will be go to 'list' page
    template_name_suffix = '_create'


#bookmark_detail.html
class BookmarkDetailView(DetailView):
    model = Bookmark

#bookmark_update.html
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'target_url'] #Fields to be updated
    template_name_suffix = '_update'

#bookmark_delete.html
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('mainlist')
    template_name_suffix = '_delete'
