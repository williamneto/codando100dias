# -*- coding: utf-8 -*-
from mezzanine.blog.models import BlogPost
from mezzanine.blog.models import BlogCategory


def all_pages(request):	
	blog_posts = BlogPost.objects.all()	

	return {"blog_posts": blog_posts}
