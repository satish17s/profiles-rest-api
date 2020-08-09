from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers





class HelloApiView(APIView):
    """test api view"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of apiview"""
        an_apiview=['uses Http method as functions (get,post,patch,put,delete)',
        'is similiar to traditional djnago view',
        'gives most control over application logic',
        'is mapped manualy in URLs',

        ]

        return Response({'message':'hello','an_apiview':an_apiview})


    def post(self,request):
        """create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST
            )


    def put(self,request,pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})


    def patch(self,request,pk=None):
        """handle partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})
