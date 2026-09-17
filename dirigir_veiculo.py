class dirigir_veiculo:
    def verificar(self, idade, carteira):
        if idade >= 18 and carteira:
            print("Você pode dirigir")
        else:
            print("Você não pode dirigir e/ou é menor de idade.")

idade = int(input("Digite sua idade\n"))
resposta = input("Você possui carteira de motorista? (sim/não)\n").strip().lower()
carteira = resposta == "sim"

verificador = dirigir_veiculo()
verificador.verificar(idade, carteira)
