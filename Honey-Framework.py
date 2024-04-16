import time
import random

class Bee:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __init__(self, cost):
        self.cost = cost
        self.production_rate = 1  # Manuka honey production rate per 4 minutes

class HoneyFramework:
    def __init__(self):
        self.bees = []
        self.honey = 0
        self.manuka_honey = 0
        self.money = 0
        self.level = 1
        self.bonus_active = False
        self.bonus_end_time = 0
        self.achievements = []
        self.quests = {
            "Produce 1000 honey": {"reward": 500, "completed": False},
            "Reach level 5": {"reward": 1000, "completed": False},
            # Add more quests as desired
        }
        self.bee_production_interval = 240  # 4 minutes in seconds
        self.last_production_time = time.time()
        self.manuka_bush_cost = 1000  # Cost of purchasing a Manuka bush
        self.honey_price = 10  # Initial price of honey
        self.manuka_honey_price = 100  # Initial price of Manuka honey
        self.production_boost_cost = 2000  # Cost of purchasing a honey production boost
        self.inventory_capacity = 20  # Initial inventory storage capacity
        self.initialize_bees()

    def initialize_bees(self):
        # Define different types of bees
        self.bees.append(Bee("Worker Bee", 100))
        self.bees.append(Bee("Drone Bee", 200))
        self.bees.append(Bee("Queen Bee", 500))

    def wait(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_production_time
        if time_elapsed >= self.bee_production_interval:
            self.produce_honey()
            self.produce_manuka_honey()  # Produce Manuka honey
            self.last_production_time = current_time
            print(f"You now have {self.honey} honey pots and {self.manuka_honey} Manuka honey pots.")
            self.check_level_up()
            self.random_event()
            self.update_market_prices()
            self.check_quests()
        else:
            print(f"You need to wait {int(self.bee_production_interval - time_elapsed)} more seconds before honey production.")

    def produce_honey(self):
        honey_produced = len(self.bees)
        self.honey += honey_produced

    def produce_manuka_honey(self):
        # Manuka honey production is a percentage of regular honey production
        manuka_honey_produced = len(self.bees)  # Each bee produces 1 unit of Manuka honey
        self.manuka_honey += manuka_honey_produced

    def sell_honey(self):
        total_money = self.honey * self.honey_price + self.manuka_honey * self.manuka_honey_price
        self.money += total_money
        print(f"You sold your honey and Manuka honey for a total of ${total_money}.")
        self.honey = 0
        self.manuka_honey = 0
        self.check_achievement()

    def buy_bee(self):
        print("Available bees to buy:")
        for i, bee in enumerate(self.bees):
            print(f"{i+1}. {bee.name} - Cost: ${bee.cost}")
        choice = input("Choose a bee to buy (1-3): ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(self.bees):
                selected_bee = self.bees[choice - 1]
                if self.money >= selected_bee.cost:
                    self.money -= selected_bee.cost
                    self.bees.append(selected_bee)
                    print(f"You bought a {selected_bee.name}!")
                else:
                    print("You don't have enough money to buy this bee.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def buy_manuka_bush(self):
        if self.money >= self.manuka_bush_cost:
            self.money -= self.manuka_bush_cost
            print("You bought a Manuka bush!")
        else:
            print("You don't have enough money to buy a Manuka bush.")

    def buy_bonus(self):
        if self.money >= 1500:
            self.money -= 1500
            self.bonus_active = True
            self.bonus_end_time = time.time() + 600  # bonus lasts for 10 minutes
            print("Bonus activated! You now produce double honey for 10 minutes.")
        else:
            print("You don't have enough money to buy the bonus.")

    def upgrade_bee(self):
        print("Available upgrades:")
        # Define available upgrades and their costs
        upgrades = {
            "Increase production rate": 200,
            "Unlock special ability": 500,
            # Add more upgrades as desired
        }
        for i, (upgrade, cost) in enumerate(upgrades.items(), 1):
            print(f"{i}. {upgrade} - Cost: ${cost}")
        choice = input("Choose an upgrade: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(upgrades):
                selected_upgrade = list(upgrades.keys())[choice - 1]
                upgrade_cost = list(upgrades.values())[choice - 1]
                if self.money >= upgrade_cost:
                    # Apply selected upgrade
                    # Logic for upgrading bees goes here
                    self.money -= upgrade_cost
                    print(f"You upgraded your bees with {selected_upgrade}!")
                else:
                    print("You don't have enough money to buy this upgrade.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def research_and_development(self):
        print("Available research options:")
        research_options = {
            "Increase bee production interval": 500,
            "Expand honey storage capacity": 1000,
            "Increase inventory storage capacity": 750,  # New research option
            # Add more research options as desired
        }
        for i, (option, cost) in enumerate(research_options.items(), 1):
            print(f"{i}. {option} - Cost: ${cost}")
        choice = input("Choose a research option: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(research_options):
                selected_option = list(research_options.keys())[choice - 1]
                research_cost = list(research_options.values())[choice - 1]
                if self.money >= research_cost:
                    # Apply selected research option
                    if selected_option == "Increase inventory storage capacity":
                        self.inventory_capacity_researched = True
                        # Increase inventory storage capacity
                        self.inventory_capacity += 10
                        print("You conducted research to increase inventory storage capacity.")
                    elif selected_option == "Increase bee production interval":
                        if not self.honey_storage_capacity_researched:
                            print("You need to research 'Expand honey storage capacity' first.")
                            return
                        self.bee_production_interval_researched = True
                        self.bee_production_interval -= 60  # Decrease production interval by 1 minute
                        print("You conducted research to increase bee production interval.")
                    elif selected_option == "Expand honey storage capacity":
                        self.honey_storage_capacity_researched = True
                        # Increase honey storage capacity
                        self.honey_storage_capacity += 10
                        print("You conducted research to expand honey storage capacity.")
                    else:
                        print(f"You invested in {selected_option}!")
                    self.money -= research_cost
                    print(f"You invested in {selected_option}!")
                else:
                    print("You don't have enough money to invest in this option.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def buy_production_boost(self):
        if self.money >= self.production_boost_cost:
            # Apply production boost
            # Logic for applying production boost goes here
            self.money -= self.production_boost_cost
            print("You bought a honey production boost!")
        else:
            print("You don't have enough money to buy a honey production boost.")

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

    def check_quests(self):
        for quest, info in self.quests.items():
            if not info["completed"]:
                if quest == "Produce 1000 honey" and self.honey >= 1000:
                    self.money += info["reward"]
                    info["completed"] = True
                    print(f"Quest completed: {quest}! You earned ${info['reward']}.")

    def play(self):
        while True:
            print("\n1. Wait for more honey\n2. Sell honey\n3. Buy a bee\n4. Buy a Manuka bush\n5. Buy 2x honey bonus\n6. Upgrade bees\n7. Research & Development\n8. Buy production boost\n9. Check achievements\n10. Quit")
            choice = input("Choose an action: ")
            if choice == '1':
                self.wait()
            elif choice == '2':
                self.sell_honey()
            elif choice == '3':
                self.buy_bee()
            elif choice == '4':
                self.buy_manuka_bush()
            elif choice == '5':
                self.buy_bonus()
            elif choice == '6':
                self.upgrade_bee()
            elif choice == '7':
                self.research_and_development()
            elif choice == '8':
                self.buy_production_boost()
            elif choice == '9':
                print("Achievements:")
                for achievement in self.achievements:
                    print(achievement)
            elif choice == '10':
                print("Exiting the game...")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    HoneyFramework = HoneyFramework()
    HoneyFramework.play()
