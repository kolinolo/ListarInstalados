import subprocess

import re

regular = r'FriendlyName : (\S ?)*[0-9]{14}'


def listar_certificados_expirados():

    certificados = []

    ps_script_path = "C:\\temp\\listaCert.ps1"  # Caminho do script temporário

    with open(ps_script_path, "w") as ps_file:
        ps_file.write(f'''Get-ChildItem -Recurse Cert:''')

    # Executar o script PowerShell
    resultado = subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps_script_path], shell=True, check=True, capture_output=True, text=True)

    padraoNomes = re.compile(regular)
    resultadoNomes = padraoNomes.finditer(resultado.stdout)



    for cert in resultadoNomes:

        if cert.group() == 'FriendlyName : ':
            continue

        else:
            certificados.append(cert.group().replace('FriendlyName : ', ''))

    return certificados


lista = listar_certificados_expirados()

for certificado in lista:
    print(certificado)
print('\n\n', '{} certificados'.format(len(lista)))