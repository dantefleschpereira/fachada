
'''
Facade é um padrão de projeto estrutural que fornece uma interface simplificada para um 
conjunto complexo de classes, bibliotecas ou subsistemas. 
Ele atua como uma fachada (daí o nome) que oculta a complexidade subjacente e fornece uma 
interface mais simples e unificada para ser usada pelos clientes.

O padrão de projeto Fachada é implementado por meio da criação de uma classe que atua como 
uma fachada para um conjunto de classes ou subsistemas. Essa classe possui métodos públicos 
que encapsulam a funcionalidade dessas classes ou subsistemas subjacentes, ocultando assim 
sua complexidade do cliente.

A ideia por trás do padrão Fachada é fornecer uma interface de alto nível que seja mais fácil
de usar e entender, evitando que os clientes tenham que lidar diretamente com a complexidade
interna do sistema. Ele simplifica o uso do sistema, fornecendo uma camada adicional de abstração.
'''

class SubsistemaA:
    def metodo_a(self):
        print("Método A do SubsistemaA")

class SubsistemaB:
    def metodo_b(self):
        print("Método B do SubsistemaB")

class Fachada:
    def __init__(self):
        self.subsistema_a = SubsistemaA()
        self.subsistema_b = SubsistemaB()

    def operacao_simples(self):
        print("Operação simples da Fachada")
        self.subsistema_a.metodo_a()
        self.subsistema_b.metodo_b()

# Uso da fachada
fachada = Fachada()
fachada.operacao_simples()

