from datetime import datetime
import DbLabs
import re

buscaPJ = DbLabs.buscaDominio().buscaCNPJ


class certInstalado:

    def __init__(self, stringOrigem):

        self.validade = None
        self.cliente = None
        self.origem: str = stringOrigem


        self.defineCliente()
        self.defineValidade()

    def defineCliente(self):

        padraoCnpj = re.compile(r"[0-9]{14}")
        cnpj = padraoCnpj.finditer(self.origem)


        for match in cnpj:
            self.cliente = buscaPJ(match.group())

    def defineValidade(self):

        padraoValidade = re.compile(r"NotAfter {5}: (\d{2}/){2}\d{4}")
        validade = padraoValidade.finditer(self.origem)

        for match in validade:

            validadeNO = match.group().replace("NotAfter     : ", "")

            self.validade = datetime.strptime(validadeNO, "%d/%m/%Y")

        pass