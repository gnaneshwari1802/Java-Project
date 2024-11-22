from django.db import models

# Create your models here.


class Destination(models.Model):
    # id: int
    name = models.CharField(max_length=100, default="Unnamed Destination")  # Add a default value here
    img = models.ImageField(upload_to='pics', blank=True, null=True)  # Image field, optional (nullable)
    desc = models.TextField(default="No description")  # Provide a default description if not provided
    price = models.IntegerField()  # <-- Set default value here
    offer = models.BooleanField(default=False)  # Optional offer field, default to False

def __str__(self):
    return self.name