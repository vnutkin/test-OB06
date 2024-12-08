import random
class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, other):
        other.health = max(0, other.health-self.attack_power)
    def is_alive(self):
        if self.health > 0 :
            return True
        else:
            return False
    def info(self):
        print(f'{self.name},{self.health},{self.attack_power}')
class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.init_health = player.health
        self.init_attack_power = player.attack_power
    def start(self):
        game_on = True
        while game_on:
            round = 0
            while self.computer.is_alive() and self.player.is_alive():
                round +=1
                print(f'Раунд {round}. {self.computer.name}, здоровье:{self.computer.health} против {self.player.name}, здоровье: {self.player.health}')
                pow_comp = random.randint(1, self.init_attack_power)
                pow_play = random.randint(1, self.init_attack_power)
                if pow_comp > pow_play:
                   print(f'{self.computer.name} ударил {self.player.name} с силой {pow_comp}')
                   print(f'{self.player.name} ударил {self.computer.name} с силой {pow_play}')

                else:
                    print(f'{self.player.name} ударил {self.computer.name} с силой {pow_play}')
                    print(f'{self.computer.name} ударил {self.player.name} с силой {pow_comp}')
                self.computer.attack_power = pow_comp
                self.computer.attack(self.player)
                self.player.attack_power = pow_play
                self.player.attack(self.computer)
            if  self.computer.is_alive():
                print(f'Победил {self.computer.name}, здоровье {self.computer.health}')
            else:
                if self.player.is_alive():
                    print(f'Победил {self.player.name}, здоровье {self.player.health}')
                else:
                    print(f'Погибли оба: {self.computer.name}, {self.player.name}')
            ans = int(input('Играть снова?(1-да, 0 - нет)'))
            if ans == 0:
                game_on = False
            else:
                self.computer.health = self.init_health
                self.player.health = self.init_health
hero = Hero
comp = hero('IdeaCentre',100,20)
play = hero('Илья М.',100,20)
game = Game
game1 = game(play,comp)
game1.start()