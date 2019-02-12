from django.shortcuts import render, HttpResponse
# Create your views here.

classroom = {'박길동': 28, '박성민': 29, '홍': 100, '김': 10}

def info(request):
    teacher = '홍길동'
    return render(request, 'info.html', {'classroom': classroom, 'teacher' : teacher})
    
def student(request, name, teach):
    age = classroom.get(name, 'unknown') # 앞으로 딕셔너리 값을 가져올 때는 .get을 써서 오류를 방지하자(None값이라도 반환)
    teach = {'age': 100, 'name' : '하하하', 'nickname': '하하하하'}
    return render(request, 'student.html', {'name': name, 'age': age, 'teach': teach})