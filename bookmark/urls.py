from django.urls import path
from .views import BookmarkMainlistView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    path('', BookmarkMainlistView.as_view(), name='mainlist'), #as_vew() should be used in the class view
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'), #int type Primary Key
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]