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
    path('tournaments/completed/',views.TournamentCView.as_view()),
    path('tournaments/completed/<int:id>/',views.TournamentCView.as_view()),
    path('teams/',views.TeamView.as_view()),
    path('teams/<int:id>/',views.TeamView.as_view()),
    path('players/',views.PlayerView.as_view()),
    path('players/<int:id>/',views.PlayerView.as_view()),
    path('matches/',views.MatchView.as_view()),
    path('matches/<int:id>/',views.MatchView.as_view()),
    path('tournaments/<int:id>/stats/',views.StatView.as_view()),
]
