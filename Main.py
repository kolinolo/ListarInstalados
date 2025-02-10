import subprocess

import re

regular = r'FriendlyName : (\S ?)*[0-9]{14}'


def listar_certificados_expirados():

    certificados = []

    ps_script_path = "C:\\temp\\import_cert.ps1"  # Caminho do script temporário

    with open(ps_script_path, "w") as ps_file:
        ps_file.write(f'''Get-ChildItem -Recurse Cert:''')

    # Executar o script PowerShell
    resultado = subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps_script_path], shell=True, check=True, capture_output=True, text=True)

    padraoNomes = re.compile(regular)
    resultadoNomes = padraoNomes.finditer(resultado.stdout)

    for certificado in resultadoNomes:

        if certificado.group() == 'FriendlyName : ':
            continue

        else:
            certificados.append(certificado.group().replace('FriendlyName : ', ''))

    return certificados


lista = listar_certificados_expirados()

for certificado in lista:
    print(certificado)
print('\n\n', '{} certificados'.format(len(lista)))