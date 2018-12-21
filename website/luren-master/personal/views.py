from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from index.models import *
from .admin import *
import datetime
import json

# Create your views here.

def personal_index_views(request):
	url = request.META.get('HTTP_REFERER', '/login')
	if 'uid' in request.session:
		return render(request,'personal_index.html')
	else:
		return redirect(url)
	# else:
	# 	return redirect('/login/')

def about_views(requset):
	return render(requset,'personal_about.html')


def board_views(request):
	return render(request,'personal_board.html')


def mood_views(request):
	return render(request,'personal_mood.html')


def articleEdit_views(request):
	if request.method =="POST":
		localtime = datetime.datetime.now()+ datetime.timedelta(hours=8)
		u_id = request.session['uid']
		a_title = request.POST['title']
		a_content = request.POST['content']
		a_cover = request.POST['cover_image']
		a_time = localtime.strftime('%Y-%m-%d %H:%M:%S')
		print(type(a_time))
		dic={
			'u_id_id':u_id,
			'a_title':a_title,
			'a_content':a_content,
			'a_cover':a_cover,
			'a_time':a_time,
		}
		Article(**dic).save()
		return redirect('/personal/index/')
	else:
		myform = BlogEditorAdminForm()
		return render(request,'articleEdit.html',locals())


def upload_portrait_views(request):
	xid=request.session['uid']
	str_id = 'uid=('+str(xid)+')&'
	img = request.FILES["u_portrait"]
	content = img.read()
	img_url = '/Users/cire/Downloads/Websites/Luren_project/Luren/media/portraits/'+str_id+img.name
	u_portrait = '/media/portraits/'+str_id+img.name

	with open(img_url,'wb') as f:
		f.write(content)

	return render(request,'personal_about.html',locals())



def load_articles_views(request):
	if 'uid' in request.session:
		uid = request.session['uid']
		articles = Article.objects.filter(u_id=uid)[:8]
		if articles:
			# articles_L=[]
			# print(articles)
			# for a in articles:
			# 	jsonA = json.dumps(a.to_dict())
			# 	print(jsonA)
			# 	articles_L.append(jsonA)
			# print(articles_L)
			jsonStr = serializers.serialize('json',articles)
			print("****"*88,jsonStr)

			return HttpResponse(jsonStr)
		else:
			return redirect('/personal/index/')
	else:
		redirect('/')


def load_about_views(request):

	# if 'uid' in request.session and 'reader_id'=='uid':
	if 'sessionid' in request.COOKIES:
		# if 'uid' =='reader_id':
		uid = request.session['uid']
		user = User.objects.get(id=uid)
		print(user)
		dic = user.to_dict()
		dic['status'] = 1
	else:
		user = User.boject.get(id='article_id')
		dic = user.to_dict()
		dic['status'] = 0
	return HttpResponse(json.dumps(dic))





def load_mood_views(request):
	# var article_id = request.['request']
	pass
def load_board_views(request):
	pass


def userinfos_views(request):
	uid = request.post['uid']
	dic = {
		'u_name':request.POST['uname'],
		'u_email':request.POST['uemail'],
		'u_gender':request.POST['ugender'],
		'u_age':request.POST['uage'],
		'u_address':request.POST['uaddress'],
		'u_profile':request.POST['uprofile'],
		'u_portrait':u_portrait,
	}
	User(**dic).update(id=uid)
	return redirect('/personal/about/')