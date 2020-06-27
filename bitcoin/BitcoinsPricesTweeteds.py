import os
import urllib
import json
import time
try:
    import twitter
except ModuleNotFoundError:
    os.system("pip3 install python-twitter")
    import twitter
"""
CLASS USER

POSSUI AS INFORMAÇÕES DE TOKEN E KEYS DO USUÁRIO
#c_key = consumer_key
#c_s = consumer_secret
#a_t_k = access_token_key
#a_t_s = access_token_secret

"""
class user(object):

    def __init__(self, c_key, c_s, a_t_k, a_t_s):
        
        self.c_key = c_key
        self.c_s = c_s
        self.a_t_k = a_t_k
        self.a_t_s = a_t_s
        self.api = twitter.Api(consumer_key=self.c_key,
                  consumer_secret=self.c_s,
                  access_token_key=self.a_t_k,
                  access_token_secret=self.a_t_s)

"""
ERROR

Erro personalizado caso ocorra um erro na instalação dos módulos
"""
class error(Exception):
    def __str__(self):
        return "\n\nOcorreu algum erro. Verifique se seu computador possui os comandos git e pip em seu path."


"""
MAIN

Funcão principal
Verifica se a pasta python-twitter existe

"""
def main():

    # print("\n\nANTES DE INICIAR O PROGRAMA, É NECESSÁRIO CRIAR UM APLICATIVO PRÓPRIO NO TWITTER")
    # print("\nPARA SABER COMO CRIAR SEU APLICATIVO, ACESSE O LINK: https://python-twitter.readthedocs.io/en/latest/getting_started.html")
    
    # cont = input("Deseja continuar o programa? Digite sim para continuar: ")
    # if(cont[0].lower() == 's'):
    #     print("\n\nSerá necessário instalar alguns módulos para a aplicação funcionar.")
    #     install = input("\nDeseja instalar todas as dependências necessárias? Digite sim para instalar: ")

    #     if(install[0].lower() == 's'):
    #         try:
    #             os.system("git clone git://github.com/bear/python-twitter.git")
    #             os.system("pip install -r python-twitter/requirements.txt")
    #             os.system("python python-twitter/setup.py build")
    #             os.system("python python-twitter/setup.py install")
    #             print("\n\nTwitter API already installed")
    #         except:
    #             raise error
    #         finally:
    #             setUserInformation()
    #     else:
    #         exit()      
    # else:
    #     exit()
    setUserInformation()


"""
SETUSERINFORMATION

Cria uma instância da class user e envia as informações do usuário
"""

def setUserInformation():

    global userInfo
    # c_key = input("Digite sua consumer_key: ")
    # c_s = input("Digite sua consumer_secret_key: ")
    # a_t_k = input("Digite seu access_token_key: ")
    # a_t_s = input("Digite seu access_token_secret_key: ")
    #userInfo = user(c_key, c_s, a_t_k, a_t_s)
    userInfo = user(
                'objGJIZv27jFxxSxzjNVVRGQN'
                ,'aTyOTxrmfldgFmRDu8Ptd5wHUOr3avDTHoC3dlYFSNU4Kqzn3m'
                ,'3235947009-IQKmlhocvgNOGrHaJCPWE9m5Ay5PPFIXQ9Kd5MN'
                ,'vrOG9SwohLwxoovBdNEYjAbQAtUmK4uhHNv1P9yEQ14XO'
                )
    get_bitcoin_price()
"""
POST

Faz um tweet a cada uma hora
"""

"""
GET_BITCOIN_PRICE

Pega a cotação do bitcoin em libras, dolar e euro
Informações retiradas deste repositório: https://gist.github.com/marcoscastro/737d18df025f3c1cbadc5d03ca00bf7a
"""
def get_bitcoin_price():

            while True:
                try:
                    url = "http://api.coindesk.com/v1/bpi/currentprice.json"
                    with urllib.request.urlopen(url) as url:
                        response = url.read()
                        data = json.loads(response.decode('utf-8'))
                        USD = float(data['bpi']['USD']['rate'].replace(",", ""))
                        GBP = float(data['bpi']['GBP']['rate'].replace(",", ""))
                        EUR = float(data['bpi']['EUR']['rate'].replace(",", ""))            
                except urllib.error.HTTPError:
                    print('URL inexistente!')
                finally:
                    post(USD, GBP, EUR)
                    time.sleep(3600)

"""
POST

Cria o tweet com as informações necessárias
"""
def post(USD, GBP, EUR):
    emReal = 
    print("\nBuscando as informações sobre o preço do bitcoin...")
    userInfo.api.PostUpdate("O preço do bitcoin em:\nUSD: $ %.2f\nGBP: £ %.2f\nEUR: € %.2f"%(USD, GBP, EUR))
    print("\nTweet feito!")
    
if __name__ == '__main__':
    main()