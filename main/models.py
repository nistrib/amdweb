from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    code_block = models.TextField()
    github_link = models.URLField()

    def __str__(self):
        return self.title
