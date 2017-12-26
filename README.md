# Symphonys API Documentation

## 全局声明

* 传输协议: http
* 主机域名: www.desckie.com
* 请求方法: GET
* URL规则: 所有URL中，<code>cn</code>为获取中文返回，<code>en</code>为获取英文返回。

## 目录
* <a href="https://github.com/Lizonghang/Symphonys#获取首页轮播图" style="text-decoration:none;">获取首页轮播图</a>

## 获取首页轮播图

#### API
```
/api/home/banner/cn/list/
```

#### 返回
```
{
    "body": [
        {
            "subtitle": "SICHUAN SYMPHONY ORCHESTRA ",
            "order": 1,
            "img": "http://www.desckie.com/assets/media/image/model_20171226133630431.png",
            "title": "四川交响乐团"
        }
    ],
    "error": 0
}
```

