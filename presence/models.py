from django.db import models

class ClassesTest(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)


class Utilisateur(models.Model):
    matricule = models.CharField(max_length=20)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    type_user = models.IntegerField()

class Classe(models.Model):
    nom = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

class Etudiant(models.Model):
    user_id = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    classe_id = models.ForeignKey(Classe, on_delete=models.CASCADE)

class Matiere(models.Model):
    classe_id = models.ForeignKey(Classe, on_delete=models.CASCADE)
    inttule = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

class ClasseEnseignant(models.Model):
    user_id = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    classe_id = models.ForeignKey(Classe, on_delete=models.CASCADE)

class ClasseMatiere(models.Model):
    classe_id = models.ForeignKey(Classe, on_delete=models.CASCADE)
    matiere_id = models.ForeignKey(Matiere, on_delete=models.CASCADE)



