// 引入express模块
var express = require('express');
// 创建Web服务器对象
var app = express();
// 静态资源处理
app.use(express.static('public'));

// 设置允许跨域
app.all('*', (req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  next();
});

app.get('/get', (req, res) => {
  //使用send()方法返回字符串'Hello Express, GET'
  res.send('Hello Express, GET');
});

app.post('/post', (req, res) => {
  //使用send()方法返回字符串'Hello Express, POST'
  res.send('Hello Express, POST');
});

app.post('/xml', (req, res) => {
  res.send('OK')
});

app.get('/xml', (req, res) => {
  // 设置响应头
  res.setHeader('Content-Type', 'text/xml');
  // 返回XML格式数据
  res.send('<?xml version="1.0" encoding="utf-8" ?><book><name>红楼梦</name><author>曹雪芹</author></book>');
});

app.post('/json', (req, res) => {
  res.send('OK');
});

app.get('/json', (req, res) => {
  var data = {
    name: '红楼梦',
    author: '曹雪芹'
  };
  res.send(data);
});

app.get('/cors', (req, res) => {
  res.send('跨域请求成功!')
});

// 监听3000端口
app.listen(3000, () => {
  console.log('服务器启动成功...');
});
