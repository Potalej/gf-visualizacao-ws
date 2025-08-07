# gf-visualizacao-ws
Visualização em tempo real do gravidade-fortran usando WebSockets.

## Visualizando localmente

Se estiver rodando uma simulação em um computador e for fazer a visualização na mesma máquina, então basta gerar o "index.html" rodando

```shell
python3 atualizar_html.py
```

Com o visualizador gerado, inicie o servidor, abra o navegador na página de visualização e rode a simulação com a opção `"exibir": true`.

## Visualizando em outra máquina

Se estiver rodando a simulação em uma máquina e for visualizar em outra, será preciso expor a porta do WebService de alguma forma. Sugiro usar o [ngrok](https://ngrok.com/) com um endereço fixo.

Com tudo instalado, atualize o endereço do WebService no "config.json" para:

```json
"webservice": "wss://seu-endereco-ngrok.ngrok-free.app/ws"
```

Gere o "index.html" e inicie o ngrok usando a porta devida (pré-definida como 8001):

```shell
ngrok http --url=seu-endereco-ngrok.ngrok-free.app 8001
```

Aora inicie o servidor do python, abra o navegador na página de visualização e rode a simulação com a opção `"exibir": true`.
