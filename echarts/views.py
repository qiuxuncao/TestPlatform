# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render

# Create your views here.


def echarts(request):
    # 下面等价于：select distinct auth,count() as blog_count from cms_blogpost group by auth
    # auth_count_blog=BlogPost.objects.values('auth').distinct().annotate(blog_count=Count('auth')).all()
    # print '第1个作者的数量为：', auth_count_blog
    # auth_count_blog=[{'blog_count': 1, 'auth': u'guchen'}, {'blog_count': 1, 'auth': u'\u6c6a\u5a07'},
    # {'blog_count': 7, 'auth': u'\u8c37\u6668'}]
    auth_count_blog = {'blog_count': [10, 15, 20],
                       'auth': ["grn", "watryto", "zyruhu"]}
    #  向js中传递数据必须json.dumps()处理
    return render(request, 'echarts.html', {'auth_count_blog': json.dumps(auth_count_blog)})


