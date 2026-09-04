import questionary

# Propriedades: nome, quantidade_horas = 220, valor_hora, cargo

# Quantidade de horas fixas:
# Estag     110
# Demais    220

# Valor hora por cargo:
# Estag         R$ 14,73    => 1621.40
# Junior        R$ 9,10     => 2000
# Pleno         R$ 22,73    => 5000.60
# Senior        R$ 36,37    => 8001.40
# Especialista  R$ 68,19    => 15001.8

# Aumento máximo de 20% e n pode para estag

# PLR:
# Estag         0.40
# Junior        1.0
# Pleno         1.5
# Senior        3.5
# Especialista  5.0
class Funcionario:
    def __init__(self, nome: str, cargo: str):
        self.nome = nome
        self.cargo = cargo

        self.percentual_aumento = 1

        if self.cargo == "Estag":
            self.quantidade_horas = 110
        else:
            self.quantidade_horas = 220

        if self.cargo == "Estag":
            self.valor_hora = 14.74
        elif self.cargo == "Junior":
            self.valor_hora = 9.10
        elif self.cargo == "Pleno":
            self.valor_hora = 22.73
        elif self.cargo == "Senior":
            self.valor_hora = 36.37
        elif self.cargo == "Especialista":
            self.valor_hora = 68.19


    def calcular_salario(self) -> float:
        salario = self.valor_hora * self.quantidade_horas
        aumento = salario * (self.percentual_aumento / 100)
        return salario + aumento

    # Função com retorno do tipo float
    def calcular_plr(self) -> float:
        # Estag         0.40
        # Junior        1.0
        # Pleno         1.5
        # Senior        3.5
        # Especialista  5.0
        if self.cargo == "Estag":
            multiplicador = 0.40
        elif self.cargo == "Junior":
            multiplicador = 1
        elif self.cargo == "Pleno":
            multiplicador = 1.5
        elif self.cargo == "Senior":
            multiplicador = 3.5
        elif self.cargo == "Especialista":
            multiplicador = 5.0

        salario: float = self.calcular_salario()

        plr: float = salario * multiplicador
        return plr

    def conceder_aumento(self, percentual_aumento):
        if self.cargo == "Estag":
            print("Estagiário não pode receber aumento")
            return False

        if percentual_aumento > 20:
            print("Não é possível conceder mais do que 20% de aumento")
            return False

        self.percentual_aumento = percentual_aumento


def exemplo_funcionario():
    cargos = ["Estag", "Junior", "Pleno", "Senior", "Especialista"]

    nome = input("Digite o nome do colaborador: ").strip()

    while len(nome) < 3 or len(nome) > 50:
        print("Nome deve conter no mínimo 3 caracteres e no máximo 50")
        nome = input("Digite o nome do colaborador: ").strip()

    cargo = input("Digite o cargo: ").strip().capitalize()
    # pip install questionary
    # import questionary
    # cargo = questionary.select("Escolha o cargo", choices=cargos).ask()

    while cargo not in cargos:
        print("Cargo inválido")
        cargo = input("Digite o cargo: ").strip().capitalize()

    funcionario: Funcionario = Funcionario(nome, cargo)

    conceder_aumento = input("Deseja conceder aumento para o colaborador: [s/n] ").upper().strip()
    # if conceder_aumento.upper().strip() == "S" or conceder_aumento.upper().strip() == "SIM":
    if conceder_aumento == "S" or conceder_aumento == "SIM":
        percentual_aumento = float(input("Digite o percentual de aumento: "))
        funcionario.conceder_aumento(percentual_aumento)

    print(f"""
Funcionário: {funcionario.nome}
Cargo: {funcionario.cargo}
Quantidade de horas: {funcionario.quantidade_horas}
Valor hora: {funcionario.valor_hora:.2f}
Salário: {funcionario.calcular_salario():.2f}
PLR: {funcionario.calcular_plr():.2f}""")

if __name__ ==  "__main__":
    exemplo_funcionario()
