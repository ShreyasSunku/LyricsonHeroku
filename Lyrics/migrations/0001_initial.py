# Generated by Django 3.2.7 on 2021-11-17 06:34

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('FamilyName', models.CharField(blank=True, max_length=50, null=True)),
                ('FullName', models.CharField(blank=True, max_length=50, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('DoB', models.DateField(blank=True, null=True)),
                ('DoD', models.DateField(blank=True, null=True)),
                ('BirthPlace', models.CharField(blank=True, max_length=50, null=True)),
                ('Awards', models.TextField(blank=True, max_length=500, null=True)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/Actor/')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Certificate', models.CharField(max_length=50)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/Certificate/')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=50)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/Country/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Genre', models.CharField(max_length=50)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/Genre/')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(max_length=50)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/Language/')),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo_Image', models.ImageField(blank=True, null=True, upload_to='images/Logo/')),
            ],
        ),
        migrations.CreateModel(
            name='MovieDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('FamilyName', models.CharField(blank=True, max_length=50, null=True)),
                ('FullName', models.CharField(blank=True, max_length=50, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('DoB', models.DateField(blank=True, null=True)),
                ('DoD', models.DateField(blank=True, null=True)),
                ('BirthPlace', models.CharField(blank=True, max_length=50, null=True)),
                ('Awards', models.TextField(blank=True, max_length=500, null=True)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/MovieDirector/')),
            ],
        ),
        migrations.CreateModel(
            name='MusicDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('FamilyName', models.CharField(blank=True, max_length=50, null=True)),
                ('FullName', models.CharField(blank=True, max_length=50, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('DoB', models.DateField(blank=True, null=True)),
                ('DoD', models.DateField(blank=True, null=True)),
                ('BirthPlace', models.CharField(blank=True, max_length=50, null=True)),
                ('Awards', models.TextField(blank=True, max_length=500, null=True)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/MusicDirector/')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('FamilyName', models.CharField(blank=True, max_length=50, null=True)),
                ('FullName', models.CharField(blank=True, max_length=50, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('DoB', models.DateField(blank=True, null=True)),
                ('DoD', models.DateField(blank=True, null=True)),
                ('BirthPlace', models.CharField(blank=True, max_length=50, null=True)),
                ('Awards', models.TextField(blank=True, max_length=500, null=True)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/Producer/')),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('FamilyName', models.CharField(blank=True, max_length=50, null=True)),
                ('FullName', models.CharField(blank=True, max_length=50, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('DoB', models.DateField(blank=True, null=True)),
                ('DoD', models.DateField(blank=True, null=True)),
                ('BirthPlace', models.CharField(blank=True, max_length=50, null=True)),
                ('Awards', models.TextField(blank=True, max_length=500, null=True)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/Singer/')),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudioName', models.CharField(max_length=50)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/Studio/')),
            ],
        ),
        migrations.CreateModel(
            name='Wood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WoodName', models.CharField(max_length=50)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/Wood/')),
            ],
        ),
        migrations.CreateModel(
            name='YouTube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('youtube', embed_video.fields.EmbedVideoField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MovieName', models.CharField(max_length=50)),
                ('ReleaseDate', models.DateField(blank=True, null=True)),
                ('RunTimeMinutes', models.IntegerField(null=True)),
                ('Review', models.CharField(blank=True, max_length=100, null=True)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/Movie/')),
                ('Actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lyrics.actor')),
                ('Certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lyrics.certificate')),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lyrics.country')),
                ('Genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lyrics.genre')),
                ('Language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lyrics.language')),
                ('MovieDirector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lyrics.moviedirector')),
                ('MusicDirector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lyrics.musicdirector')),
                ('Producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lyrics.producer')),
                ('Studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lyrics.studio')),
                ('Wood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lyrics.wood')),
                ('YouTube', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.youtube')),
            ],
        ),
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SongName', models.CharField(max_length=50)),
                ('Lyrics', models.TextField(blank=True, null=True)),
                ('MusicLabel', models.CharField(blank=True, max_length=50, null=True)),
                ('Upload', models.ImageField(blank=True, null=True, upload_to='images/Lyrics/')),
                ('Actor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.actor')),
                ('Language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.language')),
                ('Movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.movie')),
                ('MovieDirector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.moviedirector')),
                ('MusicDirector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.musicdirector')),
                ('Singer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.singer')),
                ('YouTube', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.youtube')),
            ],
        ),
    ]
