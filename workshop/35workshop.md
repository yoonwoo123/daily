# 35workshop

```javascript
let concat = function (str1, str2) {
    return `${str1}-${str2}`
}

let checkLongStr = function (string) {
    if (string.length > 10) {
        return true
    } else {
        return false
    }
}

if (checkLongStr(concat('Happy', 'Hacking'))) {
    console.log('LONG STRING')
} else {
    console.log('SHORT STRING')
}
```

