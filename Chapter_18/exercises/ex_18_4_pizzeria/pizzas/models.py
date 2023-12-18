from django.db import models

# Create your models here.


class Pizza(models.Model):
    """Represent a pizza that can be ordered from the pizzeria."""
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the name of the pizza."""
        return self.name


class Topping(models.Model):
    """Represent a topping that can be added to a pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Toppings"

    def __str__(self):
        """Return the name of the topping."""
        if len(self.name) > 25:
            return f"{self.name[:25]}..."
        else:
            return self.name
