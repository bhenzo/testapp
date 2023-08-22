from flask import Flask
import os
import requests
from flask import request
import threading

app = Flask(__name__)


def thread_func(url):
    x = requests.get(f'http://{url}', verify=False)


@app.route('/')
def hello():
    loops = request.args.get('loops') or 10
    th_amount = request.args.get('th_amount') or 50
    url = request.args.get('url')
    threads = []
    if url is None:
        return "Ingrese url"

    print(f"URL IS {url}")
    for i in range(int(loops)):
        th_list = []
        for t in range(int(th_amount)):
            x = threading.Thread(target=thread_func, args=(url,))
            th_list.append(x)
            x.start()
        for t in th_list:
            t.join()


    return f"listo las {loops} con {th_amount} hilos!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')