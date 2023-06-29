from django.urls import path

from transactions.views import (
    TransactionViewSet,
    ReportView,
)

app_name = "transactions"
urlpatterns = [
    path("report/v0/", ReportView.as_view(), name="report-v0"),
    path("v0/", TransactionViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "<trx_id>/v0/",
        TransactionViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]
