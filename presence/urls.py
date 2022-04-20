from  django.urls import path , include
from rest_framework.routers import DefaultRouter
from  .views import current_datetime, ClassesTestViewSet,UtilisateurViewSet,ClasseMatiereViewSet,ClasseViewSet,ClasseEnseignantViewSet,EtudiantViewSet,MatiereViewSet
router = DefaultRouter()
router.register(r'classestest',ClassesTestViewSet , basename='classestest')
router.register(r'utilisateurs',UtilisateurViewSet , basename='utilisateurs')
router.register(r'classes_matieres',ClasseMatiereViewSet , basename='classes_matieres')
router.register(r'classes',ClasseViewSet , basename='classes')
router.register(r'classes_enseignants',ClasseEnseignantViewSet , basename='classes_enseignants')
router.register(r'etudiants',EtudiantViewSet , basename='etudiants')
router.register(r'matieres',MatiereViewSet , basename='matieres')

urlpatterns = [
    path("api/",include(router.urls)),
    path("api/date",current_datetime),

]