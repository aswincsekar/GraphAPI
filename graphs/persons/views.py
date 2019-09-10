# path = graph.run(
#     "MATCH (b1:Person {name: 'Jim'}),(b2:Person {name: 'superman'}), p = shortestPath((b1)-[*..15]-(b2)) RETURN p").to_ndarray()

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .utils import StructuredThingSerializer
from .models import Person
from rest_framework import viewsets
from rest_framework.response import Response


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