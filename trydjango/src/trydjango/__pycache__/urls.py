from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from pages import home_view # type: ignore

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),

]