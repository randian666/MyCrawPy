#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import pymysql
import uuid

db = pymysql.connect("","","","" )

DOMTree=parse("LocList.xml")
collection=DOMTree.documentElement
countryRegion = collection.getElementsByTagName("CountryRegion")
with db.cursor() as cursor:
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)
    for country in countryRegion:
        local = ''
        countryId=''
        #国家
        if country.hasAttribute("Name") and country.hasAttribute("Code"):
            if country.getAttribute("Code")=='1':
                local='zh_cn'
            else:
                local='en_us'
            countrySql="INSERT INTO data_location(uuid,parent_id,code,name,lang,layer) VALUES('%s',%d,'%s','%s','%s',%d)" \
                       %(uuid.uuid1(),0,country.getAttribute("Code"),country.getAttribute("Name"),local,1)
            # 执行sql语句
            cursor.execute(countrySql)
            #省会主键ID
            countryId=db.insert_id()
            print("国家: %s,code:%s" % (country.getAttribute("Name"),country.getAttribute("Code")))
        #省
        state=country.getElementsByTagName("State")
        for sta in state:
            if sta.hasAttribute("Name") and sta.hasAttribute("Code"):
                staSql = "INSERT INTO data_location(uuid,parent_id,code,name,lang,layer) VALUES('%s',%d,'%s','%s','%s',%d)" \
                             % (uuid.uuid1(), countryId, sta.getAttribute("Code"), sta.getAttribute("Name"), local, 2)
                # 执行sql语句
                cursor.execute(staSql)
                staId=db.insert_id()
                print("省会: %s,code:%s" % (sta.getAttribute("Name"), sta.getAttribute("Code")))
            #市区
            citys=sta.getElementsByTagName("City")
            for city in citys:
                if city.hasAttribute("Name") and city.hasAttribute("Code"):
                    citySql ="INSERT INTO data_location(uuid,parent_id,code,name,lang,layer) VALUES('%s',%d,'%s','%s','%s',%d)" \
                             % (uuid.uuid1(), staId, city.getAttribute("Code"), city.getAttribute("Name"), local, 3)
                    # 执行sql语句
                    cursor.execute(citySql)
                    cityId = db.insert_id()
                    print("市区/区: %s,code:%s" % (city.getAttribute("Name"), city.getAttribute("Code")))
                regions = city.getElementsByTagName("Region")
                #县城
                for region in regions:
                    if region.hasAttribute("Name") and region.hasAttribute("Code"):
                        regionSql ="INSERT INTO data_location(uuid,parent_id,code,name,lang,layer) VALUES('%s',%d,'%s','%s','%s',%d)" \
                                 % (uuid.uuid1(), cityId, region.getAttribute("Code"), region.getAttribute("Name"), local, 4)
                        # 执行sql语句
                        cursor.execute(regionSql)
                        print("县城: %s,code:%s" % (region.getAttribute("Name"), region.getAttribute("Code")))
    # 执行sql语句
    db.commit()