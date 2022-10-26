nginx动态认证
nginx 编译安装时添加参数 --with-http_auth_request_module
此模块是基于http响应状态码做权限控制的auth_request模块
如果返回码是2XX 认证通过，返回相对应资源
返回码是4XX 认证失败返回401

nginx 配置
server{
  listen 8087;
  location / {
    auth_request /check;
    root /ser/data ;
    autoindex on;
    autoindex_exact_size off;
    autoindex_localtime on;
    add_header Cache-Control no-store;
  }
  location /check{
    proxy_pass http://127.0.0.1:8084/check;
    proxy_set_header Authorization $http_Authorization;
    proxy_set_header name 'hzw';
  }
}

server{
  #鉴权服务器
  listen 8084;
  location /check{
    proxy_pass http://127.0.0.1:8085/auth;
    proxy_set_header Authorization $http_Authorization;
  }
}