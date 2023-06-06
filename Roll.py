#imports

from random import randint

#funções

def rolling(a,b):
    dados = []
    for i in range(b):
        rolagem = randint(1,a)
        dados.append(rolagem)    
    return dados

def rolling_mod(a,b,c):
    dados = []
    dado1 = []
    for i in range(b):
        rolagem = randint(1,a)
        dados.append(rolagem)  
        dado1.append(rolagem+c)  
    return dados, dado1

def rolling_comp(a,b,c,d,e,f):
    dados = []
    dado1 = []
    dados_npc=[]
    dado2=[]
    cont_i = 0
    cont_e = 0
    for i in range(b):
        rolagem = randint(1,a)
        dados.append(rolagem)  
        dado1.append(rolagem+c) 
        cont_i += dado1[i]
    for i in range(e):
        rolagem = randint(1,d)
        dados_npc.append(rolagem)  
        dado2.append(rolagem+f) 
        cont_e += dado2[i]
    if cont_i > cont_e:
        venc = cont_i
        p = "você"
    elif cont_e > cont_i:
        venc = cont_e
        p = "inimigo"
    else:
        p = "empate" 

    return dados,dado1,cont_i,dados_npc,dado2,cont_e,venc, p

def rolling_vs(a,b,c,d):
    y_dam = a + b
    e_l = c + d
    e_lp = e_l - y_dam
    if 0 < e_lp:
        st_e = "vivo"
    else:
        st_e = "morto"
  
    return y_dam,e_lp,st_e
#programa

print('')
print('Olá invocador, leia as opções a seguir para continuar.🐉')
print('')
print('1- Rolagem de dados simples.🎲')
print('2- Rolagem de dados + modificadores🍺')
print('3- Rolagem de dados + modificadores x adversario. ⚔️')
print('')
op = int(input('Digite a opção que deseja executar: '))
while op > 3 or op < 1 :
    op = int(input('Digite uma opção valida: '))
if op == 1:
    dado = int(input('Digite a quantidade de lados do dado que deseja rolar: '))
    qtd = int(input('Diga a quantidade de vezes que deseja rolar: '))
    resp = rolling(dado,qtd)    
    for i in range(len(resp)):
        print(f'O resultado da rolagem {i+1} foi: {resp[i]}')

if op == 2:
    dado = int(input('Digite a quantidade de lados do dado que deseja rolar: '))
    qtd = int(input('Diga a quantidade de vezes que deseja rolar: '))
    mod = int(input('Digite a soma de seus modificadores: '))
    resp_dado,resp_mod= rolling_mod(dado,qtd,mod)
    for i in range(len(resp_dado)):
        print(f'O resultado da rolagem {i+1} foi {resp_dado[i]} + {mod} foi de: {resp_mod[i]}')
    
if op == 3:
    print('')
    print('Opções👻')
    print('')
    print('1- Teste simples: sua rolagem x rolagem do NPC. 🥊')
    print('2- Confronto: sua rolagem x vida do adv. 🌠')
    print('')
    op_3 = int(input('Diga a opção que deseja executar: '))
    while 1 > op_3 or op_3 > 2:
        op_3 = int(input('Digite uma opção valida: '))
    if op_3 == 1:
        dado = int(input('Digite a quantidade de lados do dado que deseja rolar: '))
        qtd = int(input('Diga a sua quantidade de rolagens: '))
        mod = int(input('Digite a soma de seus modificadores: '))
        print('')
        dado_adv = int(input('Digite a quantidade de lados do dado do adversario: '))
        qtd_adv = int(input('Diga a quantidade de rolagens do adversario: '))
        mod_npc = int(input('Digite a soma dos modificadores do adversario: '))
        resp_dado,resp_mod,tot1,resp_dado_npc,resp_mod_npc,tot2,win,pi= rolling_comp(dado,qtd,mod,dado_adv,qtd_adv,mod_npc)
        print('')
        for i in range(len(resp_dado)):
    
            print(f'O resultado da sua rolagem {i+1} foi {resp_dado[i]} + {mod} foi de: {resp_mod[i]}')
        print("")
        print('⚔️')
        print("")
        for i in range(len(resp_dado_npc)):
            print(f'O resultado da rolagem {i+1} do adversario foi de {resp_dado_npc[i]} + {mod_npc} foi de: {resp_mod_npc[i]}')
        print('')
        print(f'O somatório das suas rolagens foi: {tot1}')
        print('')
        print(f'O somatório das rolagens do adversário foi: {tot2}')
        print('')
        if pi == 'você':
            print('Você derrotou o inimigo')
        elif pi == "inimigo":
            print("O Adversario foi o vencedor")
        else:
            print('Você e o adversario empataram')
        print('')
    if op_3 == 2:
        atb = input('Diga o atributo que usará: ')
        s_n = input('Você possui alguma arma(sim/não): ')
        if s_n == "sim":
            dan_arm= int(input('Informe o dano da sua arma: '))
        elif s_n == "não":
            dan_arm = 0
        mot_atb = int(input(f'Digite o seu modificador de {atb}: '))
        vida_adv = int(input('Informe a vida do adversario: '))
        mod_adv = int(input('Digite a resitencia do adversario: '))
        dan_atk,vida_patk, stts_adv = rolling_vs(dan_arm,mot_atb,vida_adv,mod_adv)
        print(f'Seu dano de ataque foi: {dan_atk} ')
        print(f'A nova vida do adversario é: {vida_patk} ')
        if stts_adv == 'morto':
            print('O adversario foi derrotado')
        else:
            while stts_adv == "vivo":
                print('O adversario ainda está vivo')
                comb = input('Deseja continuar no combate (sim/não): ')
                if comb == "não":
                    print('')
                    print('Combate encerrado')
                    break
                else:
                    print('')
                    print('Novo ataque será efetuado')
                    atb = input('Diga o atributo que usará: ')
                    s_n = input('Você possui alguma arma(sim/não): ')
                    if s_n == "sim":
                        dan_arm= int(input('Informe o dano da sua arma: '))
                    elif s_n == "nâo":
                        dan_arm = 0
                    mot_atb = int(input(f'Digite o seu modificador de {atb}: '))
                    vida_adv = vida_patk
                    mod_adv = int(input('Digite a resitencia do adversario: '))
                    dan_atk,vida_patk, stts_adv= rolling_vs(dan_arm,mot_atb,vida_adv,mod_adv)
                    print(f'Seu dano de ataque foi: {dan_atk} ')
                    print(f'A nova vida do adversario é: {vida_patk} ')
                    if stts_adv == 'morto':
                        print('O adversario foi derrotado')

                        






    
