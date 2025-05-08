import random
import pygame
import os


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



def roll1():
    waiting = True
    print("Press E to roll the dice...")
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    roll1 = random.randrange(1,7)
                    waiting = False
                    print (f"You rolled a {roll1}!")
    return roll1



def roll2():
    waiting = True
    print("Press E to roll the dice...")
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
    p1_money = 100
    p2_money = 100

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                     
        roll_text = font.render("Press E to roll the dice", True, (255,255,255))
        text_rect = roll_text.get_rect()
        text_rect.center = (400,550)
        screen.blit(roll_text, text_rect)

        if turn == 0:
            p1_outcome = None
            p1_outcome1 = roll1()    
            #p1_outcome = p1_roll(screen, font)
            p1_dec = decision(p1_outcome1)
            p1_outcome2 = roll2()
            if p1_outcome2 > p1_outcome1:
                print("the roll was higher")
            elif p1_outcome2 < p1_outcome1:
                print("the roll was lower")
            elif p1_outcome2 == p1_outcome1:
                print("Same!! Lose $50")

            turn = 1

            
            



        pygame.display.flip()
        dt = clock.tick(24)

    pygame.quit()

    

        
                    
                   


if __name__ == "__main__":
    main()