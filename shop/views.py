from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic, View
from rest_framework.views import APIView, Response
from django.db.models import Q
from functools import reduce
from .models import Item
from .serializers import listSerializer, itemSerializer
import json

class ItemList(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        serializer = listSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = itemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response({"Status": "Added"})





class detailedItem(APIView):
    def get(self, request, item_id, *args, **kwargs):
        items = Item.objects.filter(pk=item_id)
        serializer = listSerializer(items, many=True)
        return Response(serializer.data)

    def delete(self, request, item_id, *args, **kwargs):
        item = Item.objects.filter(pk=item_id)
        item.delete()
        return Response({"Status":"Deleted"})

    def patch(self, request, item_id):
            try:
                obj = Item.objects.get(pk=item_id)
            except Item.DoesNotExist:
                return Response({'error': 'Object does not exist'}, status=404)

            serializer = itemSerializer(obj, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)

            return Response(serializer.errors, status=400)


class FilteredItemList(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, search_query, *args, **kwargs):
        query_parts = search_query.split()
        items = Item.objects.filter(reduce(lambda q, value: q | Q(name__icontains=value) | Q(brandName__icontains=value), query_parts, Q()))
        serializer = listSerializer(items, many=True)
        return Response(serializer.data)




