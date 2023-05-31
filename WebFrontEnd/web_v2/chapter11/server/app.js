// 引入express模块
var express = require('express');
// 创建Web服务器对象
var app = express();
// 设置允许跨域
app.all('*', (req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  next();
});
// GET请求
app.get('/get', (req, res) => {
  // 对客户端做出响应
  res.send('Hello, GET');
});
// POST请求
app.post('/post', (req, res) => {
  // 对客户端做出响应
  var data = {
    user: 'zhangsan',
    pass: '123456'
  };
  res.send(data);
});
// 监听3000端口
app.listen(3000, () => {
  console.log('服务器启动成功...');
});
