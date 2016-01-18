#!/usr/bin/evn python
#coding=utf-8

from django.utils.safestring import mark_safe


def Pager(page , all_page_count):
    # page:当前页， all_page_count：总页数
    
    page_html=[]
    
    #首页
    first_html="<a href='/company/host/%s'>首页</a>" %(1,)
    page_html.append(first_html)
    
    #上一页
    if page<=1:
#         prev_html="<a href='#'>上一页</a>"
        prev_html="<a href='/company/host/%s'>上一页</a>" %(1,)
    else:
        prev_html="<a href='/company/host/%s'>上一页</a>" %(page-1)
    page_html.append(prev_html)
    
    #主体页码
    for i in range(all_page_count):
        if page==i+1:
            a_html="<a class='selected' href='/company/host/%s'>%s</a>" %(i+1,i+1)
        else:
            a_html="<a href='/company/host/%s'>%s</a>" %(i+1,i+1)
        page_html.append(a_html)
    #下一页
    if page>=all_page_count:
#         next_html="<a href='#'>下一页</a>"
        next_html="<a href='/company/host/%s'>下一页</a>" %(all_page_count,)
    else:
        next_html="<a href='/company/host/%s'>下一页</a>" %(page+1)
    page_html.append(next_html)
    
    #尾页
    end_html="<a href='/company/host/%s'>尾页</a>" %(all_page_count,)
    page_html.append(end_html)
    page_string=mark_safe(''.join(page_html))
    #     page=mark_safe("<a href='/company/host/1'>1</a>") # 只显示首页时
    
    return page_string