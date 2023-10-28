from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country (models.Model):
    name =models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural =  "Countries"

    def __str__(self):
        return f"{self.name}, {self.code}"

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self):
     return f"{self.street}, {self.postal_code}, {self.city}"
    
    class Meta:
        verbose_name_plural =  "Address Enteries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True,related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,
                            editable=False, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country)
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def save(self, *args, **keywoards):
        self.slug = slugify(self.title)
        super().save(*args, **keywoards)

    def __str__(self):
        return f"{self.title} ({self.rating})"
