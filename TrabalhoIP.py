numAulas = []
materia = 'G'
professor = 'H'
carga_horaria = 1.00
confirmDisciplina = int(0)
turma = []
Substitui = 'on'
confirmTurma = 0
dadosAlunos = []
Alunos = 0
estudante = 'u'
media = 0.00
frequencia = 0.00
aprovado = []
reprovadoFalta = []
reprovadoNota = []
dicioNota1 = {}
dicioNota2 = {}
dicioMedia = {}
dicioAulAs = {}
dicioFreq = {}

# Funcoes da area disciplina.

def disciplina():
    confirmDisciplina = 0
    while confirmDisciplina == 0:
        print('Informe os dados da disciplina: ')
        materia = input('Matéria: ')
        professor = input('Professor(a): ')
        carga_horaria = int(input('Número de aulas: '))
        numAulas.append(carga_horaria)
        print(f'Deseja prosseguir com a alteração?\n Matéria: {materia}\n Professor(a): {professor}\n Número de aulas: {carga_horaria} horas\n Digite 1 para confirmar as alterações ou qualquer número para refazer as alterações.')
        confirmVolta = int(input())
        if confirmVolta == 1:
            print('Alterações Salvas')
            break

# funcoes da area Turma

def classe():
    confirmTurma = 0
    while confirmTurma == 0:
        print('Escreva o nome do aluno para adicionar na turma ou digite:\n1 para excluir alunos\n2 para substituir alunos\n3 para voltar ao início\n')
        print(turma)
        aluno = input()
        turma.append(aluno)
        if aluno == '1':
            turma.remove('1')
            exclui()
        if aluno == '2':
            turma.remove('2')
            substitui()
        if aluno == '3':
            turma.remove('3')
            break

# Exclusão de alunos

def exclui():
    confirmExclui = 0
    while confirmExclui == 0:
        print(turma)
        alunoExcluido = input('Escreva o nome do aluno para excluir ou digite 1 para sair: ')
        if alunoExcluido == '1':
            confirmExclui = 1
            break
        if alunoExcluido not in turma:
            print('Esse aluno não está na turma')
        if alunoExcluido in turma:
            turma.remove(alunoExcluido)
            print(turma)
        if alunoExcluido in aprovado:
            aprovado.remove(alunoExcluido)
        if alunoExcluido in reprovadoFalta:
            reprovadoFalta.remove(alunoExcluido)
        if alunoExcluido in reprovadoNota:
            reprovadoNota.remove(alunoExcluido)

# Substituicao de aluno

def substitui():
    Substitui = 0
    while Substitui == 0:
        tamanhoTurma = len(turma)
        for contador in range(tamanhoTurma):
            print(f'{contador}) {turma[contador]}\n')
        alunoSubstituido = int(input('Digite o índice do aluno que deseja substituir ou -1 para sair: '))
        if alunoSubstituido == -1:
            break
        if alunoSubstituido > contador:
            print('Digite um índice existente')
            continue
        alunoUrsupador = input('Digite o nome do aluno para efetuar a substituição: ')
        turma[alunoSubstituido] = alunoUrsupador

# funcoes da area aluno

def alunos():
    while Alunos == 0:
        print(turma)
        estudante = input('Selecione um aluno dentro da turma para adicionar suas notas e frequência ou digite 1 para sair.\n')
        if estudante == '1':
            break
        if estudante not in turma:
            print('Esse estudante não está na turma.')
            continue
        if estudante in turma:
            nota1 = float(input('Insira a nota da primeira unidade: '))
            nota2 = float(input('Insira a nota da segunda unidade: '))
            aulasAssistidas = int(input('Insira o número de aulas frequentadas: '))
            media = (nota1 + nota2) / 2
            frequencia = 100 * aulasAssistidas / numAulas[-1]

            dicioNota1[estudante] = nota1
            dicioNota2[estudante] = nota2
            dicioMedia[estudante] = media
            dicioAulAs[estudante] = aulasAssistidas
            dicioFreq[estudante] = frequencia

            if media >= 7.00 and frequencia >= 75:
                aprovado.append(estudante)
            if media < 7.00:
                reprovadoNota.append(estudante)
            if frequencia < 75:
                reprovadoFalta.append(estudante)

# funcoes da area relatorio

def relatorio():
    relatorios = 0
    while relatorios == 0:
        print(f'Digite um número para gerar um relatório: \n1) Geral\n2) Só dos aprovados\n3) Só dos reprovados por falta\n4) Só dos reprovados por nota\nQualquer outro número para sair\n')
        numero = int(input())

        if numero == 1:
            aprovados()
            reprovadoF()
            reprovadoN()
        if numero == 2:
            aprovados()
        if numero == 3:
            reprovadoF()
        if numero == 4:
            reprovadoN()
        if numero < 1 or numero > 4:
            break
        pedirDnovo = input('Digite 1 para pedir outro relatório ou qualquer outro número para sair.')
        if pedirDnovo != '1':
            break

# relatorio aprovados

def aprovados():
    print('Alunos aprovados')
    print()
    tamanhoAprovados = len(aprovado)
    for contador in range(tamanhoAprovados):
        print(aprovado[contador])
        print('Nota 1: ', dicioNota1.get(aprovado[contador]))
        print('Nota 2: ', dicioNota2.get(aprovado[contador]))
        print('Média: ', dicioMedia.get(aprovado[contador]))
        print('Aulas assistidas: ', dicioAulAs.get(aprovado[contador]))
        print('Frequência: ', dicioFreq.get(aprovado[contador], '%'))

# relatorio reprovados por falta

def reprovadoF():
    print('Alunos reprovados por falta')
    print()
    tamanhoReprovadoFalta = len(reprovadoFalta)
    for contador in range(tamanhoReprovadoFalta):
        print(reprovadoFalta[contador])
        print('Nota 1: ', dicioNota1.get(reprovadoFalta[contador]))
        print('Nota 2: ', dicioNota2.get(reprovadoFalta[contador]))
        print('Média: ', dicioMedia.get(reprovadoFalta[contador]))
        print('Aulas assistidas: ', dicioAulAs.get(reprovadoFalta[contador]))
        print('Frequência: ', dicioFreq.get(reprovadoFalta[contador], '%'))

# relatorio reprovados por nota

def reprovadoN():
    print('Alunos reprovados por nota')
    print()
    tamanhoReprovadoNota = len(reprovadoNota)
    for contador in range(tamanhoReprovadoNota):
        print(reprovadoNota[contador])
        print('Nota 1: ', dicioNota1.get(reprovadoNota[contador]))
        print('Nota 2: ', dicioNota2.get(reprovadoNota[contador]))
        print('Média: ', dicioMedia.get(reprovadoNota[contador]))
        print('Aulas assistidas: ', dicioAulAs.get(reprovadoNota[contador]))
        print('Frequência: ', dicioFreq.get(reprovadoNota[contador], '%'))

# funcoes da parte entrada

def entrada():
    entrada = 0
    while entrada == 0:
        print(f'Sistema Academico\n \nDigite um número para usufruir de suas funções\n1) Informações da disciplina \n2) Gerenciamento de turma \n3) Lançamento de notas \n4) Impressão de relatório \nDigite qualquer outro número para sair.')
        funcao = int(input())
        if funcao == 1:
            disciplina()
        if funcao == 2:
            classe()
        if funcao == 3:
            alunos()
        if funcao == 4:
            relatorio()
        if funcao < 1 or funcao > 4:
            break

entrada()
