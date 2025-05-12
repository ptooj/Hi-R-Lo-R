import random
import pygame
import os
import time




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
        
def rolling_anim(frame_c, frames):
    folder_path = r"C:\Users\lbern\Desktop\PFDA\FINAL\Hi-R-Lo-R\src\dice_anim"
    os.chdir(folder_path)
    for i in range(frame_c):
        filename = f"frame_{i:02d}_delay-0.03s.png"
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Missing frame: {filename}")
        image = pygame.image.load(filename)
        frames.append(image)
    




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
    bg = pygame.image.load(r"C:\Users\lbern\Desktop\PFDA\FINAL\Hi-R-Lo-R\src\tablebg.jpg").convert()
    screen.blit(bg, (0, 0))
    font = pygame.font.SysFont(None, 60)
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
    roll_text = font.render("Press E to roll the dice", True, (255,255,255))
    decide_text = font.render("Will the next roll be higher or lower\nType H for higher, L for lower", True, (255,255,255))
    text_rect = roll_text.get_rect()
    text_rect.center = (400,550)
    screen.blit(roll_text, text_rect)

    pygame.display.flip()



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
                     
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
                            current_frame = 0
                            current_loop = 0
                            max_loop = random.randrange(1,3)
                            frame_c = 24
                            frames = []
                            folder_path = r"C:\Users\lbern\Desktop\PFDA\FINAL\Hi-R-Lo-R\src\dice_anim"
                            os.chdir(folder_path)
                            for i in range(frame_c):
                                filename = f"frame_{i:02d}_delay-0.03s.png"
                                if not os.path.exists(filename):
                                    raise FileNotFoundError(f"Missing frame: {filename}")
                                image = pygame.image.load(filename)
                                frames.append(image)


            if is_rolling:
                #dice = rolling_anim(frame_c, frames)
                screen.blit(bg, (0,0))  
                screen.blit(frames[current_frame], (300, 200))
                current_frame += 1
                time.sleep(.016)
                if current_frame >= 23:
                    current_loop +=1
                    current_frame = 0
                    if current_loop > max_loop:
                        is_rolling = False
                        is_decide = True
                        roll1 = random.randrange(1,7)
                        

            if is_decide:
                p1_dec = decision(roll1)
                payout = money(roll1, p1_dec)

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