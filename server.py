import Pyro4
import sys
sys.path.append("Codigo_Aux/")
##from funcoes_aux import *
import funcoes_aux
import classe_cliente
import threading

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class servidor():        
    def __init__(self):
        self.lista_players=[]
        self.jogador_atual=funcoes_aux.escolha_aleatoria_jogador()
        self.ganhador="NENHUM"
        self.escolheu_verde=False
        self.escolheu_vermelho=False
        self.jogar_denovo=False

    def get_escolheu_verde(self):
        return self.escolheu_verde
    def get_jogador_atual(self):
        return self.jogador_atual
    def get_lista_players(self):
        return self.lista_players
    def get_escolheu_vermelho(self):
        return self.escolheu_vermelho
    def get_jogar_denovo(self):
        return self.jogar_denovo
    def set_jogar_denovo(self,condicao):
        self.jogar_denovo=condicao
    def set_escolheu_verde(self,condicao):
        self.escolheu_verde=condicao
    def set_escolheu_vermelho(self,condicao):
        self.escolheu_vermelho=condicao

    def set_ganhador(self,ganhador):
        self.ganhador=ganhador
    def get_ganhador(self):
        return self.ganhador
    
    def add_player(self,cliente):
##        print(cliente)
##        cliente=return_obj_name_server(uri)
        self.lista_players.append(cliente)
##        print("Cor: "+cliente.get_minhas_pecas())
        if(cliente.get_minhas_pecas()=="RED"):
            self.escolheu_vermelho=True
        elif(cliente.get_minhas_pecas()=="GREEN"):
            self.escolheu_verde=True
        if len(self.lista_players)==2:
            self.print_to_all()
        print(self.lista_players)
    def del_player(self,nome):
        ns=Pyro4.locateNS()
        for element in self.lista_players:
            if element.get_my_username()==nome:
                if(element.get_minhas_pecas()=="RED"):
                    print("passou no RED")
                    self.escolheu_vermelho=False
                    ns.remove("Cliente_"+element.get_my_username())
                    self.lista_players.remove(element)
                elif(element.get_minhas_pecas()=="GREEN"):
                    print("passou no GREEN")
                    self.escolheu_verde=False
                    ns.remove("Cliente_"+element.get_my_username())
                    self.lista_players.remove(element)
        self.chat=[]
        self.ganhador="NENHUM"
                
        print(self.lista_players)
    def pode_add_player(self):
        if (len(self.lista_players)<2):
            return True
        else:
            return False
        
    def troca_jogador(self):
        if(self.jogador_atual=="RED"):
            self.jogador_atual= "GREEN"
        elif(self.jogador_atual=="GREEN"):
            self.jogador_atual= "RED"
##        for player in self.lista_players:
##            player.Att_tabuleiro()
            
    def reset_game(self):
        self.jogador_atual=funcoes_aux.escolha_aleatoria_jogador()
        self.ganhador="NENHUM"
##        self.escolheu_verde=False
##        self.escolheu_vermelho=False
        self.jogar_denovo=False
    def adversario_add_mensagem_Chat(self,quem_mandou,mensagem):
        for player in self.lista_players:
            if player.get_my_username()!=quem_mandou:
                print("Passou por aqui")
                player.add_mensagem_Chat(mensagem)
##                player.att_chat(screen)
    def print_to_all(self):
        for player in self.lista_players:
            player.print()
    def adversario_att_tabuleiro(self,quem_mandou):
        for player in self.lista_players:
            if player.get_my_username()!=quem_mandou:
##                print("Passou por aqui")
                player.Att_tabuleiro()
    def adversario_troca_cor(self,peca_destino,peca_atual,quem_mandou):
        for player in self.lista_players:
            if player.get_my_username()!=quem_mandou:
##                print("Passou por aqui")
                player.troca_cor(peca_destino,peca_atual)
    def adversario_reset_tabuleiro(self,quem_mandou):
        for player in self.lista_players:
            if player.get_my_username()!=quem_mandou:
##                print("Passou por aqui")
                player.reset_tabuleiro()
        
def register_name_server_object():
    daemon = Pyro4.Daemon()
    uri=daemon.register(classe_cliente.cliente)
    ns=Pyro4.locateNS()
    ns.register("clientes",uri)
    print('Before Request Loop')
    threading.Thread(target=daemon.requestLoop).start()
    print('After Pyro4 Daemon')

##    print(uri)
def return_obj_name_server(uri):
    return Pyro4.Proxy(uri)
def main():
    daemon = Pyro4.Daemon()
    uri=daemon.register(servidor)
    ns=Pyro4.locateNS()
    ns.register("servidor",uri)
##    register_name_server_object()
    print(uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
