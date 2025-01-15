import subprocess

# Listar pacotes desatualizados
outdated = subprocess.check_output(['pip', 'list', '--outdated'], text=True).splitlines()

# Atualizar cada pacote
for line in outdated[2:]:  # Ignorar cabeçalhos
    package = line.split()[0]
    subprocess.run(['pip', 'install', '--upgrade', package])
