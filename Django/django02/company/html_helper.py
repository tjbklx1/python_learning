#!/usr/bin/evn python
#coding=utf-8

from django.utils.safestring import mark_safe

class PageInfo:
    def __init__(self,current_page,all_count,per_items=1):
        
#         per_item=5  # 每一页显示的条目数
#         start=(page-1)*per_item
#         end=page*per_item
    
        self.current_page=current_page
        self.all_count=all_count
        self.per_items=per_items
        
    @property
    def start(self):
        return (self.current_page-1)*self.per_items
    
    @property
    def end(self):
        return self.per_items*self.current_page
    
    @property
    def all_page_count(self):
        
#    总页数
#     all_page=count/per_item
#     all_page=count/per_item+1

        temp=divmod(self.all_count,self.per_items)
        if temp[1]==0:
            all_page_count=temp[0]
        else:
            all_page_count=temp[0]+1
        return all_page_count


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
    
    begin=page-5
    end=page+5
    
    if all_page_count<11:
        begin=0
        end=all_page_count
    else:
        if page<6:
            begin=0
            end= 11
        else:
            if page+6>all_page_count:
                begin=page-6
                end=all_page_count
            else:
                begin=page-6
                end=page+5
    
    #主体页码
    for i in range(begin,end):
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