from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'music'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('password_change_form/', views.password_change_form, name='password_change_form'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='music/password_reset.html'),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='music/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='music/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='music/password_reset_complete.html'),
         name='password_reset_complete'),

    path('create_album/', views.create_album, name='create_album'),
    path('<int:album_id>/', views.detail, name='detail'),
    path('<int:album_id>/create_song/', views.create_song, name='create_song'),
    re_path(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    re_path(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    re_path(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    re_path(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
    re_path(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),

]
