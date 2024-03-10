import os, sys

# Verificando parometros
if len(sys.argv) < 2:
    print(f'Uso: {sys.argv[0]} arquivo.zip password.txt')
    sys.exit(1)

# Verificando se tem pyzipper
try:
    import pyzipper
except Exception:
    print('Instalando pyzipper')
    os.system('python3 -m pip install pyzipper')
    print('Inicie novamente')

# Variaveis
arquivo = sys.argv[1]
senhas = sys.argv[2]

# Check
if not os.path.isfile(arquivo):
    print('Coloque um arquivo ZIP valido!')
    exit()
elif not os.path.isfile(senhas):
    print('Coloque um arquivo de Senhas valido!')
    exit()
    
# COdigo
senhas_armazenadas = open(senhas).read().split('\n')
for password in senhas_armazenadas:
    with pyzipper.AESZipFile(arquivo, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
        try:
            extracted_zip.extractall(pwd=str.encode(password))
            
            os.system('clear')
            print(f'Senha: {password}')
            
        except RuntimeError:
            print(f'Senha Incorreta! -> {password}')