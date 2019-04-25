# 30workshop

```python
# models.py
from.django.db import models

class Hashtag(models.Model):
    content = models.TextField(unique=True)

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, blank=True, related_name="posts" )


```

