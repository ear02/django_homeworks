from django.contrib import admin
from django.urls import path, include

app_name = 'journal'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls', namespace='journal')),
]
