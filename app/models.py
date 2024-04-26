from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    
    email=models.EmailField(default="hai@gmail.com")

    def __str__(self):
        return self.topic_name


class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return str(self.id)

        
class AcessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    details=models.CharField(max_length=100,default='write author details here!')
    
    def __str__(self):
        return self.author