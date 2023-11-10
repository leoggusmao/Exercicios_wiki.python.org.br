#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('/'))

        if day < 1 or month < 1 or year < 1:
            return False

        if month > 12:
            return False

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Verificar ano bissexto (divisível por 4, exceto quando é divisível por 100 e não por 400)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29

        if day > days_in_month[month - 1]:
            return False

        return True

    except ValueError:
        return False

def main():
    while True:
        date_input = input("Digite uma data no formato dd/mm/aaaa (ou 'sair' para encerrar): ")

        if date_input.lower() == 'sair':
            break

        if is_valid_date(date_input):
            print("Data válida!")
        else:
            print("Data inválida!")

if __name__ == "__main__":
    main()