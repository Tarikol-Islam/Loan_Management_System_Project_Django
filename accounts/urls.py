from django.urls import path
from . import views
from .views import clientList

app_name='accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('borrower/',clientList.as_view(), name="clientlist" ),
	path('borrower/update/(?P<id>\d+)/',views.clientUpdate, name='update_client'),
	path('borrower/create/',views.createCLient, name='create_client'),
	path('borrower/delete/(?P<id>\d+)/', views.clientDelete, name='delete_client'),
	]

