# Symphonys API Documentation

## 全局声明

* 传输协议: http
* 主机域名: www.desckie.com
* 请求方法: GET
* 中英文切换: <code>cn</code>为获取中文返回，<code>en</code>为获取英文返回。
* 获取简介/详情: <code>abstract</code>为获取介绍简介，<code>detail</code>为获取介绍全文。
* 正序与逆序: 从最近开始<code>reverse</code>，从最早开始<code>sequence</code>。
* 整数占位符: <code>{{INSTRUMENT_ID}}</code>、<code>{{ID}}</code>、<code>{{PAGE}}</code>，代表对应标识的整数值。

## API

* 获取首页轮播图: <code>/api/home/banner/cn/list/</code>
* 获取首页新闻列表: <code>/api/home/news/cn/list/</code>
* 获取乐团介绍内容: <code>/api/intro/intro/cn/</code>
* 获取乐团团长列表: <code>/api/intro/leader/cn/list/</code>
* 获取乐团团长详情: <code>/api/intro/leader/cn/detail/{{ID}}/</code>
* 获取驻团指挥列表: <code>/api/intro/conductor/cn/list/</code>
* 获取驻团指挥介绍详情: <code>/api/intro/conductor/cn/detail/{{ID}}/</code>
* 获取艺术总监内容: <code>/api/intro/director/cn/</code>
* 获取乐器种类列表: <code>/api/intro/instrument/cn/</code>
* 获取乐团成员列表: <code>/api/intro/performer/cn/list/{{INSTRUMENT_ID}}/</code>
* 获取音乐会列表: <code>/api/musicale/musicale/cn/list/{{PAGE}}/</code>
* 获取音乐会详情: <code>/api/musicale/musicale/cn/detail/{{ID}}/</code>
* 获取月季列表: <code>/api/musicale/festival/cn/list/{{PAGE}}/</code>
* 获取月季详情: <code>/api/musicale/festival/cn/detail/{{ID}}/</code>
* 获取天姿国乐新闻列表: <code>/api/beautymelody/news/cn/list/{{PAGE}}/</code>
* 获取天姿国乐新闻全文: <code>/api/beautymelody/news/cn/detail/{{ID}}/</code>
* 获取歌剧院新闻列表: <code>/api/opera/news/cn/list/{{PAGE}}/</code>
* 获取歌剧院新闻全文: <code>/api/opera/news/cn/detail/{{ID}}/</code>
* 获取事业动态列表: <code>/api/businessdynamics/news/cn/list/reverse/{{PAGE}}/</code>
* 获取事业动态全文: <code>/api/businessdynamics/news/cn/detail/{{ID}}/</code>
* (待补)搜索: <code>/api/search?keyword=KEYWORD</code>
