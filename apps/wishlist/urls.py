from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^createItem$', views.createItem),
    url(r'^dashboard$', views.dashboard),
    url(r'^show_item$',views.show_item),
    url(r'^delete/(?P<item_id>\d+)$',views.delete),
    url(r'^results/(?P<item_id>\d+)$', views.results),
    url(r'^create/(?P<item_id>\d+)$', views.create),
    url(r'^removeItem/(?P<item_id>\d+)$', views.removeItem),
    

]       