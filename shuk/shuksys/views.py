from django.http.response import ResponseHeaders
from rest_framework import response, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try: 
        user = User.objects.get(username = username)
        
    except User.DoesNotExist:
        return Response({"status":"error",'message':'Usuario o contraseña ingresados son invalidos'}, status=status.HTTP_200_OK)

    pwd_valido = check_password(password, user.password)

    if not pwd_valido:
        return Response({"status":"error",'message':'Usuario o password ingresados son invalidos'}, status=status.HTTP_200_OK)
    
    token, create = Token.objects.get_or_create(user=user)
    return Response({"status":"sucess","message":token.key, "staff":user.is_staff},status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def prueba(request):
    mensajes = request.user.id
    return Response(mensajes)

  

        
 


    

