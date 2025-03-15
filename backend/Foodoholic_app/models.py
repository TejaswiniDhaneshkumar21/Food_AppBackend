from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    genus = models.CharField(max_length=100, blank=True)
    family = models.CharField(max_length=100, blank=True)
    order = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

# Removed the old Food model since we are now using FoodInfo for all backend CRUD operations.

class FoodInfo(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    sugar = models.FloatField(null=True, blank=True)
    calories = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'Food_Info'  # This ensures the table name is exactly "Food_Info"

    def __str__(self):
        return self.name
