from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Lyrics, \
    Movie, \
    Singer, \
    MusicDirector, \
    Actor, \
    MovieDirector, \
    Language, \
    YouTube, \
    Logo


def movies_data(request):
    all_movies = Movie.objects.all()
    telugu_movies = Movie.objects.filter(Language__Language='Telugu')
    hindi_movies = Movie.objects.filter(Language__Language='Hindi')
    tamil_movies = Movie.objects.filter(Language__Language='Tamil')
    kannada_movies = Movie.objects.filter(Language__Language='Kannada')
    malayalam_movies = Movie.objects.filter(Language__Language='Malayalam')
    english_movies = Movie.objects.filter(Language__Language='English')

    return render(request, 'Lyrics/movies.html', {'all_movies': all_movies,
                                                  'telugu_movies': telugu_movies,
                                                  'hindi_movies': hindi_movies,
                                                  'tamil_movies': tamil_movies,
                                                  'malayalam_movies': malayalam_movies,
                                                  'kannada_movies': kannada_movies,
                                                  'english_movies': english_movies,
                                                  })


def movies_list(request, id):
    m_list = Lyrics.objects.filter(Movie__id=id)
    return render(request, 'Lyrics/movies_songs_list.html', {'m_list': m_list})


def LyricsList(request):
    lyrics_data = Lyrics.objects.all()[::-1]
    telugu_songs = Lyrics.objects.filter(Language__Language='Telugu')
    hindi_songs = Lyrics.objects.filter(Language__Language='Hindi')
    tamil_songs = Lyrics.objects.filter(Language__Language='Tamil')
    kannada_songs = Lyrics.objects.filter(Language__Language='Kannada')
    malayalam_songs = Lyrics.objects.filter(Language__Language='Malayalam')
    english_songs = Lyrics.objects.filter(Language__Language='English')

    return render(request, 'Lyrics/LyricsList.html', {'lyrics_data': lyrics_data,
                                                      'telugu_songs': telugu_songs,
                                                      'hindi_songs': hindi_songs,
                                                      'tamil_songs': tamil_songs,
                                                      'kannada_songs': kannada_songs,
                                                      'malayalam_songs': malayalam_songs,
                                                      'english_songs': english_songs,
                                                      })


def LyricsPage(request, id):
    s_lyrics = get_object_or_404(Lyrics, id=id)
    return render(request, 'Lyrics/LyricsPage.html', {'lp': s_lyrics})


def Languages(request):
    lang_list = Language.objects.all()
    return render(request, 'Lyrics/language.html', {'lang_list': lang_list})


def lang_songs(request, id):
    # l_songs = Lyrics.objects.filter(Language=Language)
    l_songs = Lyrics.objects.filter(Language__id=id)

    return render(request, 'Lyrics/lang_songs.html', {'l_songs': l_songs})


def Singers(request):
    singers_data = Singer.objects.all()
    return render(request, 'Lyrics/singers.html', {"singers_data": singers_data})


def singers_songs(request, id):
    s_songs = Lyrics.objects.filter(Singer__id=id)
    return render(request, 'Lyrics/singers_song_list.html', {'s_songs': s_songs})


def musicDirector(request):
    musicDir_data = MusicDirector.objects.all()
    return render(request, 'Lyrics/musicDirector.html', {'musicDir_data': musicDir_data})


def musicDir_mov(request, id):
    md_mov = Lyrics.objects.filter(MusicDirector__id=id)
    return render(request, 'Lyrics/musicDirector_movies.html', {'md_mov': md_mov})


def actors(request):
    actors_data = Actor.objects.all()
    return render(request, 'Lyrics/actor.html', {'actors_data': actors_data})


def actors_songs(request, id):
    actor_songs = Lyrics.objects.filter(Actor__id=id)
    return render(request, 'Lyrics/actor_songs_list.html', {'actor_songs': actor_songs})


def movieDirector(request):
    movieDir_data = MovieDirector.objects.all()
    return render(request, 'Lyrics/movieDirector.html', {'movieDir_data': movieDir_data})


def movieDir_mov(request, id):
    mod_mov = Lyrics.objects.filter(MovieDirector__id=id)
    return render(request, 'Lyrics/movieDirector_movies.html', {'mod_mov': mod_mov})


def About(request):
    return render(request, 'Lyrics/about.html')


def Contact(request):
    return render(request, 'Lyrics/contact.html')


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        song_search = Lyrics.objects.filter(SongName__contains=searched)
        movie_search = Movie.objects.filter(MovieName__contains=searched)
        actor_search = Actor.objects.filter(FirstName__contains=searched)
        singer_search = Singer.objects.filter(FirstName__contains=searched)
        musicDir_search = MusicDirector.objects.filter(FirstName__contains=searched)
        movieDir_search = MovieDirector.objects.filter(FirstName__contains=searched)
        language_search = Language.objects.filter(Language__contains=searched)

        return render(request, 'Lyrics/search.html', {'searched': searched,
                                                      'song_search': song_search,
                                                      'movie_search': movie_search,
                                                      'actor_search': actor_search,
                                                      'singer_search': singer_search,
                                                      'musicDir_search': musicDir_search,
                                                      'movieDir_search': movieDir_search,
                                                      'language_search': language_search,
                                                      })
    else:
        return render(request, 'Lyrics/search.html')


def actor_bio(request, id):
    actor = get_object_or_404(Actor, id=id)
    return render(request, 'Lyrics/actor_bio.html', {'actor': actor})


def singer_bio(request, id):
    singer = get_object_or_404(Singer, id=id)
    return render(request, 'Lyrics/singer_bio.html', {'singer': singer})


def musicDir_bio(request, id):
    musicDir = get_object_or_404(MusicDirector, id=id)
    return render(request, 'Lyrics/musicDir_bio.html', {'musicDir': musicDir})


def movieDir_bio(request, id):
    movieDir = get_object_or_404(MovieDirector, id=id)
    return render(request, 'Lyrics/movieDir_bio.html', {'movieDir': movieDir})


def video(request):
    youtube_video = YouTube.objects.all()
    return render(request, 'Lyrics/youtube_video.html', {'youtube_video': youtube_video})


def movie_details(request, id):
    mov_details = get_object_or_404(Movie, id=id)
    return render(request, 'Lyrics/movie_details.html', {'mov_details': mov_details})