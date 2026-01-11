from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import ProductSerializer
from rest_framework import status
from ..models import Product

@api_view(['GET','POST'])
def product_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        print(product)
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    # for post request
    if request.method == 'POST':
        # title = request.data.get('title')
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data posted successfully",'data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    






