# 35homework

1. JS 는 ES6 이전과 이후로 많은 것이 바뀌었다. ES5 까지는 ‘var ‘키워드로 변수
  를 선언했다면, ES6 이후로는 ‘let’ 과 ‘const’ 키워드가 등장했다.
  ‘let’ 과 ‘const’ 의 차이점과 언제 사용하는지 간략하게 기술하시오.

  1. JS 는 ES6 이전과 이후로 많은 것이 바뀌었다. ES5 까지는 ‘var ‘키워드로 변수
    를 선언했다면, ES6 이후로는 ‘let’ 과 ‘const’ 키워드가 등장했다.
    ‘let’ 과 ‘const’ 의 차이점과 언제 사용하는지 간략하게 기술하시오.

  2. JS 에서는 key – value 로 이루어진 자료구조를 Object 라고 부른다. Object
    와 JSON 의 차이를 간략하게 기술하시오.

  3. 해당 코드에서 ‘Value’ 에 접근하는 두 가지 방법(코드)을 모두 작성하시오.

  4. 아래 주석에 따라 JS 코드를 작성하시오.

     

2. JS 에서는 key – value 로 이루어진 자료구조를 Object 라고 부른다. Object
  와 JSON 의 차이를 간략하게 기술하시오.

  Object 는 자바스크립트의 기본 데이터 타입이고,

  JSON (JavaScriptObejctNotation) 은 Javascript 객체 문법을 따르는 문자 기반의 데이터 포맷입니다.

  또한 JavaScript 가 아니더라도 JSON을 읽고 쓸 수 있는 기능이 다수의 프로그래밍 환경에서 제공됩니다.

  

3. 해당 코드에서 ‘Value’ 에 접근하는 두 가지 방법(코드)을 모두 작성하시오.

   myObject.key 와 myObject['key'] 이다.

   

4. 아래 주석에 따라 JS 코드를 작성하시오.

   1. h1 태그를 선택한 뒤, header 라는 상수에 할당한다.
   2.  브라우저 콘솔에 header 안의 내용을 출력한다.
   3. header 안의 내용을 'Happy Hacking!' 으로 변경한다.

```javascript
var header = document.querySelector('h1')
        document.querySelector('h1')
        header.innertext = 'Happy Hacking'
```

