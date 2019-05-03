# 36homework

1. DOM에서 특정 요소를 선택할 때 document.querySelector() 뿐만 아니라 document.querySelectorAll() 역시 사용할 수 있다. 둘의 차이를 검색하여 기 술하시오.

   `documnet.querySelector()` : 특정 CSS 선택자를 가진 첫 번째 요소를 선택하는 메서드 없으면 NULL 리턴

   `document.querySelectorAll()` :  특정 CSS 선택자를 가진 모든 요소를 선택하는 메서드

   ​							      없으면 빈 배열을 가지고 온다.

   

2. JS에서 자주 사용하는 EventListener 들 중 아래와 같은 것들이 있다. 각각 간 략하게 어떤 Trigger 를 의미하는지 조사하여 간략하게 기술하시오.

   * click : 마우스 버튼 클릭시 발생
   * mouseover : 마우스 커서를 올려놓았을 때 발생
   * mouseout : 마우스 커서를 올려놓았다가 밖으로 나갈 때 발생
   * mousemove : 마우스 커서를 움직일 때 발생
   * keypress : 키보드가 눌리는 순간 발생
   * keydown : 키보드가 눌려있을 때 발생
   * keyup : 키보드가 눌려있다가 떼는 순간 발생
   * load : 페이지를 전부 다 읽어들인 후에 발생
   * scroll : 스크롤바가 스크롤되는 경우 발생
   * change : 텍스트 박스의 값이 변경되는 경우 발생

   

3. DOM 에 요소를 추가할 때, innerHTML += 의 방법과 appendChild() 함수를 통해 추가하는 방법이 있다. 둘의 차이를 간략하게 기술하시오.

`innerHTML` : 특정 요소의 내용을 가져오거나, 특정 요소의 내용을 변경합니다.

`appendChild` : 선택한 요소 안에 자식 요소를 추가합니다.

