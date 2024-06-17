from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Show
from .serializers import ShowSerializer
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.generics import ListAPIView

class UpdateShowView(View):
    def put(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        form_data = request.body.decode('utf-8')
        data = {}
        
        fields = form_data.split('------WebKitFormBoundary')
        for field in fields:
            lines = field.split('\r\n')
            if lines and len(lines) > 2:
                name_line = lines[1]
                value_line = lines[3]
                name = name_line.split('name="')[1].split('"')[0]
                value = value_line.strip()
                data[name] = value
        
       
        serializer = ShowSerializer(show, data=data)  
               
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors, status=400)


class ShowList(APIView):

    def get(self, request):
        shows = Show.objects.all()
        serializer = ShowSerializer(shows, many=True)  
        return Response({'shows': serializer.data})


    def post(self, request):
        serializer = ShowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShowDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Show, pk=pk)

    def get(self, request, pk):  
        show = self.get_object(pk)
        serializer = ShowSerializer(show)        
        return Response(serializer.data)

    
    def delete(self, request, pk):          
        show = self.get_object(pk)        
        show.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShowListByYear(ListAPIView):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()
    print("queryset:",queryset)
    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.query_params.get('year')
        print("year:",year)
        if year:
            queryset = queryset.filter(year_of_release=year)
        return queryset
