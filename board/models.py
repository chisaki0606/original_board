from django.db import models

class Topic(models.Model):
  title = models.CharField('タイトル', max_length=200)
  text = models.TextField('本文')
