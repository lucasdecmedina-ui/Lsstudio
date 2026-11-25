from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
import webbrowser

directory = Path(__file__).resolve().parent
url = 'http://localhost:8793/'
try:
    server = ThreadingHTTPServer(('127.0.0.1', 8793), partial(SimpleHTTPRequestHandler, directory=str(directory)))
except OSError as error:
    print(f'Nao foi possivel iniciar a previa na porta 8793: {error}')
    print('Feche outro servidor que esteja usando essa porta e tente novamente.')
    raise SystemExit(1)

threading.Thread(target=server.serve_forever, daemon=True).start()
print(f'LS Studio Santos: {url}')
print('Mantenha esta janela aberta enquanto visualiza o site.')
webbrowser.open(url)
try:
    input('Pressione Enter para encerrar a previa.\n')
except (KeyboardInterrupt, EOFError):
    pass
finally:
    server.shutdown()
    server.server_close()
