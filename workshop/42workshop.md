# 42workshop

```html
<body>
    <div id="app">
        <button v-on:click="plusCnt">+1</button><br>
        <h2>Counter: {{ cnt }}</h2>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue"></script>
    <script>
        const app = new Vue({
            el: '#app',
            data: {
                cnt: 0
            },
            methods: {
                plusCnt: function(){
                    this.cnt += 1
                }
            }
        })
    </script>
</body>
```

