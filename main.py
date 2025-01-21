### importar bibliotecas "App" e "Builder"
### criar o nosso aplicativo
### criar a função build

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

import requests

GUI = Builder.load_file("screen.kv")

class MeuAplicativo (App):

    def build(self):
        Window.clearcolor = (.5,.5,.7,1)
        return GUI
    
    def on_start(self):

        cotacao_dolar = self.cotacao('USD')
        cotacao_euro = self.cotacao('EUR')
        cotacao_bitcoin = self.cotacao('BTC')
        cotacao_ethereum = self.cotacao('ETH')
        
       
        self.root.ids['moeda1'].text = f"DÓLAR: R$ {self.real(cotacao_dolar)}"  
        self.root.ids['moeda2'].text = f"EURO: R$ {self.real(cotacao_euro)}"
        self.root.ids['moeda3'].text = f"BITCOIN: R$ {self.real(cotacao_bitcoin)}"
        self.root.ids['moeda4'].text = f"ETHEREUM: R$ {self.real(cotacao_ethereum)}"
   
   
    def cotacao(self, moeda):
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = requests.get(link)

        dic_requisicao = (requisicao.json())
        cotacao = dic_requisicao[f'{moeda}BRL']['bid'] ## Bid é o valor de venda para cotação disponível na API ###
       
        return cotacao
    

    def real(self, moeda):
        a = "{:,.2f}".format(float(moeda))
        b = a.replace(',','v')
        c = b.replace('.',',')
        return c.replace('v','.')


MeuAplicativo().run()