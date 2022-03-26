function insertStr() {
    var f=document.form1;
    var value=f.str.value;
    if (value != "") {
        // 从最终的TextNode节点开始，慢慢形成<tbody>结构
        var text = document.createTextNode(value);
        var td = document.createElement("td");
        var tr = document.createElement("tr");
        var tbody = document.createElement("tbody");
        td.appendChild(text);
        tr.appendChild(td);
        tbody.appendChild(tr);
        var parNode = document.getElementById("table1");
        parNode.insertBefore(tbody, parNode.firstChild);
        // parNode.appendChild(tbody);
    }
}