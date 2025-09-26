from django.db import models

# Create your models here.
class Crawlings(models.Model):
    company_name = models.CharField(max_length=100)
    stock_code = models.IntegerField()
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)