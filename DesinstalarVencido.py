import os
from printTool import colorizar
import Listar
import datetime

HOJE = datetime.datetime.today()
PASTA = os.listdir(fr"{os.path.expanduser("~")}\AppData\Roaming\Microsoft\SystemCertificates\My\Certificates")


def listarVencidos():
    vencidos = []
    lista_itens = Listar.listar_iteracoes()

    for item in lista_itens:

        if item.validade < HOJE:
            vencidos.append(item)
            desinstalar(item)
    for item in vencidos:
        print(colorizar(item.origem,"vermelho"))
    print(f"{len(vencidos)} Certificados vencidos desinstalados")


def desinstalar(item):

    os.remove(fr"{os.path.expanduser("~")}\AppData\Roaming\Microsoft\SystemCertificates\My\Certificates\{item.thumbPrint}")


listarVencidos()






