import classes

kozelnytska = classes.Street("Козельницька")
kozelnytska.set_description("Сонячна вулиця переповнена щасливими студентами.")

stryiska = classes.Street("Стрийська")
stryiska.set_description("Людна вулиця, що веде до 'Ашану'.")

franko = classes.Street("І.Франка")
franko.set_description("Вулиця з цікавими магазинчиками.")

krakivska = classes.Street("Краківська")
krakivska.set_description("Поблизу знаходиться 'Краківський базар', щось Вам точно впаде в око.")

stryiska.link_street(kozelnytska, "південь")
stryiska.link_street(krakivska, "захід")
krakivska.link_street(stryiska, "схід")
krakivska.link_street(franko, "північ")
franko.link_street(krakivska, "південь")
franko.link_street(kozelnytska, "схід")
kozelnytska.link_street(franko, "захід")
kozelnytska.link_street(stryiska, "північ")

lotr = classes.Enemy("Лотр", "Негідник, розбійник, грабіжник. Фацет")
lotr.set_conversation("Щось тут занадто тихо...")
lotr.set_weakness("телефон")
stryiska.set_character(lotr)

kavaler = classes.Friend("Кавалер", "Чоловік, який розважає жінку в товаристві, супроводить її під час прогулянки")
kavaler.set_conversation("Завжди радий допомогти панні.")
kozelnytska.set_character(kavaler)


zbuj = classes.Enemy("Збуй", "Розбійник, грабіжник.")
zbuj.set_conversation("Гуляєш на самоті?")
zbuj.set_weakness("ліхтарик")
franko.set_character(zbuj)

batiar = classes.Friend("Батяр", "гульвіса, п'яничка, популярний у жінок брутальний чоловік кінця 19-початку 20 століття")
batiar.set_conversation("Чи не хочете заскочити до шинку?")
krakivska.set_character(batiar)

laidak = classes.Unique("Лайдак", "Вбога бездомна людина")
laidak.set_conversation("Кожен день однаковий...")
laidak.set_weakness("магічна зброя")
laidak.set_info("Цей ворог найсильніший з усіх.\nЩоб перемогти його потрібно мати магічну зброю")
krakivska.set_character(laidak)

phone = classes.Secure("телефон")
phone.set_description("З допомогою нього можна викликати поліцію")
krakivska.set_item(phone)

torch = classes.Secure("ліхтарик")
torch.set_description("Грабіжники остерігаються освітлених місць.")
kozelnytska.set_item(torch)

cake = classes.Food("тістечко")
cake.set_description("Усі люблять тістечка.")
franko.set_item(cake)

magic = classes.Secure("магічна зброя")
magic.set_description("Допоможе здолати боса.")
stryiska.set_item(magic)

current_street = kozelnytska
shield = {}
points = []
command_list = ["взяти", "пригостити", "захищатися", "поговорити"]

dead = False

while dead == False:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    print(command_list)
    command = input("> ")

    if command in ["північ", "південь", "схід", "захід"]:

        current_street = current_street.move(command)
    elif command == "поговорити":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "захищатися":
        if isinstance(inhabitant, classes.Enemy):
            if isinstance(inhabitant, classes.Unique):
                inhabitant.get_info()
                print("Чим будете захищатися?")
                defend_with = input()
                boss = inhabitant

                if defend_with == "магічна зброя":
                    print("Ви перемогли боса!")
                    points.append(boss.name)
                    print("Вітаємо Ви пройшли гру!")
                    print(f"Ваші переможені вороги: {points}")
                    dead = True
                else:
                    print("Вас переміг грабіжник.")
                    print("Кінець гри")
                    dead = True
            
            else:
                print("Чим будете захищатися?")
                print(list(shield.keys()))
                defend_with = input()

                if defend_with in shield:
                    if inhabitant.defend(defend_with) == True:
                        points.append(inhabitant.name)
                        print("Ви перемогли грабіжника!")
                        current_street.character = None
                    else:
                        print("Вас переміг грабіжник.")
                        print("Кінець гри")
                        dead = True
                else:
                    print("У вас немає " + defend_with)
        else:
            print("Немає від кого захищатися")
    
    elif command == "пригостити":
        print("Чим пригостити?")
        defend_with = input()
        if inhabitant is not None:
            if defend_with in shield.keys():
                if shield[defend_with].__class__.__name__ == "Food":
                    print("Інша людина вдячна за гостинець")
                else:
                    print("Можна пригостити лише їжею")
            else:
                print("У вас немає " + defend_with)

    elif command == "взяти":
        if item is not None:
            print(item.get_name() + " тепер у вашому інвентарі")
            shield[item.get_name()] = item
            current_street.set_item(None)
        else:
            print("Немає чого брати!")
    else:
        print("Неправильна команда")
