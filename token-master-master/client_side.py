import requests
# SERVER_IP = '127.0.0.1' # UPDATED SERVER IP FOR WINDOWS PC - WHERE FLASK IS RUNNING
SERVER_IP = 'vermavinay982.pythonanywhere.com'
token_endpoint=f"https://{SERVER_IP}/book_token"
# token_endpoint=f"http://{SERVER_IP}:5000/book_token"


name = input("Enter your name: ")
# sell_token(name)
# response = requests.post(url=token_endpoint, data=data)

response = requests.get(url=token_endpoint, params={'name':name})
print(response.text)