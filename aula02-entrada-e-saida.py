nome = 'Guilherme'
idade = 27
altura = 1.81
#tipo_nome = type(nome)
#tipo_idade = type(idade)
#tipo_altura = type(altura)

print(nome, 'tem', idade, 'anos', 'e mede', altura)
print(nome + ' tem ' + str(idade) + ' anos' + ' e mede ' + str(altura))


nome = input('Escreva seu nome:')
idade = input('Escreva sua idade:')
altura = input('Escreva sua altura:')

print(nome, 'tem', idade, 'anos', 'e mede', altura)
print(type(nome), type(idade), type(altura))

