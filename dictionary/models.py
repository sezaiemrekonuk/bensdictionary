from django.db import models
from django.utils.text import slugify

class comesFrom(models.Model):
    original = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.original
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.original)
        super(comesFrom, self).save(*args, **kwargs)

class typeOf(models.Model):
    type = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    
    def __str__(self):
        return self.type
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.type)
        super(typeOf, self).save(*args, **kwargs)

class Structure(models.Model):
    structureType = models.ManyToManyField(typeOf, blank=True, null=True)
    turkish = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    description = models.TextField()
    extraInformation = models.CharField(max_length=200, blank=True, null=True)
    # alsoCheck = I will create a processor for this task
    example = models.TextField(blank=True, null=True)
    etymology = models.TextField(blank=True, null=True)
    original = models.ManyToManyField(comesFrom, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.turkish
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.turkish)
        super(Structure, self).save(*args, **kwargs)
