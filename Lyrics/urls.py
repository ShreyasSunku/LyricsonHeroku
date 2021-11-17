from django.urls import path
from . import views

urlpatterns = [

    path('', views.LyricsList, name='lyricsList'),
    path('Languages/', views.Languages, name='languages'),
    path('Singers/', views.Singers, name='singers'),
    path('MusicDirectors/', views.musicDirector, name='musicDirector'),
    path('MovieDirectors/', views.movieDirector, name='movieDirector'),
    path('About/', views.About, name='about'),
    path('Contact/', views.Contact, name='contact'),
    path('Actors/', views.actors, name='actor'),
    path('Lyrics/<int:id>/', views.LyricsPage, name='lyrics'),
    path('Singers/<int:id>/', views.singers_songs, name='singerSongs'),
    path('MusicDirector/<int:id>/', views.musicDir_mov, name='musicDir_mov'),
    path('MovieDirector/<int:id>/', views.movieDir_mov, name='movieDir_mov'),
    path('Actor/<int:id>/', views.actors_songs, name='actors_songs'),
    # path('Language/<slug:Language>/', views.lang_songs, name='lang_songs'),
    path('Language/<int:id>/', views.lang_songs, name='lang_songs'),
    path('search/', views.search, name='search'),
    path('movies/', views.movies_data, name='movies_data'),
    path('movies/<int:id>/', views.movies_list, name='m_list'),
    path('actor/bio/<int:id>/', views.actor_bio, name='actor_bio'),
    path('singer/bio/<int:id>/', views.singer_bio, name='singer_bio'),
    path('MusicDirector/bio/<int:id>/', views.musicDir_bio, name='musicDir_bio'),
    path('MovieDirector/bio/<int:id>/', views.movieDir_bio, name='movieDir_bio'),
    path('youtube/', views.video, name='youtube'),
    path('MovieDetails/<int:id>/', views.movie_details, name='movie_details'),
]