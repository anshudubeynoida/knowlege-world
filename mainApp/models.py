from email.policy import default
from enum import unique
from django.db import models

class Maincategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class blogpost(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    maincategory = models.ForeignKey(Maincategory,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    posturl=models.CharField(max_length=55,null=False,blank=False,default="")
    description = models.TextField(default="",null=False,blank=False)
    paragraph1= models.TextField(default="",null=False,blank=False)
    paragraph2= models.TextField(default="",null=False,blank=False)
    pic1 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    pic2 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    
    def __str__(self):
        return self.name

conatctstatus = ((0,"Active"),(1,"Done"))
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    captcha = models.CharField(max_length=15)
    status = models.IntegerField(choices=conatctstatus,default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.subject        




