def pattern3():
    n = 10
    for i in range(n):
        number = 1
        # Adiciona espaços para alinhar a saída
        print(" " * ((n - i) * 2), end="")
        for j in range(i + 1):
            # Exibe o número com alinhamento de 4 espaços
            print(f"{number:4}", end="")
            number = number * (i - j) // (j + 1)
        print()  # Nova linha ao final de cada iteração externa

if __name__ == "__main__":
    pattern3()
    input()
