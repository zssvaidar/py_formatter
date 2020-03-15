from django.urls import path
from .views import ProfileListView, ProfileView, ProfileParserView
urlpatterns = [
    path('', ProfileListView.as_view(), name='profilers'),
    path('<int:pk>/', ProfileView.as_view(), name= 'profiler'),
    path('<int:pk>/parsed', ProfileParserView.as_view(), name= 'profiler_parsed'),
    path('<int:pk>/parsed1', ProfileParserView.as_view(), name= 'profiler_parsed_date'),


]
