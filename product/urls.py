from django.urls import path
from . import views
urlpatterns = [
    path('',views.Categoryview, name="Category"),
    path('task-list/',views.CategoryListview, name="task-List"),

]