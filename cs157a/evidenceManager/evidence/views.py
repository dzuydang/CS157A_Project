from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Suspects
from .models import Evidence
from .models import Cases
from .models import Employees
from .models import ChainOfCustody
from .models import Addresses
from .models import Security
from .models import Documents
from .models import LegalEntities
from django.http import HttpResponse

def landingPage(request):
    return HttpResponse("Welcome to the Landing Page")

@csrf_exempt  # Disable CSRF for simplicity (use cautiously in production)
def search_suspects(request):
    print("made it here")
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query', '')

        # Extract suspectId, suspectName, and suspectAge from the query string
        suspect_id = None
        suspect_name = None
        suspect_age = None

        if "SuspectID =" in query:
            print("made it here 2")
            suspect_id = query.split("SuspectID =")[1].split("'")[1].strip()
        if "Name LIKE" in query:
            suspect_name = query.split("Name LIKE")[1].split("'")[1].strip('%').strip()
        if "Age =" in query:
            suspect_age = query.split("Age =")[1].split("'")[1].strip()

        print(f"suspect_id: {suspect_id}, suspect_name: {suspect_name}, suspect_age: {suspect_age}")

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
        query = data.get('query', '')

        # Initialize filters
        evidence_id = None
        case_id = None
        evidence_type = None

        # Extract evidenceId, caseId, and evidenceType from the query string
        if "EvidenceID =" in query:
            evidence_id = query.split("EvidenceID =")[1].split("'")[1].strip()
        if "CaseID LIKE" in query:
            case_id = query.split("CaseID LIKE")[1].split("'")[1].strip('%').strip()
        if "EvidenceType =" in query:
            evidence_type = query.split("EvidenceType =")[1].split("'")[1].strip()

        print(f"evidence_id: {evidence_id}, case_id: {case_id}, evidence_type: {evidence_type}")

        # Query the database dynamically
        evidence = Evidence.objects.all()
        if evidence_id:
            evidence = evidence.filter(evidence_id=evidence_id)
        if case_id:
            evidence = evidence.filter(case__case_number__icontains=case_id)
        if evidence_type:
            evidence = evidence.filter(evidence_type=evidence_type)

        # Serialize results into a JSON-compatible format
        results = list(evidence.values())
        return JsonResponse(results, safe=False)

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def search_cases(request):
    print("made it here 3")
    if request.method == 'POST':
        try:
            # Parse the request body
            data = json.loads(request.body)

            # Extract query filters
            query = data.get('query')
            search_case_id = None
            case_status = None

            if query:
                # Parse the query string to extract conditions
                query_lines = query.split("\n")
                for line in query_lines:
                    line = line.strip()
                    if line.startswith("AND CaseID"):
                        search_case_id = line.split("=")[1].strip().strip("'")
                    elif line.startswith("AND CaseStatus"):
                        case_status = line.split("=")[1].strip().strip("'")

            # Query the database dynamically
            cases = Cases.objects.all()
            if search_case_id:
                cases = cases.filter(case_id=search_case_id)
            if case_status:
                cases = cases.filter(case_status=case_status)

            # Serialize results into a JSON-compatible format
            results = list(cases.values())
            return JsonResponse(results, safe=False)

        except Exception as e:
            # Return a detailed error message
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def search_documents(request):
    if request.method == 'POST':
        try:
            # Parse the request body
            data = json.loads(request.body)

            # Extract query filters
            query = data.get('query')
            document_id = None
            document_type = None

            if query:
                # Parse the query string to extract conditions
                query_lines = query.split("\n")
                for line in query_lines:
                    line = line.strip()
                    if line.startswith("AND DocumentID"):
                        document_id = line.split("=")[1].strip().strip("'")
                    elif line.startswith("AND DocumentType"):
                        document_type = line.split("=")[1].strip().strip("'")

            # Query the database dynamically
            documents = Documents.objects.all()
            if document_id:
                documents = documents.filter(document_id=document_id)
            if document_type:
                documents = documents.filter(document_type=document_type)

            # Serialize results into a JSON-compatible format
            results = list(documents.values())
            return JsonResponse(results, safe=False)

        except Exception as e:
            # Return a detailed error message
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def search_legal_entities(request):
    if request.method == 'POST':
        try:
            # Parse the request body
            data = json.loads(request.body)

            # Initialize variables for filtering
            query = data.get('query')
            legal_entity_id = None
            legal_entity_type = None
            legal_entity_city = None
            legal_entity_state = None

            if query:
                # Parse the query string to extract conditions
                query_lines = query.split("\n")
                for line in query_lines:
                    line = line.strip()
                    if line.startswith("AND LegalEntityID"):
                        legal_entity_id = line.split("=")[1].strip().strip("'")
                    elif line.startswith("AND EntityType"):
                        legal_entity_type = line.split("=")[1].strip().strip("'")
                    elif line.startswith("AND City"):
                        legal_entity_city = line.split("LIKE")[1].strip().strip("'%")
                    elif line.startswith("AND State"):
                        legal_entity_state = line.split("=")[1].strip().strip("'")

            # Query the database dynamically
            entities = LegalEntities.objects.all()
            if legal_entity_id:
                entities = entities.filter(legal_entity_id=legal_entity_id)
            if legal_entity_type:
                entities = entities.filter(entity_type=legal_entity_type)
            if legal_entity_city:
                entities = entities.filter(city__icontains=legal_entity_city)
            if legal_entity_state:
                entities = entities.filter(state=legal_entity_state)

            # Serialize results into a JSON-compatible format
            results = list(entities.values())
            return JsonResponse(results, safe=False)

        except Exception as e:
            # Return a detailed error message
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)