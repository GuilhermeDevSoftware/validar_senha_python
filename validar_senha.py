import re 

def validar_senha(senha):
    padrao_senha = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    return bool(re.match(padrao_senha, senha))

senhas = ['Senha123', 'senha123', 'Valida22', 'SENHA123']

for s in senhas:
    print(f"A senha {s} é valida: {validar_senha(s)}")