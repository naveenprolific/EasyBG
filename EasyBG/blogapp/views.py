from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article 
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle
# Create your views here.
def article_list(request):
	article = Article.objects.all().order_by('date')
	context = {
	'article':article,
	}
	return render(request,'blogapp/home.html',context)

def article_details(request, slug):
	article = Article.objects.get(slug=slug)
	context ={
	'article':article,
	}
	return render(request,'blogapp/article_details.html',context)
@login_required(login_url= '/accounts/login/')
def article_create(request):
	if request.method == 'POST':
		form = CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('blogapp:list')
	else:
		form = CreateArticle(None)
	context={'form':form}
	return render(request,'blogapp/article_create.html',context)
