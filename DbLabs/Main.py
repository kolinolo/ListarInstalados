from .OBJCliente import endereco, Cliente, responsavel

""" Primeira Versão Git"""


class buscaDominio:

    def __init__(self):
        import sqlanydb

        self.__conn = sqlanydb.connect(uid='externo', pwd='1020ethos', host='Servidor:2638', AutoStop="Yes")

        self.listaClientes = []
        self.listarClientes()
        self.ultimoCliente = 0

    def getMunicipio(self, codMunicipio):
        comando = f"SELECT * FROM bethadba.gemunicipio WHERE codigo_municipio = {codMunicipio}"

        cursor = self.__conn.cursor()
        cursor.execute(comando)
        C = cursor.fetchone()
        cursor.close()
        try:
            return C[2]
        except:
            return None

    def listarClientes(self):

        clientes = []
        comando = f"SELECT * FROM bethadba.geempre"

        cursor = self.__conn.cursor()
        cursor.execute(comando)
        listaClientes = cursor.fetchall()
        cursor.close()

        for C in listaClientes:

            if C[87] is not None:
                munCliente = self.getMunicipio(C[87])

            else:
                munCliente = None

            enderecoCliente = endereco(C[2], C[8], C[1], C[13], C[87], C[17], munCliente)

            if C[46] is not None:
                munResp = self.getMunicipio(C[46])
            else:
                munResp = None

            enderecoResp = enderecoCliente.endereco(C[41], C[45], C[38], C[44], C[46], C[17], munResp)

            responsavelLeg = responsavel(C[16], C[37], enderecoResp)
            cliente = Cliente(C[83], C[10], C[73], C[4], C[9], C[21], C[19], enderecoCliente, responsavelLeg)
            if cliente.cod < 1000:
                self.ultimoCliente = cliente.cod
            clientes.append(cliente)

        for ct in range(len(clientes)):  # Cliente atual

            for cc in range(ct, len(clientes)):  # Comparativo

                if clientes[ct].razao > clientes[cc].razao:
                    tempCliente = clientes[ct]
                    clientes[ct] = clientes[cc]
                    clientes[cc] = tempCliente

        self.listaClientes = clientes
        return clientes

    def buscaRamoAproximado(self, stringDoRamo):
        clientesDoRamo = []

        for clienteAtual in self.listarClientes():
            ramo = str(clienteAtual.ramo)

            if str(stringDoRamo) in str(ramo) and not clienteAtual.filial() and clienteAtual.situacao == "A":
                clientesDoRamo.append(clienteAtual)

        temp = ""
        for ca in range(len(clientesDoRamo)):
            for co in range(ca, len(clientesDoRamo)):

                if clientesDoRamo[ca].cod > clientesDoRamo[co].cod:
                    temp = clientesDoRamo[ca]
                    clientesDoRamo[ca] = clientesDoRamo[co]
                    clientesDoRamo[co] = temp

        for item in clientesDoRamo:
            print(f"{item.cod} - {item.razao} - {item.cnpj}")

        return clientesDoRamo

    def buscaCNPJ(self, CNPJ):
        for temp in self.listaClientes:
            if temp.cnpj == CNPJ:
                return temp

    def buscaPorCod(self, cod):

        for temp in self.listaClientes:
            if str(temp.cod) == cod:
                return temp

    def querryToDF(self, comando):
        import pandas as pd

        cursor = self.__conn.cursor()
        cursor.execute(comando)
        dataFrame = pd.read_sql(comando, self.__conn)

        return dataFrame
