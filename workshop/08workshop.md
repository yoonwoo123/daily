# 08workshop

Flask에서 Dictionary자료형을 이용하여 다음 조건을 만족하는 ‘나만의 영어 단어장 ’ 페이지를 만들어보세요 .

```python
@app.route('/dictionary/<string:word>')
def dictionary(word):
    dictionarys = {'apple': '사과', 'banana': '바나나'}
    if word in dictionarys:
        return f'{word}은(는) {dictionarys[word]}!'
    else:
        return f'{word}라는 단어가 없습니다.'
```

