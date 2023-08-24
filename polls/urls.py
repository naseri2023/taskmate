from django.urls import path
from . import views

app_name="polls"
urlpatterns=[path("",views.index,name="index"),
             path("about",views.index2,name="index2"),
             path("delete/<list_id>",views.delete,name="delete"),
             path("croos_off/<list_id>",views.cross_off,name="cross_off"),
             path("uncroos/<list_id>",views.uncross,name="uncross"),
             path("edit/<list_id>",views.edit,name="edit")
             ]