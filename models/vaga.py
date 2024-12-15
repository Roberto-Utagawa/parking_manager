from models.enums import StatusVaga
from datetime import datetime

from datetime import datetime

class Vaga:
    def __init__(self, id, localizacao):
        self.ID = id
        self.localizacao = localizacao
        self.status = StatusVaga.LIVRE

    def __str__(self):
        return f"ID: {self.ID}, Localização: {self.localizacao}, Status: {self.status}"


class GerenciadorDeVagas:
    def __init__(self):
        self.vagas = []  # Lista para armazenar vagas


    # Método para criar uma nova vaga
    def criar_vaga(self, id, localizacao):
        # Verifica se a vaga com o mesmo ID já existe
        for vaga in self.vagas:
            if vaga.ID == id:
                print(f"Erro: Vaga com ID {id} já existe.")
                return
        
        nova_vaga = Vaga(id, localizacao)
        self.vagas.append(nova_vaga)
        print(f"Vaga criada com sucesso: {nova_vaga}")


    # Método para visualizar todas as vagas
    def ver_vagas(self):
        if not self.vagas:
            print("Nenhuma vaga cadastrada.")
            return
        
        print("Lista de Vagas:")
        for vaga in self.vagas:
            print(vaga)


    # Método para remover uma vaga pelo ID
    def remover_vaga(self, id):
        for vaga in self.vagas:
            if vaga.ID == id:
                self.vagas.remove(vaga)
                print(f"Vaga removida com sucesso: ID {id}")
                return
        print(f"Erro: Vaga com ID {id} não encontrada.")
    

    # Busca vaga por ID
    def buscar_vaga_por_id(self, id):
        for vaga in self.vagas:
            if vaga.ID == id:
                return vaga
        print(f"Erro: Vaga com ID {id} não encontrada.")
        return None
    
    
    # Método para alterar o status de uma vaga
    def alterar_status(self, id, novo_status: StatusVaga):
        vaga = self.buscar_vaga_por_id(id)
        if vaga:
            vaga.status = novo_status
            print(f"Status da vaga {id} alterado para {novo_status.value}.")