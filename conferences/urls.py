from django .urls import path
from . import views



urlpatterns  = [
    path('',views.conference,name="conference"),
    path('conferences/create/',views.createconference,name="create"),
    path('conferences/<str:pk>/',views.individualconference),
    path('conferences/<str:pk>/update/',views.updateconference),
    path('conferences/<str:pk>/delete/',views.deleteconference)
]