from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class PreStudents(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'pages/')
    description = RichTextUploadingField()

    def __str__(self):
        return self.title



class Questions(models.Model):
    questions = models.ForeignKey(PreStudents, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    answer = RichTextUploadingField()

    def __str__(self):
        return self.question