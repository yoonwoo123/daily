# 17workshop

```python
# models.py
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    birthday = models.DateField(max_length=30)
    age = models.IntegerField(max_length=30)
    
    def __str__(self):
        return f'{self.name}'
    
# admin.py
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'birthday', 'age',]
admin.site.register(Student, StudentAdmin)
```

