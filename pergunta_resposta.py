# Pergunta e resposta
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25','55','10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4','5','2','1'],
        'Resposta': '5',
    }
]

qtd_acertos = 0

for questionario in perguntas:
    print('Pergunta:', questionario['Pergunta'])
    print()

    opcoes = questionario['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    resposta = input('Escolha uma opção: ')

    acertou = False
    resposta_int = None
    qtd_opcoes = len(opcoes)

    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == questionario['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou')
        
    else:
        print('Errou')

    print()

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
