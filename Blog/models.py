from django.db import models


# Create your models here.




class Blog(models.Model):
    title = models.CharField(max_length=100, default="")
    bloggers_name = models.CharField(max_length=100, default="")
    blog = models.TextField(max_length=5000, default="")


    image = models.ImageField(upload_to='images/blogs/',blank=True)


    def __str__(self):
        return self.title

