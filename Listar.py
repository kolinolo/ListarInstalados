
import subprocess
import OBJcertIntalado
from printTool import colorizar

regular = r'FriendlyName : (\S ?)*[0-9]{14}'


def listar_iteracoes():
    itens = []
    ps_script_path = "C:\\temp\\listaCert.ps1"  # Caminho do script temporário

    with open(ps_script_path, "w") as ps_file:
        ps_file.write(f'''Get-ChildItem -Recurse Cert:''')

    # Executar o script PowerShell
    resultado = subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps_script_path], shell=True,
                               check=True, capture_output=True)

    saida_decodificada: str = resultado.stdout.decode("UTF-8", errors="replace")

    print(colorizar(saida_decodificada,'verde'))

    saida_decodificada = saida_decodificada.replace("\r\n", "\n")

    for iteracao in saida_decodificada.split("\n\n"):

        item = valida_item(iteracao)

        if item is not None:
            itens.append(item)

    return itens


def valida_item(iteracao):

    try:
        obj = OBJcertIntalado.certInstalado(iteracao)

        if obj.cnpj is None: return None

    except:

        return None

    return obj





