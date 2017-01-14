
from .models import Album,Songs
from django.shortcuts import render,get_object_or_404


def index(request):
    all_albums=Album.objects.all()
    #context={'all_albums':all_albums}
    return render(request, 'music/index.html', {'all_albums':all_albums})


def detail(request , album_id):
    album=get_object_or_404(Album, pk=album_id) #replaces all the try except statement in one line
    return render(request, 'music/detail.html', {'album':album})


def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.songs_set.get(pk=request.POST['song'])
    except (KeyError , Songs.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album,'error_message':"You did not select a valid song",})
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})