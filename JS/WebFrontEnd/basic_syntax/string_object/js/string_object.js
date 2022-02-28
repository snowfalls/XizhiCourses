function check() {
    var flag = true;
    var pass = document.getElementById("pass").value;
    for (var i = 0; i < pass.length; i++) {
        if ((pass.charAt(i) < "0") || (pass.charAt(i) > '9')) {
            flag = false;
        }
    }
    if (flag) {
        alert("输入合法");
    }
    else {
        alert("输入不合法，只能是数字");
    }
}