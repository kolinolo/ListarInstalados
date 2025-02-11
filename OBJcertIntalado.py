from datetime import datetime
import re



class certInstalado:

    def __init__(self, stringOrigem):


        self.validade = None
        self.cnpj = None
        self.origem: str = stringOrigem
        self.thumbPrint = None

        self.defineThumbPrint()
        self.defineCliente()
        self.defineValidade()

    def defineCliente(self):

        padraoCnpj = re.compile(r"FriendlyName : (\S ?)*[0-9]{14}")
        cnpj = padraoCnpj.finditer(self.origem)


        for match in cnpj:
            self.cnpj = match.group()[-14:]

    def defineValidade(self):

        padraoValidade = re.compile(r"NotAfter {5}: (\d{2}/){2}\d{4}")
        validade = padraoValidade.finditer(self.origem)

        for match in validade:

            validadeNO = match.group().replace("NotAfter     : ", "")

            self.validade = datetime.strptime(validadeNO, "%d/%m/%Y")

        pass

    def defineThumbPrint(self):

        padraoThumb = re.compile(r"Thumbprint {3}: .*")
        TP = padraoThumb.finditer(self.origem)

        for match in TP:
            self.thumbPrint = match.group().replace("Thumbprint   : ", "")



        pass