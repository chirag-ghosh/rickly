from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index.as_view(),name = 'index'),
    path('tournaments/',views.TournamentView.as_view()),
    path('tournaments/<int:id>/',views.TournamentView.as_view()),
    path('tournaments/unscheduled/',views.TournamentUView.as_view()),
    path('tournaments/unscheduled/<int:id>/',views.TournamentUView.as_view()),
    path('tournaments/scheduled/',views.TournamentSView.as_view()),
    path('tournaments/scheduled/<int:id>/',views.TournamentSView.as_view()),
]