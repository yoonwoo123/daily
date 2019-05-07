# 43workshop

v-bind와 v-model 디렉티브를 활용하여, 다음와 같이 'Go!' 링크를 누르면 입력 창에 작성한 URL로 가도록 하는 '주소가 변하는 링크'를 만들어 봅시다.

```html
<body>
    <div id="app">
        <input type="text" v-model="url">          
        <a v-bind:href="url">Go!</a><br>
    </div>
        <script src="https://cdn.jsdelivr.net/npm/vue"></script>
        <script>
            const app = new Vue({
                el: '#app',
                data: {
                    url : ''
                },
                methods: {
                }
            })
        </script>
</body>
```



