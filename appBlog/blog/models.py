from django.db import models
from django.conf import settings
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ['name']

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=100, unique=True)
    manufacturer = models.CharField(max_length=100, blank=True)
    release_year = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"
        ordering = ['name']

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=150, unique=True)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Desarrollador"
        verbose_name_plural = "Desarrolladores"
        ordering = ['name']

    def __str__(self):
        return self.name


class VideoGame(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name="games")
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True, related_name="games")
    platforms = models.ManyToManyField(Platform, related_name="games")
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)

    class Meta:
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    text = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title