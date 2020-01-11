from django.urls import path,include
#from .views import SchoolListView,SchoolDetailedView,SchoolCreateView,SchoolUpdateView,SchoolDeleteView
from . import views
from django.contrib.auth import views as auth_views
app_name='feedback'

urlpatterns=[
   path('',views.CommentCreateView.as_view(),name='home'),
   path('list/',views.CommentListView.as_view(),name='list'),
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  # url(r'^download/(?P<path>.*)$', serve, {'document root': settings.MEDIA_ROOT})
   path('download/',views.download,name='download')
]
