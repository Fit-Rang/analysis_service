from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.utils import generate_short_id
from . import models
from .serializers import ProfileSerializer

@api_view(['GET'])
def get_all_profiles(request):
    user_id = generate_short_id(request.headers.get("X-User"))
    if not user_id:
        return Response({"msg": "Missing user ID"}, status=status.HTTP_400_BAD_REQUEST)

    profiles = models.get_profiles(user_id)

    if not profiles.exists():
        return Response({"msg": "No Profiles Shared"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProfileSerializer(instance=profiles, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

