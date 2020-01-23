# Script: Scrap Jules Site
# Author: Mek
# Date: 20200120

# Librairies
import requests
from bs4 import BeautifulSoup
import json
import os

# Main Class
class Scrap(object):
    def __init__(self):
        self.domain = "https://www.jules.com"
        self.cateogries = ['Décontracté', 'Classique', 'Soirée', 'Chic']
        # pulls
        self.url_pulls = self.domain + "/fr-fr/l/pull/?sz=144"
        self.data_pulls = []
        # pantalons
        self.url_pantalons = self.domain + "/fr-fr/l/pantalon/?sz=144"
        self.data_pantalons = []
        # veste 
        self.url_vestes = self.domain + "/fr-fr/l/veste/?sz=48"
        self.data_vestes = []
        # costume
        # t-shirt 
        self.url_tshirts = self.domain + "/fr-fr/l/t-shirt/?sz=168"
        self.data_tshirts = []
        # chemise
        # chaussures
        # accessoire
        
        # Burton chaussure homme : https://www.zalando.fr/chaussures-homme/
        
    def parseHTML(self, typeProduit):
        products = self.soup.find_all(attrs={"class": "product"})
        print("products number", len(products))
        for product in products:
            produits = {}
            try:
                produits['url_img'] = ''
                produits['url_onmouseover'] = product.img['onmouseover'].split("'")[1]
                produits['url_onmouseout'] = product.img['onmouseout'].split("'")[1]
            except:
                produits['url_img'] = product.img['data-src']
                produits['url_onmouseover'] = ''
                produits['url_onmouseout'] = ''
            produits['name'] = product.h2.a.string
            prices = product.find_all(attrs={"class": "value"})
            if len(prices) == 2:
                produits['price_striked'] = prices[0]['content']
                produits['price'] = prices[1]['content']
            else:
                produits['price_striked'] = 0
                produits['price'] = prices[0]['content']
            
            percent_reduc = product.find(attrs={"class": "percent"})
            if product.find(attrs={"class": "percent"}) != None:
                percent_reduc = product.find(attrs={"class": "percent"}).string
                produits['percent_reduc'] = percent_reduc.strip()
            else:
                produits['percent_reduc'] = 0

            # Catégorie
            produits['categorie'] = self.cateogries[0]
            
            if typeProduit == 'Pulls':
                self.data_pulls.append(produits)
            elif typeProduit == 'Pantalons':
                self.data_pantalons.append(produits)
            elif typeProduit == 'Vestes':
                self.data_vestes.append(produits)   
            elif typeProduit == 'T-Shirts':
                self.data_tshirts.append(produits)
            break
    
    def getPulls(self):
        htm = requests.get(self.url_pulls).text
        self.soup = BeautifulSoup(htm, 'lxml')
        print("Pulls")
        self.parseHTML('Pulls')
        

    def getPantalons(self):
        htm = requests.get(self.url_pantalons).text
        self.soup = BeautifulSoup(htm, 'lxml')
        print("Pantalons")
        self.parseHTML('Pantalons')

    def getVestes(self):
        htm = requests.get(self.url_vestes).text
        self.soup = BeautifulSoup(htm, 'lxml')
        print("Vestes")
        self.parseHTML('Vestes')

    def getTShirts(self):
        htm = requests.get(self.url_tshirts).text
        self.soup = BeautifulSoup(htm, 'lxml')
        print("T-Shirts")
        self.parseHTML('T-Shirts')

    def getChaussures(self):
        print("Chaussures")

    def getChemises(self):
        print("Chemises")
        
    def getData(self):
        # htm = requests.get(self.url_pulls).text
        # self.soup = BeautifulSoup(htm, 'lxml')
        #print(self.soup)
        # Pulls
        self.getPulls()
        # Pantalons
        self.getPantalons()
        # Vestes
        self.getVestes()
        # T-Shirts
        self.getTShirts()


# Programme principal
if __name__ == "__main__":
    result = Scrap()
    result.getData()
    print(result.data_pulls)
    print(result.data_pantalons)
    print(result.data_vestes)
    print(result.data_tshirts)

