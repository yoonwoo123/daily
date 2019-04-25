# 34homework

1. HTTP 상태 코드에서 200 Ok는 요청에 대해 성공적으로 수행하였음을 나타낸 다. 아래의 HTTP 응답 코드의 의미를 작성하시오.

  * 404 : Page Not Found (서버와 통신할 수는 있지만 서버가 요청한 바를 찾을 수 없다)
  * 405 : 메서드가 허용되지 않습니다.		
  * 500 :  내부 서버 오류

  ​		

2. Django에서 지정된 레코드에 값이 없을 때 404 에러를 나타내도록 하는 shortcut은 무엇인가. (import 문 포함)

   

   `from django.shortcuts import get_object_or_404`

   

3. 아래의 설명 중 REST API 설계 기본 규칙에 어긋난 것은?
  – (1) 자원에 필요한 경우 CRUD 동사 표현이 들어갈 수 있다. – (2) 자원은 대문자보다 소문자를 사용한다. – (3) URL에 HTTP Method를 사용하지 않는다. – (4) 자원간의 연관 관계가 있는 경우 posts/1/comments/ 와 같이 작성한다. – (5) URL에서 변하는 부분은 posts/<int:post_pk>/ 와 같이 유일한 값이다.



​	(1) CRUD 동사 표현이 들어갈 수 없다.

