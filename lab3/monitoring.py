import requests
import json
import logging
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)

def main(url):     
    try:
         r = requests.get(url)
         data = json.loads(r.content)
         logging.info("Server is available. Server time: %s", data['date'])
         logging.info("Viewed page: %s", data['current_page'])
         logging.info("Server request contains this fields:")
         for key in data.keys():
              logging.info("Key: %s, Data: %s", key, data[key])
    except Exception as x:
         logging.error("Server is unavailable")
    

if __name__ == '__main__':
    while(True):
        main("http://localhost:8000/health")
        time.sleep(60)

