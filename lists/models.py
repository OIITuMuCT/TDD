from django.db import models
from django.urls import reverse

# Create your models here.
class List(models.Model):
    """ список """
    def get_absolute_url(self):
        """ получить абсолютный url """
        return reverse('view_list', args=[self.id])

    def __str__(self):
        return List.__name__
class Item(models.Model):
    """ элемент списка """
    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
