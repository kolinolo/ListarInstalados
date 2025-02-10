import os


def PastaCod(cod):

    naturezas = ["Simples Nacional", "Lucro Real", "lucro Presumido"]

    for natureza in naturezas:
        for pasta in os.listdir(fr"\\servidor\Ethos\SERVIDOR\{natureza}\Clientes ativos"):
            try:
                codPasta = pasta.split(" - ")[-1]

                if int(codPasta) == cod:
                    return fr"\\servidor\Ethos\SERVIDOR\{natureza}\Clientes ativos\{pasta}"

            except ValueError:
                continue

