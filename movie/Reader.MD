环境搭建：
安装Scrapy可以使用pip命令：pip install Scrapy

1、创建工程
scrapy startproject movie
2、创建爬虫程序
scrapy genspider meijutt meijutt.com
#meiju 为爬虫的名称，meijutt.com为要爬取的网站的域名。
3. 文件说明
scrapy.cfg     项目的配置信息，主要为Scrapy命令行工具提供一个基础的配置信息。（真正爬虫相关的配置信息在settings.py文件中）
items.py      设置数据存储模板，用于结构化数据，如：Django的Model
pipelines     数据处理行为，如：一般结构化的数据持久化
settings.py   配置文件，如：递归的层数、并发数，延迟下载等
spiders       爬虫目录，如：创建文件，编写爬虫规则
4. 设置数据存储模板
items.py
5. 编写爬虫
meijutt.py
6. 修改配置文件
settings.py
7. 编写数据处理脚本
pipelines.py
8. 执行爬虫
cd movie
#运行爬虫
scrapy crawl meijutt --nolog
#运行爬虫并输入到指定的文件中
scrapy crawl meijutt --nolog -o movie.csv



