from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User)

    # addition classes
    role = models.CharField(max_length=64,blank=True)
    telephone = models.CharField(max_length=32,blank=True)
    title = models.CharField(max_length=32,blank=True)

    profil_pic = models.ImageField(upload_to='profile_pics',blank=True)
    qr_code = models.ImageField(upload_to="qr_codes",blank=True)

    def __str__(self):
        return self.user.username


class Village(models.Model):
    name=models.CharField(max_length=128)
    country=models.CharField(max_length=32,null=True)

    def __str__(self):
        return str(self.name)



class Person(models.Model):
    firstname = models.CharField(max_length=64,blank=False)
    lastname = models.CharField(max_length=64,blank=False)
    village = models.ForeignKey(Village,on_delete=models.CASCADE)
    #journal_id = models.ForeignKey(Journal)

    age = models.IntegerField()
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.firstname + " " + self.lastname

class Journal(models.Model):
    createdate = models.DateField(auto_now_add=True)
    updatedate = models.DateField(auto_now=True)
    #person = models.ForeignKey(Person,null=True)
    person = models.OneToOneField(Person,null=True)
    def __str__(self):
        return str(self.person)



class JournalEntries(models.Model):
    journal_id = models.ForeignKey(Journal)
    createdate = models.DateField(auto_now_add=True)
    updatedate = models.DateField(auto_now=True)
    journaltxt = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.journal_id) + " " + str(self.createdate)



class Campain(models.Model):
    name=models.CharField(max_length=128)
    active=models.BooleanField(default=False)

    def __str__(self):
        return self.name
