from django.db import models


class Directory(models.Model):

    company = models.CharField(max_length=255)
