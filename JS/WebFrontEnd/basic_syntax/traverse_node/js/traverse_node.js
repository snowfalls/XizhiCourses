var elementName = "";
function countTotalElement(node) {
    var total = 0;
    if (node.nodeType == 1) {
        total++;
        elementName = elementName + node.tagName + "\r\n";
    }
    for (var m = node.firstChild; m != null; m = m.nextSibling) {
        total += countTotalElement(m);
    }
    return total;
}