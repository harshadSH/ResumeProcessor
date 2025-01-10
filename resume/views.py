from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CandidateSerializer
from .utils import parse_resume
from .models import Candidate
from django.shortcuts import render
from django.http import JsonResponse
import tempfile

def save_temp_file(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=file.name.split('.')[-1]) as temp_file:
        for chunk in file.chunks():
            temp_file.write(chunk)
        return temp_file.name

class ResumeExtractionView(APIView):
    def get(self, request):
        # Retrieve all candidates from the database
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Get the resume file from the request
        resume_file = request.FILES.get('resume')
        if not resume_file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Extract content based on file type
            if resume_file.name.endswith('.pdf') or resume_file.name.endswith(('.doc', '.docx')):
                temp_path = save_temp_file(resume_file)
                data = parse_resume(temp_path)
            else:
                return JsonResponse({"error": "Unsupported file type!"}, status=400)

            # Create a Candidate object and save it to the database
            candidate = Candidate.objects.create(
                first_name=data.get('first_name', ''),
                email=data.get('email', ''),
                mobile_number=data.get('mobile_number', '')
            )

            # Serialize the Candidate data for the response
            serializer = CandidateSerializer(candidate)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

def upload_resume(request):
    if request.method == "POST":
        resume_file = request.FILES.get('resume')
        if not resume_file:
            return JsonResponse({"error": "No file uploaded!"}, status=400)

        try:

            temp_path = save_temp_file(resume_file)
            data = parse_resume(temp_path)


            Candidate.objects.create(
                first_name=data.get('first_name', ''),
                email=data.get('email', ''),
                mobile_number=data.get('mobile_number', '')
            )
            return JsonResponse({"message": "Resume processed successfully!"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, 'upload_resume.html')
