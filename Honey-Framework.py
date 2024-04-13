import time
import random

class HoneyFramework:
    def __init__(self):
        self.bees = 1
        self.honey = 0
        self.money = 0
        self.level = 1
        self.bonus_active = False
        self.bonus_end_time = 0
        self.achievements = []

    def wait(self):
        time.sleep(60)  # wait for 1 minute
        self.honey += self.bees * (2 if self.bonus_active and time.time() < self.bonus_end_time else 1)
        print(f"You now have {self.honey} honey pots.")
        self.check_level_up()
        self.random_event()

    def sell_honey(self):
        self.money += self.honey * 15
        print(f"You sold your honey and now have ${self.money}.")
        self.honey = 0
        self.check_achievement()

    def buy_bee(self):
        if self.money >= 100:
            self.money -= 100
            self.bees += 1
            print(f"You bought a bee! You now have {self.bees} bees.")
            if self.bees == 2:  # The first bee is already there at the start
                self.achievements.append("Achievement unlocked: Bought your first bee!")
                print(self.achievements[-1])
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
            self.achievements.append(f"Leveled up to level {self.level}")
            print(f"Congratulations! You leveled up to level {self.level}.")

    def check_achievement(self):
        if self.money >= 1000 and "Achievement unlocked: Earned $1000!" not in self.achievements:
            self.achievements.append("Achievement unlocked: Earned $1000!")
            print(self.achievements[-1])

    def random_event(self):
        event = random.randint(1, 10)
        if event == 1:
            print("A bear ate some of your honey!")
            self.honey -= 10
        elif event == 2:
            print("A generous beekeeper gave you some honey!")
            self.honey += 10

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
