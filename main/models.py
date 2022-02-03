from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Enrollee(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'pages/')
    description = RichTextUploadingField()

    def __str__(self):
        return self.title



class Questions(models.Model):
    questions = models.ForeignKey(Enrollee, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    answer = RichTextUploadingField()

    def __str__(self):
        return self.question

class Quotas(models.Model):
    title = models.CharField(max_length=255)
    table = RichTextUploadingField()

    def __str__(self):
        return self.title


class Programs(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'pages/')
    content = RichTextUploadingField()
    scheme = RichTextUploadingField()
    table = RichTextUploadingField()

    def __str__(self):
        return self.title

class Ads(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Category(models.Model):
    category = models.ForeignKey(Ads, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ad(models.Model):
    ad = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'pages/', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

class CentralDepartments(models.Model):
    icon = models.ImageField(upload_to='pages/')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pages/')
    boss = models.CharField(max_length=255)
    time = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    content = RichTextUploadingField()

    def __str__(self):
        return self.name


class Departments(models.Model):
    icon = models.ImageField(upload_to='pages/')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pages/')
    boss = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    content = RichTextUploadingField()

    def __str__(self):
        return self.name


class Management(models.Model):
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pages/')
    full_name = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    work_activities = RichTextUploadingField()

    def __str__(self):
        return self.position

class ExternalDepartment(models.Model):
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pages/')
    full_name = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name