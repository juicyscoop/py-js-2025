

import requests

# jednoducha funkce ktra se podiva na url a stahne html na danem url

def read_html_from_url(url: str):
    response = requests.get(url)
    return response

urll = "https://www.wikipedia.org/"

res = read_html_from_url(urll)
print("res: ", res)
print(":HTML CONTENT: ")

print(res.text)


#print("res: ", res.__dict__)
#html_content = res._content.decode("utf-8")
#print("HTML: \n\n")
#print(html_content)


