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
        # costume
        # t-shirt
        # chemise
        # chaussures
        # accessoire
        
        # Burton chaussure homme : https://www.zalando.fr/chaussures-homme/
        

    def getPulls(self):
        products = self.soup.find_all(attrs={"class": "product"})
        print("products number", len(products))
        for product in products:
            pulls = {}
            try:
                pulls['url_img'] = ''
                pulls['url_onmouseover'] = product.img['onmouseover'].split("'")[1]
                pulls['url_onmouseout'] = product.img['onmouseout'].split("'")[1]
            except:
                pulls['url_img'] = product.img['data-src']
                pulls['url_onmouseover'] = ''
                pulls['url_onmouseout'] = ''
            pulls['name'] = product.h2.a.string
            prices = product.find_all(attrs={"class": "value"})
            if len(prices) == 2:
                pulls['price_striked'] = prices[0]['content']
                pulls['price'] = prices[1]['content']
            else:
                pulls['price_striked'] = 0
                pulls['price'] = prices[0]['content']
            
            percent_reduc = product.find(attrs={"class": "percent"})
            if product.find(attrs={"class": "percent"}) != None:
                percent_reduc = product.find(attrs={"class": "percent"}).string
                pulls['percent_reduc'] = percent_reduc.strip()
            else:
                pulls['percent_reduc'] = 0

            # Catégorie
            pulls['categorie'] = self.cateogries[0]
            
            self.data_pulls.append(pulls)
            #break

    def getPantalon(self):
        print("getPantalon")

    def getVeste(self):
        print("getVeste")

    def getTShirt(self):
        print("getTShirt")

    def getChaussure(self):
        print("getChaussure")

    def getChemise(self):
        print("getChemise")
        
    def getData(self):
        htm = requests.get(self.url_pulls).text
        self.soup = BeautifulSoup(htm, 'lxml')
        #print(self.soup)

        # Pulls
        self.getPulls()
       


# Programme principal
if __name__ == "__main__":
    result = Scrap()
    result.getData()
    print(result.data_pulls)

