from django.db import models

class csvFile(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank = True)
    isPrimary = models.BooleanField(default = False)
    title = models.CharField(max_length=100, blank=True, default='')
    album = models.CharField(max_length=100, blank=True, default='Main')
    comment = models.TextField(blank = True, default='')
    csvFile = models.FileField(upload_to='csvFiles/')
    class Meta:
        ordering = ('created',)
