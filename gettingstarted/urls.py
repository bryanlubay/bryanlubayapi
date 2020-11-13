from django.urls import path, include
from django.contrib import admin
from hello import views

admin.autodiscover()

import hello.views

urlpatterns = [
    path("get_data/<str:state>/", views.get_data, name="get_data"),
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
