from django.db import models

# Create your models here.


class Pizza(models.Model):
    """Represent a pizza that can be ordered from the pizzeria."""
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the name of the pizza."""
        return self.name
