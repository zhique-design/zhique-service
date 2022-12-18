from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ZhiQue import permissions
from blog.models import Category
from .serializers import CategorySerializer


# Create your views here.
class CategorySelectOptionView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, version):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

