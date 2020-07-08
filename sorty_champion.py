import random
import sys
from prettytable import PrettyTable

## Apenas para controle de quantidade de execuções ate chegar no resultado
x = 1

champions = [
    "Henrique Piccolo",
    "Fernando Wiek",
    "Wesley",
    "Andre",
    "Lucas Souza",
    "Leandro L."
]

## Lista de recem chegados que ainda nao tem conhecimento dos processos e arquitetura
n_buddies = [
    #"Henrique Piccolo",
    "Andre"
]

def rulesChampion(champion, buddy, semana, semana_ver):
    ## Regra         
    ## Nao pode ser buddy quem esta na lista n_buddies
    ## Nao pode ser champion e buddy na mesma semana
    if buddy not in n_buddies and  champion != buddy:
        while semana_ver >= 0:
            ## Verifica se foi champion ou buddy na semana y
            if champion == champion_semana[semana-semana_ver] or champion == buddy_semana[semana-semana_ver] or buddy == champion_semana[semana-semana_ver] or buddy == buddy_semana[semana-semana_ver]:
                return False
            semana_ver -= 1
        return True
    return False

def main():
    global semana
    global champion_semana
    global buddy_semana
    global qtd_semanas
    global qtd_semanas_ver
    global x
    
    ## Determina quantas semanas serao apresentadas de resultado
    if len(sys.argv) > 1:
        qtd_semanas = int(sys.argv[1])
    else:
        qtd_semanas = 10
        
    ## Determina quantas semanas anteriores a verificar se a pessoa foi/nao champion/buddy
    if len(sys.argv) > 2:
        qtd_semanas_ver = int(sys.argv[2])
    else:
        qtd_semanas_ver = 1
    semana = 0
    
    champion_semana = [0] * qtd_semanas
    buddy_semana = [0] * qtd_semanas
    t = PrettyTable(['Semana', 'Champion', 'Buddy'])
    
    while semana < qtd_semanas:
        status=False
        
        while status == False:
            ##Random champion e buddy
            ## Quem esta na lista de n_buddies ficara como champion nas primeiras semanas
            if semana < len(n_buddies) and len(n_buddies) > 0:
                champion = random.choice(n_buddies)
            else:
                champion = random.choice(champions)
            buddy = random.choice(champions)
            
            ## Valida regras de champion
            if rulesChampion(champion, buddy, semana, qtd_semanas_ver):
                ## Adiciona valores na tabela para ser apresentado o resultado
                t.add_row([semana, champion, buddy])
                buddy_semana[semana] = buddy
                champion_semana[semana] = champion
                status = True
                
        semana += 1
    
    ## Valida se todos serao champion pelo menos 1x
    if qtd_semanas > len(champions):
        for champion in champions:
            semana = 0
            value = False
            while semana < qtd_semanas and value == False:
                if champion == champion_semana[semana]:
                    value = True
                semana += 1
            if value == False:
                x += 1
                main()

    print(t)
    print("Foi processado " + str(x) + " vez(es) ate chegar neste resultado")
    exit()

if __name__ == "__main__":
    main()