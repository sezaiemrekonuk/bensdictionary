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
    structureType = models.ForeignKey(typeOf, on_delete=models.CASCADE, null=True)
    turkish = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    description = models.TextField()
    extraInformation = models.CharField(max_length=200, blank=True, null=True)
    example = models.TextField(blank=True, null=True)
    etymology = models.TextField(blank=True, null=True)
    original = models.ForeignKey(comesFrom, null=True, blank=True, on_delete=models.CASCADE)
    last_searched = models.DateTimeField(auto_now=False, blank=True, null=True)
    search_count = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    
    
    def __str__(self):
        return self.turkish
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.turkish)
        super(Structure, self).save(*args, **kwargs)

class Correct(models.Model):
    toStructure = models.ForeignKey(Structure, on_delete=models.CASCADE)
    corrector = models.CharField(max_length=200)
    corrector_mail = models.EmailField()
    correction = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.corrector

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject