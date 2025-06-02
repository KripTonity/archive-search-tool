import requests
from bs4 import BeautifulSoup

def search(query):
    url = f"https://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&query={query}&version=1.2"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "xml")

        records = soup.find_all("record")
        results = []

        for record in records[:5]:  # limite les résultats pour le test
            title = record.find("dc:title")
            identifier = record.find("dc:identifier")
            if title and identifier:
                results.append(f"{title.text} - {identifier.text}")
        return results if results else ["No results found."]
    except Exception as e:
        return [f"[ERROR] Gallica scraper failed: {e}"]

