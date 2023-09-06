import time

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        self.concluida = True

# Classe para representar a lista de tarefas
class ListaDeTarefas:

    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, qtd):
        for i in range (0, qtd):
            descricao = input("Digite a descrição da tarefa {} : ".format(i+1))
            tarefa = Tarefa(descricao)
            self.tarefas.append(tarefa)
            cont_add =+1
            print("\033[92m\nNova tarefa adicionada a lista!\033[0m")

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            print("\033[92m\nTarefa removida com sucesso!!!\033[0m")
        else:
            print("\033[91m\nNão há tarefa com esse indice!\n\033[0m")

    def marcar_tarefa_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            if self.tarefas[indice].concluida == False:
                self.tarefas[indice].concluir()
                print("\033[92m\nParabéns!!! Essa Tarefa foi concluída!\n\033[0m")
            else:
                print("\033[93m\nEssa tarefa já foi concluída anteriormente!!\033[0m")

        else:
            print("\033[91m\nNão há atividade com esse indice para ser concluída\033[0m")

    def mostrar_tarefas(self):
        if len(self.tarefas) == 0:
            print("\033[93m!!Ainda não há nenhuma tarefa cadastrada!!\033[0m")

        for i, tarefa in enumerate(self.tarefas):
            if tarefa.concluida == False:
                print("{}. \033[91m [Pendente] {}\033[0m".format(i+1, tarefa.descricao))
            elif tarefa.concluida == True:
                print("{}. \033[92m [Pendente] {}\033[0m".format(i+1, tarefa.descricao))

# Função principal do aplicativo
def main():
    lista_de_tarefas = ListaDeTarefas()

    print("\033[93mOlá, seja bem Vindo ao Programa WARSAM PARA controle de atividades!\033[0m")
    time.sleep(1)

    while True:
        print("\n\033[93m===== Aplicativo de Lista de Tarefas =====")

        print("\nEscolha uma das opções abaixo opção: ")

        time.sleep(0.2)
        print("1. Adicionar Tarefa")
        time.sleep(0.2)
        print("2. Remover Tarefa")
        time.sleep(0.2)
        print("3. Marcar Tarefa como Concluída")
        time.sleep(0.2)
        print("4. Mostrar Tarefas")
        time.sleep(0.2)
        print("0. Sair")
        time.sleep(0.2)
        print("="*42+"\033[0m")
        escolha = input(">>>")


        if escolha == "1": # adicionar atividade
            qtd = int(input("quantas atividades você deseja adicionar?"))
            lista_de_tarefas.adicionar_tarefa(qtd)
            lista_de_tarefas.mostrar_tarefas()
            time.sleep(1)


        elif escolha == "2": # remover atividade
            lista_de_tarefas.mostrar_tarefas()
            time.sleep(1)
            indice = int(input("Digite o índice da tarefa a ser removida: ")) - 1
            lista_de_tarefas.remover_tarefa(indice)
            lista_de_tarefas.mostrar_tarefas()
            time.sleep(1)


        elif escolha == "3": # concluir tarefa
            lista_de_tarefas.mostrar_tarefas()
            time.sleep(1)
            indice = int(input("Digite o índice da tarefa concluída: ")) - 1
            lista_de_tarefas.marcar_tarefa_concluida(indice)
            lista_de_tarefas.mostrar_tarefas()
            time.sleep(1)

        elif escolha == "4": # mostrar atividades
            lista_de_tarefas.mostrar_tarefas()
            time.sleep(5)

        elif escolha == "0":
            print("\n\033[93mObrigado por usar os serviços WARSAM para controle de atividade!!\nAté a próxima!!\033[0m")
            time.sleep(1)
            break

        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    main()