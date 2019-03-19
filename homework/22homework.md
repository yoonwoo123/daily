# 22homework

1. attachment column에 파일을 저장하려고 한다. 아래의 (a)에 정의 해야 하는 field는?

   `ImageField()`		

   

2. 사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더 내부의 '/uploaded_files'로 지정하고자 한다. 이 때, settings.py에 작성해야 할 설정 2가지와 이것이 의미하는 바를 간략하게 작성하시오.

   ```python
   # /uploaded_files/ 경로에 파일 저장
   MEDIA_URL = '/uploaded_files/'
   # 디렉토리 안에 파일들 검색
   MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')
   ```

   

3. 개발자가 작성한 CSS 파일이나 넣고자 하는 이미지 파일 등이 Django 프로젝트 폴더 내부의 '/assets'에 있 다. '이 폴더 안에 정적 파일이 있다.'라고 Django 프로젝트에게 알려주기 위해서 settings.py에 작성해야 하는 설정을 작성하시오.

   ```python
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'assets'),
   ]
   ```