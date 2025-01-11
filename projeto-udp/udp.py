import socket


def cabecalho():
    print("\n" * 2)
    print("Olá! Este código faz uma requisição diretamente a uma URL alvo.")
    print("Acessa uma porta, retornando a resposta de uma requisição ao servidor alvo.")
    print("Exemplo: Digite sua URL: www.google.com / Digite a porta: 80")
    print("\n" * 2)


cabecalho()


ip = input("Digite sua URL: ")
porta = input("Digite a porta: ")


try:
    porta = int(porta)
except ValueError:
    print("Erro: A porta deve ser um número inteiro.")
    exit()

try:
   
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    mensagem = "TESTEAAABBBCCC".encode('utf-8')

   
    cliente.sendto(mensagem, (ip, porta))


    data, addr = cliente.recvfrom(4096)

  
    print("Resultado:")
    print(data.decode('utf-8'))

except socket.gaierror:
    print("Erro: URL inválida ou não encontrada. Verifique o endereço e tente novamente.")
except UnicodeDecodeError:
    print("Erro: Não foi possível decodificar os dados recebidos.")
except Exception as MD:
    print(f"Erro inesperado: {MD}")
