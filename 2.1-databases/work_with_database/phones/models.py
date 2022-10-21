from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=40, blank=True)

    def __str__(self):
        return f'{self.name}'
