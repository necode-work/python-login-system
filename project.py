#Bestimmung der Einlogdaten
users = {
    "sk": "fml",
    "ym": "lml",
    "a": "1",
    "b": "2"
}

enteru = None
enterp = None

#Funktion zur Vermeidung der Erstellung einer repetetativen Fehlermeldung
def error():
    print("Invalid input!")

#Anzeigen des Status (wo das Programm aktuell ist) zur besseren Übersicht/Zugriff
def state(name):
    print("==", name, "==")

#Funktion zur Eingabe bei multiple-choice Fragen
def decision():
    choice = input("Choose an option: ").strip().lower()
    if choice in ("1", "one"):
        return 1
    elif choice in ("2", "two"):
        return 2
    elif choice in ("3", "three"):
        return 3
    elif choice in ("4", "four"):
        return 4
    elif choice in ("5", "five"):
        return 5
    else:
        return None

#Loginfunktion: Überprüft, ob der User existiert, wenn ja, wird das entsprechende Passwort abgefragt
def login():
    global enteru, enterp
    while True:
        state("LOGIN")
        enteru = input("username:")
        enterp = input("password:")

        if enteru not in users:
            print("Unknown user")
            continue
        elif enterp != users[enteru]:
            print("Wrong password")
            continue
        else:
            print("Login successful, welcome", enteru, "!")
            return enteru, enterp

#Änderung des Benutzernamens (nur per Sizung möglich, nicht permanent)
#Überprüfung, ob der Benutzername bereits existiert bzw. ob es der alte ist
#Anschließend wird der alte Benutzername entfernt und der neue an dessen Stelle gefügt
def change_username():
    global enteru
    while True:
        state("CHANGE USERNAME")
        new_username = input("New username:")

        if new_username == enteru:
            print("New username can't be old username!")
            continue
        elif new_username in users:
            print("Username already exists!")
            continue

        confirmnu = input("Confirm new username:")
        if confirmnu != new_username:
            print("Usernames don't match!")
            continue

        password = users.pop(enteru)
        users[new_username] = password
        enteru = new_username
        print("Username changed to", enteru, "!")
        return enteru

#Siehe oben
#Letztendliche Entfernung des alten Passworts und Einfügen des neuen unterscheidet sich, da es sich hier um ein Value und oben um ein Key handelt
def change_password():
    global enterp
    while True:
        state("CHANGE PASSWORD")
        new_password = input("New password:")

        if new_password == users[enteru]:
            print("New password can't be old password!")
            continue

        confirmnp = input("Confirm new password:")
        if confirmnp != new_password:
            print("Passwords don't match!")
            continue

        users[enteru] = new_password
        enterp = new_password
        print("Password changed!")
        return enterp

#Funktion zur Optimierung der Nutzereingabe
#options ist eine Variable, die später durch die unten angeführten Listen (pizzas, sizes, etc.) definiert wird
#Als nächstes bildet man das Menü ab, indem durch range(len()) die Anzahl der Optionen (z.B. 0,1,2) registriert wird, beim abbilden aber mit 1 addiert wird, da Listen bei 0 anfangen und der User typischerweise 1... gewöhnt ist
#Dahinter steht dann die Option, die der Zahl entspricht, z.B. 1 - Pizza Magherita
#Anschließend kann der User eine der Optionen wählen
#Wenn der Input ungültig ist (kleiner als 1, größer als die Spanne der Liste oder sonstiges, was nicht der Liste entspricht) startet der Loop von vorne
#Wenn der Input gültig ist, gibt man das Value -1 zurück, da die Pizza Magherita ja z.B. der 0 entspricht, der User aber 1 eingibt
def menudm(options):
    while True:
        for i in range(len(options)):
            print(i + 1, "-", options[i])

        choicep = decision()
        if choicep is None or choicep < 1 or choicep > len(options):
            error()
            continue
        return choicep - 1

#Diese Funktion dient dazu, Pizza zu bestellen (nur im Programm)
#Mit der oberen Funktion menudm(options) werden die verfügbaren Gerichte bzw. Getränke aufgelistet und abgefragt, was der User möchte
#Am Ende steht dann die gesamte Bestellung
def drippymold():
    state("PIZZATIME")
    print("Welcome to DrippyMold, have a look at the menu!")

    pizzas = ["Pizza Magherita", "Pizza Hawaii", "Pizza Salami", "Pizza Hut Classic"]
    sizes = ["Small-scale sized", "Medium-meal sized", "Family-feast sized"]
    sauces = ["Sweet-sour sauce", "Cheese sauce", "Spicy sauce", "Chef's special sauce"]
    drinks = ["Coke", "Pineapple juice", "Pepsi", "Ice tea (peach)"]

    print("Choose a pizza:")
    pizza = menudm(pizzas)

    print("Choose a size:")
    size = menudm(sizes)

    print("Choose a sauce:")
    sauce = menudm(sauces)

    print("Choose a drink:")
    drink = menudm(drinks)

    print(
        "Your",
        sizes[size].lower(),
        pizzas[pizza],
        "with",
        sauces[sauce].lower(),
        "and",
        drinks[drink].lower(),
        "is on the way!"
    )

#Funktion zur Erstellung eines "Homescreen-artigen" Interfaces
def menu():
    state("MENU")
    print("1. Change login credentials")
    print("2. Order Pizza")
    print("3. Log out")
    print("4. Shut down")
    return decision()

#Funktion für die 1. Option vom Menü, anschließend Aktualisierung der Login-Eingaben
def loginchange():
    while True:
        state("LOGIN CHANGE")
        print("1: Change password")
        print("2: Change username")
        subchoice = decision()

        if subchoice == 1:
            change_password()
            break
        elif subchoice == 2:
            change_username()
            break
        else:
            error()
enteru, enterp = login()

#Das ganze Programm zur einfacheren Übersicht extrem komprimiert durch viele Funktionen
while True:
    menuchoice = menu()

    if menuchoice == 1:
        loginchange()
    elif menuchoice == 2:
        drippymold()
    elif menuchoice == 3:
        enteru, enterp = login()
    elif menuchoice == 4:
        exit()
