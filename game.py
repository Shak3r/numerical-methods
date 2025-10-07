def guess_number():
    print("Загадай число від 1 до 100, а я його відгадаю!")
    print("Відповідай символами: '>' (більше), '<' (менше), '=' (вгадав).")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        attempts += 1
        mid = (low + high) // 2
        print(f"Твоє число {mid}?")
        answer = input("Відповідь: ")

        if answer == "=":
            print(f"Ура! Я вгадав число {mid} за {attempts} спроб(и) 🎉")
            break
        elif answer == ">":
            low = mid + 1
        elif answer == "<":
            high = mid - 1
        else:
            print("Будь ласка, використовуй тільки '>', '<' або '='.")

guess_number()
