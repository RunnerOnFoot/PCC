from django.contrib import admin

from .models import Meal
from .models import MealItem

admin.site.register(Meal)
admin.site.register(MealItem)
