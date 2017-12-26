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

## 获取乐团介绍内容

#### API
```
/api/intro/intro/cn/
```

#### 返回
```
{
    "body": {
        "content_cn": "<p style=\"text-align:center;\">\r\n\t<img src=\"http://www.desckie.com/assets/media/image/fulltext_20171226135432117.jpg\" width=\"500\" height=\"210\" alt=\"\" title=\"\" align=\"\" />\r\n</p>\r\n<p>\r\n\t<hr />\r\n</p>\r\n<p>\r\n\t<p style=\"font-family:&quot;\">\r\n\t\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;四川交响乐团是四川省级事业性职业乐团，也是中国西部独具资源优势的乐团。目前，乐团涵盖完全编制的管弦乐队、享誉世界的民乐品牌 “天姿国乐”、专业的室内合唱团。川交自成立以来一直活跃于中外音乐作品的各类重量级演出舞台，已举办了包括交响乐、歌剧、清唱剧、室内乐、民乐、合唱等多种艺术形式的主题音乐会达一千余场。\r\n\t</p>\r\n\t<p style=\"font-family:&quot;\">\r\n\t\t<br />\r\n\t</p>\r\n\t<p style=\"font-family:&quot;\">\r\n\t\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;川交与国内外著名音乐家建立了长期良好的合作关系，不断邀请国内外著名指挥家、独奏家、歌唱家合作演出。川交演出曲目以涵盖范围广、内容形式丰富为特色，不断赢得观众的掌声和乐迷的热捧，艺术水平也在不断地提升，影响力不断扩大。\r\n\t</p>\r\n\t<p style=\"font-family:&quot;\">\r\n\t\t<br />\r\n\t</p>\r\n\t<p style=\"font-family:&quot;\">\r\n\t\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;川交始终坚持中国交响乐作品的原创性，近年来先后创作推出了交响乐组曲《古蜀之光》《红色浪漫》《上善蜀水》、歌剧《鸣凤》、音乐剧《我是川军》等精品力作，受到主流媒体以及业内专家的一致好评。\r\n\t</p>\r\n\t<p style=\"font-family:&quot;\">\r\n\t\t<br />\r\n\t</p>\r\n\t<p style=\"font-family:&quot;\">\r\n\t\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;川交除每年举办一系列高品质交响音乐会外，还常年坚持举办大型惠民音乐活动，包括高雅音乐进校园、进军营进社区等普及性质的惠民音乐会，在图书馆、博物馆、文化馆等开展公益音乐讲座等活动，坚持致力于交响音乐的大众普及推广和公益文化服务。\r\n\t</p>\r\n\t<p style=\"font-family:&quot;\">\r\n\t\t<br />\r\n\t</p>\r\n\t<p style=\"font-family:&quot;\">\r\n\t\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;近年来，川交按照国际惯例和标准，大力推进职业化改革发展进程。2016年12月19日，特聘新加坡籍世界著名青年指挥家Darrell Ang先生（中文名：洪毅全）出任艺术总监，在他的带领下，川交将立足本土，放眼世界，努力“用好世界语言，讲好中国故事”，不断开拓创新、融合发展，开启音乐季音乐会、国际巡演、作品原创、教育培训、高雅艺术普及与推广的崭新的航程。\r\n\t</p>\r\n</p>"
    },
    "error": 0
}
```