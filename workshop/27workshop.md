# 27workshop

*  아래의 회원가입 페이지는 django.contrib.auth.forms 안에 있는 UserCreationForm() 을 활용한 것이다. 아래 페이지를 위한 view, url, template 을 작성하세요.



```python
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        user_form = UserCreationForm()
    context = {'user_form': user_form}
    return render(request, 'accounts/signup.html', context)
```



```python
# urls.py

from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
        path('', views.signup, name="signup"),
]
```



```html
templates

{% extends 'boards/base.html' %}
{% block body %}
{% load crispy_forms_tags %}
<form method="POST">
    {% csrf_token %}
    {{ user_form|crispy }}
    <input type="submit" value="회원가입신청">
</form>
{% endblock %}
```

