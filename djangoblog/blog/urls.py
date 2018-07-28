from django.conf.urls import url
from . import views


# Add url patterns here
# These url patterns will direct links to the associated view 
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^about/$', views.about_page, name='about_page'),
    url(r'^search/$', views.search_posts, name='search_page'),
    url(r'^projects/$', views.projects_page, name='projects_page'),
    url(r'^resume/$', views.resume_page, name='resume_page'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]