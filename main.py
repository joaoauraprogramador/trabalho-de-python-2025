import os
import json
from storage import salvar_dados, carregar_dados
from ui import selecionar_1, selecionar_2, selecionar_3
from services import cadastrar, listar, buscar, atualizar, remover
from reports import menu_relatorios 

USUARIOS_ARQUIVO = "data/usuarios.json"
PROJETOS_ARQUIVO = "data/projetos.json"
TAREFAS_ARQUIVO ="data/tarefas.json"

if not os.path.exists('data'):
    os.makedirs('data')

usuarios = carregar_dados(USUARIOS_ARQUIVO)
projetos = carregar_dados(PROJETOS_ARQUIVO)
tarefas = carregar_dados(TAREFAS_ARQUIVO)

print("\n--- Sistema de Gerenciamento de Projetos ---")

while True:
    x = selecionar_1()
    
    if x == 1:
        y = selecionar_2()
        
        if y == 1:
            usuario = cadastrar(1, usuarios, projetos, tarefas)
            if usuario:
                usuarios.append(usuario)
                salvar_dados(USUARIOS_ARQUIVO, usuarios)
                print("\nUsuário cadastrado!")
        
        elif y == 2:
            listar(1, usuarios, projetos, tarefas)
            
        elif y == 3:
            buscar(1, usuarios, projetos, tarefas)
            
        elif y == 4:
            if atualizar(1, usuarios, projetos, tarefas):
                salvar_dados(USUARIOS_ARQUIVO, usuarios)
                
        elif y == 5:
            if remover(1, usuarios, projetos, tarefas):
                salvar_dados(USUARIOS_ARQUIVO, usuarios)

    elif x == 2:
        y = selecionar_2()
        
        if y == 1:
            projeto = cadastrar(2, usuarios, projetos, tarefas)
            if projeto:
                projetos.append(projeto)
                salvar_dados(PROJETOS_ARQUIVO, projetos)
                print("\nProjeto cadastrado!")
        
        elif y == 2:
            listar(2, usuarios, projetos, tarefas)
            
        elif y == 3:
            buscar(2, usuarios, projetos, tarefas)
            
        elif y == 4:
            if atualizar(2, usuarios, projetos, tarefas):
                salvar_dados(PROJETOS_ARQUIVO, projetos)
                
        elif y == 5:
            if remover(2, usuarios, projetos, tarefas):
                salvar_dados(PROJETOS_ARQUIVO, projetos)
                
    elif x == 3:
        y = selecionar_3()
        
        if y == 1:
            tarefa = cadastrar(3, usuarios, projetos, tarefas)
            if tarefa:
                tarefas.append(tarefa)
                salvar_dados(TAREFAS_ARQUIVO, tarefas)
                print("\nTarefa cadastrada!")
                
        elif y == 2:
            listar(3, usuarios, projetos, tarefas)
            
        elif y == 3:
            if atualizar(3, usuarios, projetos, tarefas):
                salvar_dados(TAREFAS_ARQUIVO, tarefas)
                
        elif y == 4:
            if remover(3, usuarios, projetos, tarefas):
                salvar_dados(TAREFAS_ARQUIVO, tarefas)
                
    elif x == 4:
        menu_relatorios(tarefas, projetos, usuarios)
        
    elif x == 5:
        print("\nSistema encerrado. Dados salvos.")
        break