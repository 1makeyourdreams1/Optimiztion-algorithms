class Salon:
    def __init__(self):
        self.staff = Staff()
        self.service = Service()

    def create_master(self):
        master = Master(self.staff.admins)
        self.staff.add_master(master)
        master.get_supervisor().add_sub(master)

    def create_admin(self):
        admin = Admin(self.staff.owners)
        self.staff.add_admin(admin)
        admin.get_supervisor().add_sub(admin)

    def create_owner(self):
        owner = Owner()
        self.staff.add_owner(owner)

    def create_haircut(self):
        hc = Haircut()
        self.service.add_haircut(hc)

    def create_coloring(self):
        cl = Coloring()
        self.service.add_coloring(cl)

    def output(self):
        print("Мастера: ")
        for o in self.staff.masters:
            print(f"    {o.get_name()} {o.get_surname()}")
        print("Администраторы: ")
        for o in self.staff.admins:
            print(f"    {o.get_name()} {o.get_surname()}", end="")
            if len(o.get_subs()) != 0:
                print(" Подчиненные:", [f"{s.get_name()} {s.get_surname()}" for s in o.get_subs()])
            print()
        print("Владельцы:")
        for o in self.staff.owners:
            print(f"    {o.get_name()} {o.get_surname()}", end="")
            if len(o.get_subs()) != 0:
                print(" Подчиненные:", [f"{s.get_name()} {s.get_surname()}" for s in o.get_subs()])
            print()
        print("Услуги: ")
        print("    Стрижки: ", [f"{o.get_name()}" for o in self.service.get_haircuts()])
        print("    Окрашивание: ", [f"{o.get_name()}" for o in self.service.get_coloring()])

    def query1(self, salary):
        print(f"\nПоиск сотрудников с зарплатой большей {salary}:")
        found = False
        all_staff = self.staff.masters + self.staff.admins + self.staff.owners
        for person in all_staff:
            if person.get_salary() and float(person.get_salary()) >= float(salary):
                print(f"Имя: {person.get_name()}, Фамилия: {person.get_surname()}, Класс: {person.__class__.__name__}")
                found = True
        if not found:
            print("Сотрудники с такой зарплатой не найдены.")

    def query2(self, name):
        print(f"\nПоиск сотрудников по имени {name}:")
        found = False
        all_staff = self.staff.masters + self.staff.admins + self.staff.owners
        for person in all_staff:
            if person.get_name() == name:
                print(f"Имя: {person.get_name()}, Фамилия: {person.get_surname()}, Класс: {person.__class__.__name__}")
                found = True
        if not found:
            print("Сотрудники с таким именем не найдены.")

    def query3(self, age, class_name):
        print(f"\nПоиск сотрудников класса {class_name.__name__} с возрастом {age}:")
        found = False
        class_list = []
        if class_name == Master:
            class_list = self.staff.masters
        elif class_name == Admin:
            class_list = self.staff.admins
        elif class_name == Owner:
            class_list = self.staff.owners
        for person in class_list:
            if person.get_age() == age:
                print(f"Имя: {person.get_name()}, Фамилия: {person.get_surname()}, Возраст: {person.get_age()}")
                found = True
        if not found:
            print(f"Сотрудники класса {class_name.__name__} с таким возрастом не найдены.")


class Staff:
    def __init__(self):
        super().__init__()
        self.masters = []
        self.admins = []
        self.owners = []
        self.age = None
        self.name = None
        self.gender = None
        self.surname = None
        self.grade = None
        self.salary = None

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def add_master(self, master):
        self.masters.append(master)


    def add_admin(self, admin):
        self.admins.append(admin)


    def add_owner(self, owner):
        self.owners.append(owner)


class Master(Staff):
    def __init__(self, admins):
        super().__init__()
        self.supervisor = None
        print("Создание Мастера")
        self.set_age(input("Введите возраст: "))
        self.set_name(input("Введите имя: "))
        self.set_gender(input("Введите пол: "))
        self.set_surname(input("Введите фамилию: "))
        self.set_grade(input("Введите квалификацию: "))
        self.set_salary(input("Введите зарплату: "))
        print("Администраторы:")
        for i in range(len(admins)):
            print(f"\t{i + 1}. {admins[i].get_name()} {admins[i].get_surname()}")
        while self.supervisor is None:
            try:
                self.supervisor = admins[int(input("Введите номер админа: ")) - 1]
            except:
                print("Неверный ввод")
        print("Мастер создан!")

    def get_supervisor(self):
        return self.supervisor
class Admin(Staff):
    def __init__(self, owners):
        super().__init__()
        self.supervisor = None
        self.subordinate = []
        print("Создание Администратора")
        self.set_age(input("Введите возраст: "))
        self.set_name(input("Введите имя: "))
        self.set_gender(input("Введите пол: "))
        self.set_surname(input("Введите фамилию: "))
        self.set_grade(input("Введите квалификацию: "))
        self.set_salary(input("Введите зарплату: "))
        print("Владельцы:")
        for i in range(len(owners)):
            print(f"\t{i + 1}. {owners[i].get_name()} {owners[i].get_surname()}")
        while self.supervisor is None:
            try:
                self.supervisor = owners[int(input("Введите номер владельца: ")) - 1]
            except:
                print("Неверный ввод")
        print("Администратор создан!")


    def get_supervisor(self):
        return self.supervisor

    def get_subs(self):
        return self.subordinate


    def add_sub(self, sub):
        self.subordinate.append(sub)


class Owner(Staff):
    def __init__(self):
        super().__init__()
        self.subordinate = []
        print("Создание Владельца")
        self.set_age(input("Введите возраст: "))
        self.set_name(input("Введите имя: "))
        self.set_gender(input("Введите пол: "))
        self.set_surname(input("Введите фамилию: "))
        self.set_grade(input("Введите квалификацию: "))
        self.set_salary(input("Введите зарплату: "))
        print("Владелец создан!")

    def add_sub(self, sub):
        self.subordinate.append(sub)

    def get_subs(self):
        return self.subordinate


class Service:
    def __init__(self):
        super().__init__()
        self.haircuts = []
        self.coloring = []
        self.name = None
        self.price = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_haircuts(self):
        return self.haircuts

    def get_coloring(self):
        return self.coloring

    def add_haircut(self, haircut):
        self.haircuts.append(haircut)

    def add_coloring(self, coloring):
        self.coloring.append(coloring)



class Haircut(Service):
    def __init__(self):
        super().__init__()
        print("Создание стрижки")
        self.set_name(input("Введите название: "))
        self.set_price(input("Введите стоимость: "))
        self.style = input("Введите стиль: ")
        print("Стрижка добавлена")


class Coloring(Service):
    def __init__(self):
        super().__init__()
        print("Создание окрашивания")
        self.set_name(input("Введите название: "))
        self.set_price(input("Введите стоимость: "))
        self.color = input("Введите цвет: ")
        print("Окрашивание добавлено")



if __name__ == '__main__':
    salon = Salon()  # Создание объекта Salon
    while True:
        print("\nВведите команду:")
        print("1 - Создать Мастера")
        print("2 - Создать Администратора")
        print("3 - Создать Владельца")
        print("4 - Создать Прическу")
        print("5 - Создать Окрашивание")
        print("6 - Вывести информацию о персонале")
        print("7 - Запрос 1: Поиск по зарплате большей указанной")
        print("8 - Запрос 2: Поиск по имени")
        print("9 - Запрос 3: Поиск по возрасту и классу")
        print("0 - Выйти")

        command = input("Команда: ")

        if command == "1":
            if len(salon.staff.admins) == 0:
                print("Чтобы создать мастера, небоходимо создать администратора")
            else:
                salon.create_master()
        elif command == "2":
            if len(salon.staff.owners) == 0:
                print("Чтобы создать администратора, небоходимо создать владельца")
            else:
                salon.create_admin()
        elif command == "3":
            salon.create_owner()
        elif command == "4":
            salon.create_haircut()
        elif command == "5":
            salon.create_coloring()
        elif command == "6":
            salon.output()
        elif command == "7":
            salary = input("Введите зарплату для поиска: ")
            salon.query1(salary)
        elif command == "8":
            name = input("Введите имя для поиска: ")
            salon.query2(name)
        elif command == "9":
            age = input("Введите возраст для поиска: ")
            class_input = input("Введите класс для поиска (Master, Admin, Owner): ")
            if class_input == "Master":
                salon.query3(age, Master)
            elif class_input == "Admin":
                salon.query3(age, Admin)
            elif class_input == "Owner":
                salon.query3(age, Owner)
            else:
                print("Неверное название класса.")
        elif command == "0":
            print("Выход...")
            break
        else:
            print("Неверная команда, попробуйте снова.")
