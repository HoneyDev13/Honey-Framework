import time

class HoneyFramework:
    def __init__(self):
        self.bees = 1
        self.honey = 0
        self.money = 0
        self.level = 1
        self.bonus_active = False
        self.bonus_end_time = 0

    def wait(self):
        time.sleep(60)  # wait for 1 minute
        self.honey += self.bees * (2 if self.bonus_active and time.time() < self.bonus_end_time else 1)
        print(f"You now have {self.honey} honey pots.")
        self.check_level_up()

    def sell_honey(self):
        self.money += self.honey * 15
        print(f"You sold your honey and now have ${self.money}.")
        self.honey = 0

    def buy_bee(self):
        if self.money >= 100:
            self.money -= 100
            self.bees += 1
            print(f"You bought a bee! You now have {self.bees} bees.")
        else:
            print("You don't have enough money to buy a bee.")

    def buy_bonus(self):
        if self.money >= 1500:
            self.money -= 1500
            self.bonus_active = True
            self.bonus_end_time = time.time() + 600  # bonus lasts for 10 minutes
            print("Bonus activated! You now produce double honey for 10 minutes.")
        else:
            print("You don't have enough money to buy the bonus.")

    def check_level_up(self):
        if self.honey >= self.level * 100:
            self.level += 1
            print(f"Congratulations! You leveled up to level {self.level}.")

    def play(self):
        while True:
            print("\n1. Wait for more honey\n2. Sell honey\n3. Buy a bee\n4. Buy 2x honey bonus")
            choice = input("Choose an action: ")
            if choice == '1':
                self.wait()
            elif choice == '2':
                self.sell_honey()
            elif choice == '3':
                self.buy_bee()
            elif choice == '4':
                self.buy_bonus()

HoneyFramework = HoneyFramework()
HoneyFramework.play()
