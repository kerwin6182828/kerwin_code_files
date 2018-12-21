import datetime
import json
import time
import re

import os
from pyquery import PyQuery as pq

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
import json
import time
import re

import os
from pyquery import PyQuery as pq

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# from .forms import *

from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

# Create your views here.
def index_views(request):
    # instance = Article.objects.get(id=1)
    # context = get_object_or_404(Article,id=1)
    queryset = Article.objects.all()  # .order_by("-a_time")
    # user_name = User.objects.get(user_name)
    a = Paginator.page_range
    print(a)

    # print(username)
    paginator = Paginator(queryset, 8)  # Show 25 contacts per page

    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    context = {
        "object_list": queryset,
        # "username": user_name
    }

    # return render(request,'index.html', locals())
    return render(request, 'index.html', context)


def listing(request):
    contact_list = Contacts.objects.all()

    return render(request, 'list.html', {'contacts': contacts})


def login_views(request):
    return render(request,'login.html', locals())

def register_views(request):
    return render(request,'register.html', locals())

def home_views(request):
    return render(request,'home.html', locals())


def article_views(request, a_id):
    full_path = request.get_full_path()
    print()
    if 'uid' in request.session and 'uphone' in request.session:
        # session中有登录信息
        session_id = request.session["uid"]
        # 读者的头像（即“我”的头像）
        reader_portrait = User.objects.get(id=session_id).u_portrait
        reader_name = User.objects.get(id=session_id).u_name
        reader_id = session_id


    # 文章对象
    a_id = int(a_id)
    article_obj = Article.objects.get(id=a_id)
    a_title = article_obj.a_title
    a_content = article_obj.a_content
    a_time = article_obj.a_time
    a_cover = article_obj.a_cover
    a_time = article_obj.a_time
    article_obj.a_page_views += 1
    article_obj.save()
    a_page_views = article_obj.a_page_views
    a_like_num = article_obj.a_like_num
    a_collect = article_obj.a_collect

    # 用户对象(文章作者)
    user_obj = article_obj.u_id
    u_id = user_obj.id
    u_name = user_obj.u_name
    u_portrait = user_obj.u_portrait
    author_id = u_id




    return render(request, "article.html", locals())
    # return HttpResponse("<h1> hello </h1> "+ a_content)













def show_views(request):
    # 文章对象
    a_id = request.GET["a_id"]
    article_obj = Article.objects.get(id=int(a_id))
    a_title = article_obj.a_title
    a_content = article_obj.a_content

    # 用户对象（文章的作者id）
    user_obj = article_obj.u_id
    u_id = user_obj.id



    # return render(request, "article.html", locals())
    # return HttpResponse("ok")
    return HttpResponse(a_content)


def test_views(request):
    dic = {
        "t_time": datetime.datetime.now()
    }
    Test(**dic).save()



    return HttpResponse("test ok")


def comment_show_views(request):
    if 'uid' in request.session and 'uphone' in request.session:
        # session中有登录信息
        session_id = request.session["uid"]
        if request.method == "POST":
            print("88"*188, request.POST)
            comment_text = request.POST["comment_text"]
            a_id = request.POST["a_id"]
            reader_id = request.POST["reader_id"]
            Comment(a_id=Article.objects.get(id=a_id), from_uid=User.objects.get(id=reader_id), c_text=comment_text, c_time=datetime.datetime.now()).save()
            com_query = Comment.objects.filter(a_id=a_id)
            floor = 1
            com_lst = []
            for com in com_query:
                dic = {
                    "comment_id":com.id,
                    "commentator_portrait":com.from_uid.u_portrait,
                    "commentator_name":com.from_uid.u_name,
                    "comment_time":str(com.c_time)[:19],
                    "floor":floor,
                    "comment_text":com.c_text,
                }
                floor += 1
                com_lst.append(dic)
            com_lst_json = json.dumps(com_lst)
            return HttpResponse(com_lst_json)
        elif request.method == "GET":
            a_id = request.GET["a_id"]
            com_query = Comment.objects.filter(a_id=a_id)
            floor = 1
            com_lst = []
            for com in com_query:
                reply_query = com.reply_set.all()
                reply_list = []
                for reply in reply_query:
                    dic2 = {
                        "reply_id":reply.id,
                        "replyer_portrait":reply.from_uid.u_portrait,
                        "replyer_name":reply.from_uid.u_name,
                        "bei_reply_name":Comment.objects.get(id=com.id).from_uid.u_name,
                        "reply_time":str(reply.r_time)[:19],
                        "reply_text":reply.r_text,
                    }
                    reply_list.append(dic2)

                dic = {
                    "comment_id":com.id,
                    "commentator_portrait":com.from_uid.u_portrait,
                    "commentator_name":com.from_uid.u_name,
                    "comment_time":str(com.c_time)[:19],
                    "floor":floor,
                    "comment_text":com.c_text,
                    "reply_list":reply_list,
                }
                floor += 1
                com_lst.append(dic)
            com_lst_json = json.dumps(com_lst)
            return HttpResponse(com_lst_json)


def insert_reply_views(request):
    reply_text = request.POST["reply_text"]
    c_id = request.POST["c_id"]
    replyer_id = request.POST["replyer_id"]
    Reply(c_id=Comment.objects.get(id=c_id), from_uid=User.objects.get(id=replyer_id),to_uid=Comment.objects.get(id=c_id).from_uid.id, r_text=reply_text, r_time=datetime.datetime.now()).save()
    rep_query = Reply.objects.filter(c_id=c_id)
    rep_lst = []
    floor = 1
    for rep in rep_query:
        dic = {
            "rep_floor":floor,
            "reply_id":rep.id,
            "replyer_portrait":rep.from_uid.u_portrait,
            "replyer_name":rep.from_uid.u_name,
            "bei_reply_name":Comment.objects.get(id=c_id).from_uid.u_name,
            "reply_time":str(rep.r_time)[:19],
            "reply_text":rep.r_text,
        }
        rep_lst.append(dic)
        floor += 1
    rep_lst_json = json.dumps(rep_lst)
    return HttpResponse(rep_lst_json)



















# 该试图用于将2000个静态HTML的content存入article数据库
def content_views(request):
    # 获取指定静态文件夹内的所有html文件名
    article_lst = os.listdir(os.path.dirname("./static/content/"))
    for article_filename in article_lst:
        with open("./static/content/"+article_filename, encoding="utf-8") as f:
            # with open("./static/content/"+"Page_4_trip2387687774.html", encoding="utf-8") as f:

            html = f.read()
            # 使用pyquery对html文本进行css选择，得到需要的字符串
            query = pq(html)
            title = query(".trip-summary h2").html()
            # 剔除掉标题中的标签符号
            title_clean = "".join(re.findall(r"[\u4E00-\u9FA5]+|[\u0000-\u00FF]+", title))

            comments = query(".photo-comment").items()
            comments_lst = []
            for comment in comments:
                comment_str = str(comment.html())
                # 两种方式去剔除表情符号
                # comment_clean = "".join(re.findall(r"[\u4E00-\u9FA5]+|[\u0000-\u00FF]+", comment_str))
                comment_clean = "".join(re.findall(r"[\u0000-\u9FA5]+", comment_str))

                # print("this is clean: ", comment_clean)
                # 为所有文本元素添加 p 标签
                comment_clean = '<p id="main_text_content">' + comment_clean + '<p>'
                comments_lst.append(comment_clean)

            imgs = query(".waypoint .fancy-group img").items()
            imgs = [str(img.attr("data-retina")) for img in imgs]

            content = comments_lst.copy()
            i = 1
            for img in imgs:
                # 为所有图片链接地址套上img标签
                img_tag = '<img src="' + img + '" alt="">'
                content.insert(i, img_tag)
                i += 2
            # print(content)
            content_str = "<br><br>".join(content)

            user_obj = User.objects.get(id=1)

            dic = {
                "u_id":user_obj,
                "a_title":title_clean,
                "a_content":content_str,
                "a_cover":imgs[6],
                "a_time":datetime.datetime.now()
            }
            try:
                # 插入数据库
                Article(**dic).save()
            except Exception as reason:
                print("可能是文件太大了，数据库存不进去：", reason)
            # 测试时候开启，不能一下跑太多

    return HttpResponse("文章内容插入完毕")





# 老王的视图

# 注册
def register_views(request):
    if request.method == "GET":
        return render(request,"register.html")
    else:
        # 将register的数据导入数据库
        dic = {
            "u_phone": request.POST['uphone'],
            "u_pwd": request.POST['upwd'],
            "u_name": request.POST['uname'],
            "u_email": request.POST['uemail'],
        }
        # 将数据插入进数据库 - 注册
        User(**dic).save()
        # 根据uphone的值再查询数据库
        u = User.objects.get(u_phone=request.POST['uphone'])
        # 将用户id和uphone保存进session
        request.session['uid'] = u.id
        request.session['uphone'] = u.u_phone

        return redirect('/')




# 登陆
def login_views(request):
    referer = request.META["HTTP_REFERER"]
    url = '/'
    if request.method == "GET":
        #判断session
        if 'uid' in request.session and 'uphone' in request.session:
            #session中有登录信息
            return redirect(url)
        else:
            #session中没有登录信息，判断cookie
            if 'uid' in request.COOKIES and 'uphone' in request.COOKIES:
                #cookie中有登录信息
                uid = request.COOKIES['uid']
                uphone = request.COOKIES['uphone']
                #保存登录信息到session中
                request.session['uid'] = uid
                request.session['uphone'] = uphone
                return redirect(url)
            else:
                #cookie中也没有登录信息
                return render(request,'login.html', locals())

    else:
        #post流程
        #登录，对uphone,upwd信息到数据库中查重
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        referer = request.POST["referer"]
        uList = User.objects.filter(u_phone=uphone,u_pwd=upwd)
        if uList:
            #查重了，表示可以正常登录
            uid = uList[0].id
            uphone = uList[0].u_phone
            #保存信息到session中
            request.session['uid'] = uid
            request.session['uphone'] = uphone
            #判断是否记住密码
            resp = redirect(referer)
            if 'rem_pwd' in request.POST:
                #如果有记住密码，则保存登录信息到cookie中
                resp.set_cookie('uid',uid,60*60*24*366)
                resp.set_cookie('uphone',uphone,60*60*24*366)
            return resp
        else:
            #没有用户信息，跳出错误信息
            errMsg = "用户名或密码错误，请重新输入"
            # return HttpResponse("error")
            return render(request,'login.html',locals())


#找回密码页面
def find_password_views(request):
    return render(request,"find_password.html")


# 检查手机号是否存在
def check_uphone_views(request):
    if request.method == "POST":
        # 接收前端传递过来的手机号码
        uphone = request.POST['uphone']
        uList = Users.objects.filter(u_phone=uphone)
        if uList:
            # 如果条件为真，则表示手机号码已经存在
            # 响应 status值为0，用于通知客户端手机号码已存在
            # 响应 text值为 “手机号码已存在”
            dic = {
                "status": "0",
                "text": '手机号码已存在',
            }
            return HttpResponse(json.dumps(dic))
        else:
            # 反之，不存在相应的手机号
            # 响应 status值为1
            # 响应 text值为
            dic = {
                "status": "1",
                "text": "",
            }
            return HttpResponse(json.dumps(dic))




def log_out_views(request, a_url):
    print(request.session["uid"])
    print(request.session["uphone"])
    print("///"*88, a_url)
    del request.session["uid"]
    del request.session["uphone"]
    return redirect(a_url)

def like_views(request):
    if 'uid' in request.session and 'uphone' in request.session:
        session_id = request.session["uid"]
        a_obj = Article.objects.get(id=request.POST["a_id"])
        a_obj.a_like_num += 1
        a_obj.save()
        a_like_num = a_obj.a_like_num
        dic = {
            "status":1,
            "a_like_num":a_like_num,
        }
        return HttpResponse(json.dumps(dic))
    else:
        dic = {
            "status":0,
        }
        return HttpResponse(json.dumps(dic))


def collect_views(request):
    if 'uid' in request.session and 'uphone' in request.session:
        session_id = request.session["uid"]
        a_obj = Article.objects.get(id=request.POST["a_id"])
        a_obj.a_collect += 1
        a_obj.save()
        a_collect = a_obj.a_collect
        dic = {
            "status":1,
            "a_collect":a_collect,
        }
        return HttpResponse(json.dumps(dic))
    else:
        dic = {
            "status":0,
        }
        return HttpResponse(json.dumps(dic))
