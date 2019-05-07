# 41workshop

```html
<body>
    <div id="app">
        <ul>
            <li v-for="number in numbers" v-if="number %2===0">
                {{ number }}
            </li>
        </ul>

    </div>


    <script src="https://cdn.jsdelivr.net/npm/vue"></script>
    <script>
        var app = new Vue({
            el: '#app',
            data: {
                numbers: [0,1,2,3,4,5,6,7,8,9],
            },
        })
    </script>
</body>
```

