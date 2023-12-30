from django.db import models


class Meal(models.Model):
    """
    An model for a single meal.
    """
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the meal.
        """
        return self.name


class MealItem(models.Model):
    """
    An individual part of a meal.
    """
    name = models.CharField(max_length=200)
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name='items')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the meal item.
        """
        return self.name
