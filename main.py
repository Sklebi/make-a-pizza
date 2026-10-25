import math, random, time
from collections import Counter

# Idea: Pizzaria

balance = 0
inventory = [] 
skill_level = 0 
is_running = True
multiplier = 1
success = False

approvedText = ["I really felt connected to this job", "I really think that I am the right one for this job", "yes", "no i do not think so", "mhm", "my strengths? Everything.",
                "you should hire me", "where I see myself in 5 years, in your position :3", "my hair gel? I knew you thought it looked amazing! hire me!", "yeah i agree", "i definitely approve of that LOL!",
                "i believe that what you said was entirely correct", "I think that you are the best manager ever!"]



class showInventory:
    @classmethod
    def showInv(cls, data_list):
        frequencies = Counter(data_list)
        print("This is what is in your inventory:")
        for item, count in frequencies.items():
            print(f"{item}: x{count}")
            time.sleep(.5)

class Employee:
    def __init__(self, name, cost, cashProduction):
        self.name = name
        self.cost = cost
        self.cashProduction = cashProduction

    def work(self, balance):
        balance += self.cashProduction
        for atime in range(30, 0, -1):
            print(f"you have {atime} seconds left")
            time.sleep(1)
        print(f"Your current balance: {balance}")
        return balance

    def named(self):
        print(f"Hello! I am {self.name} and I am ready for this interview")

    def talk(self):
        time.sleep(1)
        ranApprovedtext = random.choice(approvedText)
        print(f"{self.name}: {ranApprovedtext}")

    def talkSad(self):
        time.sleep(1)
        ranSad = random.choice(sad)
        print(f"{self.name}: {ranSad}")

    def buyEmployee(self, balance):
        if balance < self.cost:
            print("You do not have enough money to buy the employee....")
            return balance, False
        else: 
            print("Buying the employee....")
            time.sleep(1)
            balance -= self.cost
            print(f"Your balance is now ${balance}")
            return balance, True

        
    def costShow(self):
        print(f"The cost of the employee is: ${self.cost}")
        time.sleep(0.5)
        print(f"The cash production of the employee is: ${self.cashProduction}")

sad = ["aww damn it!", "for real?", "you suck!", "I was waiting for ages!", "I declined my DREAM job for this!", 
       "alright..", "I understand.", "this is my 93rd failed interview..", "this is my 92nd failed interview...",
       "are you sure?? dang..."]


class Customer:
    def __init__(self, name, order):
        self.name = name
        self.order = order
        self.money = 0.0
        self.chosen_toppings = []
        self.ableto = True

    def moneyMultiplier(self, multiplier):
        min_money = 600* multiplier
        max_money = 1000* multiplier
        self.money = round(random.uniform(min_money, max_money), 2)

    def orderPizza(self, inventory): 
        if not inventory: 
            self.chosen_toppings = []
            self.ableto = False
            time.sleep(1)
            return f"You do not have enough to fulfill their order"
        else:
            maxToppings = min(3, len(inventory))
            numToppings = random.randint(1, maxToppings)
            self.chosen_toppings = random.sample(inventory, numToppings)

            if len(self.chosen_toppings) == 1:
                topping_string = self.chosen_toppings[0]
            else: 
                topping_string = ", ".join(self.chosen_toppings[:-1]) + f" and {self.chosen_toppings[-1]}"

            return f" {self.name} wants {topping_string} in their order"

positive_answers = ["yes", "sure", "ofc", "mhm", "yeah", "y", "ye"]
negative_answers = ["no", "nope", "nah", "nop", "n", "never", "na", "q"]
valid_answers = set(positive_answers + negative_answers)
customer_names = [
    "Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Charlotte", "William", "Sophia",
    "James", "Amelia", "Benjamin", "Isabella", "Lucas", "Mia", "Henry", "Evelyn", "Alexander", "Harper",
    "Mason", "Camila", "Michael", "Gianna", "Ethan", "Abigail", "Daniel", "Luna", "Jacob", "Ella",
    "Logan", "Elizabeth", "Jackson", "Sofia", "Levi", "Avery", "Sebastian", "Scarlett", "Mateo", "Eleanor",
    "Jack", "Madison", "Owen", "Layla", "Theodore", "Penelope", "Aiden", "Aria", "Samuel", "Chloe",
    "Joseph", "Grace", "John", "Ellie", "David", "Nora", "Wyatt", "Hazel", "Matthew", "Zoey",
    "Luke", "Riley", "Asher", "Janis", "Carter", "Aurora", "Julian", "Lily", "Grayson", "Nova",
    "Leo", "Hannah", "Jayden", "Emilia", "Gabriel", "Zoe", "Isaac", "Stella", "Lincoln", "Elena",
    "Anthony", "Paisley", "Hudson", "Audrey", "Dylan", "Maya", "Ezra", "Elizabeth", "Thomas", "Iris",
    "Charles", "Ruby", "Christopher", "Eva", "Jaxon", "Rose", "Maverick", "Amara", "Josiah", "Valerie", "Asha", "AshaAI"
]

costs = random.randint(10000, 100000)
cashProduction = random.randint(1,1000000)

actions = ("""
-----ACTIONS------
1. buy ingredients
2. go to the pizzaria
3. check inventory 
4. check balance
5. quit
------------------
""")

pizzariaActions = ("""
-----PIZZARIA------
1. go back to actions
2. buy decorations
3. serve a customer
4. hire an employee
5. work the employee
------------------
""")

ingredientList = {
    "1": ("Dough", 300),
    "2": ("Tomato Sauce", 100),
    "3": ("Cheese", 200), 
    "4": ("Pepperoni", 300),
    "5": ("Sausage", 600),
    "6": ("Bell Peppers", 900),
    "7": ("Pinapple", 1200),
    "8": ("Bacon", 1300),
    "9": ("Ham", 1500),
    "10": ("Halal Beef", 2000),
    "11": ("Basil", 2300),
    "12": ("Olives", 2500),
}
ingredientListnum = ["1", "2", "3", "4", '5', '6',"7", "8", "9", "10", '11', '12']
# to remove: 

while is_running:
    print("---Welcome to pizzaria simulator---")
    time.sleep(1)
    name = input("What is your first name?: ").strip().capitalize()
    while not name.isalpha(): 
        print("Please enter a name that is letters only.")
        time.sleep(1)
        name = input("What is your first name?: ").strip().capitalize()

    time.sleep(1)
    print(f"hi, {name}.")
    time.sleep(1)

    inAction = True
    while inAction: 
        alines = actions.splitlines()
        for line in alines: 
            print(line)
            time.sleep(0.5)
        time.sleep(1)

        userAction = input("What would you like to do?: ")
        while userAction not in ["1", '2', '3', '4', '5']:
            print("Please enter a valid action (either 1, 2, 3, 4 or 5.)")
            userAction = input("What would you like to do?: ")
        else: 
            # action #1
            if userAction == "1":
                inIngredient = True
                while inIngredient:
                    print("These are the ingredients that you can buy: ")
                    print("------ingredients------")
                    for number, (ingredient, ingredientCost) in ingredientList.items():
                        print(f"[{number}] {ingredient}: ${ingredientCost}")
                        time.sleep(0.2)
                    leavingIngredient = len(ingredientList) + 1
                    print(f"[{leavingIngredient}] Leave")
                    time.sleep(1)
                    asking1 = True
                    while asking1: 
                        userIngredient = input("What would you like to do?: ")
                        userIngredient_int = int(userIngredient)
                        if not userIngredient.isdigit(): 
                            print("please enter in a number")
                            time.sleep(1)
                            continue
                        
                        elif userIngredient_int == leavingIngredient: 
                            time.sleep(1)
                            print("...returning...")
                            time.sleep(1)
                            inIngredient = False
                            asking1 = False

                        elif userIngredient in ingredientListnum:
                            chosenIngredient, chosenPrice = ingredientList[userIngredient]
                            if balance >= chosenPrice:
                                inventory.append(chosenIngredient)
                                print(f"...you bought {chosenIngredient}!")
                                time.sleep(1)
                                continue

                            elif balance < chosenPrice:
                                print("you do not have enough money!")
                                time.sleep(1)
                                print(f"The item costs {chosenPrice} but you only have ${balance}")

                        else: 
                            time.sleep(1)
                            print("...returning...")
                            time.sleep(1)
                            inIngredient = False
                            asking1 = False
            # action #2
            if userAction == "2":
                pizzariaOpen = True
                while pizzariaOpen:
                    
                    if "Dough" in inventory and "Tomato Sauce" in inventory and "Cheese" in inventory: 
                        time.sleep(0.5)
                        print("Going to the pizzaria!")
                        time.sleep(.5)
                        inventoryPrint = showInventory.showInv(inventory)

                        time.sleep(1)
                        # pizzaria opened 
                        plines = pizzariaActions.splitlines()
                        for line in plines:
                            print(line)
                            time.sleep(0.3)
                        time.sleep(1)
                        asking2 = True

                        while asking2: 
                            pizzaUser = input("What would you like to do?: ")
                            if pizzaUser not in ["1","2","3",'4', "5"]:
                                print("You need to enter a valid answer!")
                                continue

                            elif pizzaUser == "1":
                                print("...returning to actions...")
                                time.sleep(1)
                                pizzariaOpen = False
                                asking2 = False

                            elif pizzaUser == "5":
                                if success == True:
                                    print("starting cash production...")
                                    employee.work(balance)
                                    asking2 = False
                                    continue
                                else:
                                    print("you do not have an employee")
                                    continue

                            elif pizzaUser == "3":
                                pizzaUser2 = True
                                while pizzaUser2:
                                    customer_name = random.choice(customer_names)
                                    customer = Customer(customer_name, order=None)
                                    customer.moneyMultiplier(multiplier=multiplier)
                                    customersOrder = customer.orderPizza(inventory)

                                    print("A new customer has arrived!")
                                    print(customersOrder)
                                    action3 = True
                                    while action3:
                                        if customer.ableto == False: 
                                            action3 = False
                                            asking2 = False
                                            pizzaUser2 = False
                                            pizzariaOpen = False
                                        else: 
                                            fulfilling = True
                                            while fulfilling: 
                                                fulfill = input("would you like to fufill the order?: (q to quit) ").lower()
        
                                                if fulfill not in valid_answers:
                                                    print("Please enter a valid answer: yes or no.")
                                                    continue
                                                
                                                elif fulfill.lower() == "q":
                                                    print("...returning...")
                                                    fulfilling = False
                                                    action3 = False
                                                    pizzaUser2 = False
                                                    asking2 = False

                                                elif fulfill in negative_answers:
                                                    print("....rejecting the customer....")
                                                    time.sleep(1)
                                                    action3 = False
                                                    fulfilling = False

                                                elif fulfill in positive_answers:
                                                    has_ingredients = True
                                                    for topping in customer.chosen_toppings:
                                                        if inventory.count(topping) < customer.chosen_toppings.count(topping):
                                                            has_ingredients = False
                                                            print(f"you do not have {topping} and therefore you cannot make this order.")
                                                            time.sleep(1)
                                                            break

                                                    if has_ingredients:
                                                        print(f"fulfilling order for {customer_name}...")
                                                        time.sleep(1)

                                                        for topping in customer.chosen_toppings:
                                                            if topping in inventory: 
                                                                inventory.remove(topping)

                                                        print("Order is COMPLETE!!")

                                                        balance = round(balance + customer.money, 2)
                                                        print(f"you have earned ${customer.money}")
                                                        time.sleep(1)
                                                        print(f"your new balance is ${balance}")
                                                        action3 = False
                                                        fulfilling = False
                                                    else:
                                                        print("You do not have enough stuff in your inventory.")
                                                        time.sleep(1)
                                                        action3 = False
                                                        fulfilling = False
                                                else: 
                                                    action3 = False
                                                    pizzaUser2 = False
                                                    fulfilling = False
                                                    break
                                        

                            elif pizzaUser == "2":
                                inDecoration = True
                                while inDecoration: 
                                    print("...going to dome hepot...")
                                    decorationList = {
                                        "1": ("Flower", 3000, 2),
                                        "2": ("Mysterious Painting", 5000, 3),
                                        "3": ("Wallpaper", 10000, 4), 
                                        "4": ("Painting from Ebay", 15000, 4.5),
                                        "5": ("Fancy Chairs", 50000, 5),
                                        "6": ("Fancy  Tables", 100000, 7),
                                        "7": ("Fancy Vase", 300000, 8),
                                        "8": ("Scent Blower", 700000, 9),
                                        "9": ("Gold Pillar", 1000000, 10),
                                        "10": ("Designed Curtains", 20000000, 11),
                                        "11": ("Knick Knack", 230000000, 12),
                                        "12": ("Wax Statue of Lionel Messi", 1000000000000, 100),
                                    }

                                    decorationListnum = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
                                    print("-----Dome Hepot-----")
                                    for number, (decoration, decorPrice, Dmultiplier) in decorationList.items():
                                        print(f"[{number}] {decoration}: ${decorPrice} | Multiplier: {Dmultiplier}")
                                        time.sleep(0.2)
                                    leavingDecoration = len(decorationList) + 1
                                    print(f"[{leavingDecoration}] Leave")
                                    time.sleep(1)
                                    decorAskingAction = True
                                    while decorAskingAction:
                                        decorUser = input("What would you like to do?: ").lower()
                                        decorUser_int = int(decorUser)

                                        if not decorUser.isdigit():
                                            print("Please enter in a valid number")
                                            time.sleep(1)
                                            continue

                                        elif decorUser_int == leavingDecoration:
                                            time.sleep(1)
                                            print("...returning...")
                                            time.sleep(1)
                                            decorAskingAction = False
                                            inDecoration = False

                                        elif decorUser in decorationListnum:
                                            chosenDecor, chosenDecorprice, chosenMultiplier = decorationList[decorUser]
                                            if balance >= chosenDecorprice:
                                                balance -= chosenDecorprice
                                                multiplier += chosenMultiplier
                                                print(f"Your new multipler is: {multiplier}")
                                                time.sleep(1)
                                                continue

                            elif pizzaUser == "4":
                                inJob = True
                                while inJob: 
                                    print("Going to indeed to pick up some workers.")
                                    time.sleep(1)
                                    jobOffer = input("Would you like to make your job offer?: ").lower()
                                    if jobOffer not in valid_answers:
                                        print("Please enter a valid answer.")
                                        continue
                                    elif jobOffer in negative_answers:
                                        print("...returning...")
                                        inJob = False
                                    elif jobOffer in positive_answers: 
                                        print("Okay!")
                                        time.sleep(1)
                                        madlibs = input("Please enter the heading of your job offering: ").lower()
                                        time.sleep(1)
                                        print("INPUT APPROVED!")
                                        madlibs2 = input("Please enter the description of the job: ").lower()
                                        time.sleep(1)
                                        print("INPUT APPROVED!")
                                        time.sleep(1)
                                        print("please wait some seconds until you get your first canidate!")
                                        waiting = True
                                        while waiting:
                                            seconds = random.randint(1, 59)
                                            for second in range(seconds):
                                                print("elevator music.....")
                                                time.sleep(1)
                                            employee_name = random.choice(customer_names)
                                            employee = Employee(employee_name, costs, cashProduction)
                                            print("OH!!! A CANIDATE!")
                                            interview = input("Would you like to interview them?: ").lower()
                                            while interview not in valid_answers:
                                                print("please input a valid answer: ")
                                                interview = input("Would you like to interview them?: ").lower()
                                            else:
                                                if interview in negative_answers:
                                                    print("...skipping the canidate...")
                                                    continue
                                                elif interview in positive_answers:
                                                    employee.named()
                                                    interviewQuestion = input("Ask them a question: ")
                                                    print(interviewQuestion)
                                                    time.sleep(0.5)
                                                    employee.talk()
                                                    interviewQuestion2 = input("Ask them another question: ")
                                                    print(interviewQuestion2)
                                                    time.sleep(1)
                                                    employee.talk()
                                                    interviewQuestion3 = input("Ask them your final question: ")
                                                    time.sleep(1)
                                                    employee.talk()
                                                    hired = input("Would you like to hire them?: ").lower()

                                                    while hired not in valid_answers: 
                                                        print("please enter a valid answer")
                                                        hired = input("Would you like to hire them?: ").lower()
                                                    else:
                                                        if hired in negative_answers:
                                                            print("You have let the employee know...")
                                                            time.sleep(1)
                                                            employee.talkSad()
                                                            waiting = False
                                                        elif hired in positive_answers: 
                                                            employee.costShow()
                                                            buyEmployee = input("Would you like to purchase them?: ").lower()
                                                            while buyEmployee not in valid_answers:
                                                                print("Please enter a valid answer.")
                                                                buyEmployee = input("Would you like to purchase them?: ").lower()
                                                            else:
                                                                if buyEmployee in negative_answers:
                                                                    print("You have let the employee know...")
                                                                    time.sleep(1)
                                                                    employee.talkSad()
                                                                    waiting = False
                                                                elif buyEmployee in positive_answers:
                                                                    employee.buyEmployee(balance)
                                                                    balance, success = employee.buyEmployee(balance)
                                                                    if success: 
                                                                        waiting = False
                                                                        inJob = False
                                                                        asking2 = False

                    else:
                        time.sleep(1)
                        print("You need dough, sauce and cheese in order to open your pizzaria.")
                        pizzariaOpen = False

            # action #3
            if userAction == "3":
                    showInventory.showInv(inventory)
                
            # action #4
            if userAction == "4":
                print(f"Your balance is ${balance}")

            # action #5
            if userAction == "5":
                leaving = True
                while leaving: 
                    userSure1 = input("Are you sure you want to leave? ").lower()
                    if userSure1 not in valid_answers: 
                        print("That is not a valid response to my QUESTION!")
                    elif userSure1 in negative_answers:
                        print("yay! returning to actions...")
                        time.sleep(1)
                        leaving = False
                    elif userSure1 in positive_answers:
                        userSure2 = input("are you sure? I would be sad if you left :(!: ").lower()
                        if userSure2 not in valid_answers:  
                            print("that is not a valid response to my QUESTION!")
                        elif userSure1 in negative_answers:
                            print("yay!! returning to actions...")
                            time.sleep(1)
                            leaving = False
                        elif userSure2 in positive_answers:
                            print("okay.... goodbye!")
                            time.sleep(1)
                            leaving = False
                            is_running = False
                            inAction = False