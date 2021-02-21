from django.shortcuts import render

posts = [
    {
        'author': 'Eddy Guo',
        'title': 'Blog Post 1',
        'content': 'First Post', 
        'date_posted': 'February 20, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post', 
        'date_posted': 'February 20, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')