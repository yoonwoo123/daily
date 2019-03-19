# 20workshop

```python
class Question(models.Model):
    title = models.CharField(max_length=50)
    
class Choice(models.Model):
    content = models.CharField(max_length=50)
    votes = models.IntegerField()
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
```

