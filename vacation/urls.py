from django.contrib import admin
from django.urls import path, include
import crud.urls
import crud.views
import accounts.urls
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.welcome, name="welcome"),
    path('crud/', include(crud.urls)),
    path('accounts/', include(accounts.urls)),
]
