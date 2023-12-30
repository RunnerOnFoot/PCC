from django.shortcuts import render


def index(request):
    """The home page for Meal Plan."""
    return render(request, 'meal_plans/index.html')
