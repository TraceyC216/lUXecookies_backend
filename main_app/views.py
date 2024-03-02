from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Cookie
from .serializers import *

# Create your views here.

def about(request):
    return render(request, 'about.js')

@api_view(['GET', 'POST'])
def cookies_list(request):
    if request.method == 'GET':
        data = Cookie.objects.all()

        serializer = CookieSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CookieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def category_list(request, category):
    data = Cookie.objects.filter(category=category).values()
    serializer = CookieSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_detail(request, id):
    print(type(id))
    cookie = Cookie.objects.get(id=id)
    print(cookie)
    serializer = CookieSerializer(cookie, context={'request': request}, many=False)
    return Response(serializer.data)


    
# @api_view(['PUT', 'DELETE'])
# def cookies_detail(request, pk):
#     try:
#         cookie = Cookie.objects.get(pk=pk)
#     except Cookie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.methos == 'PUT':
#         serializer = CookieSerializer(cookie, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         cookie.delete()
#         return Response(status=status.HTTP_24_NO_CONTENT)
    