import random
import pygame
import os
import time







def decision(ai, screen, font, m_font, money, turn):
    waiting = True
    #h_odds = round(((-calc + 6) / 6 * 100), 1)
    #l_odds = round(((calc - 1) / 6 * 100), 1)
    money1_text = m_font.render(f"P1 money : ${money[0]}", True, (255,255,255))
    money2_text = m_font.render(f"P2 money : ${money[1]}", True, (255,255,255))
    decide_text = font.render("Will the next roll be higher or lower?", True, (255,255,255))
    help_text = font.render("Type H for higher, L for lower", True, (255,255,255))
    text_rect = decide_text.get_rect()
    text_rect1 = help_text.get_rect()
    text_rect.center = (400,400)
    text_rect1.center = (400,450)
    money_rect1 = money1_text.get_rect()
    money_rect2 = money2_text.get_rect()
    money_rect1.center = (100,550)
    money_rect2.center = (700,550)
    screen.blit(decide_text, text_rect)
    screen.blit(help_text, text_rect1)
    screen.blit(money1_text, money_rect1)
    screen.blit(money2_text, money_rect2)
    pygame.display.flip()
    if (ai == True and turn == 1):
        return
    
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    dec = 0
                    waiting = False
                if event.key == pygame.K_l:
                    dec = 1
                    waiting = False    
    return dec

def moneycalc(calc, dec):
    match dec:
        case 0:
            payout = calc * 10
        case 1:
            payout = (-calc + 7) * 10
    
    return payout
    
def transition(turn, font, screen, money, bg):
    time.sleep(2.5)
    if money[turn] < 1:
        tr_text = font.render(f"P{turn + 1} has no money, so they died", True, (255,255,255))  
        text_rect = tr_text.get_rect()
        text_rect.center = (400, 300)
        screen.blit(bg, (0,0))
        screen.blit(tr_text, text_rect)
        pygame.display.flip()
        time.sleep(2.5)  
        pygame.quit()
    elif money[turn] >= 250:
        tr_text = font.render(f"P{turn + 1} reached $250! They win", True, (255,255,255))  
        text_rect = tr_text.get_rect()
        text_rect.center = (400, 300)
        screen.blit(bg, (0,0))
        screen.blit(tr_text, text_rect)
        pygame.display.flip()
        time.sleep(2.5)  
        pygame.quit()
    else:
        tr_text = font.render(f"P{turn + 1} now has ${money[turn]}", True, (255,255,255))         
        text_rect = tr_text.get_rect()
        text_rect.center = (400, 300)
        screen.blit(bg, (0,0))
        screen.blit(tr_text, text_rect)
        pygame.display.flip()
        time.sleep(2.5)
        return True




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
    font = pygame.font.SysFont(None, 60)
    m_font = pygame.font.SysFont(None, 30)
    turn = 0
    payout = 0
    money = [100, 100]
    dice = pygame.image.load(r"C:\Users\lbern\Desktop\PFDA\FINAL\Hi-R-Lo-R\src\still_dice.png").convert()
    wait_for_roll1 = True
    is_rolling = False
    is_decide = False
    is_scoring = False
    roll_text = None
    roll = [0,0]
    rollcount = 0
    final_text = None
    ai = False




    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        
                    
        if running:
            
            while wait_for_roll1:

                if roll_text == None:
                    roll_text = font.render(f"P{turn +1} press E to roll the dice", True, (255,255,255))
                    text_rect = roll_text.get_rect()
                    text_rect.center = (400,550)
                    screen.blit(bg, (0,0))
                    screen.blit(roll_text, text_rect)
                    screen.blit(dice, (300, 200))


                    pygame.display.flip()

                if (ai == True and turn == 1):
                    time.sleep(1.5)
                    is_rolling = True
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

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            if ai != True:
                                ai = True
                            elif ai:
                                ai = False
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
                screen.blit(bg, (0,0))  
                screen.blit(frames[current_frame], (300, 200))
                current_frame += 1
                time.sleep(.016)
                if current_frame >= 23:
                    current_loop +=1
                    current_frame = 0
                    if current_loop > max_loop:
                        is_rolling = False                        
                        roll[rollcount] = random.randrange(1,7)
                        outcome_text = font.render(f"P{turn + 1} rolled a {roll[rollcount]}!", True, (255,255,255))
                        text_rect = outcome_text.get_rect()
                        text_rect.center = (400, 100)
                        screen.blit(bg, (0,0)) 
                        screen.blit(outcome_text, text_rect)
                        pygame.display.flip()
                        
                        if rollcount == 0:
                            is_decide = True
                            rollcount += 1
                        elif rollcount == 1:
                            is_scoring = True
                            rollcount = 0
                        
                        

            if is_decide:

                if (ai == True and turn == 1):
                    decision(ai, screen, font, m_font, money, turn)
                    time.sleep(2.5)
                    h_odds = round(((-roll[0] + 6) / 6 * 100), 1)
                    l_odds = round(((roll[0] - 1) / 6 * 100), 1)
                    choice_num = random.randrange(1,6)
                    if roll[0] == 1:
                        dec = 0
                    elif roll[0] == 6:
                        dec = 1
                    else:
                        if h_odds > l_odds:
                            dec = 0
                            if choice_num == 5:
                                dec = 1
                        elif h_odds < l_odds:
                            dec = 1
                            if choice_num == 5:
                                dec = 0
                    payout = moneycalc(roll[0], dec)
                    is_decide = False
                    wait_for_roll1 = True
                    screen.blit(bg, (0,0)) 
                    roll_text = None

                else:
                    dec = decision(ai, screen, font, m_font, money, turn)
                    payout = moneycalc(roll[0], dec)
                    is_decide = False
                    wait_for_roll1 = True
                    screen.blit(bg, (0,0)) 
                    roll_text = None

            if is_scoring:
                if roll[1] > roll[0]:
                    match dec:
                        case 0: 
                            final_text = font.render(f"P{turn + 1} guessed correctly! Got ${payout}", True, (255,255,255))
                            money[turn] += payout
                        case _:
                            payout = abs(payout-60)
                            final_text = font.render(f"P{turn + 1} guessed wrong! Lost ${payout}", True, (255,255,255))
                            money[turn] -= payout
                elif roll[1] < roll[0]:
                    match dec:
                        case 0:
                            payout = abs(payout-60)
                            final_text = font.render(f"P{turn + 1} guessed wrong! Lost ${payout}", True, (255,255,255))
                            money[turn] -= payout
                        case _:
                            final_text = font.render(f"P{turn + 1} guessed correctly! Got ${payout}", True, (255,255,255))
                            money[turn] += payout
                elif roll[1] == roll[0]:
                    final_text = font.render(f"P{turn + 1} rolled identically! Lost $50", True, (255,255,255))
                    money[turn] -= 50
                
                text_rect = final_text.get_rect()
                text_rect.center = (400, 400)
                screen.blit(final_text, text_rect)
                pygame.display.flip()
                is_scoring = False
                roll_text = None
                wait_for_roll1 = transition(turn, font, screen, money, bg)
                if turn == 0:
                    turn = 1
                elif turn == 1:
                    turn = 0
         




        pygame.display.flip()
        dt = clock.tick(24)


    

    pygame.quit()

    

        
                    
                   


if __name__ == "__main__":
    main()