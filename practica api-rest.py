import requests
import pandas as pd

url = "https://openlibrary.org/search.json"

params = {"q": "Gabriel Garcia Marquez"}

response = requests.get(url, params=params)

data = response.json()

for book in data['docs'][:5]:
    print(book.get("title"), "-", book.get("author_name", ["Desconocido"])[0])


df = pd.DataFrame(data['docs'])
print(df.columns)
df.head()