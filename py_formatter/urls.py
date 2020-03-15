from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',include(('py_formatter.apps.profiler.urls', 'profiler'), namespace='profiler')),
    path('api/profiler/',include(('py_formatter.apps.profiler.api.urls', 'profiler-gc'), namespace='profiler-gc')),
]
if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)




# from django.conf import settings
# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls.static import static
# from .apps.profiler.api.views import ProfileListView
# from rest_framework import routers
# router = routers.DefaultRouter()
# #
# router.register(r'profiler', ProfileListView, basename ='profiler')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('/',include((router.urls, 'profiler'), namespace='profiler')),
#     path('api/',include((router.urls, 'profiler-gc'), namespace='profiler-gc')),
# ]
# urlpatterns += router.urls
# if(settings.DEBUG):
#     urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#     urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
