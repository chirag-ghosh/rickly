from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Scoreline, Tournament, Team, Player, Match
from .serializers import TournamentSerializer, TeamSerializer, PlayerSerializer, MatchSerializer, StatSerializer, ScorelineSerializer
class Index(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin,
):
    def get(self, request):
        return Response('WAOW',status=200)
class TournamentView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the Tournament item by that id
            try:
        # Check if the tournament the user wants to update exists
                queryset = Tournament.objects.get(id=id)
            except Tournament.DoesNotExist:
            # If the tournament does not exist, return an error response
                return Response({'errors': 'This Tournament does not exist.'}, status=400)

        # Serialize tournament item from Django queryset object to JSON formatted data
            read_serializer = TournamentSerializer(queryset)

        else:
        # Get all tournament items from the database using Django's model ORM
            queryset = Tournament.objects.all().exclude(name='Idle Teams')

        # Serialize list of tournament from Django queryset object to JSON formatted data
            read_serializer = TournamentSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)


    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer = TournamentSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():

        # If user data is valid, create a new todo item record in the database
            todo_item_object = create_serializer.save()

        # Serialize the new todo item from a Python object to JSON format
            read_serializer = TournamentSerializer(todo_item_object)

        # Return a HTTP response with the newly created todo item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
      # Check if the todo item the user wants to update exists
            todo_item = Tournament.objects.get(id=id)
        except Tournament.DoesNotExist:
      # If the todo item does not exist, return an error response
            return Response({'errors': 'This tournament does not exist.'}, status=400)

    # If the todo item does exists, use the serializer to validate the updated data
        update_serializer = TournamentSerializer(todo_item, data=request.data)

    # If the data to update the todo item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

      # Data was valid, update the todo item in the database
            todo_item_object = update_serializer.save()

      # Serialize the todo item from Python object to JSON format
            read_serializer = TournamentSerializer(todo_item_object)

      # Return a HTTP response with the newly updated todo item
            return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)
    def delete(self, request, id=None):
        try:
      # Check if the todo item the user wants to update exists
            todo_item = Tournament.objects.get(id=id)
        except Tournament.DoesNotExist:
      # If the todo item does not exist, return an error response
            return Response({'errors': 'This tournament does not exist.'}, status=400)

    # Delete the chosen todo item from the database
        todo_item.delete()

    # Return a HTTP response notifying that the todo item was successfully deleted
        return Response(status=204)
class TournamentUView(
  TournamentView,
):
    def get(self,request,id = None):
        if id:
            try:
                T = Tournament.objects.get(id=id)
                print(T)
                if(T.scheduled == True):
                    return Response({'errors': 'This tournament is scheduled.'}, status = 400)
            except:
                return Response({'errors': 'This tournament does not exist.'}, status=400)
            read_serializer = TournamentSerializer(T)
        else:
        # Get all tournament items from the database using Django's model ORM
            queryset = Tournament.objects.all().filter(scheduled=False).exclude(name='Idle Teams')

        # Serialize list of tournament from Django queryset object to JSON formatted data
            read_serializer = TournamentSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data) 
    def post(self, request, id):
        try:
            T = Tournament.objects.get(id=id)
        except Tournament.DoesNotExist:
            return Response({'errors': 'This tournament does not exist.'}, status=400)
        T.setschedule()
        T.save()
        read_serializer = TournamentSerializer(T)
        return Response(read_serializer.data, status=200)
class TournamentSView(
  TournamentView
):
    def get(self,request,id = None):
        if id:
            try:
                T = Tournament.objects.get(id=id)
                if(T.scheduled == False):
                    return Response({'errors': 'This tournament is not scheduled.'}, status = 400)
            except:
                return Response({'errors': 'This tournament does not exist.'}, status=400)
            read_serializer = TournamentSerializer(T)
        else:
        # Get all tournament items from the database using Django's model ORM
            queryset = Tournament.objects.all().filter(scheduled=True).exclude(name='Idle Teams')

        # Serialize list of tournament from Django queryset object to JSON formatted data
            read_serializer = TournamentSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data) 
    def post(self, request, id):
        try:
            T = Tournament.objects.get(id=id)
        except Tournament.DoesNotExist:
            return Response({'errors': 'This tournament does not exist.'}, status=400)
        T.trycomplete()
        T.save()
        read_serializer = TournamentSerializer(T)
        return Response(read_serializer.data, status=200)
class TournamentCView(
  TournamentView
):
    def get(self,request,id = None):
        if id:
            try:
                T = Tournament.objects.get(id=id)
                if(T.completed == False):
                    return Response({'errors': 'This tournament is not completed.'}, status = 400)
            except:
                return Response({'errors': 'This tournament does not exist.'}, status=400)
            return redirect('/tournaments/'+str(id)+'/')
        # Get all tournament items from the database using Django's model ORM
        try:
            queryset = Tournament.objects.all().filter(completed=True)
        except:
            return Response({'errors:','No scheduled Tournament.'}, status=200)
        # Serialize list of tournament from Django queryset object to JSON formatted data
        read_serializer = TournamentSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data) 
    def post(self, request, id):
        try:
            T = Tournament.objects.get(id=id)
        except Tournament.DoesNotExist:
            return Response({'errors': 'This tournament does not exist.'}, status=400)
        return response(T.data, status=200)
class TeamView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the Team item by that id
            try:
        # Check if the tournament the user wants to update exists
                queryset = Team.objects.get(id=id)
            except Team.DoesNotExist:
            # If the tournament does not exist, return an error response
                return Response({'errors': 'This todo item does not exist.'}, status=400)

        # Serialize tournament item from Django queryset object to JSON formatted data
            read_serializer = TeamSerializer(queryset)

        else:
        # Get all tournament items from the database using Django's model ORM
            queryset = Team.objects.all().exclude(name='Uncapped')

        # Serialize list of tournament from Django queryset object to JSON formatted data
            read_serializer = TeamSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)


    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer = TeamSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():

        # If user data is valid, create a new todo item record in the database
            todo_item_object = create_serializer.save()

        # Serialize the new todo item from a Python object to JSON format
            read_serializer = TeamSerializer(todo_item_object)

        # Return a HTTP response with the newly created todo item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
      # Check if the todo item the user wants to update exists
            todo_item = Team.objects.get(id=id)
        except Team.DoesNotExist:
      # If the todo item does not exist, return an error response
            return Response({'errors': 'This tournament does not exist.'}, status=400)

    # If the todo item does exists, use the serializer to validate the updated data
        update_serializer = TeamSerializer(todo_item, data=request.data)

    # If the data to update the todo item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

      # Data was valid, update the todo item in the database
            todo_item_object = update_serializer.save()

      # Serialize the todo item from Python object to JSON format
            read_serializer = TeamSerializer(todo_item_object)

      # Return a HTTP response with the newly updated todo item
            return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)
    def delete(self, request, id=None):
        try:
      # Check if the todo item the user wants to update exists
            todo_item = Team.objects.get(id=id)
        except Team.DoesNotExist:
      # If the todo item does not exist, return an error response
            return Response({'errors': 'This tournament does not exist.'}, status=400)

    # Delete the chosen todo item from the database
        todo_item.delete()

    # Return a HTTP response notifying that the todo item was successfully deleted
        return Response(status=204)
class PlayerView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the Player item by that id
            try:
        # Check if the tournament the user wants to update exists
                queryset = Player.objects.get(id=id)
            except Player.DoesNotExist:
            # If the tournament does not exist, return an error response
                return Response({'errors': 'This todo item does not exist.'}, status=400)

        # Serialize tournament item from Django queryset object to JSON formatted data
            read_serializer = PlayerSerializer(queryset)

        else:
        # Get all tournament items from the database using Django's model ORM
            queryset = Player.objects.all()

        # Serialize list of tournament from Django queryset object to JSON formatted data
            read_serializer = PlayerSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)


    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer = PlayerSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():

        # If user data is valid, create a new todo item record in the database
            todo_item_object = create_serializer.save()

        # Serialize the new todo item from a Python object to JSON format
            read_serializer = PlayerSerializer(todo_item_object)

        # Return a HTTP response with the newly created todo item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
      # Check if the todo item the user wants to update exists
            todo_item = Player.objects.get(id=id)
        except Player.DoesNotExist:
      # If the todo item does not exist, return an error response
            return Response({'errors': 'This tournament does not exist.'}, status=400)

    # If the todo item does exists, use the serializer to validate the updated data
        update_serializer = PlayerSerializer(todo_item, data=request.data)

    # If the data to update the todo item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

      # Data was valid, update the todo item in the database
            todo_item_object = update_serializer.save()

      # Serialize the todo item from Python object to JSON format
            read_serializer = PlayerSerializer(todo_item_object)

      # Return a HTTP response with the newly updated todo item
            return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)
    def delete(self, request, id=None):
        try:
      # Check if the todo item the user wants to update exists
            todo_item = Player.objects.get(id=id)
        except Player.DoesNotExist:
      # If the todo item does not exist, return an error response
            return Response({'errors': 'This tournament does not exist.'}, status=400)

    # Delete the chosen todo item from the database
        todo_item.delete()

    # Return a HTTP response notifying that the todo item was successfully deleted
        return Response(status=204)

class MatchView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the Match item by that id
            try:
        # Check if the tournament the user wants to update exists
                queryset = Match.objects.get(id=id)
            except Match.DoesNotExist:
            # If the tournament does not exist, return an error response
                return Response({'errors': 'This todo item does not exist.'}, status=400)

        # Serialize tournament item from Django queryset object to JSON formatted data
            read_serializer = MatchSerializer(queryset)

        else:
        # Get all tournament items from the database using Django's model ORM
            queryset = Match.objects.all()

        # Serialize list of tournament from Django queryset object to JSON formatted data
            read_serializer = MatchSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)


    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer = MatchSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():

        # If user data is valid, create a new todo item record in the database
            todo_item_object = create_serializer.save()

        # Serialize the new todo item from a Python object to JSON format
            read_serializer = MatchSerializer(todo_item_object)

        # Return a HTTP response with the newly created todo item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
      # Check if the todo item the user wants to update exists
            todo_item = Match.objects.get(id=id)
        except Match.DoesNotExist:
      # If the todo item does not exist, return an error response
            return Response({'errors': 'This tournament does not exist.'}, status=400)

    # If the todo item does exists, use the serializer to validate the updated data
        update_serializer = MatchSerializer(todo_item)

    # If the data to update the todo item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

      # Data was valid, update the todo item in the database
            todo_item_object = update_serializer.save()

      # Serialize the todo item from Python object to JSON format
            read_serializer = MatchSerializer(todo_item_object)

      # Return a HTTP response with the newly updated todo item
            return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)
    def delete(self, request, id=None):
        try:
      # Check if the todo item the user wants to update exists
            todo_item = Match.objects.get(id=id)
        except Match.DoesNotExist:
      # If the todo item does not exist, return an error response
            return Response({'errors': 'This tournament does not exist.'}, status=400)

    # Delete the chosen todo item from the database
        todo_item.delete()

    # Return a HTTP response notifying that the todo item was successfully deleted
        return Response(status=204)

class StatView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the Match item by that id
            try:
        # Check if the tournament the user wants to update exists
                t = Tournament.objects.get(id=id)
                queryset = []
                for q in t.team_set.all():
                    for x in q.player_set.all():
                        queryset.append(x)
            except Tournament.DoesNotExist:
            # If the tournament does not exist, return an error response
                return Response({'errors': 'This todo item does not exist.'}, status=400)

        # Serialize tournament item from Django queryset object to JSON formatted data
            read_serializer = StatSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)
class ScorelineView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the Match item by that id
            try:
        # Check if the tournament the user wants to update exists
                queryset = Scoreline.objects.get(id=id)
            except Scoreline.DoesNotExist:
            # If the tournament does not exist, return an error response
                return Response({'errors': 'This todo item does not exist.'}, status=400)

        # Serialize tournament item from Django queryset object to JSON formatted data
            read_serializer = ScorelineSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)
