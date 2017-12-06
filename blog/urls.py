from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/$', views.newPost, name='new_post'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.viewPost, name='view_post'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editPost, name='edit_post'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.deletePost, name='delete_post'),

    url(r'^user(?:/(?P<step>[0-9]))?/$', views.newUser, name='user_new'),
    url(r'^user/usercheck/$', views.signupUserCheck, name='user_signup_check'),
    url(r'^user/(?P<userName>\w+)/$', views.viewUser, name='user_view'),
    url(r'^user/(?P<userName>\w+)/posts/$', views.postsUser, name='user_posts'),
    url(r'^user/(?P<userName>\w+)/edit/$', views.editUser, name='user_edit'),
    url(r'^user/confirm/(?P<hashCode>\w+)/edit/$', views.confirmUser, name='user_confirm'),

    url(r'^login/$', views.loginUser, name='user_login'),
    url(r'^login/usercheck/$', views.loginUserCheck, name='user_login_check'),
    url(r'^logout/$', views.logoutUser, name='user_logout'),

]
