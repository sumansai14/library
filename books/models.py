from django.db import models
from django.contrib.auth.models import User
#from bootstrap.forms import BootstrapForm, Fieldset
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    slug = models.SlugField(unique=False)
    is_issued = models.BooleanField(default=False)
    issued_to = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.name


class BookUserMap(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return (self.book.name + " is requested by " + self.user.username)


class ReturnRequestList(models.Model):
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return (self.book.name + " is being returned")
