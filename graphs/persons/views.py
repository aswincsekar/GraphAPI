from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .utils import StructuredThingSerializer
from .models import Person
from rest_framework import viewsets, status
from rest_framework.response import Response
from py2neo import Graph
from rest_framework.decorators import action


class PersonViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        page = request.query_params.get("page",1)
        page_size = request.query_params.get("page_size",10)
        queryset = Person.nodes.all()[(page-1)*page_size:page*page_size]
        serializer = StructuredThingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.nodes.all()
        person = Person.nodes.get(uid=pk)
        serializer = StructuredThingSerializer(person)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        age = data.get("age", None)
        name = data.get("name", None)
        p = Person(name=name, age=age)
        p.save()
        return Response(data={"uid":p.uid,"name":p.name,"age":p.age}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        data = request.data
        age = data.get("age", None)
        name = data.get("name", None)
        p = Person.nodes.filter(uid=pk)
        if p:
            p.name=name
            p.age=age
            p.save()
            return Response(data={"uid":p.uid,"name":p.name,"age":p.age}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        data = request.data
        age = data.get("age", None)
        name = data.get("name", None)
        p = Person.nodes.filter(uid=pk)
        if p:
            p.name = name if name else p.name
            p.age = age if age else p.age
            p.save()
            return Response(data={"uid": p.uid, "name": p.name, "age": p.age}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        p = Person.nodes.filter(uid=pk)
        if p:
            p.delete()
            return  Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def shortest_path(self, request):
        start_id = request.query_params.get("start",None)
        end_id = request.query_params.get("end", None)
        graph = Graph("bolt://neo4j:adminpass@localhost:7687")
        path = graph.run("MATCH (b1:Person {uid: '"+start_id+"'}),(b2:Person {uid: '"+end_id+"'}), p = shortestPath((b1)-[*..15]-(b2)) RETURN p").to_ndarray()
        return Response(data={"path_length":list(path.shape)[-1]})
