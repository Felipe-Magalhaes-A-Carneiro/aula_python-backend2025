from pathlib import Path

print(Path.cwd())

caminho = Path('/aula_python-backend2025')
# ou, no nosso caso, pode fazer:
# caminho = Path(Path.cwd())

# mostrar / interar os arquivos na pasta mencionada
arquivos = caminho.iterdir()

for arquivo in arquivos:
    print(arquivo)