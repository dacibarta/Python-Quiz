from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("question/", views.add_question),
    path("question/addrecord", views.add_question_record),
]
