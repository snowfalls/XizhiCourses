function showTime() {
    var w;
    var now = new Date();
    var y = now.getFullYear();
    var m = now.getMonth() + 1;
    var d = now.getDate();
    var day = now.getDay();
    var h = now.getHours();
    var minu = now.getMinutes();
    m = ((m < 10) ? "0" : "") + m;
    d = ((d < 10) ? "0" : "") + m;
    h = ((h < 10) ? "0" : "") + m;
    minu = ((minu < 10) ? "0" : "") + minu;
    if (day == 0)
        w = "天";
    else if (day == 1)
        w = "一";
    else if (day == 2)
        w = "二";
    else if (day == 3)
        w = "三";
    else if (day == 4)
        w = "四";
    else if (day == 5)
        w = "五";
    else
        w = "六";
 
    var str = "" + y + "年" + m + "月" + d + "日  " + "星期" + w + "  \n现在是" + h + ":" + minu + ", ";
    if (h <= 8 && h > 0)
        str += "早上好";
    else if (h <= 12)
        str += "上午好";
    else if (h <= 18)
        str += "下午好";
    else
        str += "晚上好";
    
    txt.innerText = str;
    setTimeout("showTime()", 6000);
}