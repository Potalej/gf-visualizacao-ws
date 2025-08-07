import asyncio
import websockets
import threading
from time import perf_counter
from config import configs

porta_web = configs['porta']
clientes = set()

async def websocket_handler(ws):
    clientes.add(ws)
    print("Alguém acessou!")
    try:
        async for _ in ws:
            pass
    finally:
        clientes.remove(ws)

async def enviar_msg(msg):
    for ws in list(clientes):
        t0 = perf_counter()
        await ws.send(msg)
        t1 = perf_counter()
        if t1 - t0 > 0.1:
            print("Cliente lento, ", t1 - t0)

def receber_do_fortran(callback, loop):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 50007))
    s.listen()
    s.settimeout(60)
    print("Socket fortran online!")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Conectado por {addr}")

            data = conn.recv(4)
            N = int.from_bytes(data, byteorder='little', signed=False)
            print(f"N = {N}")
            tamanho = N * 60

            while True:
                try:
                    data = conn.recv(tamanho).decode()
                except:
                    break

                try:
                    string = ';'.join([','.join(linha.split()) for linha in data.strip().splitlines()])
                    asyncio.run_coroutine_threadsafe(callback(string), loop)
                except:
                    continue
        conn.close()

async def iniciar():
    loop = asyncio.get_running_loop()

    threading.Thread(target=receber_do_fortran, args=(enviar_msg, loop), daemon=True).start()

    ws_server = await websockets.serve(websocket_handler, '0.0.0.0', porta_web)
    print(f"Servidor WebSocket rodando na porta {porta_web}...")
    await ws_server.wait_closed()

if __name__ == "__main__":
    asyncio.run(iniciar())
