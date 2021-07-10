from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name = "top"),
    path("prefecture/<str:article_id>",views.prefecture, name="prefecture"),
    path("weather/<str:article_id>",views.weather, name="weather"),
    path("select/<str:article_id>",views.select, name="select"),
    path("weather2/<str:article_id>",views.weather2, name="weather2"),
    path("gaiyou",views.gaiyou, name="gaiyou"),
    path("toukou",views.toukou, name="toukou"),
]