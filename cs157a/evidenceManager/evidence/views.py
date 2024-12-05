from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Suspects
from .models import Evidence
from django.http import HttpResponse

def landingPage(request):
    return HttpResponse("Welcome to the Landing Page")

@csrf_exempt  # Disable CSRF for simplicity (use cautiously in production)
def search_suspects(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        suspect_id = data.get('suspectId')
        suspect_name = data.get('suspectName')
        suspect_age = data.get('suspectAge')

        # Query the database dynamically
        suspects = Suspects.objects.all()
        if suspect_id:
            suspects = suspects.filter(suspect_id=suspect_id)
        if suspect_name:
            suspects = suspects.filter(name__icontains=suspect_name)
        if suspect_age:
            suspects = suspects.filter(age=suspect_age)

        # Serialize results into a JSON-compatible format
        results = list(suspects.values())
        return JsonResponse(results, safe=False)

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def search_evidence(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        evidence_id = data.get('evidenceId')
        case_id = data.get('caseId')
        evidence_type = data.get('evidenceType')

        evidence = Evidence.objects.all()
        if evidence_id:
            evidence = evidence.filter(evidence_id=evidence_id)
        if case_id:
            evidence = evidence.filter(case_id=case_id)
        if evidence_type:
            evidence = evidence.filter(evidence_type=evidence_type)

        results = list(evidence.values())
        return JsonResponse(results, safe=False)

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def search_cases(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        case_id = data.get('searchCaseId')
        case_status = data.get('caseStatus')

        cases = Cases.objects.all()
        if case_id:
            cases = cases.filter(case_id=case_id)
        if case_status:
            cases = cases.filter(case_status=case_status)

        results = list(cases.values())
        return JsonResponse(results, safe=False)

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def search_documents(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        document_id = data.get('documentId')
        document_type = data.get('documentType')

        documents = Documents.objects.all()
        if document_id:
            documents = documents.filter(document_id=document_id)
        if document_type:
            documents = documents.filter(document_type=document_type)

        results = list(documents.values())
        return JsonResponse(results, safe=False)

    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def search_legal_entities(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        legal_entity_id = data.get('legalEntityId')
        legal_entity_type = data.get('legalEntityType')
        legal_entity_city = data.get('legalEntityCity')
        legal_entity_state = data.get('legalEntityState')

        entities = LegalEntities.objects.all()
        if legal_entity_id:
            entities = entities.filter(legal_entity_id=legal_entity_id)
        if legal_entity_type:
            entities = entities.filter(entity_type=legal_entity_type)
        if legal_entity_city:
            entities = entities.filter(city__icontains=legal_entity_city)
        if legal_entity_state:
            entities = entities.filter(state=legal_entity_state)

        results = list(entities.values())
        return JsonResponse(results, safe=False)

    return JsonResponse({"error": "Invalid request method"}, status=400)
