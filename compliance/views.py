from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .serializers import CNICSerializer, NTNSerializer, TaxBracketSerializer, ZakatSerializer
from .utils import calculate_tax, calculate_zakat

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
            tax_info = calculate_tax(income)
            return Response({
                "annual_salary": income,
                "tax_slab": tax_info["tax_slab"],
                "tax_rate": tax_info["tax_rate"],
                "tax_owed": tax_info["tax_owed"]
            }, status=200)
        else:
            return Response({"valid": False, "errors": serializer.errors}, status=400)


class ZakatView(ListCreateAPIView):
    serializer_class = ZakatSerializer
    get_queryset = lambda self: None

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            asset_value = serializer.validated_data['asset_value']
            zakat_info = calculate_zakat(asset_value)
            return Response({
                "asset_value": asset_value,
                "nisab_threshold": zakat_info["nisab_threshold"],
                "meets_nisab": zakat_info["meets_nisab"],
                "zakat_due": zakat_info["zakat_due"]
            }, status=200)
        else:
            return Response({"valid": False, "errors": serializer.errors}, status=400)