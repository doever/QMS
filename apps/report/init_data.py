#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2018/4/6 22:21'
'''
生成生产数据
    参数:
        order_type:订单类型,只需传入订单类型首字符缩写,例如退换,'TH',生成TH170101-0001;
        start_date:订单的开始日期;
        end_date:订单的结束日期;
        num:生成订单的数量,默认10000条
        kwargs:如果用户传入的字典的value是列表,则在列表中寻找数据返回,若用户不
               知道该传什么数据,则只需要传入整型数据,即可生成对应长度的数据,
               如果传入getname,可对应生成name,传入bool类型,返回0或1
        
'''

import random
from datetime import datetime,timedelta
import unittest
import pymysql


class InitDb(object):
    def __init__(self,order_type,start_date,end_date,num=10000,**kwargs):
        self.order_type = order_type
        self.start_date = start_date
        self.end_date = end_date
        self.num = num
        self.kwargs = kwargs

    first_name_li = [
                    '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何',
                    '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏',
                    '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史',
                    '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄',
                    '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜',
                    '阮', '蓝', '闵', '席', '季', '麻', '强', '贾', '路', '娄', '危', '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '钟', '徐',
                    '邱', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍', '包', '诸', '左', '石', '崔', '宁', '龙', '池', '乔', '姬', '欧']

    last_name_li = ['对', '酒', '当', '歌', '人', '生', '几', '何', '慨', '当', '以', '慷', '忧', '思', '难', '忘', '关', '关', '雎', '鸠', '在',
                    '河', '之', '洲', '窈', '窕', '淑', '女', '君', '子', '好', '逑', '参', '差', '荇', '菜', '左', '右', '流', '之', '窈', '窕',
                    '淑', '女', '寤', '寐', '求', '之', '求', '之', '不', '得', '寤', '寐', '思', '服', '七', '月', '流', '火', '九', '月', '授',
                    '衣', '一', '日', '觱', '发', '二', '日', '栗', '烈', '无', '衣', '无', '褐', '何', '以', '卒', '岁', '三', '日', '于', '耜',
                    '四', '日', '举', '趾', '同', '我', '妇', '子', '桃', '之', '夭', '夭', '灼', '灼', '其', '华', '之', '子', '于', '归', '宜',
                    '其', '室', '家', '桃', '之', '夭', '夭', '有', '蕡', '其', '实', '之', '子', '于', '归', '宜', '其', '家', '室', '绿', '兮',
                    '衣', '兮', '绿', '衣', '黄', '里', '心', '之', '忧', '矣', '曷', '维', '其', '已', '绿', '兮', '衣', '兮', '绿', '衣', '黄',
                    '裳', '心', '之', '忧', '矣', '曷', '维', '其', '绿', '兮', '丝', '兮', '女', '所', '治', '兮', '习', '习', '谷', '风', '维',
                    '风', '及', '雨']

    def get_random(self,data_list):
        metadata = ''
        if isinstance(data_list,list):
            metadata = random.choice(data_list)
            return metadata

        elif isinstance(data_list,bool):
            metadata = random.choice([0,1])
            return metadata

        elif isinstance(data_list,int):
            for i in range(data_list):
                ran = str(random.randint(0,9))
                metadata += ran
            return metadata

        # 传入getname参数表示,随机获取一个名字
        elif data_list =='getname':
            leng = random.randint(1,3)
            first_name = random.choice(InitDb.first_name_li)
            last_name = ''
            for i in range(leng):
                last_name += random.choice(InitDb.last_name_li)
            metadata = first_name+last_name
            return metadata

        else:
            return metadata

    @classmethod
    def init_date(cls,d):
        if d < 9:
            d = '0' + str(d)
            return str(d)
        else:
            return str(d)

    def get_billno(self):
        date = (self.end_date-self.start_date).days
        incr = random.randint(0,date)
        date = self.start_date + timedelta(days=incr)
        createdate = str(date)
        installdate = str(date + timedelta(days=random.randint(1,10)))
        year = str(date.year)[2:4]
        month = InitDb.init_date(date.month)
        day = InitDb.init_date(date.day)
        no = str(random.randint(0,9999))
        # no = '1'
        if len(no) < 4:
            ran = 4-len(no)
            for i in range(0,ran):
                no = '0' + no
        billno = self.order_type+year+month+day+'-'+no

        return billno, createdate, installdate

    def prod_data(self):
        li = []
        for i in range(self.num):
            new_dict = {}
            billno, createdate, installdate = self.get_billno()
            new_dict['billno'] = billno
            new_dict['createdate'] = createdate
            new_dict['installdate'] = installdate
            for k,v in self.kwargs.items():
                new_dict[k] = self.get_random(v)
            li.append(new_dict)
        return li


if __name__ == '__main__':
    db = pymysql.connect(host='localhost', user='root', password='cl', db='loopapi', port=3306, charset='utf8')
    cur = db.cursor()
    start_date = datetime(2010,10,1)
    end_date = datetime(2018,1,1)
    cur.execute("select province,city,area from kft_province p left join kft_city c on p.id=c.father_id left join kft_area a on c.id=a.father_id")
    res = cur.fetchall()
    custom_defined = {
        "billstate":[-100,-110,-120,100,120,150],
        "billsort":['正常','换货单','补单','退货单'],
        "areacode":['100835','100836','100837','100838','100839','100841','100855','100856','100857','100859','100860'],
        "machinesid":['P10001','P14130','P10006','P10003','P10008','P10005','P10010','P10012'],
        "customer_name":'getname',
        "installer": 'getname',
        "agent": 'getname',
        "isspecial":True,
        "ishouse":True,
        "A3":True,
        "A7":['公共','家用','浩优','浩阳','依泉','机场','战略合作部','千野']

    }
    initdb = InitDb(order_type='KH',start_date=start_date,end_date=end_date,num=20,**custom_defined)
    datas = initdb.prod_data()
    for data in datas:
        ss = str(tuple(data.values())+tuple(random.choice(res)))
        sql = "insert into report_applynew (billno,createdate,installdate,billstate,billsort,areacode," \
              "machinesid,customer_name,installer,agent,isspecial,ishouse,A3,A7,province,city,area) values %s" % ss
        cur.execute(sql)
        db.commit()

    print("done")



