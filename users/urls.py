from django.conf.urls import patterns, url
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^signup/$', views.signup, name='signup'),
                       url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
                       url(r'^logout/$', auth_views.logout, {'next_page': 'items'}, name='logout'),
                       url(r'^users_data/$', views.users_data, name='users_data'),
                       url(r'^create_item/$', views.create_item, name='create_item'),
                       url(r'^items/$', views.items, name='items'),
                       url(r'^item/(?P<item_id>\d+)$', views.show_item, name='show_item'),
                       url (r'^edit_item/(?P<item_id>\d+)$', views.edit_item, name='edit_item'),
                       url(r'^delete_item/(?P<item_id>\d+)$', views.delete_item, name='delete_item'),
                       url(r'^user_item/(?P<item_id>\d+)$', views.user_item, name='user_item'),
                       url(r'^search$', views.search, name='search'),
                       url(r'ajax/validate_username/$', views.validate_username, name='validate_username'),
                       url(r'ajax/update_interaction', views.update_interaction, name='update_interaction'),
                       )
