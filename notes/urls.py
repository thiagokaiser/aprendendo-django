from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'notes'
urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^cadastra/$', views.Cadastra, name='cadastra'),
    url(r'^lista/$', views.Lista, name='lista'),
    url(r'^note/(?P<pk>\d+)/edita/$', views.Edita, name='edita'),
    url(r'^note/(?P<pk>\d+)/detalhe/$', views.Detalhe, name='detalhe'),
    url(r'^note/(?P<pk>\d+)/delete/$', views.Delete, name='delete'),        
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),        
    url(r'^logout/$', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='logout'), 
    url(r'^profile/$', views.Profile , name='profile'),
    url(r'^profile/edit/$', views.Edit_profile , name='edit_profile'),
    url(r'^register/$', views.Register , name='register'),
    url(r'^change-password/$', views.Change_Password , name='change-password'),
    url(r'^responsavel/$', views.Add_Responsavel , name='add-responsavel'),
    url(r'^responsavel/(?P<pk>\d+)/Edit$', views.Edit_Responsavel , name='edit-responsavel'),

]
