from django.conf.urls import url 
from user import views 
 
urlpatterns = [ 
    url(r'^users/$', views.users_list),
    url(r'^register/$', views.register_user),
    url(r'^delete/(?P<pk>[0-9]+)$', views.user_del),
    url(r'^role/(?P<pk>[0-9]+)$', views.user_role),
]