function show() {
    var inputs = document.getElementsByTagName("input");
    alert("input标签的数量是"+inputs.length);
    for (var i=0;i<inputs.length;i++) {
        alert("第" + (i+1) + "个input元素的值是" + input[i].value);
    }
}