from django.db import models

# Create your models here.
class Room(models.Model):
    room_number=models.IntegerField(blank=False)
    type_room=models.CharField(max_length=200, blank=False)
    receptions=models.CharField(max_length=200,blank=False)
    floor=models.IntegerField(blank=False)

    def __str__(self):
        return self.receptions