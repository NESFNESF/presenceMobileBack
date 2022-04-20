from  rest_framework import serializers
from .models import ClassesTest , Utilisateur , Classe, Etudiant , Matiere , ClasseMatiere , ClasseEnseignant

class ClassesTestSerialize(serializers.ModelSerializer):
    class Meta:
        model = ClassesTest
        fields = '__all__'


class UtilisateurSerialize(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class ClasseSerialize(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'

class EtudiantSerialize(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'

class ClasseMatiereSerialize(serializers.ModelSerializer):
    class Meta:
        model = ClasseMatiere
        fields = '__all__'

class MatiereSerialize(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = '__all__'

class ClasseEnseignantSerialize(serializers.ModelSerializer):
    class Meta:
        model = ClasseEnseignant
        fields = '__all__'
