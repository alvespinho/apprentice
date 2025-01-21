import requests

class MeuAplicativo:

    def cotacao(self, moeda):
        try:
            # URL da API
            link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
            requisicao = requests.get(link)
            requisicao.raise_for_status()  # Verifica se ocorreu algum erro na requisição
            
            # Converte a resposta da API em JSON
            dic_requisicao = requisicao.json()
            
            # Obtém o valor da cotação (bid)
            cotacao = dic_requisicao[f'{moeda}BRL']['bid']
            
            # Exibe a cotação no terminal
            print(f'A cotação do {moeda} é: R$ {cotacao}')
        
        except requests.exceptions.RequestException as e:
            # Tratamento de erro de requisição
            print(f"Erro ao fazer requisição: {e}")
        except KeyError:
            # Caso a moeda não exista na resposta da API
            print(f"Erro: Não foi possível encontrar a cotação para {moeda}")

# Exemplo de uso
app = MeuAplicativo()
app.cotacao("USD")  # Exibe a cotação do dólar
app.cotacao("EUR")  # Exibe a cotação do euro
app.cotacao("BTC")  # Exibe a cotação do Bitcoin
