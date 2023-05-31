function hh() {
    var hText=document.getElementById("fruit").getAttribute("src");
    alert("图片路径是" + hText);
}

function check() {
    var favor=document.getElementsByName("enjoy");
    var like="你喜欢的水果是：";
    for(var i=0;i<favor.length;i++) {
        if(favor[i].checked==true) {
            like += "\n" + favor[i].getAttribute("value");
        }
    }
    alert(like);
}

function change() {
    var imgs = document.getElementsByTagName("img");
    imgs[0].setAttribute("src", "img/grape.jpg");
}