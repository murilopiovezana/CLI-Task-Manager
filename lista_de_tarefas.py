import datetime
import os
# tarefa {{{
class tarefa:
    def __init__(self,id,titulo, data, tags, lista_mae, prioridade, repeticao, concluida, nota):
        self.id = int(id)
        self.titulo = titulo
        self.nota = nota
        self.data = data # to_date(data)
        self.tags = tags
        self.lista_mae = int(lista_mae)
        self.prioridade = int(prioridade)
        self.repeticao = int(repeticao)
        self.concluida = concluida #bool(concluida)

    def lista_atributos(self):
        return [self.id, self.titulo, self.data, self.tags , self.lista_mae, self.prioridade, self.repeticao, self.concluida,self.nota]
    def renomear(self, novo_titulo):
        self.titulo = novo_titulo

    # to do: tem um erro na funcao abaixo qnd da sort em algum lugar
    def __lt__(self, other):
        if self.data != None and (other.data == None):
            return False
        elif self.data > other.data:
            return False
        elif self.data == other.data:
            return self.prioridade < other.prioridade
        else:
            return True

    def concluir(self):
        if self.concluida == True:
            print('Esta tarefá já foi concluída. Voltando para o menu.')
            Menu()
        else:
            # to do; apos concluir a tarefa, tem que criar uma nova com a data shiftada pela repeticao dela (semanal, mensal, etc.)
            self.concluida = True
            print('Tarefa concluída!')
            Menu()

    def editar_tarefa(self):
        # to do: isso nao ta muito bom, tem q dar print igual na funcao criar possivelmente
        print('O que deseja editar? Selecione o numero correspondente ao que deseja?')
        print('(1): Titulo \
            (2): Nota \
            (3): Data \
            (4): Tags \
            (5): Prioridade \
            (6): Repeticao \
            (7): Concluida ')


        dic = {1: ['titulo',self.titulo],2: ['nota',self.nota], 3: ['data',self.data], 4: ['tags',self.tags],5: ['prioridade',self.prioridade], 6: ['repeticao',self.repeticao], 7: ['concluida',self.concluida]}

        opcao = int(input())


        print('novo', dic[resposta][0], ':')
        novo = input()
        if resposta == 1:
            for tar in tarefas:
                if tar.titulo == novo:
                    print('ERRO: Ja existe uma tarefa com esse titulo')
                    Menu()

        dic[resposta][1] = resposta

# }}}

class lista:
    def __init__(self,id,nome):
        self.id = int(id)
        self.nome = nome


def to_date(st):
    dat = list(map(int,st.split()))
    try:
        return datetime.date(dat[0], dat[1], dat[2])
    except:
        print("Formato de data errada")
        Menu()

# o seguinte carrega as listas e as tarefas da memoria
# carregar {{{
maximo_id_lista = open(".maximo_id_lista")
maximo_id_lista = int(maximo_id_lista.readline())
arq_maximo_id = open(".maximo_id")
maximo_id = int(arq_maximo_id.readline())
arq_maximo_id.close()

listas = []
arquivo_listas = open(".arquivo_listas")
for linha in arquivo_listas:
    id_ls = int(str(linha))
    nome = ".lista"+str(id_ls)
    if os.path.exists(nome):
        ls = open(nome)
        ls = ls.read()
        listas.append(lista(id_ls, ls))


nome_arquivo_ids = ".arquivo_tarefas"
arquivo_tarefas = open(nome_arquivo_ids)
ids = set()
tarefas = []
novas_tarefas = []
for linha in arquivo_tarefas:
    id_tar = int(str(linha))
    nome = ".tarefa"+str(id_tar)
    if os.path.exists(nome):
        tar = open(nome)
        titulo = tar.readline()
        data = tar.readline().split('-')
        tags = tar.readline().split()
        lista_mae = int(tar.readline())
        prioridade = int(tar.readline())
        repeticao = int(tar.readline())
        concluida = bool(tar.readline())
        nota = tar.read()

        tarefas.append(tarefa(id_tar, titulo, data, tags, lista_mae, prioridade, repeticao, concluida, nota))
arquivo_tarefas.close()
# }}}


# menu {{{
def Menu():
    """ Funcao principal, menu inicial"""
    print('Ola')
    print('O que voce quer fazer?')
    print( '(C): Criar uma nova tarefa ou lista' + '\n'
            '(L): Buscar uma lista de tarefas' + '\n'
            '(B): Buscar uma tarefa'+'\n'
            '(V): Ver tarefas Concluidas'+'\n'
            '(Q): Fechar programa'
    )
    resposta = input()
    if resposta.upper() == 'C':
        criar()
    elif resposta.upper() == 'L':
        buscar_lista()
    elif resposta.upper() == 'B':
        buscar()
    elif resposta.upper() == 'V':
        None
    elif resposta.upper() == 'Q':
        None
    elif resposta.upper() == 'C':
        criar()
# }}}


# arquivar {{{

def arquivar(tar):
    """ funcao q cria um arquivo com nome ".tarefa"+id da tarefa
    que contem 9 linhas que sao, respectivamente, titulo, data, tags, lista_mae, prioridade,  repeticao, Concluida, nota
    colocar linha vazia caso parametro opcional nao informado """
    # to do
    nome_arquivo_ids = ".arquivo_tarefas"
    arquivo_tarefas = open(nome_arquivo_ids, "a")
    arquivo_tarefas.write(str(tar.id))
    arquivo_tarefas.write('\n')
    arquivo_tarefas.close()

    arquivo_ids = open
    nome = ".tarefa"+str(tar.id)
    arquivo = open(nome, "w")
    for par in tar.lista_atributos()[1:]:
        arquivo.write(str(par))
        arquivo.write('\n')

    arquivo.close()
# }}}
# criar {{{
def criar():
    # to do: precisa criar um arquivo em .data, com o formato tarefa+str(id)
    # funcao q cria uma tarefa
    global maximo_id
    global maximo_id_lista

    print('O que deseja criar?')
    print('(T): Tarefa (L): Lista (R): Retornar')
    resposta = input()
    if resposta.upper() == 'T':
        print('digite o titulo do nota:')
        titulo = input()
        for tar in tarefas:
            if tar.titulo == titulo:
                print('ERRO: Ja existe uma tarefa com esse titulo')

        print('Por favor, informe a data no formato YY MM DD')
        try:
            dat = input()
            dat = to_date(dat)
        except:
            print('Formato Invalido')
            Menu()

        print('Agora Selecione a lista mae')
        lista_mae = buscar_lista()

        print('Digite a prioridade que deseja colocar nesta tarefa, dentre as opções:')
        print('(0): Sem prioridade -- (1):Baixa -- (2): Media -- (3): Alta.')
        prioridade = int(input())
        if prioridade not in range(4):
            print('ERRO: Valor invalido')
            Menu()


        print('Digite a frequência com que a tarefa deve se repetir.')
        print('(0): Nenhuma -- (1): Diaria -- (2): Semanal -- (3): Mensal -- (4): Anual')
        frequencia = int(input())
        if int(frequencia) not in range(5):
            print('ERRO: Valor invalido')
            Menu()

        # to do, permitir mais tags
        tags = []

        print('Digite o estado atual de conclusão da tarefa. ')
        print('(0): Nao concluida -- (1): Concluida')
        concluida = int(input())
        if concluida not in range(2):
            print('ERRO: Valor invalido')
            Menu()
        if concluida == 0:
            concluida = False
        else:
            concluida = True

        print('Informe uma nota(opcional):')
        nota = input()

        tare = tarefa(maximo_id,titulo, dat, tags, lista_mae, prioridade, frequencia, concluida, nota)
        maximo_id += 1
        arq_maximo_id = open(".maximo_id", "w")
        arq_maximo_id.write(str(maximo_id))
        arq_maximo_id.close()

        tarefas.append(tare)
        arquivar(tare)

    elif resposta.upper() == 'L':
        print('Informe o nome da lista:')
        nome = input()
        for ls in listas:
            if ls.nome == nome:
                print('ERRO: Ja existe uma lista com esse nome')
                Menu()
        ls = lista(maximo_id_lista, nome)
        listas.append(ls)
        maximo_id_lista += 1

        arq_maximo_id_lista = open(".maximo_id_lista", "w")
        arq_maximo_id_lista.write(str(maximo_id_lista))
        arq_maximo_id_lista.close()
        Menu()
    elif resposta.upper() == 'R':
        Menu()
    else:
        print('ERRO: Resposta Invalida')
        criar()
# }}}
def diff(data):
    # to do
    """ retorna a diferenca entre hoje e a data informada"""
    return 0
# buscar_tarefa {{{

def buscar_tarefa():
    # busca uma tarefa da lista tarefas
    # filtro {{{
    print('Deseja Filtrar as tarefas por algum parametro')
    print('(S): Sim --- (N): Nao')
    resposta = input().lower()

    tag, so_ate_hoje, so_ate_semana, apenas_tarefas_concluidas = 0, False, False, False
    if resposta == 's':
        print('deseja filtar por tag?')
        print('(S): Sim --- (N): Nao')
        resposta = input.lower()
        if resposta == 's':
            tag = buscar_tag()

        print('deseja incluir apenas tarefas com datas ate hoje?')
        print('(S): Sim --- (N): Nao')
        resposta = input.lower()
        if resposta == 's':
            so_ate_hoje = True

        elif resposta == 'n':
            print('deseja incluir apenas tarefas com datas ate hoje?')
            print('(S): Sim --- (N): Nao')
            resposta = input.lower()
            if resposta == 's':
                so_ate_semana = True


        print('deseja buscar apenas por tarefas concluidas?')
        resposta = input().lower()
        if resposta == 's':
            apenas_tarefas_concluidas = True
        elif resposta == 'n':
            None
        else:
            erro()
    # }}}
    print('Buscar:')
    texto = input()
    tarefas_com_match = list()
    # procure tarefas {{{
    for tar in tarefas:
        match = False
        if so_ate_hoje and (diff(tar.date) > 0):
            continue
        if so_ate_semana and (diff(tar.date) > 7):
            continue
        if apenas_tarefas_concluidas and (tar.concluida == False):
            continue
        if tag != 0 and (tar.tag != tag):
            continue

        for parametro in [tar.titulo, tar.nota]:
            if texto in parametro:
                match = True
                break
        if match:
            tarefas_com_match.append(tar)
    # }}}
    if len(tarefas_com_match) == 0:
        print('ERRO: Nenhuma tarefa com esse nome foi encontrado, voce sera redirecionado para o menu principal')
        Menu()
    else:
        print('Foram Encontradas', len(tarefas_com_match),'com esse texto')
        tarefas_com_match.sort()
        for tar in tarefas_com_match:
            print(str(tar.id)+':'+tar.titulo)

        print('digite o id da tarefa para selecionar')
        id_input = int(input())

        encontrado = False
        for tar in tarefas_com_match:
            if tar.id == id_input:
                encontrado = True
                return tar
        if not encontrado:
            print('ERRO: id nao esta na lista')
            print('Voce sera redirecionadoencontrado para o menu principal')

# }}}

# deletar {{{
def deletar_tarefa(tar):
    id_tar = tar.id
    os.remove('.tarefa'+str(id_tar))
    tarefas.remove(tar)
def deletar_lista(ls):
    lista = ls.lista
    id_lista = ls.id
    for tar in tarefas:
        if tar.lista_mae == id_lista:
            deletar_tarefa(tar)
    os.remove(tarefa+str(id_lista))
    listas.remove(ls)

# }}}

# selecionar {{{
def selecionar_lista():
    """ seleciona uma lista e escolhe netre deletar a lista ou renomear ou outras coisas do readme """

    ls = buscar_lista()
    # to do: escolher o q fazer com a lista(deleta-la, renomea-la, etc.)

def selecionar_tarefa():

    tar = buscar_tarefa()
    print(tar.lista_atributos())
    print('Tarefa Selecionada:')
    print('id:', tar.id)
    print('nome:', tar.titulo)
    print('data:', tar.data)
    print('tags:', tar.tags)
    print('lista_mae:', tar.lista_mae)
    print('prioridade:', tar.prioridade)
    print('repeticao:', tar.repeticao)
    print('-----------------------------')
    print('O que deseja fazer com essa tarefa?')
    print('(D): Deletar')
    print('(E): Editar')
    print('(M): Marcar como concluida')

    resposta = input().lower()
    if resposta == 'd':
        deletar_tarefa(tar)
    elif resposta == 'e':
        tar.editar()
    elif resposta == 'm':
        tar.concluir()

# }}}
# buscar_lista {{{
def buscar_lista():
    print('Buscar:')
    texto = input()
    lista_com_match = list()
    # procure tarefas {{{
    for ls in listas:
        if texto in ls.nome:
            lista_com_match.append(ls)
    # }}}
    if len(lista_com_match) == 0:
        print('ERRO: Nenhuma lista com esse nome foi encontrado, voce sera redirecionado para o menu principal')
        Menu()
    else:
        print('Foram Encontradas', len(lista_com_match),'com esse texto')
        for ls in lista_com_match:
            print(str(ls.id)+':'+ls.nome)

        print('digite o id da lista para selecionar')
        id_input = int(input())

        encontrado = False
        for ls in lista_com_match:
            if ls.id == id_input:
                encontrado = True
                return ls.id
        if not encontrado:
            print('ERRO: id nao esta nao encontrado')
            print('Voce sera redirecionadoencontrado para o menu principal')

# }}}
# buscar {{{
def buscar():
    #  busca algo
    print('O que deseja buscar?')
    print('(L): Lista -- (T): Tarefa')
    print('(R): Retorna ao menu principal')
    resposta = input()
    if resposta.lower() == 'l':
        selecionar_lista()
    elif resposta.lower() == 't':
        selecionar_tarefa()
    else:
        print('ERRO[Opcao Invalida]: Por favor, tente novamente')
        buscar()
# }}}
Menu()
# vim: fdm=marker
