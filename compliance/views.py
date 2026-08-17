from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .serializers import CNICSerializer, NTNSerializer, TaxBracketSerializer

# Create your views here.


class CNICView(ListCreateAPIView):
    serializer_class = CNICSerializer
    get_queryset = lambda self: None  # No queryset needed for this view

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response({"valid": True, "cnic": serializer.validated_data['cnic'], "province": serializer.validated_data['province']}, status=200)
        else:
            return Response({"valid": False, "errors": serializer.errors}, status=400)


class NTNView(ListCreateAPIView):
    serializer_class = NTNSerializer
    get_queryset = lambda self: None  # No queryset needed for this view

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response({"valid": True, "ntn": serializer.validated_data['ntn'], "type": serializer.validated_data['choices']}, status=200)
        else:
            return Response({"valid": False, "errors": serializer.errors}, status=400)


class TaxBracketView(ListCreateAPIView):
    serializer_class = TaxBracketSerializer
    get_queryset = lambda self:None

    def post(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            income = serializer.validated_data['annual_salary']
            # tax_bracket = serializer.calculate_tax_bracket(income)
            return Response({"annual_salary": income, "tax_slab": "", "tax_rate": "", "tax_owed": ""}, status=200)
        else:
            return Response({"valid": False, "errors": serializer.errors}, status=400)