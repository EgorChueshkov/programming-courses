from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('teachers', views.teacher, name='teacher'),
    path('groups', views.group, name='group'),
    #path('groups/ditail-group', views.ditail_group, name='ditail-group'),
    path('create', views.create, name='create'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail')
]