# Projeto Exemplo: Calculadora de Média do Aluno
from abc import ABC, abstractmethod
import builtins


class print(ABC):
    @abstractmethod
    def format(self, message):
        """Converte a mensagem para um formato adequado para exibição."""
        pass

    @abstractmethod
    def show(self, message):
        """Exibe a mensagem ao usuário."""
        pass


class ConsolePrint(print):
    def format(self, message):
        return str(message)

    def show(self, message):
        builtins.print(self.format(message))


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


printer = ConsolePrint()
builtins.print("=== Sistema de Notas do Aluno ===")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = calcular_media(n1, n2)

printer.show(f"A média final é: {media:.2f}")

if media >= 7.0:
    printer.show("Status: APROVADO!")
else:
    printer.show("Status: REPROVADO.")