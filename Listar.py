import subprocess
import re
import DbLabs

buscaPj = DbLabs.buscaDominio().buscaCNPJ
regular = r'FriendlyName : (\S ?)*[0-9]{14}'


def listar_iteracoes():

    iteracoes = []
    ps_script_path = "C:\\temp\\listaCert.ps1"  # Caminho do script temporário

    with open(ps_script_path, "w") as ps_file:
        ps_file.write(f'''Get-ChildItem -Recurse Cert:''')

    # Executar o script PowerShell
    resultado = subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps_script_path], shell=True, check=True, capture_output=True, text=True)

    padraoNomes = re.compile(regular)
    resultadoNomes = padraoNomes.finditer(resultado.stdout)

    for item in resultado.stdout.split("\n\n"):
        iteracoes.append(item)