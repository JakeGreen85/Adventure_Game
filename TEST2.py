#TEST

xcord = 50
ycord = 150
for x in Armor:
    for y in x:
        Rect = pygame.Rect(xcord, ycord, 64, 64)
        Pic = pygame.image.load("Game Images/Pic Fin/Items/"+x+".png")
        wSurf.blit(Pic,Rect)
        wSurf.blit(frame,Rect)
        if Rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    a = 1
                    b = y
                    ChoiceText = "Would you like to buy this item?"
            stats = MediumFont.render(str(y), True, WHITE, BLACK)
            xRect = pygame.Rect(pygame.mouse.get_pos()[0]+20,pygame.mouse.get_pos()[1]+50, 5,5)
            wSurf.blit(stats, xRect)
        ycord += 50
    xcord += 50
    ycord = 150
