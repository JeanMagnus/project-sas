from django.shortcuts import get_object_or_404, render
from .models import Aluno
from .models import Sala
from .models import Professor
from .models import Solicitacao
from django.http import Http404, HttpResponseRedirect

def home(request):
    return render(request, 'alunos/home.html')
    

def cadastroalunos(request):
    return render(request, 'alunos/cadastraraluno.html')

def cadastrosalas(request):
    return render(request, 'salas/cadastrarsala.html')

def cadastroprofessores(request):
    return render(request, 'professores/cadastrarprofessor.html')

def cadastrosolicitacoes(request, sala_id):
    context = {'sala_id': sala_id}
    return render(request, 'solicitacoes/cadastrarsolicitacao.html', context=context)

def alunos(request):
    # salvar dados da tela para o banco de dados
    novo_aluno = Aluno()
    novo_aluno.nome = request.POST.get('nome')
    novo_aluno.email = request.POST.get('email')
    novo_aluno.matricula = request.POST.get('matricula')
    novo_aluno.senha = request.POST.get('senha')
    novo_aluno.save()
    
    #Exibir todos os alunos já cadastrados em uma nova página
    
    alunos = {
        'alunos': Aluno.objects.all()
    }
    
    #retornar os dados para a página de listagem de alunos
    return render(request, 'alunos/listaralunos.html', alunos)

def salas(request):
    nova_sala = Sala()
    nova_sala.setor = request.POST.get('setor')
    nova_sala.numeracao = request.POST.get('numeracao')
    nova_sala.status = request.POST.get('status')
    nova_sala.horario_disp = request.POST.get('horario_disp')
    nova_sala.save()
    
    salas = {
        'salas': Sala.objects.all()
    }
    
    return render(request, 'salas/listarsalas.html', salas)

#Listagem sala para alunos
def listarsalas(request):
    salas = {
        'salas': Sala.objects.all()
    }
    return render(request, 'salas/listarsalas.html', salas)


def professores(request):
    novo_prof = Professor()
    novo_prof.nome = request.POST.get('nome')
    novo_prof.email = request.POST.get('email')
    novo_prof.save()
    
    professores = {
        'professores': Professor.objects.all()
    }
    return render(request, 'professores/listarprofessores.html', professores)

def solicitacoes(request):
    if request.method == 'POST':
        sala_id = request.POST.get("sala_id")
        print("Valor de sala_id recebido:", sala_id)  # Adicione este print para verificar o valor
        horario = request.POST.get("horario")
        descricao = request.POST.get("descricao")
        situacao = "Em análise"

        # Verificar se o sala_id é um número válido
        if not sala_id.isdigit():
            # Se não for um número válido, faça algo (redirecione, retorne uma mensagem de erro, etc.)
            # Por exemplo, redirecione para uma página de erro ou retorne um HttpResponse com uma mensagem
            raise Http404("ID de Sala inválido")

        # Tente obter a sala com o ID fornecido
        try:
            sala = Sala.objects.get(pk=sala_id)
        except Sala.DoesNotExist:
            # Se a sala não existir, faça algo (redirecione, retorne uma mensagem de erro, etc.)
            # Por exemplo, redirecione para uma página de erro ou retorne um HttpResponse com uma mensagem
            raise Http404("Sala não encontrada")

        # Se a sala existir e o ID for um número válido, crie a nova solicitação
        nova_solic = Solicitacao(horario=horario, descricao=descricao, sala=sala, situacao=situacao)
        nova_solic.save()
    
    solicitacoes = {
        'solicitacoes': Solicitacao.objects.all()
    }
    return render(request, 'solicitacoes/listarsolicitacoes.html', solicitacoes)


def alterarsituacao(request, solicitacao_id, nova_situacao):
    solicitacao = get_object_or_404(Solicitacao, pk=solicitacao_id)

    # Verificar a nova situação e atualizar
    if nova_situacao == 'deferido':
        solicitacao.situacao = 'Deferido'
    elif nova_situacao == 'indeferido':
        solicitacao.situacao = 'Indeferido'

    solicitacao.save()
    return HttpResponseRedirect('/listarsolicitacoes/')  # Redirecionar de volta para a página de listagem
    
   