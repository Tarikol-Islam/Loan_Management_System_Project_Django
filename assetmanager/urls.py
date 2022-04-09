from django.urls import path
from . import views 


app_name='assetmanager'
urlpatterns = [
    path('', views.assetList.as_view(), name='assetlist'),
    path('create/', views.createAsset, name='create_asset'),
    path('update/(?P<id>\d+)/', views.asset_update, name="update_asset"),
    path('delete/(?P<id>\d+)/', views.asset_delete, name="delete_asset"),
	]