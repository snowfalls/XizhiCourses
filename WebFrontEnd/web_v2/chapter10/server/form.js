// 引入express模块
var express = require('express');
// 创建Web服务器对象
var app = express();
// 静态资源处理
app.use(express.static('public'));
// 解析浏览器发来的URL编码数据（表单默认编码）和JSON数据
app.use(express.urlencoded({ extended: false }));
app.use(express.json());
// 设置允许跨域
app.all('*', (req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  next();
});
// 处理POST请求
app.post('/login', (req, res) => {
  // 服务器保存的“用户名: 密码”
  var data = {
    admin: '123456',
    teach1: 'a12345',
    stu1: 'b111111'
  };
  var result = { code: 0,  msg: '登录失败' };
  // 获取请求参数
  var username = req.body.username;
  var password = req.body.password;
  // 遍历data对象
  for (k in data) {
    if (k == username && data[k] == password) {
      result.code = 1;
      result.msg = '登录成功';
      break;
    }
  }
  res.send(result);
});
// 监听3000端口
app.listen(3000, () => {
  console.log('服务器启动成功...');
});
