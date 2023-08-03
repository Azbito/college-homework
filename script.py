def bmi_calculation(weight, height):
    bmi = weight / height ** 2
    return bmi

def bmi_output(bmi):
    if bmi <= 18.5:
        return "Abaixo do peso"
    elif bmi <= 24.9:
        return "Peso normal"
    elif bmi <= 29.9:
        return "Sobrepeso"
    elif bmi <= 34.9:
        return "Obesidade grau 1"
    elif bmi <= 39.9:
        return "Obesidade grau 2"
    else: return "Obesidade grau 3"

def main():
    try:
        weight = float(input("Digite o peso em kg: "))
        height = float(input("Digite a altura em metros: "))

        bmi = bmi_calculation(weight, height)
        bmi_category = bmi_output(bmi)

        print(f"Seu IMC é {bmi:.2f}")
        print(f"Categoria: {bmi_category}")
        input("Pressione Enter para sair...")

    except ValueError:
        print("Erro: Certifique-se de que digitou um valor válido.")

if __name__ == "__main__":
    main()