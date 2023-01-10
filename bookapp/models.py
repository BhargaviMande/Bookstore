from django.db import models

# Create your models here.

class add_to_cart(models.Model):
    Book_name=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' %(self.Book_name,self.Author)

class request_for_book(models.Model):
    Book_name=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' %(self.Book_name,self.Author)

class books(models.Model):
    Book_name = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Publish_date = models.DateField()
    def __str__(self):
        return '%s %s' %(self.Book_name,self.Author)






