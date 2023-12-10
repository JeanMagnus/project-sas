from django.urls import path
from app_projetosas import views

urlpatterns = [
    #pag inicial
    path('',views.home, name="home"),
    #pag de cadastro de alunos
    path('cadastroalunos/', views.cadastroalunos,name='cadastraraluno'),
    path('alunos/', views.alunos, name='listaralunos'),
    path('cadastrosalas/', views.cadastrosalas, name='cadastrarsala'),
    path('salas/', views.salas, name='listarsalas'),
    path('listarsalas/', views.listarsalas, name='listarsalas1'),
    path('cadastroprofessores/', views.cadastroprofessores, name='cadastrarprofessor'),
    path('professores/', views.professores, name='listarprofessores'),
    path('cadastrosolicitacoes/<int:sala_id>/', views.cadastrosolicitacoes, name="cadastrarsolicitacao"),
    path('listarsolicitacoes/', views.solicitacoes, name="listarsolicitacoes"),
    path('alterarsituacao/<int:solicitacao_id>/<str:nova_situacao>/',views.alterarsituacao, name='alterarsituacao')
]
