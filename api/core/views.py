from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProdutosSerializer

import re
import requests

class Produtos(APIView):
    url = 'https://prd-api-partner.viavarejo.com.br/api/search?'

    def get(self, request):
        USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'

        resultsPerPage = request.GET.get('resultsPerPage')
        terms = request.GET.get('terms')
        store = request.GET.get('store')

        if resultsPerPage:
            self.url += 'resultsPerPage=' + resultsPerPage
        if not terms:
            return Response({'message': 'Escolha um produto para buscar nas nossas lojas!'}, status=400)
        if not store:
            return Response({'message': 'Escolha uma de nossas três lojas!'}, status=400)

        link = f'{self.url}&terms={terms}&apiKey={store}'

        
        r = requests.get(link, headers={'User-Agent': USER_AGENT})
        if r.status_code == 200:
            data = ProdutosSerializer(r.json()['products'], many=True).data
            
            for prd in data:
                cod = re.search(r'[br/](\d+).*/', prd['images']).group()
                price_json = requests.get(f'https://pdp-api.{store}.com.br/api/v2/sku{cod}price/source/EX', headers={'User-Agent': USER_AGENT})
                price = price_json.json()
                
                try:
                    print(prd['status'])
                    # if prd['description'] is None: 
                        # prd.update({"description": "Saiba mais sobre o produto clicando no link!"})
                    
                    if prd['status'] == 'UNAVAILABLE':
                        prd['name'] = "Oops, O nosso sistema não encontrou o que você procurou :/ O caminho pode não estar mais disponível."
                    else:
                        preco = price['sellPrice']['priceValue']
                        preco_desconto = price['paymentMethodDiscount']['sellPriceWithDiscount']
                        preco_cartao = price['sellPrice']['installment']

                        if preco_desconto < preco:
                            prd.update({"desconto": "Há desconto para este produto!"})
                        
                        prd.update({"preco": preco, "preco_desconto": preco_desconto, "preco_cartao": preco_cartao})

                        #if '.' not in preco:
                            #preco = preco + ",00"
                except KeyError:
                    prd.update({"preco": "", "preco_desconto": "", "preco_cartao": ""})
                    prd['name'] = "Oops, O nosso sistema não encontrou o que você procurou :/ O caminho pode não estar mais disponível ou não hã estoque deste produto."

                except Exception as error:
                    print(f'##### Erro: {type(error)} -> {error}')
                    
            return Response(data)
        else:
            return Response({'message': 'error'}, status=r.status_code)