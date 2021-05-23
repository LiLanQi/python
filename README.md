# Python学习  

## day01

* python基础语法学习   
* pycharm的安装、环境变量配置以及使用  
* 了解如何安装第三方库 ```pip intsall``

## day02  

* 了解并学习使用火车头软件爬取数据

* requests库以及BeautifulSoup库的了解，爬取简单静态网页以及理解其过程
* 了解xpath内部参数的意思```c_data.xpath('//*[@id="root"]/div/div')``
* 复习html相关知识
* 使用lxml库爬取简单静态页面

## day03  

* 查找翻页规律，爬取豆瓣排名前250的电影名称（静态页面抓取)，<https://movie.douban.com/top250?start=>
* 爬取页面所有标题<http://www.santostang.com/>
* 爬取NBA页面数据
* 爬取动态nba页面数据（如何从页面中找到json文件）  
* 爬取动态页面评论（解析真实地址抓取.json），简单输出<http://www.santostang.com/2018/07/04/hello-world/>
* 初步了解Selenium模拟浏览器抓取动态页面数据，获取前3页文章所有评论

## day04  

* 了解并学习解析网页三大方式  

     1. 使用正则表达式解析网页  

     2. 使用BeautifulSoup解析网页  

        ​    + 了解文档树

     3. 使用lxml解析网页  

        ​    + 了解Xpath的选取

* 爬取房屋价格数据  
* 学习python文件输入输出，将数据存储至.csv  
* 复习mysql数据库，结合MySQLdb第三方库将数据存储进mysql数据库
* 学习yiled关键字的作用

## day05  

* 了解反爬虫以及如何解决反爬虫  
         1. 修改爬虫间隔时间
         2. 修改请求头
         3. 获取真实地址（数据存储在json文件中，或者使用ajax载入的时候有真实地址，地址有规律，亦或者使用ajax的时候找到的其所有真实地址都是同一个，每次刷新这个地址都会得到不同的值）

* 解决中文乱码  
* 登录与简单数字验证码的处理  
         1. 使用post提交数据
         2. 处理cookies
         3. 人工方法处理简单数字验证码  

* 使用百度API获取数据  
* 了解scrapy框架

## day06  

* 简单学习scrapy框架使用，学习其API文档中  
* 学习selectorLib插件的使用，提取页面所需要的内容至.YML文件中
* 结合scrapy以及selectorLib爬取页面商品数据<http://scrapeme.live/shop/>
* 结合scrapy以及selectorLib爬取阿里巴巴商品数据，并且存储至.csv文件中
* 爬取阿里耳机商品数据，解决图片无法获取以及链接问题

## day07 

* 了解git并上传代码至github  
* 学习使用markdown语言
* 阅读squareup API文档
* 往网页中插入商品数据  





## day08  

* socket安装以及下载splash

* splash+scrapy爬取阿里动态页面失败 
* beautifulSoup爬取阿里图片失败

* 爬取dropshipping商品数据，图片爬取失败



## java学习  

* 使用url调用接口功能
* 实现图片上传、商品上传功能，并且提供接口  
* SpringBoot学习  
* Swagger学习  
* Redis学习  
* lombok插件学习  
* 改进商品上传功能
* 解决项目部署过程中的各种bug问题
* postman了解及其使用
* 图解http学习