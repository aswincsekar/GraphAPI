from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .utils import StructuredThingSerializer
from .models import Person
from rest_framework import viewsets
from rest_framework.response import Response
from py2neo import Graph
from rest_framework.decorators import action


class PersonViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Person.nodes.all()
        serializer = StructuredThingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.nodes.all()
        person = Person.nodes.get(uid=pk)
        serializer = StructuredThingSerializer(person)
        return Response(serializer.data)

    @action(detail=False)
    def shortest_path(self, request):
        start_id = request.query_params.get("start",None)
        end_id = request.query_params.get("end", None)
        graph = Graph("bolt://neo4j:adminpass@localhost:7687")
        path = graph.run("MATCH (b1:Person {uid: '"+start_id+"'}),(b2:Person {name: '"+end_id+"'}), p = shortestPath((b1)-[*..15]-(b2)) RETURN p").to_ndarray()
        return Response(data={"path_length":list(path.shape)[-1]})
