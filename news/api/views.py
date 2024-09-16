from django.http import JsonResponse
from news.models import Tags,News
from news.api.serializers import TagSerializers, NewsSerializers    
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework import generics 

def news(request):
    return JsonResponse({
        "name":"testing",
        "testing":"test",
        "data":{
            "test":"hello"
        }
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tags(request):
    data = Tags.objects.filter(is_active=True)
    serializer = TagSerializers(data, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['POST'])
def tag_post(request):
    serializer = TagSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Successfully saved"
        }, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def tag_stats(request):
    data = Tags.objects.filter(is_active=True).count()
    return Response({
        "is_active":data
    })

@api_view(['GET'])
def tag_detail(request,id):
    data = Tags.objects.filter(id=id,is_active=False).first()
    if data is not None:
        serializer = TagSerializers(data)
        return Response(serializer.data)
    return Response({})

@api_view(['POST'])
def tag_update(request, id):
    data = Tags.objects.get(id=id)
    serializer = TagSerializers(data=request.data, instance=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
                    "message":"Successfully saved",
                    "data":serializer.data,
                }, status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def tag_delete(request,id):
    data = Tags.objects.get(id=id)
    data.delete()
    return Response({
        "message":"deleted"
    })

class TagApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Tags.objects.filter(is_active=True)
        serializer = TagSerializers(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        data['created_by']=request.user.id
        data['modified_by']=request.user.id

        serializer = TagSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Successfully saved"
            }, status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST) 
    
class UpdateAndDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def put(self, request, pk):
        tag = get_object_or_404(Tags, id=pk)
        if tag.created_by.id != request.user.id:
            return Response({
                "message": "Invalid User",
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        data = request.data
        data['modified_by'] = request.user.id
        serializer = TagSerializers(data=data, instance=tag)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message" : "Successfully updated",
                "data" : serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        tag = get_object_or_404(Tags, id=pk)
        if tag.created_by.id != request.user.id:
            return Response({
                "message": "Invalid User",
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        tag.delete()
        return Response({
            "message" : "Tag Successfully deleted"
        },status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def news_today(request):
    data = News.objects.filter(is_active=True)
    serializer = NewsSerializers(data, many=True)
    print(serializer)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def news_today_create(request):
    serializer = NewsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message" : "News Successfully Created",
            "data" : serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 422)

