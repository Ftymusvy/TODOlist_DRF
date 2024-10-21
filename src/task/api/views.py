from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task.models import TodoTask
from task.api.serializers import TodoTaskSerializer

@api_view(['GET'])
def task_list(request):
    if request.method == "GET":
        query = TodoTask.objects.all()
        serializer = TodoTaskSerializer(query, many=True)
        return Response(serializer.data)



#برگرداندن ابجکت مورد نظر API
@api_view(['GET'])
def api_task_detail(request,id):
    try:
        task = TodoTask.objects.get(pk=id)
    except TodoTask.DoesNotExist:
         return Response({"error": "Task not found or has been deleted"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = TodoTaskSerializer(task)
        return Response(serializer.data)

        
#بروزرسانی ابجکت موردنظر با PUT
@api_view(['PUT'])
def api_task_update(request,pk):
    try:
        task = TodoTask.objects.get(pk=pk)
    except TodoTask.DoesNotExist:
          return Response({"error": "Task not found or has been deleted"}, status=status.HTTP_404_NOT_FOUND)
    data = {}
    if request.method == "PUT":
        serializer = TodoTaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data['anjam shod'] = "update anjam shod"
            return Response(data=data)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)    
