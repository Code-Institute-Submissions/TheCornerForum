from django.shortcuts import render

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    # Your code for posts view
    pass

def post_detail(request, slug):
    # Your code for post_detail view
    pass
