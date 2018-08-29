# -*- coding: utf-8 -*-
import json
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from api.models import Food

# Create your tests here.
class Test_FoodTestCase(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

    def test_get_all_foods(self):
        """All foods are indexed for GET /api/v1/foods"""
        Food.objects.create(name="kiwi", calories=55)
        Food.objects.create(name="banana", calories=98)
        Food.objects.create(name="tacos", calories=325)
        Food.objects.create(name="rice", calories=120)

        foods = Food.objects.all()
        food = foods[0]
        self.assertEqual(len(foods), 4)
        self.assertEqual(food.name, "kiwi")
        self.assertEqual(food.calories, 55)

        response = self.client.get('/api/v1/foods/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = response.json()
        self.assertEqual(len(result), 4)



# Create your tests here.
