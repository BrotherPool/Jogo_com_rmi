import pygame
import sys
import Pyro4
sys.path.append("Codigo_Aux/")
import funcoes_aux
import threading

server=None

def look_for_server():
    ns=Pyro4.locateNS()
    uri=ns.lookup('servidor')
    server=Pyro4.Proxy(uri)
    return server

Circ_Verde = pygame.image.load("Sprites/Elipse_1.png")
Circ_Verme = pygame.image.load("Sprites/Elipse_2.png")
Circ_Azul = pygame.image.load("Sprites/Elipse_3.png")
Circ_Verde = pygame.transform.scale(Circ_Verde, (24,24))
Circ_Verme = pygame.transform.scale(Circ_Verme, (24,24))
Circ_Azul = pygame.transform.scale(Circ_Azul, (24,24))


cinza=128,128,128,255
verde=0,200,0,255
vermelho=200,0,0,255
vermelho_forte=255,0,0,255
azul=0,0,200,255
azul_forte=0,0,255,255
branco=255,255,255,255



Cor_Circ_Verde=(26, 162, 26, 255)
Cor_Circ_Verme=(195, 26, 26, 255)
Cor_Circ_Azul=(65, 122, 162, 255)
fundo = pygame.image.load("Sprites/tabuleiro.png")
fundo = pygame.transform.scale(fundo, (480,480))
(Tam_X_Elipse,Tam_Y_Elipse)=Circ_Verde.get_rect().size

cliente=None

##    daemon.requestLoop()
@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class cliente():
    def __init__(self):
##        self.tabuleiro=[[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
##               [-1, -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1, -1, -1, -1],
##               [-1, -1, -1, -1, -1, -1,  2,  2, -1, -1, -1, -1, -1, -1, -1],
##               [-1, -1, -1, -1, -1, -1,  2,  2,  2, -1, -1, -1, -1, -1, -1],
##               [-1, -1, -1, -1, -1,  0,  2,  2,  2, -1, -1, -1, -1, -1, -1],
##               [-1,  0,  0,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0, -1],
##               [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##               [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##               [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##               [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##               [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##               [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##               [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##               [-1,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0, -1],
##               [-1, -1, -1, -1, -1,  1,  1,  1,  0, -1, -1, -1, -1, -1, -1],
##               [-1, -1, -1, -1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
##               [-1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
##               [-1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1],
##               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

        self.tabuleiro=[[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
                   [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
                   [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
                   [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
                   [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
                   [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
                   [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
                   [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
                   [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
                   [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
                   [-1, -1, -1, -1, -1,  2,  2,  2,  2, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1,  2,  2,  2, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1,  2,  2, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

        self.tabuleiro_orig=[[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
                   [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
                   [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
                   [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
                   [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
                   [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
                   [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
                   [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
                   [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
                   [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
                   [-1, -1, -1, -1, -1,  2,  2,  2,  2, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1,  2,  2,  2, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1,  2,  2, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

        self.chat=[]
        self.minhas_pecas = ""
        self.my_username=""
        
    def get_tabuleiro(self):
        return self.tabuleiro
    def reset_chat(self):
        self.chat=[]
    def print(self):
        print("teste")
    def get_chat(self):
        return self.chat
    def get_minhas_pecas(self):
        return self.minhas_pecas
    def set_minhas_pecas(self,cor):
        self.minhas_pecas=cor
    def set_my_username(self,username):
        self.my_username=username
    def get_my_username(self):
        return self.my_username
    
    def reset_tabuleiro(self):
        self.tabuleiro=funcoes_aux.zera_matriz(self.tabuleiro,self.tabuleiro_orig)

    def elimina_o_azul_do_tabuleiro(self):
        self.tabuleiro=funcoes_aux.elimina_o_3_da_matriz(self.tabuleiro)
    
    def troca_cor(self,peca_destino,peca_anterior):
        self.tabuleiro=funcoes_aux.troca_cor(self.tabuleiro,peca_destino,peca_anterior)
        
    def add_mensagem_Chat(self,mensagem):
        self.chat=funcoes_aux.add_Lista_Chat(self.chat,mensagem)
        print("Adicionou mensagem no chat")
        
    def verifica_quem_ganhou(self):
        self.ganhador=funcoes_aux.ganhou(self.tabuleiro)
        return self.ganhador
    
    def return_as_coordenadas_correspondente_tabela(self,x,y):
        return funcoes_aux.return_x_e_y_correspondete_tabela(x,y)

    def return_a_linha_coluna_da_tabela_correspondente_coordenada(self,x,y):
        return funcoes_aux.get_index_tabela(x,y)

    def coloca_azul_onde_player_pode_andar(self,x,y):
        self.tabuleiro = funcoes_aux.pode_andar(self.tabuleiro,x,y)

    def verifica_se_player_ainda_pode_andar(self,peca_destino,peca_pulada):
        return funcoes_aux.ainda_pode_andar(self.tabuleiro,peca_destino,peca_pulada)
    def Att_tabuleiro(self):
        Att_Tabuleiro()

def Att_Tabuleiro():
    global jogador_atual
    screen=pygame.display.get_surface()
    cinza=128,128,128,255
    screen.fill(cinza)
    screen.blit(fundo,(0,0))
    jogador_vermelho = pygame.image.load("Sprites/icon_jogador_vermelho.png")
    jogador_verde = pygame.image.load("Sprites/icon_jogador_verde.png")
    resize_x_red=108
    resize_x_green=104
    resize_y=100
    minha_cor=cliente.get_minhas_pecas()
    tabuleiro=cliente.get_tabuleiro()
    my_name=cliente.get_my_username()
##        tabuleiro_att=meu_objeto_cliente.get_tabuleiro()
    jogador_atual=server.get_jogador_atual()
    jogador_vermelho = pygame.transform.scale(jogador_vermelho, (resize_x_red, resize_y))
    jogador_verde = pygame.transform.scale(jogador_verde, (resize_x_green, resize_y))
    tam_matriz = (len(tabuleiro), len(tabuleiro[0]))
    
    pygame.draw.rect(screen,vermelho,(((250)-170),470,150,50))
    message_display(((250)-95),(495),"Desistir",20,(255,255,255,255))
    pygame.draw.rect(screen,azul,(((250)+20),470,150,50))
    message_display(((250)+95),(495),"Passar a vez",20,(255,255,255,255))
    
    font = pygame.font.SysFont('arial',20)
    
    if(minha_cor=="GREEN"):
        screen.blit(jogador_verde,(0,570-(resize_y/2)))
        txt = font.render(my_name, True, (0,255,0,255))
        screen.blit(txt, (110, 560))
    elif(minha_cor=="RED"):
        screen.blit(jogador_vermelho,(0,570-(resize_y/2)))
        txt = font.render(my_name, True, (255,0,0,255))
        screen.blit(txt, (110, 560))
    
    
    if(jogador_atual==minha_cor):
        if(minha_cor=="GREEN"):
            txt = font.render("Sua vez", True, (0,255,0,255))
            screen.blit(txt, (0, 0))
        elif(minha_cor=="RED"):
            txt = font.render("Sua vez", True, (255,0,0,255))
            screen.blit(txt, (0, 0))
        
    elif(jogador_atual!=minha_cor):
        if(minha_cor=="GREEN"):
            txt = font.render("Vez do adversário", True, (255,0,0,255))
            screen.blit(txt, (0, 0))
        elif(minha_cor=="RED"):
            txt = font.render("Vez do adversário", True, (0,255,0,255))
            screen.blit(txt, (0, 0))
        
    i=0
    j=0
    for i in range(0,tam_matriz[0]):
        for j in range(0,tam_matriz[1]):
            if(tabuleiro[i][j]==1):
                screen.blit(Circ_Verde,(cliente.return_as_coordenadas_correspondente_tabela(j,i)))
            elif(tabuleiro[i][j]==2):
                screen.blit(Circ_Verme,(cliente.return_as_coordenadas_correspondente_tabela(j,i)))
            elif(tabuleiro[i][j]==3 and cliente.get_minhas_pecas()==jogador_atual):
                screen.blit(Circ_Azul,(cliente.return_as_coordenadas_correspondente_tabela(j,i)))
    pygame.display.update(pygame.Rect(0, 0, 500, 630))    

def criacao_tela_de_vitoria(screen,ganhador):
    mario_feliz = pygame.image.load("Sprites/mario.png")
    luigi_feliz = pygame.image.load("Sprites/luigi.png")
    mario_triste = pygame.image.load("Sprites/mario_triste.png")
    luigi_triste = pygame.image.load("Sprites/luigi_triste.png")
    mario_feliz = pygame.transform.scale(mario_feliz, (229,400))
    luigi_feliz = pygame.transform.scale(luigi_feliz, (287, 400))
    mario_triste = pygame.transform.scale(mario_triste, (343, 400))
    luigi_triste = pygame.transform.scale(luigi_triste, (235, 400))
    screen.fill(cinza)
    largura, altura = screen.get_size()
    minha_cor=cliente.get_minhas_pecas()
    if(ganhador=="GREEN" and minha_cor=="GREEN"):
        texto="Você ganhou"
        screen.blit(luigi_feliz,(largura/2-luigi_feliz.get_width()/2,0))
    elif(ganhador=="RED" and minha_cor=="RED"):
        texto="Você ganhou"
        screen.blit(mario_feliz,(largura/2-mario_feliz.get_width()/2,0))
    elif(ganhador=="GREEN" and minha_cor=="RED"):
        texto="Você perdeu"
        screen.blit(mario_triste,(largura/2-mario_triste.get_width()/2,0))
    elif(ganhador=="RED" and minha_cor=="GREEN"):
        texto="Você perdeu"
        screen.blit(luigi_triste,(largura/2-luigi_triste.get_width()/2,0))
    
    message_display(largura/2,450,texto,35,(0,0,0,255))
    pygame.draw.rect(screen,azul,(largura/2-75,500,150,50))
    message_display((largura/2),(525),"Jogar denovo",20,(255,255,255,255))
    
    pygame.display.update()

def tela_de_vitoria(ganhador):
    sair=False
    largura=600;
    travado=False
    altura=600;
    pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Damas Chinesas")
    pygame.display.flip()
    screen = pygame.display.get_surface()
    criacao_tela_de_vitoria(screen,ganhador)
    flag=False
    while sair==False:
        
        for event in pygame.event.get():
            pygame.display.update()                                           
            if event.type==pygame.MOUSEMOTION:
                
                mouse=pygame.mouse.get_pos()
                if((largura/2+75)>mouse[0]>(largura/2-75) and 500+50>mouse[1]>500):
                    pygame.draw.rect(screen,azul_forte,(largura/2-75,500,150,50))
                    message_display((largura/2),(525),"Jogar denovo",20,(255,255,255,255))
                else:

                    pygame.draw.rect(screen,azul,(largura/2-75,500,150,50))
                    message_display((largura/2),(525),"Jogar denovo",20,(255,255,255,255))
                
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                if event.button==1:

                    if((largura/2+75)>mouse[0]>(largura/2-75) and 500+50>mouse[1]>500):
                        print("Quer jogar denovo")
                        sair=True
                        server.set_jogar_denovo(True)


            
            elif event.type==pygame.QUIT:
                sair=True
                server.del_player(cliente.get_my_username())

        if server.get_jogar_denovo()==True:
            sair=True
            server.set_jogar_denovo(False)
            server.reset_game()
            if len(server.get_lista_players()) < 2:
                travado=True
                message_display(largura/2,altura/2+280,"Aguardando o outro jogador se conectar...",20,(0,0,0,255))
                pygame.display.update()
            while(travado):
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        travado=False
                        server.del_player(cliente.get_my_username())
                    if len(server.get_lista_players()) == 2:
                        travado=False
            if len(server.get_lista_players()) == 2:
                cliente.reset_chat()
                tela_de_jogo()

def att_chat(screen):
    altura=0;
    pygame.draw.rect(screen,(255,255,255,255),[500,10,690,570])
    font = pygame.font.SysFont('arial',15)
    chat=cliente.get_chat()
    for i in chat:
        txt = font.render(i, True, (0,0,0,255))
        screen.blit(txt, (510, 20+altura-10))
        altura+=30;
    pygame.display.update(pygame.Rect(500,10,690,570))

def att_mensagem(text,screen):
    font = pygame.font.SysFont('arial',15)
    pygame.draw.rect(screen,(255,255,255,255),[500,590,690,30])
    txt = font.render(text, True, (0,0,0,255))
    screen.blit(txt, (510, 600))
    pygame.display.update(pygame.Rect(500,590,690,30))
##
##
##
def criacao_tela_de_jogo():
    screen=pygame.display.get_surface()
    largura=1200;
    altura=630;
    pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Damas Chinesas")
##    pygame.display.flip()
    screen=pygame.display.get_surface()
    Att_Tabuleiro()
##    pygame.draw.rect(screen,(255,255,255,255),[800,100,800,600])
##    pygame.draw.rect(screen,(255,255,255,255),[800,720,800,200])



    

def tela_de_jogo():
    global jogador_atual
    sair= False
    screen=pygame.display.get_surface()
    flag=False
    desistir=False
    minha_cor=cliente.get_minhas_pecas()
    my_name=cliente.get_my_username()
    nome_do_jogador=my_name+": "
    text=''
    font = pygame.font.SysFont('arial',15)
    tam_nome_jogador=len(nome_do_jogador)
    altura_texto=0
    clock = pygame.time.Clock()
    criacao_tela_de_jogo()
    att_chat(screen)
    att_mensagem(text,screen)
    pygame.display.update()
    
##    print("Isso já é na tela de jogo: "+jogador_atual)
    jogador_atual=server.get_jogador_atual()
    
    while sair==False:
        
        for event in pygame.event.get():            
            if(sair==False):
                if event.type == pygame.KEYDOWN:
        ##              K_RETURN é o enter, quando aperta imprime a mensagem
                    if event.key == pygame.K_RETURN and text!="":
                        cliente.add_mensagem_Chat(my_name+": "+text)
                        server.adversario_add_mensagem_Chat(my_name,my_name+": "+text)
                        pygame.draw.rect(screen,(255,255,255,255),[800,100,800,600])
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif(len(text)<=60 and event.key != pygame.K_RETURN):
                        text += event.unicode
##                    Att_Tabuleiro(screen)
                    att_chat(screen)
                    att_mensagem(text,screen)
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    mouse=pygame.mouse.get_pos()
                    if event.button==1:
                        if(screen.get_at(mouse)==(Cor_Circ_Verme)and minha_cor=="RED" and jogador_atual=="RED"):
                           if(flag==False):
                               cliente.elimina_o_azul_do_tabuleiro()
                               (aux,auy)=cliente.return_a_linha_coluna_da_tabela_correspondente_coordenada(mouse[0],mouse[1])
                               peca_atual=(auy,aux)
                               cliente.coloca_azul_onde_player_pode_andar(auy,aux)
                        elif(screen.get_at(mouse)==(Cor_Circ_Verde) and minha_cor=="GREEN" and jogador_atual=="GREEN"):
                           if(flag==False):
                               cliente.elimina_o_azul_do_tabuleiro()
                               (aux,auy)=cliente.return_a_linha_coluna_da_tabela_correspondente_coordenada(mouse[0],mouse[1])
                               peca_atual=(auy,aux)
                               cliente.coloca_azul_onde_player_pode_andar(auy,aux)
                        elif(screen.get_at(mouse)==(Cor_Circ_Azul)):
                           cliente.elimina_o_azul_do_tabuleiro()
                           (aux,auy)=cliente.return_a_linha_coluna_da_tabela_correspondente_coordenada(mouse[0],mouse[1])
                           peca_destino=(auy,aux)
                           cliente.troca_cor(peca_destino,peca_atual)
                           server.adversario_troca_cor(peca_destino,peca_atual,my_name)
                           flag=cliente.verifica_se_player_ainda_pode_andar(peca_destino,peca_atual)
                           peca_atual=peca_destino
                           teste_ganhador=cliente.verifica_quem_ganhou()
                           if(teste_ganhador=="GREEN"):
                                print("Verde ganhou")
                                server.set_ganhador("GREEN")
##                                func_ganhou("GREEN")
                           elif(teste_ganhador=="RED"):
                               print("Vermelho ganhou")
                               server.set_ganhador("RED")
##                               func_ganhou("RED")
                           elif(flag==False):
                               server.troca_jogador()
                               server.adversario_att_tabuleiro(my_name)
##                               jogador_atual=server.get_jogador_atual()
                        elif( (80+150)>mouse[0]>(80) and 470+50>mouse[1]>470 and minha_cor==jogador_atual):
                            ##DESISTIU
                            desistir=True
                            if(minha_cor=="RED"):
                                server.set_ganhador("GREEN")
                            elif(minha_cor=="GREEN"):
                                server.set_ganhador("RED")
##                            func_ganhou(jogador_atual)
                        elif((270+150)>mouse[0]>(270) and 470+50>mouse[1]>470 and minha_cor==jogador_atual):
                            flag=False
                            cliente.elimina_o_azul_do_tabuleiro()
                            server.troca_jogador()
                            jogador_atual=server.get_jogador_atual()
                            server.adversario_att_tabuleiro(my_name)

                    if(desistir==False):   
                        Att_Tabuleiro()
                        att_chat(screen)
                        att_mensagem(text,screen)
                elif event.type==pygame.MOUSEMOTION:
                    mouse=pygame.mouse.get_pos()
                    if( (80+150)>mouse[0]>(80) and 470+50>mouse[1]>470 and minha_cor==jogador_atual):
                        pygame.draw.rect(screen,vermelho_forte,(((250)-170),470,150,50))
                        message_display(((250)-95),(495),"Desistir",20,(255,255,255,255))
                        pygame.display.update(pygame.Rect((80,470,150,50)))
                    elif((270+150)>mouse[0]>(270) and 470+50>mouse[1]>470 and minha_cor==jogador_atual):
                        pygame.draw.rect(screen,azul_forte,(((250)+20),470,150,50))
                        message_display(((250)+95),(495),"Passar a vez",20,(255,255,255,255))
                        pygame.display.update(pygame.Rect((270,470,150,50)))
                    else:
                        pygame.draw.rect(screen,vermelho,(((250)-170),470,150,50))
                        message_display(((250)-95),(495),"Desistir",20,(255,255,255,255))
                        pygame.draw.rect(screen,azul,(((250)+20),470,150,50))
                        message_display(((250)+95),(495),"Passar a vez",20,(255,255,255,255))
                        pygame.display.update(pygame.Rect((80,470,150,50)))
                        pygame.display.update(pygame.Rect((270,470,150,50)))
                elif event.type==pygame.QUIT:
                    sair=True
                    server.del_player(my_name)
                    if(minha_cor=="RED"):
                        server.set_ganhador("GREEN")
##                        send("GANHOU GREEN",client_socket)
                    elif(minha_cor=="GREEN"):
                        server.set_ganhador("RED")
##                        send("GANHOU RED",client_socket)
        if server.get_ganhador()!="NENHUM" and sair==False:
            cliente.reset_tabuleiro()
            print("Chegou aqui")
            tela_de_vitoria(server.get_ganhador())
            sair=True

        clock.tick(60)

def text_objects(text, font,cor):
        textSurface = font.render(text, True, cor)
        return textSurface, textSurface.get_rect()
def message_display(x,y,text,size,cor):
        largeText = pygame.font.SysFont('arial',size)
        TextSurf, TextRect = text_objects(text, largeText,cor)
        TextRect.center = (x,y)
        pygame.display.get_surface().blit(TextSurf, TextRect)
def criacao_tela_de_colocar_nome():
        largura=700;
        altura=500;
        branco_escuro=(200,200,200,255)
        nome=''
        porta=''
        ip=''
        meio_x=largura/2
        meio_y=altura/2
        font = pygame.font.SysFont('arial',25)
        cor_adversario=""
        clicou_no_nome=False
        bloqueio_cor=True
        bloqueio_teclado=False
        pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Tela inicial")
        screen = pygame.display.get_surface()
        screen.fill(cinza)
    ##    pygame.display.flip()
        screen=pygame.display.get_surface()
        largura_input_box=400
        altura_input_box=50
        y_da_input_box=meio_y-altura_input_box/2
        x_da_input_box=meio_x-largura_input_box/2
        #retangulo do nome
        message_display(x_da_input_box-20,y_da_input_box-175,"Nome:",50,(0,255,255,255))
        pygame.draw.rect(screen,branco_escuro,[x_da_input_box+75,y_da_input_box-200,largura_input_box,altura_input_box])

        
        pygame.draw.rect(screen,(125,0,0,255),[(largura/2-50)-100,(altura/2+50)+100,100,50])
        pygame.draw.rect(screen,(0,125,0,255),[(largura/2-50)+100,(altura/2+50)+100,100,50])
        
        
        
        
        
        message_display(largura/2,altura/2+100,"Escolha sua cor:",50,(0,255,255,255))
        sair=False
        while(sair==False):
            
            for event in pygame.event.get():
                pygame.display.update()
                if event.type == pygame.KEYDOWN and bloqueio_teclado==False:
                        
            ##              K_RETURN é o enter, quando aperta imprime a mensagem
                        if event.key == pygame.K_RETURN:
                            if(nome!=""):
##                                server.teste(cliente)
                                register_name_server_cliente(nome)
                                localizar_name_server(nome)
                                cliente.set_my_username(nome)
                                pygame.draw.rect(screen,branco_escuro,[x_da_input_box+75,y_da_input_box-200,largura_input_box,altura_input_box])
                                txt = font.render(nome, True, (0,0,0,255))
                                screen.blit(txt, (x_da_input_box+75, y_da_input_box-200+15))
                                bloqueio_teclado=True
                                bloqueio_cor=False
                        elif event.key == pygame.K_BACKSPACE:
                            if(clicou_no_nome==True):
                                nome = nome[:-1]
                                txt = font.render(nome, True, (0,0,0,255))
                                pygame.draw.rect(screen,branco,[x_da_input_box+75,y_da_input_box-200,largura_input_box,altura_input_box])
                                screen.blit(txt, (x_da_input_box+75, y_da_input_box-200+15))
                        elif(len(nome)<21 and clicou_no_nome==True):
                            nome += event.unicode
                            txt = font.render(nome, True, (0,0,0,255))
                            pygame.draw.rect(screen,branco,[x_da_input_box+75,y_da_input_box-200,largura_input_box,altura_input_box])
                            screen.blit(txt, (x_da_input_box+75, y_da_input_box-200+15))
                elif event.type==pygame.MOUSEMOTION:
                    mouse=pygame.mouse.get_pos()
                    if bloqueio_cor==False:
                        
                        #verde
                        if((largura/2-50)+200>mouse[0]>(largura/2-50)+100 and (altura/2+100+100)>mouse[1]>(altura/2+50+100) and server.get_escolheu_verde()==False):
                            pygame.draw.rect(screen,(0,255,0,255),[(largura/2-50)+100,(altura/2+50)+100,100,50])
                        #vermelho
                        elif((largura/2-50)>mouse[0]>(largura/2-150) and (altura/2+100+100)>mouse[1]>(altura/2+50+100) and server.get_escolheu_vermelho()==False):
                            pygame.draw.rect(screen,(255,0,0,255),[(largura/2-50)-100,(altura/2+50)+100,100,50])
                        else:
                            pygame.draw.rect(screen,(0,125,0,255),[(largura/2-50)+100,(altura/2+50)+100,100,50])
                            pygame.draw.rect(screen,(125,0,0,255),[(largura/2-50)-100,(altura/2+50)+100,100,50])
                    elif(bloqueio_teclado==False):                    
                        #nome
                        if((x_da_input_box+75+largura_input_box)>mouse[0]>(x_da_input_box+75) and (y_da_input_box-200+altura_input_box)>mouse[1]>(y_da_input_box-200)):
                            pygame.draw.rect(screen,branco,[x_da_input_box+75,y_da_input_box-200,largura_input_box,altura_input_box])
                            txt = font.render(nome, True, (0,0,0,255))
                            screen.blit(txt, (x_da_input_box+75, y_da_input_box-200+15))
                        else:
                            pygame.draw.rect(screen,branco_escuro,[x_da_input_box+75,y_da_input_box-200,largura_input_box,altura_input_box])
                            txt = font.render(nome, True, (0,0,0,255))
                            screen.blit(txt, (x_da_input_box+75, y_da_input_box-200+15))
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    mouse=pygame.mouse.get_pos()
                    if bloqueio_cor==False:
                        
                        if event.button==1:
                            #verde
                            if( (largura/2-50)+200>mouse[0]>(largura/2-50)+100 and (altura/2+100+100)>mouse[1]>(altura/2+50+100) and server.get_escolheu_verde()==False):
                                cliente.set_minhas_pecas("GREEN")
                                server.add_player(cliente)
    ##                            server.add_player(my_username,minhas_pecas)
    ##                            print(meu_objeto_cliente.get_minhas_pecas())
                                bloqueio_cor=True
                                if(cor_adversario==""):
                                    message_display(largura/2,altura/2+125+100,"Aguardando o outro jogador escolher a cor...",20,(0,0,0,255))
                            #vermelho
                            elif((largura/2-50)>mouse[0]>(largura/2-150) and (altura/2+100+100)>mouse[1]>(altura/2+50+100) and server.get_escolheu_vermelho()==False):
                                cliente.set_minhas_pecas("RED")
                                print("Cor: "+cliente.get_minhas_pecas())
                                server.add_player(cliente)
                                bloqueio_cor=True
                                if(cor_adversario==""):
                                    message_display(largura/2,altura/2+125+100,"Aguardando o outro jogador escolher a cor...",20,(0,0,0,255))
                    elif(bloqueio_teclado==False):
                        #nome
                        if((x_da_input_box+75+largura_input_box)>mouse[0]>(x_da_input_box+75) and (y_da_input_box-200+altura_input_box)>mouse[1]>(y_da_input_box-200)):
                            clicou_na_porta=False
                            clicou_no_nome=True
                            clicou_no_ip=False
                            pygame.draw.rect(screen,branco,[x_da_input_box+75,y_da_input_box-200,largura_input_box,altura_input_box])
                        txt = font.render(nome, True, (0,0,0,255))
                        screen.blit(txt, (x_da_input_box+75, y_da_input_box-200+15))
                elif event.type==pygame.QUIT:
                    if((bloqueio_cor==False and bloqueio_teclado==True) or (bloqueio_cor==True and bloqueio_teclado==False)):
                        sair=True
            if len(server.get_lista_players())==2:
                print("2 jogadores se conetaram")
                sair=True
                tela_de_jogo()
def register_name_server_cliente(nome):
    daemon = Pyro4.Daemon()
    uri=daemon.register(cliente)
    ns=Pyro4.locateNS()
    ns.register("Cliente_"+nome,uri)
##    print('Before Request Loop')
    threading.Thread(target=daemon.requestLoop).start()
##    print('After Pyro4 Daemon')
def localizar_name_server(nome):
    global cliente
    ns=Pyro4.locateNS()
    uri=ns.lookup("Cliente_"+nome)
    cliente=Pyro4.Proxy(uri)

##    daemon = Pyro4.Daemon()
##    threading.Thread(target=daemon.requestLoop).start()

if __name__ == "__main__":
    pygame.init();
    server=look_for_server()
##    register_name_server_object()
##    Thread_daemon()
    print("Achou server")
    if(server.pode_add_player()):
##        cliente.set_minhas_pecas("GREEN")
##        print("Cor: "+cliente.get_minhas_pecas())
##        server.add_player(uri)
        criacao_tela_de_colocar_nome()
##        server.teste(cliente)
    else:
        print("Servidor só comporta 2 jogadores")
    pygame.quit()
    sys.exit(0)
##    input("\nEspera")

