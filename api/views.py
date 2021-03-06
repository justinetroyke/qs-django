from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from api.serializers import FoodSerializer
from rest_framework import viewsets
from api.models import Food
from rest_framework.response import Response
import json

class FoodViews(viewsets.ViewSet):
    def list(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    def retrieve(self, request, food_id=None):
        foods = Food.objects.all()
        food = get_object_or_404(foods, id=food_id)
        serializer = FoodSerializer(food)
        return Response(serializer.data)
