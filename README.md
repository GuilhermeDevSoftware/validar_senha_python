# Validador de Senhas com Regex

Este exercício utiliza expressões regulares em Python para validar senhas com base em critérios específicos.

## Funcionalidade

- Define a função `validar_senha` que recebe uma senha como entrada.
- Utiliza regex para verificar se:
  - Possui ao menos uma letra minúscula.
  - Possui ao menos uma letra maiúscula.
  - Possui ao menos um número.
  - Possui no mínimo 8 caracteres.
- Retorna `True` se a senha for válida, `False` caso contrário.

## Exemplo de uso

```python
senhas = ['Senha123', 'senha123', 'Valida22', 'SENHA123']

for s in senhas:
    print(f"A senha {s} é valida: {validar_senha(s)}")
```

## Saída esperada
```
A senha Senha123 é valida: True  
A senha senha123 é valida: False  
A senha Valida22 é valida: True  
A senha SENHA123 é valida: False
```
## Regex utilizada
```
r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
```
