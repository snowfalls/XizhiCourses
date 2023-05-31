function delNode() {
    var dNode = document.getElementById("sixty1");
    document.body.removeChild(dNode);
}

function repNode() {
    var oldimage=document.getElementById("sixty2");
    var newimage = document.createElement("img");

    newimage.setAttribute("src", "img/repimg.jpg");
    document.body.replaceChild(newimage, oldimage);
}