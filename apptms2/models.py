from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):  # __unicode__ on Python 2
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __unicode__(self):  # __unicode__ on Python 2
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
