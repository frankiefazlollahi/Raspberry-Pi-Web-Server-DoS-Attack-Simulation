import requests
import threading

url = "http://10.0.0.8"  # Raspberry Pi's IP
num_threads = 100   # Number of concurrent threads
def send_request():
    while True:
        try:
            response = requests.get(url)
            print(response.status_code)
        except Exception as e:
            print(e)

threads = []
for i in range(num_threads):  
    t = threading.Thread(target=send_request)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
