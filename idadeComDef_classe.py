class VerificadorIdade:
    def verificar(self, idade):
        if idade >= 18:
            print("Você pode dirigir")
        else:
            print("Menor de idade")


idade = int(input('Digite sua idade: '))

verificador = VerificadorIdade()
verificador.verificar(idade)

print("Fim do programa")
