from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user import models, serializers
from .utils import query
from .serializers import VerdictResponseSerializer
from user.utils import generate_short_id
import json
import re

def clean_ai_json(raw_response: str) -> dict:
    match = re.search(r"```json\s*(\{.*?\})\s*```", raw_response, re.DOTALL)
    json_string = match.group(1) if match else raw_response

    return json.loads(json_string)

@api_view(['POST', 'OPTIONS'])
def get_verdict(request):
    if request.method == 'OPTIONS':
        return Response(status=200)

    user_id = generate_short_id(request.headers.get("X-User"))
    product = request.data.get("product")
    owner = request.data.get("profile")

    if not user_id or not product:
        return Response(
            {"error": "Missing required fields: X-User header or product"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        if owner:
            dossier = (
                models.Dossier.objects
                .filter(owner_id=owner["id"], dossieraccess__profile_id=user_id)
                .select_related('owner')
                .first()
            )
            user_name = owner.get("full_name")
        else:
            dossier = (
                models.Dossier.objects
                .filter(owner_id=user_id)
                .select_related('owner')
                .first()
            )
            user_name = None

        if not dossier:
            return Response(
                {"error": "Dossier not found or access denied"},
                status=status.HTTP_404_NOT_FOUND
            )

        dossier_serialized = serializers.DossierSerializer(dossier).data
        verdict_raw = query(user=user_name, product=product, dossier=dossier_serialized)

        try:
            verdict = clean_ai_json(verdict_raw)
        except json.JSONDecodeError:
            return Response(
                {"error":"AI returned invalid JSON format"},
                status=500
            )

        verdict_serializer = VerdictResponseSerializer(data=verdict)
        verdict_serializer.is_valid(raise_exception=True)

        return Response(verdict_serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

