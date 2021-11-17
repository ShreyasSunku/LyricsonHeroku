from django.db import models
from embed_video.fields import EmbedVideoField


Gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others"),
)

class Logo(models.Model):
    Logo_Image = models.ImageField(upload_to='images/Logo/', null=True, blank=True)


class Actor(models.Model):
    FirstName = models.CharField(max_length=50)
    FamilyName = models.CharField(max_length=50, null=True, blank=True)
    FullName = models.CharField(max_length=50, null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=Gender_choices)
    DoB = models.DateField(null=True, blank=True)
    DoD = models.DateField(null=True, blank=True)
    BirthPlace = models.CharField(max_length=50, null=True, blank=True)
    Awards = models.TextField(max_length=500, null=True, blank=True)
    Upload = models.ImageField(upload_to='images/Actor/', null=True, blank=True)

    def __str__(self):
        return self.FirstName


class Singer(models.Model):
    FirstName = models.CharField(max_length=50)
    FamilyName = models.CharField(max_length=50, null=True, blank=True)
    FullName = models.CharField(max_length=50, null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=Gender_choices)
    DoB = models.DateField(null=True, blank=True)
    DoD = models.DateField(null=True, blank=True)
    BirthPlace = models.CharField(max_length=50, null=True, blank=True)
    Awards = models.TextField(max_length=500, null=True, blank=True)
    Upload = models.ImageField(upload_to='images/Singer/', null=True, blank=True)

    def __str__(self):
        return self.FirstName


class MusicDirector(models.Model):
    FirstName = models.CharField(max_length=50)
    FamilyName = models.CharField(max_length=50, null=True, blank=True)
    FullName = models.CharField(max_length=50, null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=Gender_choices)
    DoB = models.DateField(null=True, blank=True)
    DoD = models.DateField(null=True, blank=True)
    BirthPlace = models.CharField(max_length=50, null=True, blank=True)
    Awards = models.TextField(max_length=500, null=True, blank=True)
    Upload = models.ImageField(upload_to='images/MusicDirector/', null=True, blank=True)

    def __str__(self):
        return self.FirstName


class MovieDirector(models.Model):
    FirstName = models.CharField(max_length=50)
    FamilyName = models.CharField(max_length=50, null=True, blank=True)
    FullName = models.CharField(max_length=50, null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=Gender_choices)
    DoB = models.DateField(null=True, blank=True)
    DoD = models.DateField(null=True, blank=True)
    BirthPlace = models.CharField(max_length=50, null=True, blank=True)
    Awards = models.TextField(max_length=500, null=True, blank=True)
    Upload = models.ImageField(upload_to='images/MovieDirector/', null=True, blank=True)

    def __str__(self):
        return self.FirstName


class Studio(models.Model):
    StudioName = models.CharField(max_length=50)
    Upload = models.ImageField(upload_to='images/Studio/', null=True, blank=True)

    def __str__(self):
        return self.StudioName


class Producer(models.Model):
    FirstName = models.CharField(max_length=50)
    FamilyName = models.CharField(max_length=50, null=True, blank=True)
    FullName = models.CharField(max_length=50, null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=Gender_choices)
    DoB = models.DateField(null=True, blank=True)
    DoD = models.DateField(null=True, blank=True)
    BirthPlace = models.CharField(max_length=50, null=True, blank=True)
    Awards = models.TextField(max_length=500, null=True, blank=True)
    Upload = models.ImageField(upload_to='images/Producer/', null=True, blank=True)

    def __str__(self):
        return self.FirstName


class Country(models.Model):
    Country = models.CharField(max_length=50)
    Upload = models.ImageField(upload_to='images/Country/', null=True, blank=True)

    def __str__(self):
        return self.Country


class Wood(models.Model):
    WoodName = models.CharField(max_length=50)
    Upload = models.ImageField(upload_to='images/Wood/', null=True, blank=True)

    def __str__(self):
        return self.WoodName


class Language(models.Model):
    Language = models.CharField(max_length=50)
    Upload = models.ImageField(upload_to='images/Language/', null=True, blank=True)

    def __str__(self):
        return self.Language


class Genre(models.Model):
    Genre = models.CharField(max_length=50)
    Upload = models.ImageField(upload_to='images/Genre/', null=True, blank=True)

    def __str__(self):
        return self.Genre


class Certificate(models.Model):
    Certificate = models.CharField(max_length=50)
    Upload = models.ImageField(upload_to='images/Certificate/', null=True, blank=True)

    def __str__(self):
        return self.Certificate


class YouTube(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    youtube = EmbedVideoField()

    def __str__(self):
        return self.Name


class Movie(models.Model):
    MovieName = models.CharField(max_length=50)
    Actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    ReleaseDate = models.DateField(null=True, blank=True)
    MovieDirector = models.ForeignKey(MovieDirector, on_delete=models.CASCADE)
    MusicDirector = models.ForeignKey(MusicDirector, on_delete=models.CASCADE)
    Studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    Producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    Wood = models.ForeignKey(Wood, on_delete=models.CASCADE)
    Language = models.ForeignKey(Language, on_delete=models.CASCADE)
    Genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    RunTimeMinutes = models.IntegerField(null=True)
    Certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    Review = models.CharField(max_length=100, null=True, blank=True)
    Upload = models.ImageField(upload_to='images/Movie/', null=True, blank=True)
    YouTube = models.ForeignKey(YouTube, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.MovieName


class Lyrics(models.Model):
    SongName = models.CharField(max_length=50)
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    Actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True, blank=True)
    Singer = models.ForeignKey(Singer, on_delete=models.CASCADE, null=True, blank=True)
    MovieDirector = models.ForeignKey(MovieDirector, on_delete=models.CASCADE, null=True, blank=True)
    MusicDirector = models.ForeignKey(MusicDirector, on_delete=models.CASCADE, null=True, blank=True)
    Language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    Lyrics = models.TextField(null=True, blank=True)
    MusicLabel = models.CharField(max_length=50, null=True, blank=True)
    Upload = models.ImageField(upload_to='images/Lyrics/', null=True, blank=True)
    YouTube = models.ForeignKey(YouTube, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.SongName


