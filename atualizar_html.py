from config import configs

with open(configs['arquivo_base'], 'r') as arq:
    base_string = arq.read()

# Substitui o link
nova_string = base_string.replace("LINK_FLAG", configs['webservice'])

with open('index.html', 'w') as arq:
    arq.write(nova_string)