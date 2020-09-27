T = int(input()) # casos de testes

for i in range(T):
    N = int(input()) # numero de estudantes da turma ?
    if (0 <= N <=100):  # minimo 0 maximo 100 estudantes (só cabe 100 alunos)
        nome = [] # lista com os nomes dos alunos
        freq = [] # lista com a frequencia do respectivo aluno i
        for i in range(N): # cadastrar informação do estudante i até N
            _nome = input() # variavel nome (auxiliar)
            if len(_nome) < 100 and _nome.isalpha(): # só aceita para cada nome de estudante 100 caractere e A a Z 
                nome.append(_nome)
            else:
                print("deu ruim, teu nome nao eh com numero nem é gigante")
                break
            _freq = input() # cadastrar frequencia
            for i in range(len(freq)) # nao entendi aqui sou eu quem escolho a quantidade de frequencia? é aleatório

    else:
        print("numero de estudantes invalido tente de novo")
print(nome)