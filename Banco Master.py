print('=== SISTEMA DE AUDITORIA: ANÁLISE DE CDB ===')
teto_regulatorio = 13

nome_fundo = input('Digite o nome do fundo: ')
taxa_juros = float(input('Digite a Taxa de juros oferecida: '))

print('-----------------------------------------------------------')
print(f'RELÁTORIO PRELIMINAR:\nFundo Analisado: {nome_fundo}\nTaxa oferecida: {taxa_juros:.1f}%\nTeto Regulatório: {teto_regulatorio:.1f}%')

risco_critico = False

if taxa_juros > teto_regulatorio:
    risco_critico = True
    print('[Alerta critico!] Taxa incompatível')
else:
    print('A taxa está dentro da normalidade regulatória!')

if risco_critico == True:
    print('Parecer do Auditor: Ativo bloqueado para novas emissões.')
else:
    print('Parecer do Auditor: Ativo liberado para comercialização.')
