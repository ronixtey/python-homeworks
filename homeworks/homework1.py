while True:
    x = input("Сколько вам лет: ");
    try:
        x = int(x);
        if x >= 0 and x < 18:
            print("Вы юноша");
        elif x >= 18 and x < 45:
            print("Вы молодой");
        elif x >= 45 and x < 60:
            print("Вы среднего возраста");
        elif x <= 60 and x > 90:
            print("Вы старец");
        else:
            print("Вы долгожитель");
        break;
    except ValueError:
        print("Введите число!");
