# 21workshop

```python
# views.py
def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    # choices = question.choice_set.all()
    context = {
        'question':question,
        #'choices':choices
    }
    return render(request, 'choices/detail.html', context)
```



```html
<!--html-->
<h1>{{ question.title }}</h1>
{% for choice in question.choice_set.all %}
<li> {{ choice.content }} : {{ choice.votes }}표</li>
{% endfor %}
```

