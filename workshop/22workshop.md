# 22workshop

## STEP 1. 부트스트랩(bootstrap-4.0.0-dist)을 다운로드

그 후 압축을 푼다. 압축을 풀면 `bootstrap-4.0.0-dist` 안에`css`, `js` 두 폴더가 있다.



## STEP 2. 적용할 프로젝트를 선택한다.

## STEP 3. Bootstrap 폴더를 프로젝트 폴더안으로 옮긴다.

project

> -index.html

> -bootstrap-4.0.0-dist

​	| - css

​	| - js

이런식으로 넣어준다.

## STEP 4.  LINK TO YOUR COPY OF BOOTSTRAP

```python
# settings.py 설정 변경해준다.

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]
```

```html
# 적용할 html에 적용
{% load static %}
<link rel="stylesheet" href="{% static 'bootstrap-4.0.0-dist/css/bootstrap.min.css' %}"/>
```

