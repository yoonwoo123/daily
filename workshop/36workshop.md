# 36workshop

```javascript
// #change-btn 을 button 상수에 할당한다.
const changeBtn = document.querySelector('#change-btn')
// h1 태그를 header 상수에 할당한다.
const header = document.querySelector('h1')
// clickCount 변수를 0으로 초기화 한다.
let clickCount = 0
// button에 'click' eventListener를 추가한다. 클릭이 일어나면,
changeBtn.addEventListener('click', function(e){
    console.log(e)
    // clickCount가 1씩 올라간다.
    clickCount += 1
    // header 안의 내용을 clickCount로 바꾼다.
    header.innerHTML = clickCount
})	
```

