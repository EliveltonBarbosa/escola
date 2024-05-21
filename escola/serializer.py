from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula



class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        
        
class MatriculasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
