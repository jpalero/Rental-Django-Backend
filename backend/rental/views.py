from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo
from .serializers import UserInfoSerializer

# Create your views here.
class UserList(APIView):
    def get(self, request, format=None):
        userinfo = UserInfo.objects.all()
        serializer = UserInfoSerializer(userinfo, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return UserInfo.objects.get(pk=pk)
        except UserInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userinfo = self.get_object(pk)
        serializer = UserInfoSerializer(userinfo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        userinfo = self.get_object(pk)
        serializer = UserInfoSerializer(userinfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userinfo = self.get_object(pk)
        userinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
