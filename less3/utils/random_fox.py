import requests
def fox():
    url = "https://randomfox.ca/floof"
    #url1 = "https://mail.ru"

    response = requests.get(url)
    #response.raise_for_status()

    #return response.text
    return response.json().get('image')

if __name__ == '__main__':
    print(fox())