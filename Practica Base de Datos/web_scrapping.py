from bs4 import BeautifulSoup
import requests
import pandas as pd

def extract_property_info_from_csv(csv_name):
    result_data=[]

urls=pd.read_csv(csv_filename)["URL"]

from url in urls:
    response=requests.get(url)

if response.status_code!=200:
    print("La solicitud para {url} ha fallado")

html_code=response.text
soup=BeautifulSoup(html_code,"html.parser")

precio=soup.find("p",class_="titlebar__price").get_text(strip=True)
titulo=soup.find("h2",class_="titlebar__title").get_text(strip=True)
direccion=soup.find("h2",class__="titlebar__address").get_text(strip=True)
result_data.apprend({"Precio":precio,"Titulo":titulo,"Direccion":direccion})

url="https://www.argenprop.com/departamentos/venta/caballito?"
links_finales=[]


#Iteramos por las diversas paginas
for pagina in range(1,10):
    url_pagina=url+f"pagina-{pagina}"

#hacemos la request
response=requests.get(url_pagina)
soup=BeautifulSoup(response.content,"html.parser")

#aca obtenemos los a href y los bloques que contengan a
links=soup.find_all("a")
links_dptos=[]
for link in links:
    if "departamento" in link.text:
        links_dptos.append(link)


for link in links_dptos:
    links_finales.append("https://www.argenprop.com"+link["href"])

for link in links_finales:
    print (link)


columna=["URL"]
dataframe=pd.DataFrame(links_finales,columns=columna)
print (dataframe)

dataframe.to_csv("argenprop_lista.csv")
df="argenprop_lista.csv"
    property_info_df=extract_property_info_from_csv(df)

print(property_info_df)