import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE = "https://www.dkut.ac.ke"

def scrape_faq():
    url = f"{BASE}/index.php/frequently-asked-questions-faqs"
    resp = requests.get(url, verify=False)
    soup = BeautifulSoup(resp.text, "html.parser")
    faqs = []
    for q, a in zip(soup.select("strong"), soup.select("p")):
        faqs.append({"question": q.text.strip(), "answer": a.text.strip()})
    return faqs

def scrape_csit_docs():
    urls = [
        f"{BASE}/index.php/component/content/article?id=572"
    ]
    docs = []
    for u in urls:
        resp = requests.get(u, verify=False)
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.find("h1").text if soup.find("h1") else "No Title"
        text = soup.get_text("\n")
        docs.append({"title": title, "text": text})
    return docs

if __name__ == "__main__":
    import json
    faqs = scrape_faq()
    docs = scrape_csit_docs()
    with open("../data/faqs.json", "w") as f:
        json.dump(faqs, f, indent=2)
    with open("../data/docs.json", "w") as f:
        json.dump(docs, f, indent=2)
