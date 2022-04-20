from django.shortcuts import render
from  .serialize import ClassesTestSerialize ,UtilisateurSerialize,ClasseSerialize,EtudiantSerialize,ClasseMatiereSerialize,MatiereSerialize,ClasseEnseignantSerialize
from  .models import ClassesTest,Utilisateur,Classe,ClasseMatiere,ClasseEnseignant,Etudiant,Matiere
from  rest_framework import viewsets
from django.http import HttpResponse
import datetime
# Create your views here.

class ClassesTestViewSet(viewsets.ModelViewSet):
    serializer_class = ClassesTestSerialize
    queryset = ClassesTest.objects.all()

class UtilisateurViewSet(viewsets.ModelViewSet):
    serializer_class = UtilisateurSerialize
    queryset = Utilisateur.objects.all()

class ClasseViewSet(viewsets.ModelViewSet):
    serializer_class = ClasseSerialize
    queryset = Classe.objects.all()

class EtudiantViewSet(viewsets.ModelViewSet):
    serializer_class = EtudiantSerialize
    queryset = Etudiant.objects.all()

class MatiereViewSet(viewsets.ModelViewSet):
    serializer_class = MatiereSerialize
    queryset = Matiere.objects.all()

class ClasseMatiereViewSet(viewsets.ModelViewSet):
    serializer_class = ClasseMatiereSerialize
    queryset = ClasseMatiere.objects.all()

class ClasseEnseignantViewSet(viewsets.ModelViewSet):
    serializer_class = ClasseEnseignantSerialize
    queryset = ClasseEnseignant.objects.all()

def current_datetime(request):

    now = datetime.datetime.now()
    html = ClassesTest.objects.all().values_list()
    return HttpResponse(html)

