from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):

    # Relationships
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    # Fields
    nickname = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to="upload/profile/")
    desc = models.TextField(max_length=200)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("game_Profile_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("game_Profile_update", args=(self.pk,))


class Room(models.Model):

    # Relationships
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=20)
    
    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("game_Room_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("game_Room_update", args=(self.pk,))


class Escmap(models.Model):

    # Relationships
    room = models.ForeignKey("game.room", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    order = models.IntegerField()
    name = models.CharField(max_length=20)
    mapdata = models.JSONField(default={ 
        'mapWidth' : 12,
        'mapHeight' : 12,
        'tiles' : [],
        'block' : [],
        'objects' : [],
        'events' : [],
        } )

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("game_Escmap_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("game_Escmap_update", args=(self.pk,))


class Access(models.Model):

    # Relationships
    target_map = models.OneToOneField("game.escmap", on_delete=models.CASCADE)

    # Fields
    code = models.CharField(max_length=9)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("game_Access_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("game_Access_update", args=(self.pk,))