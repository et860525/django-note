from django.db import models

# Create your models here.
class Post(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __repr__(self):
        return self.headline