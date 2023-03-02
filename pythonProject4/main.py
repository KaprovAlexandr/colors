slovo = input("Введите слово: ")
for i in range(len(slovo)):
    if slovo[i] == "ф" or slovo[i] == "Ф":
        print("Ого! Это редкое слово!")
        break
    else:
        print("Эх, это не очень редкое слово...")
        break