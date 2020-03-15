from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from ..models import profile
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from rest_framework.response import Response

import datetime

class ProfileListView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    queryset = profile.objects.all()
    serializer_class = ProfileSerializer
    template_name = 'profiler/profiles.html'

    def get(self, request):
        queryset = profile.objects.all()
        serializer_class = ProfileSerializer(queryset, many=True, context={'request':request})
        return Response({'profiles': serializer_class.data})

    def post(self, request, format=None):
        serializer_class = ProfileSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'profiles': serializer_class.data})

        return Response(serializer.errors)

class ProfileView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profiler/profile.html'

    def get(self, request, pk, format=None):
        self.pk=pk
        queryset = self.get_object()
        serializer_class = ProfileSerializer(queryset,  context={'request':request})
        return Response({'profile':serializer_class.data, 'date':datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})

    def put(self, request, pk, format=None):
        self.pk = pk
        queryset = self.get_object()
        serializer_class = ProfileSerializer(queryset, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'profiles':serializer_class.data})
        return Response(serializer_class.errors)

    def delete(self, request, pk, format=None):
        self.pk=pk
        snippet = self.get_object()
        snippet.delete()
        return Response()

    def get_object(self):
        try:
            return profile.objects.get(id=self.pk)
        except profile.DoesNotExist:
            raise Http404
        return

class ProfileParserView(APIView):

    def get(self, request, pk, format=None):
        self.pk=pk
        queryset = self.get_object()
        serializer_class = ProfileSerializer(queryset,  context={'request':request})

        response = Response({'profile': serializer_class.data, 'date':datetime.datetime.now().strftime("%Y-%m-%d %H hour")})
        if(request.resolver_match.url_name=='profiler_parsed_date'):
            response = Response({'profile': serializer_class.data})

        response['Content-Disposition'] = 'attachment; filename=file.xml'
        return response


    def get_object(self):
        try:
            return profile.objects.get(id=self.pk)
        except profile.DoesNotExist:
            raise Http404
        return
