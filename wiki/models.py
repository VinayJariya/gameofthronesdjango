from django.db import models

# Create your models here.

class House(models.Model):
    house_name = models.CharField(max_length = 100)
    banner = models.CharField(max_length = 500)
    current_ruler = models.CharField(max_length = 100)
    slogan = models.CharField(max_length = 200)
    sigil = models.CharField(max_length = 200)
    founder = models.CharField(max_length = 100)
    region = models.CharField(max_length = 50)
    religion = models.CharField(max_length = 50)
    description = models.CharField(max_length = 4000)

    def __str__(self):
        return self.house_name + ' - ' + self.slogan

class Character(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    photo = models.CharField(max_length = 1000)
    alive = models.BooleanField(default = True)
    title = models.CharField(max_length = 100)
    portrayed_by = models.CharField(max_length = 100)
    description = models.CharField(max_length = 4000)

    def __str__(self):
        return self.name + ' of House ' + self.house.house_name
