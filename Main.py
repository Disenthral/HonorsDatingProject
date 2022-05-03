
import random
import time
import pygame
#this returns random pairs of Contestants
pygame.init()
def perfectPairs():
    Contestants=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    Contestant_pairs=[]
    while Contestants:
        First=Contestants.pop(0)
        Second=random.choice(Contestants)
        Contestants.remove(Second)
        Contestant_pairs.append((First, Second))
    return Contestant_pairs

#This ends the week, returns the number of correct couples and a pair of contestants and if they are the best fit or not.
def endWeek(Pairs, PerfectPairs,CC):
    correctCouples=0
    for p in PerfectPairs:
        if p in Pairs:
            correctCouples+=1
    UnChosenPairs=[]
    for p in Pairs:
        if not p in CC:
            UnChosenPairs.append(p)
    truthBoothPair=random.choice(list(UnChosenPairs))
    truthBooth=False
    if truthBoothPair in PerfectPairs:
        truthBooth=True
    return (correctCouples,truthBoothPair,truthBooth)
def game():
    PP=perfectPairs()
    print(PP)
    step(PP,0,set(),set(),1)
    
def nogame():
    PP=perfectPairs()
    print(PP)
    noVisualStep(PP,0,set(),set(),1)
    
def noVisualStep(PerfectPairs,NumberOfCC, CorrectCouples, IncorrectCouples,week):
    print('Week: '+str(week))
    res=algo1(PerfectPairs,NumberOfCC, CorrectCouples,IncorrectCouples)
    if res[1]==8:
        print('Game Concluded')
        return
    noVisualStep(PerfectPairs, res[1], res[2],res[3],week+1)
    
def step(PerfectPairs, NumberOfCC, CorrectCouples, IncorrectCouples, week):
    pygame.init()
    res=algo1(PerfectPairs,NumberOfCC,CorrectCouples, IncorrectCouples)
    running=True
    counter=200
    screen=pygame.display.set_mode((500,500))
    screen.fill((255,255,255))
    font=pygame.font.SysFont('arial', 50)
    #draws initial Circles and numbers
    for i in range(0,8):
        pygame.draw.circle(screen,(0,0,0), [40+i*60, 150], 30, 2)
        pygame.draw.circle(screen,(0,0,0), [40+i*60, 350], 30, 2)
        
        text= font.render(str(i+1), True, (0,0,0))
        textrect=text.get_rect()
        textrect.center=(40+i*60,150)
        
        text2=font.render(str(9+i), True, (0,0,0))
        text2rect=text2.get_rect()
        text2rect.center=(40+i*60, 350)
        
        screen.blit(text, textrect)
        screen.blit(text2,text2rect)
        
    weektext=font.render('Week: '+ str(week), True, (0,0,0))
    weektextrect=weektext.get_rect()
    weektextrect.center=(250, 250)
        
    screen.blit(weektext, weektextrect)
    while counter>0:
        pygame.display.update()
        counter-=1
    #resets screen
    screen.fill((255,255,255))
    #draws circles again
    #black for unknown pairs
    #blue for true truthbooth
    #red for false truthbooth
    #gold for CC
    black=(0,0,0)
    blue=(0,0,255)
    red=(255,0,0)
    gold=(255,255,0)
    color=None
    for i in range(0,2):
        for c in range(0,2):
            if res[0][5*c]==res[4][1]:
                if res[4][2]:
                    color=blue
                else:
                    color=red
            elif res[0][5*c] in res[2]:
                color=gold
            else:
                color=black
            pygame.draw.circle(screen, color, [40+i*55,50+250*c],30,2)
            
            if res[0][1+5*c]==res[4][1]:
                if res[4][2]:
                    color=blue
                else:
                    color=red
            elif res[0][1+5*c] in res[2]:
                color=gold
            else:
                color=black
            pygame.draw.circle(screen, color, [200+i*55,50+250*c],30,2)
            
            if res[0][2+5*c]==res[4][1]:
                if res[4][2]:
                    color=blue
                else:
                    color=red
            elif res[0][2+5*c] in res[2]:
                color=gold
            else:
                color=black
            pygame.draw.circle(screen, color, [360+i*55,50+250*c],30,2)
            
            text= font.render(str(res[0][5*c][i]), True, (0,0,0))
            textrect=text.get_rect()
            textrect.center=(40+i*55,50+250*c)
            
            text2= font.render(str(res[0][1+5*c][i]), True, (0,0,0))
            text2rect=text2.get_rect()
            text2rect.center=(200+i*55,50+250*c)
            
            text3= font.render(str(res[0][2+5*c][i]), True, (0,0,0))
            text3rect=text3.get_rect()
            text3rect.center=(360+i*55,50+250*c)
             
            screen.blit(text, textrect)
            screen.blit(text2,text2rect)
            screen.blit(text3, text3rect)
            
        if res[0][3]==res[4][1]:
            if res[4][2]:
                color=blue
            else:
                color=red
        elif res[0][3] in res[2]:
            color=gold
        else:
            color=black
        pygame.draw.circle(screen, color, [120+i*55,175],30,2)
        
        if res[0][4]==res[4][1]:
            if res[4][2]:
                color=blue
            else:
                color=red
        elif res[0][4] in res[2]:
            color=gold
        else:
            color=black
        pygame.draw.circle(screen, color, [280+i*55,175],30,2)
        
        text4= font.render(str(res[0][3][i]), True, (0,0,0))
        text4rect=text4.get_rect()
        text4rect.center=(120+i*55,175)
        
        text5= font.render(str(res[0][4][i]), True, (0,0,0))
        text5rect=text5.get_rect()
        text5rect.center=(280+i*55,175)
        
        screen.blit(text4,text4rect)
        screen.blit(text5, text5rect)
    
    #draw Button
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 400, 500, 500), 2)
    buttonFont=pygame.font.SysFont('arial',70)
    buttonText=buttonFont.render('Next Step', True, (0,0,0))
    buttonRect=buttonText.get_rect()
    buttonRect.center=(250, 450)
    screen.blit(buttonText,buttonRect)
    #waits for next step
    while running:
        pygame.display.update()
        ev=pygame.event.get()
        for event in ev:
            if event.type==pygame.MOUSEBUTTONUP:
                pos= pygame.mouse.get_pos()
                if pos[1]>400:
                    running=False
            if event.type==pygame.QUIT:
                pygame.quit()
                return
    if res[1]==8:
        print("Game is Concluded")
        return
    step(PerfectPairs, res[1], res[2], res[3],week+1)
 
def algo1(PerfectPairs,NumberOfCC, CorrectCouples, IncorrectCouples):
    L=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    Pairs=[]
    for p in CorrectCouples:
        Pairs.append(p)
        L.remove(p[0])
        L.remove(p[1])
    while L:
        First=L.pop(0)
        Potentials=L[:]
        for p in IncorrectCouples:
            if First== p[0]:
                if p[1] in Potentials:
                    Potentials.remove(p[1])
        #deals with gridlock
        #the second will be from the list if there are no potential new candidates
        if Potentials:
            Second=random.choice(Potentials)
        else:
            Second=random.choice(L)
        L.remove(Second)
        Pairs.append((First, Second))
    endWeekRes=endWeek(Pairs, PerfectPairs,CorrectCouples)
    if endWeekRes[2]:
        CorrectCouples.add(endWeekRes[1])
    else:
        IncorrectCouples.add(endWeekRes[1])
    
    if endWeekRes[0]==len(CorrectCouples):
        for p in Pairs:
            IncorrectCouples.add(p)
            #note that IncorrectCouples is more aptly decided couples since CorrectCouples may be added to the set without harm as they are already paired up before IncorrectCouples takes effect.
    print('p: ',Pairs)
    print('cc: ',CorrectCouples)
    print('ic: ',IncorrectCouples)
    print('tb: ', endWeekRes[1])
    return (Pairs,endWeekRes[0], CorrectCouples,IncorrectCouples, endWeekRes)

#runs the program
if __name__=='__main__':
    game()
    #nogame()

