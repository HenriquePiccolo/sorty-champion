import random
from prettytable import PrettyTable

qtd_semanas = 7
    
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

def rulesChampion(champion, buddy, semana):
    ## Regra         
    ## Nao pode ser buddy quem esta na lista n_buddies
    ## Nao pode ser champion e buddy na mesma semana
    if buddy not in n_buddies and  champion != buddy:
        ## Determina quantas semanas anteriores a verificar se a pessoa foi/nao champion/buddy
        y = 1
        while y >= 0:
            ## Verifica se foi champion ou buddy na semana y
            if champion == champion_semana[semana-y] or champion == buddy_semana[semana-y] or buddy == champion_semana[semana-y] or buddy == buddy_semana[semana-y]:
                return False
            y -= 1
        return True
    return False

def main():
    global semana
    global champion_semana
    global buddy_semana
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
            if rulesChampion(champion, buddy, semana):
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
                main()

    print(t)
    exit()

if __name__ == "__main__":
    main()