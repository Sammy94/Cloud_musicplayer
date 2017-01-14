

from django.db import models


class Album(models.Model):
    #here you have to create variable
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)


    def __unicode__(self):
        return self.artist + '-'+ self.album_title


class Songs(models.Model):
    albums = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __unicode__(self):
        return self.song_title


