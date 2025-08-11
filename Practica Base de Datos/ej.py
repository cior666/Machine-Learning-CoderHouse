import pandas as pd
import requests 
API_KEY=###############
url="https://newsapi.org/v2/top-headlines"

params={
    "q":"technology",
    "pageSize":100,
    "apiKey":API_KEY
}
#solicitud http
response=requests.get(url,params=params)

#chequeo de rta
if response.status_code==200:
    data=response.json()

    articles=data.get("articles",[])
    df=pd.DataFrame(articles)

    print(df[["author","title","publishedAt"]])


