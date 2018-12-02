from django.db import models
from django.utils import timezone


class recipe(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    details = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    # brewing_date = models.DateTimeField(
    #         blank=True, null=True)

    def stage(self):
        rice = models.IntegerField()
        water = models.IntegerField()
        yeast = models.IntegerField()
        flour = models.IntegerField()
        sub_ingredient = models.IntegerField()
        term = models.IntegerField()
