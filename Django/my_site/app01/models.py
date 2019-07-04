from django.db import models

# Create your models here.

class Account(models.Model):
    '''账户表'''
    username = models.CharField(max_length=32,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    register_date = models.DateTimeField(auto_now_add=True)
    singature = models.CharField("签名",max_length=255,null=True)

    def __str__(self):
        return self.username

class Article(models.Model):
    '''文章表'''
    title = models.CharField(max_length=255,unique=True)
    conten = models.TextField()
    account = models.ForeignKey('Account',on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag',null=True)
    pub_date = models.DateField()

    def __str__(self):
        return self.title

class Tag(models.Model):
    '''标签表'''
    name = models.CharField(max_length=64,unique=True)
    date = models.DateTimeField(auto_now_add=True)

