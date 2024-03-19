from django.http import JsonResponse
from base.models import Product,Category
from .Serializer import ProductSerializer ,CategorySerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

@api_view(['get'])
def index(request):
    return Response({"username":"dor"})

#  --------------------------------------------------------------------------------
# token view
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email']  = user.email
        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# end of token 
#  --------------------------------------------------------------------------------
# register view

@api_view(['POST','GET'])
def register(request):
    user = User.objects.create_user(
                username=request.data['newUserName'],
                email=request.data['newUseremail'],
                password=request.data['newUserPassword']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")

#end of register

# --------------------------------------------------------------------------------

# product view

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_Products(req):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=404)

@api_view(['POST'])
# Uncomment the next line if you want to restrict access to authenticated users
@permission_classes([IsAuthenticated])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=404)
    
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=204)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=404)

# end of product view
#  --------------------------------------------------------------------------------
# category view

@api_view(['GET'])
def get_categories(req):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_category(req, pk):
    try:
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)
    except Category.DoesNotExist:
        return JsonResponse({'message': 'The category does not exist'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(req):
    serializer = CategorySerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_category(req, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JsonResponse({'message': 'The category does not exist'}, status=404)
    
    serializer = CategorySerializer(category, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_category(req, pk):
    try:
        category = Category.objects.get(pk=pk)
        category.delete()
        return JsonResponse({'message': 'Category was deleted successfully!'}, status=204)
    except Category.DoesNotExist:
        return JsonResponse({'message': 'The category does not exist'}, status=404)