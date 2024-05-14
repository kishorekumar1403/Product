from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password
import jwt               #pip install pyjwt
from .models import *
from .serializers import *
from .filters import *
from .paginations import *
from .authentications import *

class superAdminView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
            queryset = superAdmin.objects.all()
            serializer = superAdminSerializer(queryset, many=True)
            return Response({'data': serializer.data})
     
    def post(self, request):
        serializer = superAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            instance = superAdmin.objects.get(id=id)
            serializer = superAdminSerializer(instance, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response({'data': serializer.data})
        except superAdmin.DoesNotExist:
            return Response({"error": "SuperAdmin not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, id):
        try:
            instance = superAdmin.objects.get(id=id)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except superAdmin.DoesNotExist:
            return Response({"error": "SuperAdmin not found"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class adminView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
            queryset = admin.objects.all()
            serializer = adminSerializer(queryset, many=True)
            return Response({'data': serializer.data})

    def post(self, request):
        # request.data['password'] = make_password(request.data['password'])
        serializer = adminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response ({'errors': serializer.errors} ,status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            instance = admin.objects.get(id=id)
            serializer = adminSerializer(instance, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response({'data': serializer.data})
        except admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, id):
        try:
            instance = admin.objects.get(id=id)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_204_NO_CONTENT)
    
class userView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
            queryset = user.objects.all()
            serializer = userSerializer(queryset, many=True)
            return Response({'data' : serializer.data})
     
    def post(self, request):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'erros':serializer.errors},status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            instance = user.objects.get(id=id)
            serializer = userSerializer(instance, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response({'data': serializer.data})
        except user.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            instance = user.objects.get(id=id)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except user.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class productView(APIView):
    authentication_classes = [userTokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
            queryset = product.objects.all()
            serializer = productSerializer(queryset, many=True)
            return Response({'data':serializer.data})
     
    def post(self, request):
        serializer = productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            queryset = product.objects.get(id=id)
            serializer = productSerializer(queryset, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response({'data':serializer.data})
        except product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'errors' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, id):
        try:
            instance = product.objects.get(id=id)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class superAdminLogin(APIView):

    def post(self, request):
        try:
            gmail = request.data.get('gmail')
            password = request.data.get('password')
            
            x = superAdmin.objects.get(gmail=gmail)

            if password == x.password:

                payload = {"superadmin":x.superAdminName, "gmail":x.gmail}

                token = jwt.encode(payload,key="login_key",algorithm="HS256")

                return Response({"payload":payload, "token":token}, status=status.HTTP_200_OK)
            else:
                return Response({"invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Exception as exp:
            return Response({"error":str(exp)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class adminLogin(APIView):

    def post(self, request):
        try:
            gmail = request.data.get('gmail')
            password = request.data.get('password')
            
            x = admin.objects.get(gmail=gmail)

            if x and check_password(password,x.password):
                payload ={"admin_name":x.adminName, "gmail":x.gmail}

                token = jwt.encode(payload,key="login_key",algorithm="HS256")

                return Response({"payload":payload, "token":token}, status=status.HTTP_200_OK)
            else:
                return Response({"invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Exception as exp:
            return Response({"error":str(exp)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class userLogin(APIView):

    def post(self, request):
        try:
            gmail = request.data.get('gmail')
            password = request.data.get('password')
            
            y = user.objects.get(gmail=gmail)
            # print(password == y.password, password, y.password, y.id)
            if password == y.password:
                
                payload = {"id": str(y.id), "gmail": y.gmail}

                token = jwt.encode(payload, key="login_key", algorithm="HS256")

                return Response({"payload": payload, "token": token}, status=status.HTTP_200_OK)
            else:
                
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except user.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as exp:
            return Response({"error": str(exp)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ProductListView(APIView):
    
    def get(self, request):
        queryset = product.objects.all()
        product_filter = productFilter(request.GET, queryset=queryset)
        filtered_queryset = product_filter.qs
        serialized_data = productSerializer(filtered_queryset, many=True).data
        return Response({'data': serialized_data})
    
class productPaginationView(generics.ListAPIView):
    queryset = product.objects.all()
    serializer_class = productSerializer
    pagination_class = productPagination