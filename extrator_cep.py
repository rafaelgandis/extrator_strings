endereco = "Rua das Folres 102, apartamento 1100, Laranjeiras, Rio de Janeiro, RJ, 12340126"

import re 

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)