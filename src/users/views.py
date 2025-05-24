import logging
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "users/index.html")


class HealthCheckView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        logger.info("Health check endpoint hit")
        return Response({"status": "healthy", "message": "API is working"})
