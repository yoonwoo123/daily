# 37homework

1. Axios 를 사용하는 아래 코드를 완성하시오. - Browser 는 axios CDN을 통해, - Node 는 npm install 과 require 를 통해 axios 를 가져와야 합니다.

```javascript
const URL = "https://dog.ceo/api/breeds/image/random"

axios.get(URL)
.then(res => {
    // imgSrc 상수에 res 에서 개 image의 URL을 뽑아서 저장한다.
    const imgSrc = res.data.message
    // imgSrc를 return 한다.
    return imgSrc
    })
.then(imageSource => {
	// imageSource 를 콘솔에 출력한다.
    console.log(imageSource)
})
```



