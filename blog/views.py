from django.shortcuts import render, HttpResponse

def blog_list(request): 
    return HttpResponse("Blog Page")

# def blog_detail(request, pk): 
#     return HttpResponse()
