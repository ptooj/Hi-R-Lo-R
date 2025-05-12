import random
import pygame
import os
import time


class RolledText():

    def __init__(self, pos, life=1000):
        self.pos = pos
        self.age = 0
        self.life = life
        self.alpha = 255
        self.surface = self.update_surface()
        self.dead = False
        

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))
        
    def draw(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)

class D_Object():

    def __init__(self, life, pos):
        life = 100
        pos = (300, 200)
        self.surf = self.update_surf()

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True

    def update_surface(self):
        surf = pygame.Surface((self.size*.8, (self.speed + self.size)*.8))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        if self.dead:
            return
        surface.blit(self.surface, self.pos)

"""def p1_roll(screen, font):
    not_rolled = True
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_e] & not_rolled:
        not_rolled = False
        roll1 = random.randrange(1,7)
        roll_text = font.render(f"You rolled a {roll1}!", True, (255,255,255))
        text_rect = roll_text.get_rect()
        text_rect.center = (400,500)
        screen.blit(roll_text, text_rect)"""



def roll1(screen):
    print("Press E to roll the dice...")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                roll1 = random.randrange(1,7)
                   
                    
            print (f"You rolled a {roll1}!")
    return roll1



def roll2(screen):
    waiting = True
    print("Press E to roll the second dice...")
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    roll2 = random.randrange(1,7)
                    waiting = False
                    print (f"You rolled a {roll2}!")
    return roll2



def decision(calc):
    waiting = True
    h_odds = round(((-calc + 6) / 6 * 100), 1)
    l_odds = round(((calc - 1) / 6 * 100), 1)

    print("Will the next roll be higher or lower?")
    print(f"Odds for higher : {h_odds}%\nOdds for lower : {l_odds}%")
    print("Type H or L for higher or lower")
    
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    print ("You picked higher")
                    dec = 0
                    waiting = False
                if event.key == pygame.K_l:
                    print ("You picked lower")
                    dec = 1
                    waiting = False     
    return dec

def money(calc, dec):
    match dec:
        case 0:
            payout = calc * 10
        case 1:
            payout = (-calc + 7) * 10
    
    return payout
        
def rolling_anim(screen, dice):
    folder_path = r"C:\Users\lbern\Desktop\PFDA\FINAL\Hi-R-Lo-R\src\dice_anim"
    os.chdir(folder_path)
    for filename in os.listdir(folder_path):
        dice = D_Object()
        """dice = pygame.image.load(filename).convert()
        screen.blit(dice, (300, 200))"""
        time.sleep(.3)
    return




def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    pygame.init()
    pygame.display.set_caption("Hi-r/Lo-R")
    fullscreen = False
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    bg = pygame.Color(0, 0, 0)
    font = pygame.font.SysFont(None, 30)
    turn = 0
    payout = 0
    p1_money = 100
    p2_money = 100
    dice = pygame.image.load(r"C:\Users\lbern\Desktop\PFDA\FINAL\Hi-R-Lo-R\src\still_dice.png").convert()
    screen.blit(dice, (300, 200))
    wait_for_roll1 = True
    is_rolling = False
    is_decide = False
    is_scoring = False



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                     
        """roll_text = font.render("Press E to roll the dice", True, (255,255,255))
        text_rect = roll_text.get_rect()
        text_rect.center = (400,550)
        screen.blit(roll_text, text_rect)"""

        if turn == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"P1 money : {p1_money}")
            print("Press E to roll the dice...")
            while wait_for_roll1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e:
                            is_rolling = True
                            wait_for_roll1 = False

            if is_rolling:
                dice = rolling_anim(screen, dice)      

            if is_decide:
                p1_dec = decision(p1_outcome1)
                payout = money(p1_outcome1, p1_dec)

            """if is_rolling2:
                p1_outcome2 = roll2(screen)"""
            if is_scoring:
                if p1_outcome2 > p1_outcome1:
                    match p1_dec:
                        case 0:
                            print(f"You guessed correctly! You got ${payout}") 
                            p1_money += payout
                        case _:
                            payout = payout + 60
                            print(f"You guessed wrong! You lose ${payout}")
                            p1_money -= payout
                elif p1_outcome2 < p1_outcome1:
                    match p1_dec:
                        case 0:
                            payout = payout + 60
                            print(f"You guessed wrong! You lose ${payout}")
                            p1_money -= payout
                        case _:
                            print(f"You guessed correctly! You got ${payout}")
                            p1_money += payout
                elif p1_outcome2 == p1_outcome1:
                    print("Same!! Lose $50")
                    p1_money -= 50
                    print(f"You now have ${p1_money}")
                    time.sleep(3)
                    turn = 1
        

        """elif turn == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"P2 money : {p2_money}")
            p2_outcome1 = roll1(screen)  
            p2_dec = decision(p2_outcome1)
            payout = money(p2_outcome1, p2_dec)
            p2_outcome2 = roll2(screen)
            if p2_outcome2 > p2_outcome1:
                match p2_dec:
                    case 0:
                        print(f"You guessed correctly! You got ${payout}") 
                        p2_money += payout
                    case _:
                        payout = payout + 60
                        print(f"You guessed wrong! You lose ${payout}")
                        p2_money -= payout
            elif p2_outcome2 < p2_outcome1:
                match p2_dec:
                    case 0:
                        payout = payout + 60
                        print(f"You guessed wrong! You lose ${payout}")
                        p2_money -= payout
                    case _:
                        print(f"You guessed correctly! You got ${payout}")
                        p2_money += payout
            elif p2_outcome2 == p2_outcome1:
                print("Same!! Lose $50")
                p2_money -= 50

            print(f"You now have ${p2_money}")
            time.sleep(3)
            turn = 0"""

        pygame.display.flip()
        dt = clock.tick(24)


    

    pygame.quit()

    

        
                    
                   


if __name__ == "__main__":
    main()