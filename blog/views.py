# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Article, Comment
from blog.forms import CommentForm
from django.http import JsonResponse
# Create your views here.
def simplJson(request):
    #article_list = Article.objects.all()
    #data = [{'id': x.id, 'title':x.title} for x in article_list]
    data = request.POST['text']
    comment = Comment(article_id=1,text=data)
    comment.save()
    return JsonResponse(comment.id,safe=False)

def article_list(request):
    article_list = Article.objects.all()
    return render(request,'article_list.html',context={'art_list':article_list})

def article_detail(request,pk):
    article = Article.objects.get(pk=pk)
    comment_list = article.comment_set.all()
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        for f in form.cleaned_data:
            print form.cleaned_data[f]
    else:
        form = CommentForm()
    return render(request,
                  'article_detail.html',
                  context={'object':article,'comment_list':comment_list,'form':form})
