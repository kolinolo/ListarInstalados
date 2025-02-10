from .AchaPasta import PastaCod


class Cliente:
    def __init__(self, razao, cod, nomeFatasia, cnpj, ramo, dataInicio, situacao, enderecoEmp, responsavelEmp):
        self.razao = razao
        self.cod = cod
        self.nomeFantasia = nomeFatasia
        self.cnpj = cnpj
        self.ramo = ramo
        self.dataEntrada = dataInicio
        self.ativa = situacao == "A"
        self.enderecoEmp = enderecoEmp
        self.responsavel = responsavelEmp
        self.pastaCliente = PastaCod(self.cod)
        self.toList = [cod, razao, cnpj, nomeFatasia, situacao, enderecoEmp, responsavelEmp]



    def filial(self):
        if self.cnpj is None: return False
        return "0001" not in self.cnpj




class responsavel:

    def __init__(self, nome, cpf, enderecoResp):
        self.nome = nome
        self.cpf = cpf
        self.endereco = enderecoResp


class endereco:

    def __init__(self, cep, bairro, logradouro, numero, codMunicipio, estado, municipio):
        self.cep = cep
        self.endereco = endereco
        self.bairro = bairro
        self.logradouro = logradouro
        self.numero = numero
        self.codMunicipio = codMunicipio
        self.estado = estado
        self.municipio = municipio
