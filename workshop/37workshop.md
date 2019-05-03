# 37workshop

```javascript
const URL = 'http://13.125.249.144:8080/ssafy/daejeon/1/posts'
        axios.get(URL)
        .then(response => {
            console.log(response)
        })
        const data = {post: {title: 'hi', content:' hihi', author:'youngwoo'}}

        axios.post(URL, data)
            .then(response => {
                console.log(response)
            })
```

