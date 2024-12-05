from django.urls import path
from . import views

urlpatterns = [
    path('search-suspects', views.search_suspects, name='search_suspects'),
    path('search-evidence', views.search_evidence, name='search_evidence'),
    path('search-cases', views.search_cases, name='search_cases'),
    path('search-documents', views.search_documents, name='search_documents'),
    path('search-legal-entities', views.search_legal_entities, name='search_legal_entities'),
    path('', views.landingPage, name='landingpage'),  # Default landing page
]