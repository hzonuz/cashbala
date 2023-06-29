from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer, ReportSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    with transaction.atomic():
        def create(self, request, *args, **kwargs):
            request.data["user"] = request.user.id
            return super().create(request, *args, **kwargs)

        def update(self, request, *args, **kwargs):
            request.data["user"] = request.user.id
            return super().update(request, partial=True, *args, **kwargs)

        def get_queryset(self):
            return Transaction.objects.filter(user=self.request.user)

        def get_object(self):
            return Transaction.objects.get(
                id=self.kwargs["trx_id"], user=self.request.user
            )


class ReportView(APIView):
    def get(self, request, *args, **kwargs):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        serializer = ReportSerializer(
            data={"start_date": start_date, "end_date": end_date},
            context={"user": request.user},
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )