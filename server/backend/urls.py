from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dealership.urls', module='dealership.urls', namespace='api')),
]

from dealership.urls import djangoapp_urlpatterns
urlpatterns += [
    path('djangoapp/', include(djangoapp_urlpatterns)),
]
