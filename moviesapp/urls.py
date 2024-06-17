from django.urls import path
from . views import ShowList, ShowDetail
from django.views.generic import RedirectView
#from . import views
from moviesapp.views import UpdateShowView 
from .views import ShowListByYear

urlpatterns = [
path('', RedirectView.as_view(url='get/shows/')),  # Redirect empty path to your desired URL
    
    # URL patterns for listing all shows and creating a new show
    path('get/shows/', ShowList.as_view(), name='get-shows'),  # GET request to list all shows
    path('post/shows/', ShowList.as_view(), name='post-shows'),  # POST request to create a new show

    # URL patterns for retrieving, updating, and deleting a particular show
    path('get/shows/<int:pk>/', ShowDetail.as_view(), name='get-show'),  # GET request to retrieve a show
    path('put/shows/<int:pk>/', UpdateShowView.as_view(), name='update-show'),  # PUT request to update a show
    path('delete/shows/<int:pk>/', ShowDetail.as_view(), name='delete-show'),  # DELETE request to delete a show

    path('shows/', ShowListByYear.as_view(), name='show-list'),
]   

