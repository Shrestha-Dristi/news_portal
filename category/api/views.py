from category.models import Category
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from category.api.serializers import CatSerializers
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class CatApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Category.objects.filter(is_active=True)
        serializer = CatSerializers(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        data['created_by']=request.user.id
        data['modified_by']=request.user.id

        serializer = CatSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Successfully saved",
                "data" : serializer.data
            }, status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST) 
    
class CatUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def put(self, request, pk):
        tag = get_object_or_404(Category, id=pk)
        if tag.created_by.id != request.user.id:
            return Response({
                "message": "Invalid User",
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        data = request.data
        data['modified_by'] = request.user.id
        serializer = CatSerializers(data=data, instance=tag)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message" : "Successfully updated",
                "data" : serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        tag = get_object_or_404(Category, id=pk)
        if tag.created_by.id != request.user.id:
            return Response({
                "message": "Invalid User",
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        tag.delete()
        return Response({
            "message" : "Tag Successfully deleted"
        },status=status.HTTP_204_NO_CONTENT)
