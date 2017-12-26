# Symphonys API Documentation

## 全局声明

* 传输协议: http
* 主机域名: www.desckie.com
* 请求方法: GET
* 中英文切换: <code>cn</code>为获取中文返回，<code>en</code>为获取英文返回。
* 获取简介/详情: <code>abstract</code>为获取介绍简介，<code>detail</code>为获取介绍全文。
* 正序与逆序: 从最近开始<code>reverse</code>，从最早开始<code>sequence</code>。
* 整数占位符: <code>{{INSTRUMENT_ID}}</code>、<code>{{ID}}</code>、<code>{{PAGE}}</code>，代表对应标识的整数值。

## 目录
* <a href="#获取首页轮播图" style="text-decoration:none;">获取首页轮播图</a>
* <a href="#获取乐团介绍内容" style="text-decoration:none;">获取乐团介绍内容</a>
* <a href="#获取乐团团长内容" style="text-decoration:none;">获取乐团团长内容</a>
* <a href="#获取驻团指挥内容" style="text-decoration:none;">获取驻团指挥内容</a>
* <a href="#获取艺术总监内容" style="text-decoration:none;">获取艺术总监内容</a>
* <a href="#获取乐器种类列表" style="text-decoration:none;">获取乐器种类列表</a>
* <a href="#获取乐团成员列表" style="text-decoration:none;">获取乐团成员列表</a>
* <a href="#音乐会" style="text-decoration:none;">音乐会</a>
* <a href="#月季" style="text-decoration:none;">月季</a>
* <a href="#获取天姿国乐介绍" style="text-decoration:none;">获取天姿国乐介绍</a>
* <a href="#获取天姿国乐新闻列表" style="text-decoration:none;">获取天姿国乐新闻列表</a>
* <a href="#获取天姿国乐新闻全文" style="text-decoration:none;">获取天姿国乐新闻全文</a>
* <a href="#获取歌剧院介绍" style="text-decoration:none;">获取歌剧院介绍</a>
* <a href="#获取歌剧院新闻列表" style="text-decoration:none;">获取歌剧院新闻列表</a>
* <a href="#获取歌剧院新闻全文" style="text-decoration:none;">获取歌剧院新闻全文</a>
* <a href="#获取事业动态列表" style="text-decoration:none;">获取事业动态列表</a>
* <a href="#获取事业动态全文" style="text-decoration:none;">获取事业动态全文</a>

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

## 获取乐团团长内容

#### API
```
/api/intro/leader/cn/list/
```

#### 返回
```
{
    "body": {
        "vice_president": [
            {
                "president_type": 1,
                "intro": "副团长、“天姿国乐”品牌创始人",
                "id": 2,
                "img": "http://www.desckie.com/assets/media/image/model_20171226140828796.png",
                "name": "牟岭虹"
            }
        ],
        "president": [
            {
                "president_type": 0,
                "intro": "党总支副书记、副团长（主持工作）",
                "id": 1,
                "img": "http://www.desckie.com/assets/media/image/model_20171226140657299.png",
                "name": "吴灵峰"
            }
        ],
        "address": "<p style=\"font-family:&quot;\">\r\n\t“新的开始”，我们携手又出发。\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t&nbsp;\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t【云端之乐】——2017/2018乐季，是四川交响乐团携手成都高新投资集团倾情为您呈现的经典交响乐盛宴。\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t&nbsp;\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t川交秉承“敬业、职业、专业”的音乐态度，立足本土，放眼世界，海纳百川，力求“用好世界语言，讲好中国故事，传播四川声音”。\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t&nbsp;&nbsp;\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t本乐季，川交的音乐家们将在艺术总监Darrell Ang先生带领下，凝聚饱满的艺术热情和诚挚的音乐梦想，将在“中国-欧洲中心”的云端-天府音乐厅为您诠释二十余套精彩的乐季音乐会。每一套音乐会都将邀请来自世界各地的不同领域、不同风格的杰出音乐家加盟。我们愿意把最好的音乐、最经典的作品、最完美的表现奉献给您，希望为您的生活乐章增添一些动人的旋律和美妙的音符。\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t&nbsp;\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t川交将在您的见证下，不断开拓创新，通过乐季音乐会、国际国内巡回演出、艺术教育、以及下基层进学校等惠民活动，努力推进专业化建设和职业化进程，为四川音乐产业发展和文化强省建设作出新的贡献。\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t&nbsp;\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t音乐是发自人类灵魂最深处的声音，是全人类触摸客观世界的共同语言。期待我们的相聚，让我们一同走进音乐，聆听经典，醉美生活，分享感动。\r\n</p>"
    },
    "error": 0
}
```

## 获取驻团指挥内容

#### API
```
/api/intro/conductor/cn/list/
```

#### 返回
```
{
    "body": [
        {
            "intro": "驻团指挥",
            "id": 1,
            "img": "http://www.desckie.com/assets/media/image/model_20171226165057300.png",
            "name": "肖超"
        },
        {
            "intro": "驻团指挥",
            "id": 2,
            "img": "http://www.desckie.com/assets/media/image/model_20171226165239838.png",
            "name": "司马健楠"
        }
    ],
    "error": 0
}
```

## 获取艺术总监内容

## API
```
/api/intro/director/cn/
```

## 返回
```
{
    "body": {
        "intro": "乐团艺术总监/首席指挥",
        "name": "洪毅全",
        "img": "http://www.desckie.com/assets/media/image/model_20171226171427894.png",
        "detail": "<p style=\"font-family:&quot;\">\r\n\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Darrell Ang在第50届贝桑松国际青年指挥大赛上包揽了所有的三个奖项：大奖、观众奖和管弦奖，这奠定了他国际职业生涯的基础，使他得以在2012年至2015年间担任了法国贝列塔尼交响乐团的音乐总监，并且在法国广播爱乐乐团、里昂国立管弦乐团、斯特拉斯堡爱乐乐团、波尔多-阿基坦国立交响乐团、里尔国立管弦乐团、米兰朱塞佩·威尔第交响乐团、阿图罗·托斯卡尼尼爱乐乐团、柏林广播交响乐团、慕尼黑交响乐团、维也纳室内乐团、维也纳广播交响乐团、哥本哈根爱乐乐团、马德里RTVE交响乐团、巴塞罗那交响乐团、斯洛伐克爱乐乐团、香港爱乐乐团、台湾爱乐乐团和台湾交响乐团、NHK交响乐团和读卖新闻交响乐团等著名乐团进行了客座演出。\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t&nbsp;\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;三年后，Darrell Ang入选了著名的安联文化基金会国际指挥学院，并且应邀与伦敦爱乐乐团和爱乐乐团进行了驻团合作。Darrell的导师包括埃萨-佩卡·萨洛宁和洛林·马泽尔，他至今对他们的宝贵建议和支持心存感激。在英国，他定期指挥皇家利物浦爱乐乐团的演出，并且常常受邀重返伦敦爱乐乐团和爱乐乐团。 他目前正在与拿索斯唱片公司合作，准备录制一些法国和亚洲作曲家的作品。他录制的首张唱片是中国作曲家周龙与陈怡的作品，在2016年获得了一项格莱美奖提名。同年12月，Darrell成为了四川交响乐团的艺术总监和首席指挥。最近，Darrell吸引到了瓦列里·捷吉耶夫的注意，这位指挥大师立即邀请他前往位于圣彼得堡的马林斯基剧院和位于符拉迪沃斯托克的马林斯基剧院滨海边疆区音乐厅进行指挥。\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t&nbsp;\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在Darrell出生的新加坡，他成为了新加坡交响乐团最年轻的助理指挥家，与音乐总监水蓝紧密合作；并且还出任新加坡国立青年管弦乐团的音乐总监。2010年，Darrell率领世界青年奥运会管弦乐团，在国际转播的新加坡首届世界青奥会上演出。作为台湾交响乐团下属的两岸青年交响乐团的首席指挥，Darrell成为了该乐团最初的核心人物，将来自海峡两岸的优秀青年家汇聚于此，在北京和台北的一流音乐厅中演出高质量的音乐会。\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t&nbsp;\r\n</p>\r\n<p style=\"font-family:&quot;\">\r\n\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Darrell非同寻常的音乐才华在他4岁学习小提琴和钢琴时崭露头角。他天生的艺术好奇心，激励着他很快开始学习作曲。在青少年期间，他带着他的音乐梦想前往维也纳，接下来去到圣彼得堡，师从Leonid Korchmar，并且继承了俄罗斯传奇指挥家伊利亚·穆欣的优秀传统。在圣彼得堡，他发展出了对于20世纪俄罗斯音乐、法国音乐和现代亚洲曲目的兴趣，这一兴趣一直留存在他的艺术个性之中。接下来，Darrell前往耶鲁大学深造，成为该大学第一位指挥学员。作为作曲家，他受德国化学公司LANXESS委约创作了《疲惫不堪的地球之号角》。Darrell可以流利地使用英语、德语、法语、意大利语和普通话，以便于用乐团成员的母语进行排练。\r\n</p>\r\n<div>\r\n\t<br />\r\n</div>"
    },
    "error": 0
}
```

## 获取乐器种类列表

#### API
```
/api/intro/instrument/cn/
```

#### 返回
```
{
    "body": [
        {
            "id": 1,
            "name": "一提琴"
        },
        {
            "id": 2,
            "name": "二提琴"
        },
        {
            "id": 3,
            "name": "中提琴"
        },
        {
            "id": 4,
            "name": "大提琴"
        },
        {
            "id": 5,
            "name": "低音提琴"
        },
        {
            "id": 6,
            "name": "长笛"
        },
        {
            "id": 7,
            "name": "双簧管"
        },
        {
            "id": 8,
            "name": "单簧管"
        },
        {
            "id": 9,
            "name": "巴松"
        },
        {
            "id": 10,
            "name": "圆号"
        },
        {
            "id": 11,
            "name": "小号"
        },
        {
            "id": 12,
            "name": "长号"
        },
        {
            "id": 13,
            "name": "定音鼓"
        },
        {
            "id": 14,
            "name": "打击乐"
        },
        {
            "id": 15,
            "name": "竖琴"
        }
    ],
    "error": 0
}
```

## 获取乐团成员列表

#### API
```
/api/intro/performer/cn/list/{{INSTRUMENT_ID}}/
```

#### 返回
```
{
    "body": [
        {
            "instrument_type": "一提琴",
            "id": 1,
            "img": "http://www.desckie.com/assets/media/image/model_20171226172326241.png",
            "name": "张旭"
        },
        {
            "instrument_type": "一提琴",
            "id": 2,
            "img": "http://www.desckie.com/assets/media/image/model_20171226172427149.png",
            "name": "杨帆"
        }
    ],
    "error": 0
}
```

## 音乐会

## 月季

## 获取天姿国乐介绍

#### API
```
/api/beautymelody/intro/cn/detail/
```

#### 返回
```
{
    "body": {
        "detail": "<p style=\"font-family:&quot;\">\r\n\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“天姿国乐”隶属于四川交响乐团，是中国西部年轻、优秀的职业女子民乐团，是中国对外文化交流的一张靓丽名片。她们的足迹遍布世界二十多个国家和地区，曾在美国肯尼迪音乐厅、捷克国家歌剧院、日本大阪音乐厅、波兰肖邦音乐厅、西班牙马德里音乐厅、莫斯科国际音乐宫、联合国万国宫等世界著名音乐圣殿成功的上演了专场音乐会，在世界各地播撒中国文化的种子，被誉为“带来奇妙音乐盛宴的乐团”。\r\n</p>\r\n<p>\r\n\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;<span style=\"font-family:&quot;\">“天姿国乐”隶属于四川交响乐团，是中国西部年轻、优秀的职业女子民乐团，是中国对外文化交流的一张靓丽名片。她们的足迹遍布世界二十多个国家和地区，曾在美国肯尼迪音乐厅、捷克国家歌剧院、日本大阪音乐厅、波兰肖邦音乐厅、西班牙马德里音乐厅、莫斯科国际音乐宫、联合国万国宫等世界著名音乐圣殿成功的上演了专场音乐会，在世界各地播撒中国文化的种子，被誉为“带来奇妙音乐盛宴的乐团”。</span>\r\n</p>\r\n<p>\r\n\t<span style=\"font-family:&quot;\">\r\n\t<p style=\"font-family:&quot;\">\r\n\t\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“天姿国乐”隶属于四川交响乐团，是中国西部年轻、优秀的职业女子民乐团，是中国对外文化交流的一张靓丽名片。她们的足迹遍布世界二十多个国家和地区，曾在美国肯尼迪音乐厅、捷克国家歌剧院、日本大阪音乐厅、波兰肖邦音乐厅、西班牙马德里音乐厅、莫斯科国际音乐宫、联合国万国宫等世界著名音乐圣殿成功的上演了专场音乐会，在世界各地播撒中国文化的种子，被誉为“带来奇妙音乐盛宴的乐团”。\r\n\t</p>\r\n\t<p style=\"font-family:&quot;\">\r\n\t\t<p style=\"font-family:&quot;\">\r\n\t\t\t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“天姿国乐”隶属于四川交响乐团，是中国西部年轻、优秀的职业女子民乐团，是中国对外文化交流的一张靓丽名片。她们的足迹遍布世界二十多个国家和地区，曾在美国肯尼迪音乐厅、捷克国家歌剧院、日本大阪音乐厅、波兰肖邦音乐厅、西班牙马德里音乐厅、莫斯科国际音乐宫、联合国万国宫等世界著名音乐圣殿成功的上演了专场音乐会，在世界各地播撒中国文化的种子，被誉为“带来奇妙音乐盛宴的乐团”。<span style=\"font-family:&quot;\"></span>\r\n\t\t</p>\r\n\t</p>\r\n</span>\r\n</p>",
        "img": "http://www.desckie.com/assets/media/image/model_20171226173939316.png"
    },
    "error": 0
}
```

## 获取天姿国乐新闻列表

#### API
```
/api/beautymelody/news/cn/list/{{PAGE}}/
```

#### 返回
```
{
    "body": {
        "max_page": 2,
        "news": [
            {
                "date": "2017-12-26",
                "abstract": null,
                "id": 6,
                "img": "http://www.desckie.com/assets/media/image/model_20171226175648728.png",
                "title": "文章6"
            },
            {
                "date": "2017-12-26",
                "abstract": null,
                "id": 5,
                "img": "http://www.desckie.com/assets/media/image/model_20171226175627802.png",
                "title": "文章5"
            },
            {
                "date": "2017-12-26",
                "abstract": null,
                "id": 4,
                "img": "http://www.desckie.com/assets/media/image/model_20171226175609254.png",
                "title": "文章4"
            },
            {
                "date": "2017-12-26",
                "abstract": null,
                "id": 3,
                "img": "http://www.desckie.com/assets/media/image/model_20171226175545411.png",
                "title": "文章3"
            },
            {
                "date": "2017-12-26",
                "abstract": null,
                "id": 2,
                "img": "http://www.desckie.com/assets/media/image/model_20171226175524233.png",
                "title": "文章2"
            }
        ]
    },
    "error": 0
}
```

## 获取天姿国乐新闻全文

#### API
```
/api/beautymelody/news/cn/detail/{{ID}}/
```

#### 返回
```
{
    "body": {
        "date": "2017-12-26",
        "detail": "<p style=\"font-family:&quot;\">\r\n\t文章1内容\r\n</p>",
        "id": 1,
        "img": "http://www.desckie.com/assets/media/image/model_20171226175413349.png",
        "title": "文章1"
    },
    "error": 0
}
```

## 获取歌剧院介绍

#### API
```
/api/opera/intro/cn/detail/
```

#### 返回

返回JSON格式与<a href="#获取天姿国乐介绍" style="text-decoration:none;">获取天姿国乐介绍</a>类似。

## 获取歌剧院新闻列表

#### API
```
/api/opera/news/cn/list/{{PAGE}}/
```

#### 返回

返回JSON格式与<a href="#获取天姿国乐新闻列表" style="text-decoration:none;">获取天姿国乐新闻列表</a>类似。

## 获取歌剧院新闻全文

#### API
```
/api/opera/news/cn/detail/{{ID}}/
```

#### 返回

返回JSON格式与<a href="#获取天姿国乐新闻全文" style="text-decoration:none;">获取天姿国乐新闻全文</a>类似。

## 获取事业动态列表

#### API
```
/api/businessdynamics/news/cn/list/reverse/{{PAGE}}/
```

#### 返回

返回JSON格式与<a href="#获取天姿国乐新闻全文" style="text-decoration:none;">获取天姿国乐新闻全文</a>类似。

## 获取事业动态全文

#### API
```
/api/businessdynamics/news/cn/detail/{{ID}}/
```

#### 返回

返回JSON格式与<a href="#获取天姿国乐新闻全文" style="text-decoration:none;">获取天姿国乐新闻全文</a>类似。