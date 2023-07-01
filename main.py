if __name__ == "__main__":
    while True:

        questinon = input("1 - з'єднює три числа, 2 - множить 4 числа, 3 - переводить метри у сантиметри, дециметри, міліметри та милі, 4 - шукає площу трикутника за стороною і висотою 5 - перевертає число  ")

        if questinon == "1":
            a = input("Введіть перше значення")
            b = input("Введіть друге значення")
            c = input("Введіть третє значення")
            print(a+b+c)

        elif questinon == "2":
            try:
                a = int(input("Введіть перше число"))
                b = int(input("введіть друге число "))
                c = int(input("Введіть третє число"))
                d = int(input("Введіть четверте число"))
                print(a*b*c*d)
            except ValueError:
                print("Вводити можна лише цифри та числа, спробуйте ще раз ")

        elif questinon == "3":
            try:
                metres = int(input("Введіть кількість метрів"))
                if metres < 0:
                    print("метри не можуть бути від'ємним значенням, введіть ще раз")
                    pass

                if metres == 0:
                    print("значення не може дрівнювати нулю, введіть ще раз")
                    pass

                centimetre = metres * 100
                decimetre = metres * 10
                miles = metres * 0.00062137119609836
                miles = round(miles, 3)
                milimetres = metres * 1000
                print("отож,", metres, "метрів - це є", centimetre, "сантиметрів", decimetre, "дециметрів", milimetres, "міліметрів", miles, "миль")

            except ValueError:
                print("Вводити можна лише цифри та числа, спробуйте ще раз ")



        elif questinon == "4":
            try:
                side_a = int(input("Введіть довжину сторони а"))
                height_a = int(input("введіть довжину висоти від сторони а "))
                print(0.5*side_a*height_a)
            except ValueError:
                print("Вводити можна лише цифри ")


        elif questinon == "5":
            try:
                number = int(input("Введіть число: "))
                reversed_number = 0

                while number > 0:
                    remainder = number % 10
                    reversed_number = (reversed_number * 10) + remainder
                    number = number // 10

                print("Результат:", reversed_number)

            except ValueError:
                print("Вводити можна лише цифри ")

        else:
            print("Введіть правильну цифру")
            pass