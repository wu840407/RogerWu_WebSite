# knowledgebase/models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)  # 新增這一欄
    published_date = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=100, blank=True, null=True)  # 可以記錄來源，例如 "Twitter ADA"

    def __str__(self):
        return self.title
