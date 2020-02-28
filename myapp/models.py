from django.db import models


class MyModel(models.Model):
    CHOICES = [(0, "Zero"), (1, "One")]

    some_integer_choice_field = models.IntegerField(choices=CHOICES)
    a1 = models.CharField(max_length=255)
    a2 = models.CharField(max_length=255)
    a3 = models.CharField(max_length=255)
    a4 = models.CharField(max_length=255)

    some_boolean_field = models.BooleanField()
    b1 = models.CharField(max_length=255)
    b2 = models.CharField(max_length=255)
    b3 = models.CharField(max_length=255)
