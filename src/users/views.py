import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializer import ErrorResponseSerializer, UserRequestSerializer, UserResponseSerializer

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "users/index.html")


class HealthCheckView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Health Check - GET",
        description="Check if the API is running and healthy",
        responses={
            200: {
                "type": "object",
                "properties": {"status": {"type": "string"}, "message": {"type": "string"}},
            }
        },
        tags=["Health Check"],
    )
    def get(self, request: Request) -> Response:
        logger.info("Health check endpoint hit")
        return Response({"status": "healthy", "message": "API is working"})


class HelloUserView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Hello User - GET",
        description="Simple greeting endpoint",
        responses={
            200: {
                "type": "object",
                "properties": {"message": {"type": "string", "example": "Hello, World!"}},
            }
        },
        tags=["Users"],
    )
    def get(self, request: Request) -> Response:
        logger.info("Hello World endpoint hit")
        return Response({"message": "Hello, World!"})

    @extend_schema(
        summary="Hello User - POST",
        description="Create user greeting with data echo",
        request=UserRequestSerializer,
        responses={
            200: UserResponseSerializer,
            400: ErrorResponseSerializer,
        },
        examples=[
            OpenApiExample(
                "User Creation Example",
                value={"username": "Jhon Doe"},
                request_only=True,
            )
        ],
        tags=["Users"],
    )
    def post(self, request: Request) -> Response:
        logger.info("Hello User POST endpoint hit")
        if request.data.get("username") is None:
            return Response({"error": "Username is required"}, status=400)

        return Response({"data": {"username": request.data.get("username")}, "message": "success"})

    @extend_schema(
        summary="Hello User - PUT",
        description="Update user greeting completely",
        request=UserRequestSerializer,
        responses={
            200: UserResponseSerializer,
            400: ErrorResponseSerializer,
        },
        examples=[
            OpenApiExample(
                "Full Update Example",
                value={"username": "Jhon Doe"},
                request_only=True,
            )
        ],
        tags=["Users"],
    )
    def put(self, request: Request) -> Response:
        logger.info("Hello User PUT endpoint hit")
        if request.data.get("username") is None:
            return Response({"error": "Username is required"}, status=400)

        return Response({"data": {"username": request.data.get("username")}, "message": "success"})

    @extend_schema(
        summary="Hello User - PATCH",
        description="Partially update user greeting",
        request=UserRequestSerializer,
        responses={
            200: UserResponseSerializer,
            400: ErrorResponseSerializer,
        },
        examples=[
            OpenApiExample(
                "Partial Update Example",
                value={"username": "Jhon Doe"},
                request_only=True,
            )
        ],
        tags=["Users"],
    )
    def patch(self, request: Request) -> Response:
        logger.info("Hello User PATCH endpoint hit")
        if request.data.get("username") is None:
            return Response({"error": "Username is required"}, status=400)

        return Response({"data": {"username": request.data.get("username")}, "message": "success"})

    @extend_schema(
        summary="Hello User - DELETE",
        description="Delete user greeting",
        request=UserRequestSerializer,
        responses={
            200: UserResponseSerializer,
            400: ErrorResponseSerializer,
        },
        examples=[
            OpenApiExample(
                "Delete User Example",
                value={"username": "Jhon Doe"},
                request_only=True,
            )
        ],
        tags=["Users"],
    )
    def delete(self, request: Request) -> Response:
        logger.info("Hello User DELETE endpoint hit")
        if request.data.get("username") is None:
            return Response({"error": "Username is required"}, status=400)

        return Response({"data": {"username": request.data.get("username")}, "message": "success"})
