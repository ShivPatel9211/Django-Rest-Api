from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
from .serializers import StudentSerializer
from .models import Student
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
# function based api 
# @csrf_exempt
# def studentDetail(request):
    # code to fatch data 
    # if request.method == 'GET':
        # json_data = request.body
        # stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        # id = pythondata.get('id',None)
        # if id is not None:
        #     std = Student.objects.get(id =id)
        #     serializer = StudentSerializer(std)
        #     json_data = JSONRenderer().render(serializer.data)
        #     return HttpResponse(json_data,content_type='application/json')
        # else:
        #     std = Student.objects.all()
        #     serializer = StudentSerializer(std , many=True)
        #     json_data=JSONRenderer().render(serializer.data)
        #     return HttpResponse(json_data,content_type='application/json')
    # code to insert new data 
    # if request.method == 'POST':
        # json_data=request.body
        # stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        # serializer = StudentSerializer(data=pythondata)
        # if serializer.is_valid():
        #     serializer.save()
        #     res = {'msg':'Data inserted successfully'}
        #     json_data=JSONRenderer().render(res)
        #     return HttpResponse(json_data,content_type='application/json')
        # else:
        #     error = JSONRenderer().render(serializer.errors)
        #     return HttpResponse(json_data,content_type='application/json')
    # code to update the existing data
    # if request.method == 'PUT':
    #    json_data = request.body
    #    stream = io.BytesIO(json_data)
    #    pythondata = JSONParser().parse(stream)
    #    id = pythondata.get('id')
    #    std = Student.objects.get(id=id)
    #    serializer = StudentSerializer(std , data=pythondata,partial=True)
    #    if serializer.is_valid():
    #        serializer.save()
    #        res = {'msg':'Data updated successfully'}
    #        json_data= JSONRenderer().render(res)
    #        return HttpResponse(json_data,content_type='application/json')
    #    else:
    #        json_data=JSONRenderer().render(serializer.errors)
    #        return HttpResponse(json_data,content_type='application/json')
    # code to delete the object 
    # if request.method == 'DELETE':
    #     json_data= request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     id = pythondata.get('id')
    #     std = Student.objects.get(id=id)
    #     std.delete()
    #     res = {'msg':'Object deleted'}
    #     json_data=JSONRenderer().render(res)
    #     return HttpResponse(json_data,content_type='application/json')

# class based api

@method_decorator(csrf_exempt,name='dispatch')
class studentDetail(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            std = Student.objects.get(id =id)
            serializer = StudentSerializer(std)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        else:
            std = Student.objects.all()
            serializer = StudentSerializer(std , many=True)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
    
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data inserted successfully'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:
            error = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        std = Student.objects.get(id=id)
        serializer = StudentSerializer(std , data=pythondata,partial=True)
        if serializer.is_valid():
           serializer.save()
           res = {'msg':'Data updated successfully'}
           json_data= JSONRenderer().render(res)
           return HttpResponse(json_data,content_type='application/json')
        else:
           json_data=JSONRenderer().render(serializer.errors)
           return HttpResponse(json_data,content_type='application/json')

    def delete(self,request,*args,**kwargs):
        json_data= request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        std = Student.objects.get(id=id)
        std.delete()
        res = {'msg':'Object deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')



