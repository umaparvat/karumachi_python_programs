import requests as req
from bs4 import BeautifulSoup

def download(download_url, file_name):
    r = req.get(download_url, allow_redirects=True)
    with open(file_name, 'wb') as f:
        f.write(r.content)

def main():
    for page_num in range(1, 624):
        url = f"https://www.capitalmind.in/archives/page/{page_num}/"
        html_text = req.get(url).text
        if not html_text:
            continue
        soup = BeautifulSoup(html_text, 'html.parser')
        for link in soup.find_all('h4'):
            for child in link.children:
                if child and child.name == 'a':
                    download(download_url=child.attrs.get('href'), file_name=child.contents[0])



if __name__ == "__main__":
    main()