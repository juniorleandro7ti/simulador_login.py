USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

print("Simulador de Login")

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
    print("Login bem-sucedido! ✅")
else:
    print("Usuário ou senha incorretos. ❌")
