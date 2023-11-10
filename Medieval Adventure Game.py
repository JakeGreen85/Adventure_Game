#Imports
import pygame, sys, random, time
from pygame.locals import*

#Pygame Initiating
pygame.init()
pygame.mixer.init()
mclock = pygame.time.Clock()

#pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

#Window Surface
WIDTH = 1000
HEIGHT = 700
wSurf = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Medieval Adventure Game")

#Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0) 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 100, 255)
DARKGREEN = (124, 200, 0)
DARKERGREEN = (0, 138, 20)
GREY = (150, 170, 150)
LIGHTGREY = (211, 211, 211)
GOLD = (255, 215, 0)
DARKERRED = (150, 0, 0)
PURPLE = (128, 0, 128)
TRANS = (0, 0, 0)

#Rects for text
TopLeftRect1 = pygame.Rect(WIDTH*1/4, 10, 5, 5)
TopLeftRect2 = pygame.Rect(WIDTH*1/4, 30, 5, 5)
TopLeftRect3 = pygame.Rect(WIDTH*1/4, 50, 5, 5)
TopLeftRect4 = pygame.Rect(WIDTH*1/4, 70, 5, 5)
TopLeftRect5 = pygame.Rect(WIDTH*1/4, 90, 5, 5)
TopLeftRect6 = pygame.Rect(WIDTH*1/4, 110, 5, 5)
TopLeftRect7 = pygame.Rect(WIDTH*1/4, 130, 5, 5)
TopLeftRect8 = pygame.Rect(WIDTH*1/4, 150, 5, 5)
TopLeftRect9 = pygame.Rect(WIDTH*1/4, 170, 5, 5)
LeftRect1 = pygame.Rect(WIDTH*1/4, 250, 5, 5)
LeftRect2 = pygame.Rect(WIDTH*1/4, 270, 5, 5)
LeftRect3 = pygame.Rect(WIDTH*1/4, 290, 5, 5)
LeftRect4 = pygame.Rect(WIDTH*1/4, 310, 5, 5)
LeftRect5 = pygame.Rect(WIDTH*1/4, 330, 5, 5)
LeftRect6 = pygame.Rect(WIDTH*1/4, 350, 5, 5)
LeftRect7 = pygame.Rect(WIDTH*1/4, 370, 5, 5)
LeftRect8 = pygame.Rect(WIDTH*1/4, 390, 5, 5)
LeftRect9 = pygame.Rect(WIDTH*1/4, 410, 5, 5)
BottomLeftRect1 = pygame.Rect(WIDTH*1/4, 510, 5, 5)
BottomLeftRect2 = pygame.Rect(WIDTH*1/4, 530, 5, 5)
BottomLeftRect3 = pygame.Rect(WIDTH*1/4, 550, 5, 5)
BottomLeftRect4 = pygame.Rect(WIDTH*1/4, 570, 5, 5)
BottomLeftRect5 = pygame.Rect(WIDTH*1/4, 50, 5, 5)
BottomLeftRect6 = pygame.Rect(WIDTH*1/4, 610, 5, 5)
BottomLeftRect7 = pygame.Rect(WIDTH*1/4, 630, 5, 5)
BottomLeftRect8 = pygame.Rect(WIDTH*1/4, 650, 5, 5)
BottomLeftRect9 = pygame.Rect(WIDTH*1/4, 670, 5, 5)
TopRect1 = pygame.Rect(WIDTH/2, 10, 5, 5)
TopRect2 = pygame.Rect(WIDTH/2, 30, 5, 5)
TopRect3 = pygame.Rect(WIDTH/2, 50, 5, 5)
TopRect4 = pygame.Rect(WIDTH/2, 70, 5, 5)
TopRect5 = pygame.Rect(WIDTH/2, 90, 5, 5)
TopRect6 = pygame.Rect(WIDTH/2, 110, 5, 5)
TopRect7 = pygame.Rect(WIDTH/2, 130, 5, 5)
TopRect8 = pygame.Rect(WIDTH/2, 150, 5, 5)
TopRect9 = pygame.Rect(WIDTH/2, 170, 5, 5)
MiddleRect1 = pygame.Rect(WIDTH/2, 250, 5, 5)
MiddleRect2 = pygame.Rect(WIDTH/2, 270, 5, 5)
MiddleRect3 = pygame.Rect(WIDTH/2, 290, 5, 5)
MiddleRect4 = pygame.Rect(WIDTH/2, 310, 5, 5)
MiddleRect5 = pygame.Rect(WIDTH/2, 330, 5, 5)
MiddleRect6 = pygame.Rect(WIDTH/2, 350, 5, 5)
MiddleRect7 = pygame.Rect(WIDTH/2, 370, 5, 5)
MiddleRect8 = pygame.Rect(WIDTH/2, 390, 5, 5)
MiddleRect9 = pygame.Rect(WIDTH/2, 410, 5, 5)
BottomRect1 = pygame.Rect(WIDTH/2, 510, 5, 5)
BottomRect2 = pygame.Rect(WIDTH/2, 530, 5, 5)
BottomRect3 = pygame.Rect(WIDTH/2, 550, 5, 5)
BottomRect4 = pygame.Rect(WIDTH/2, 570, 5, 5)
BottomRect5 = pygame.Rect(WIDTH/2, 50, 5, 5)
BottomRect6 = pygame.Rect(WIDTH/2, 610, 5, 5)
BottomRect7 = pygame.Rect(WIDTH/2, 630, 5, 5)
BottomRect8 = pygame.Rect(WIDTH/2, 650, 5, 5)
BottomRect9 = pygame.Rect(WIDTH/2, 670, 5, 5)
TopRightRect1 = pygame.Rect(WIDTH*3/4, 10, 5, 5)
TopRightRect2 = pygame.Rect(WIDTH*3/4, 30, 5, 5)
TopRightRect3 = pygame.Rect(WIDTH*3/4, 50, 5, 5)
TopRightRect4 = pygame.Rect(WIDTH*3/4, 70, 5, 5)
TopRightRect5 = pygame.Rect(WIDTH*3/4, 90, 5, 5)
TopRightRect6 = pygame.Rect(WIDTH*3/4, 110, 5, 5)
TopRightRect7 = pygame.Rect(WIDTH*3/4, 130, 5, 5)
TopRightRect8 = pygame.Rect(WIDTH*3/4, 150, 5, 5)
TopRightRect9 = pygame.Rect(WIDTH*3/4, 170, 5, 5)
RightRect1 = pygame.Rect(WIDTH*3/4, 250, 5, 5)
RightRect2 = pygame.Rect(WIDTH*3/4, 270, 5, 5)
RightRect3 = pygame.Rect(WIDTH*3/4, 290, 5, 5)
RightRect4 = pygame.Rect(WIDTH*3/4, 310, 5, 5)
RightRect5 = pygame.Rect(WIDTH*3/4, 330, 5, 5)
RightRect6 = pygame.Rect(WIDTH*3/4, 350, 5, 5)
RightRect7 = pygame.Rect(WIDTH*3/4, 370, 5, 5)
RightRect8 = pygame.Rect(WIDTH*3/4, 390, 5, 5)
RightRect9 = pygame.Rect(WIDTH*3/4, 410, 5, 5)
BottomRightRect1 = pygame.Rect(WIDTH*3/4, 510, 5, 5)
BottomRightRect2 = pygame.Rect(WIDTH*3/4, 530, 5, 5)
BottomRightRect3 = pygame.Rect(WIDTH*3/4, 550, 5, 5)
BottomRightRect4 = pygame.Rect(WIDTH*3/4, 570, 5, 5)
BottomRightRect5 = pygame.Rect(WIDTH*3/4, 50, 5, 5)
BottomRightRect6 = pygame.Rect(WIDTH*3/4, 610, 5, 5)
BottomRightRect7 = pygame.Rect(WIDTH*3/4, 630, 5, 5)
BottomRightRect8 = pygame.Rect(WIDTH*3/4, 650, 5, 5)
BottomRightRect9 = pygame.Rect(WIDTH*3/4, 670, 5, 5)

#Fonts
SmallFont = pygame.font.SysFont("gabriola", 20)
MediumFont = pygame.font.SysFont("gabriola", 30)
LargeFont = pygame.font.SysFont("gabriola", 40)
BigFont = pygame.font.SysFont("gabriola", 50)
HugeFont = pygame.font.SysFont("gabriola", 60)
GiantFont = pygame.font.SysFont("gabriola", 70)
HandFont = pygame.font.SysFont("inkfree", 25)

####################Images###################
#Backgrounds
mainmenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Main Menu.png")
endgamemenu = pygame.image.load("Game Images/Pic Lib/Landscape Background copy.png")
playmenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Play Menu.png")
placemenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Place Menu.png")
typemenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Type Menu.png")
marketmenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Market Menu.png")
armorymenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Armory Menu.png")
blacksmithmenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Blacksmith Menu.png")
blacksmithmenu2 = pygame.image.load("Game Images/Pic Fin/Backgrounds/Blacksmith Menu 2.png")
blacksmithmenu3 = pygame.image.load("Game Images/Pic Fin/Backgrounds/Blacksmith Menu 3.png")
battleback = pygame.image.load("Game Images/Pic Fin/Backgrounds/Battle Back.png")
savemenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/SaveGame Back.png")
equipmentmenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Equipment Menu.png")
statsmenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Stats Menu.png")
backpackmenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Backpack Menu.png")
comingsoonmenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Coming Soon Menu.png")
decidermenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Decider Menu.png")
weaponshop = pygame.image.load("Game Images/Pic Fin/Backgrounds/Weapon Shop.png")
settingsmenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Settings Menu.png")
dungeonmenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Dungeon Menu.png")

#Misc
battlemenu1 = pygame.image.load("Game Images/Pic Fin/Misc/BattleMenu1.png")
battlemenu2 = pygame.image.load("Game Images/Pic Fin/Misc/BattleMenu2.png")
battlemenu3 = pygame.image.load("Game Images/Pic Fin/Misc/BattleMenu3.png")
playerbar = pygame.image.load("Game Images/Pic Fin/Misc/PlayerBar.png")
dummybar = pygame.image.load("Game Images/Pic Fin/Misc/DummyBar.png")
fairybar = pygame.image.load("Game Images/Pic Fin/Misc/FairyBar.png")
pigbar = pygame.image.load("Game Images/Pic Fin/Misc/PigBar.png")
dragonbar = pygame.image.load("Game Images/Pic Fin/Misc/DragonBar.png")
goldpile = pygame.image.load("Game Images/Pic Fin/Misc/GoldPile.png")
battlebutton = pygame.image.load("Game Images/Pic Fin/Misc/Battle Button.png")
frame = pygame.image.load("Game Images/Pic Fin/Misc/Frame.png")
settings = pygame.image.load("Game Images/Pic Fin/Misc/Settings Icon.png")
armoricon = pygame.image.load("Game Images/Pic Fin/Misc/Armor Icon.png")

#Abilities
bleedstatus = pygame.image.load("Game Images/Pic Fin/Misc/Bleed.png")
stunstatus = pygame.image.load("Game Images/Pic Fin/Misc/Stunned.png")

#Player Stats
PlayerStatsDef = ['Level','Health Points','Max Health Points','Armor','Max Armor','Mana','Max Mana','Gold','Experience','Damage','Critical Hit Chance(%)','Speed']
PlayerStats = [1,100,100,0,0,100,100,1000,90,10,10,100]
PName = 'Jakob'

#Initiating status
INFIGHT = 0
STUN = 0
BLEED = 0
FLEE = 0
BOSS = 0
FAIL = 0

#Other
TUTORIAL = 0
PLACE = 'Start'
MUSIC = True
VOLUME = 0.05
BackRect = pygame.Rect(0,0,5,5)
MenuRect = pygame.Rect(370,334,1,1)

#Equipment
NoEquipment = ['no helmet','no shoulders','Old Black Shirt (0 Armor)','no hands','no wrist','no belt','Ripped Leather Pants (0 Armor)','Worn Sandals (0 Armor)','Fists']
EquipmentRect = [[615, 35],[500, 100],[730, 105],[475, 243],[750, 252],[745, 430],[495, 415],[616, 592],[472, 585]]
BagRect = [[55, 100], [150, 100], [250, 100], [340, 100], [55, 220], [150, 220], [250, 220], [340, 220], [55, 335], [150, 335], [250, 335], [340, 335], [55, 450], [150, 450], [250, 450], [340, 450]]
PlayerEquipment = ['no helmet','no shoulders','Old Black Shirt (0 Armor)','no hands','no wrist','no belt','Ripped Leather Pants (0 Armor)','Worn Sandals (0 Armor)','Fists']
PlayerCatArmor = [0,0,0,0,0,0,0,0]
ArmorTypes = ['Helmet','Shoulders','Chest','Hands','Wrists','Belts','Pants','Feet']
Helmets = [["Handcrafted Iron Helmet (50 Armor)(Req. Level 3)",1500, 50, 3],["Dragon's Head (150 Armor)(Req. Level 5)",5000,150,5]]
Shoulders = [["Handcrafted Iron Pads (50 Armor)(Req. Level 3)",1500, 50,3],["Dragon's Scales (150 Armor)",5000,150,5]]
Chests = [["Leather Chest Plate (10 Armor)(Req. Level 1)",100,10,1],["Handcrafted Iron Plate (50 Armor)(Req. Level 3)",1500,50,3],["Dragon's Chest (150 Armor)(Req. Level 5)",5000,150,5]]
Hands = [["Leather Gloves (10 Armor)(Req. Level 1)",100,10,1],["Handcrafted Iron Gloves (50 Armor)(Req. Level 3)",1500,50,3],["Dragon's Claws (150 Armor)(Req. Level 5)",5000,150,5]]
Wrists = [["Handcrafted Iron Bands (50 Armor)(Req. Level 3)",1500,50,3],["Dragon's Cuffs (150 Armor)(Req. Level 5)",5000,150,5]]
Belts = [["Handcrafted Iron Plated Belt (50 Armor)(Req. Level 3)",1500,50,3],["Dragon's Waist (150 Armor)(Req. Level 5)",5000,150,5]]
Pants = [["Leather Pants (10 Armor)(Req. Level 1)",100,10,1],["Handcrafted Iron Pants (50 Armor)(Req. Level 3)",1500,50,3],["Dragon's Legs (150 Armor)(Req. Level 5)",5000,150,5]]
Feet = [["Leather Sandals (10 Armor)(Req. Level 1)",100,10,1],["Handcrafted Iron Shoes (50 Armor)(Req. Level 3)",1500,50,3],["Dragon's Feet (150 Armor)(Req. Level 5)",5000,150,5]]
          
#Weapons
Weapons = [["Beginner's Sword (DMG 10)(Req. Level 1)",100,10,1],["Beginner's Axe (DMG 15)(Req. Level 2)",200,15,2],["Handcrafted Sword of the Lion (DMG 30)(Req. Level 3)",3000,30,3],["Handcrafted Axe of the Tiger (DMG 45)(Req. Level 4)",4500,45,4],["Sword of the Dragon's Tail (DMG 70)(Req. Level 5)",10000,70,5],["Axe of the Dragon's Tooth (DMG 100)(Req. Level 6)",15000,100,6]]

#Items
Items = [['Healing Potion (100%)',20,0,1],['Mana Potion (100%)',20,0,1],['Mystery Box',100,0,1],['Key',100,0,1]]
BAG = ['Mystery Box','Key']
MaxBagLen = 30

#Skills
AvailSkills = [['Pummel (20 Mana)(200% Player Damage)(Req. Level 1)',20,1],['Slash (15 Mana)(300% Player Damage over 6 rounds)(Req. Level 2)',15,2],['Bash (30 Mana)(100% Player Damage + Stuns enemy for 2 rounds)(Req. Level 3)',30,3],['Victory Rush (30 Mana, Enemy health under 20%)(500% Player Damage)(Req. Level 4)',30,4],['Restoration (20 Mana)(Heals 20% of player health)(Req. Level 5)',20,5],['Anvil (20 Mana)(Repairs 20% of Player Armor)(Req. Level 6)',20,6]]
PlayerSkills = [AvailSkills[0],['none',0,0],['none',0,0]]

#Player
ULvl1 = [" ","Skills: ",AvailSkills[0]," ","Weapons: ",Weapons[0]," ","Equipment: ",Chests[0], Hands[0], Pants[0], Feet[0]]
ULvl2 = [" ","Skills: ",AvailSkills[1]," ","Weapons: ",Weapons[1]]
ULvl3 = [" ","Skills: ",AvailSkills[2]," ","Weapons: ",Weapons[2]," ","Equipment: ",Helmets[0],Shoulders[0],Chests[1],Hands[1],Wrists[0],Belts[0],Pants[1],Feet[1]]
ULvl4 = [" ","Skills: ",AvailSkills[3]," ","Weapons: ",Weapons[3]]
ULvl5 = [" ","Skills: ",AvailSkills[4]," ","Weapons: ",Weapons[4]," ","Equipment: ",Helmets[1],Shoulders[1],Chests[2],Hands[2],Wrists[1],Belts[1],Pants[2],Feet[2]]
ULvl6 = [" ","Skills: ",AvailSkills[5]," ","Weapons: ",Weapons[5]]
UNLOCK = [ULvl1,ULvl2,ULvl3,ULvl4,ULvl5,ULvl6]

Armor = [Helmets,Shoulders,Chests,Hands,Wrists,Belts,Pants,Feet,Weapons,Items] ###What did I use this for in the original code??


def FileSetup():
    file = open("Game Files/GameOpen.txt","a")
    file.write("1 \n")
    file.close()
    file = open("Game Files/GameOpen.txt","r")
    fileO = file.readlines()
    print(len(fileO) == 1)
    if len(fileO) == 1:
        file1 = open("Game Files/SaveGame1.txt","w")
        file2 = open("Game Files/SaveGame2.txt","w")
        file3 = open("Game Files/SaveGame3.txt","w")
        for x in PlayerStats:
            x1 = str(x)
            file1.writelines(x1)
            file1.writelines("\n")
        file1.writelines('No Player')
        file1.writelines('\n')
        file1.writelines('No Save')
        for x in PlayerStats:
            x1 = str(x)
            file2.writelines(x1)
            file2.writelines("\n")
        file2.writelines('No Player')
        file2.writelines('\n')
        file2.writelines('No Save')
        for x in PlayerStats:
            x1 = str(x)
            file3.writelines(x1)
            file3.writelines("\n")
        file3.writelines('No Player')
        file3.writelines('\n')
        file3.writelines('No Save')
        file1.close()
        file2.close()
        file3.close()
        file.close()

    return

def PlayMenu(): #This is the main screen where player can choose to fight, see armor, buy stuff, see stats, or quit
    global INFIGHT
    global FLEE
    wSurf.blit(playmenu,BackRect)
    PrintPlayerStats()
    SettingsIcon()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            if 670 < event.pos[0] < 900 and 370 < event.pos[1] < 425:
                FSelector()
                INFIGHT = 1
                FLEE = 0
            elif 670 < event.pos[0] < 900 and 443 < event.pos[1] < 498:
                Armory()
            elif 670 < event.pos[0] < 900 and 513 < event.pos[1] < 569:
                Market()
            elif 670 < event.pos[0] < 900 and 583 < event.pos[1] < 637:
                Stats()
            elif 8 < event.pos[0] < 122 and 184 < event.pos[1] < 234:
                MainMenu()
    pygame.display.update()
    mclock.tick(40)
    return

def FSelector(): #Ask where player wants to fight
    while INFIGHT == 1:
        FPlace = 0
        wSurf.blit(placemenu,BackRect)
        SettingsIcon()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 20 < event.pos[0] < 255 and 337 < event.pos[1] < 390:
                    FPlace = 1
                    FSelector2(FPlace)
                elif 20 < event.pos[0] < 255 and 410 < event.pos[1] < 465:
                    FPlace = 2
                    FSelector2(FPlace)
                elif 20 < event.pos[0] < 255 and 482 < event.pos[1] < 535:
                    FPlace = 3
                    FSelector2(FPlace)
                elif 20 < event.pos[0] < 255 and 550 < event.pos[1] < 605:
                    FPlace = 4
                    FSelector2(FPlace)
                elif 20 < event.pos[0] < 255 and 620 < event.pos[1] < 675:
                    return
        pygame.display.update()
        mclock.tick(40)
    return

def FSelector2(FPlace): #Asking user what to fight (Boss, Normal, or Dungeon)
    while INFIGHT == 1:
        FType = 0
        wSurf.blit(typemenu,BackRect)
        SettingsIcon()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 25 < event.pos[0] < 255 and 393 < event.pos[1] < 450: #NORMAL
                    FType = 1
                    FGen(FPlace,FType)
                elif 25 < event.pos[0] < 255 and 467 < event.pos[1] < 520:#BOSS
                    FType = 2 
                    FGen(FPlace,FType)
                elif 25 < event.pos[0] < 255 and 538 < event.pos[1] < 590:#DUNGEON
                    FType = 3 
                    FGen(FPlace,FType)
                elif 25 < event.pos[0] < 255 and 607 < event.pos[1] < 661: #Go Back
                    return
        pygame.display.update()
        mclock.tick(40)
    return

def FGen(FPlace, FType): #Generating Fight
    global BOSS
    SettingsIcon()
    if FPlace == 1: #Training Dummy
        MLvl = 1
        PlaceTxt = "at the Training Camp"
        MonsterTxt = " Training Dummy "
    elif FPlace == 2: #Fairy
        MLvl = random.randint(2,3)
        if FType == 2:
            MLvl = 3
        PlaceTxt = "in Fairy Forest"
        MonsterTxt = " Fairy "
    elif FPlace == 3: #Pig
        MLvl = random.randint(4,5)
        if FType == 2:
            MLvl = 5
        PlaceTxt = "in Pig Prarie"
        MonsterTxt = " Pig "
    else: #Dragon
        MLvl = random.randint(6,7)
        if FType == 2:
            MLvl = 7
        PlaceTxt = "in the Dragon's Den"
        MonsterTxt = " Dragon "
    MLvlText = str(MLvl)
    if FType == 1: #NORMAL
        wSurf.blit(battleback,BackRect)
        EncText = MediumFont.render("You have encountered a level "+MLvlText+MonsterTxt+PlaceTxt, True, WHITE)
        BOSS = 0
        NFight(MLvl,EncText)
    elif FType == 2: #BOSS
        wSurf.blit(battleback,BackRect)
        EncText = MediumFont.render("You have encountered a level "+MLvlText+MonsterTxt+ 'boss ' +PlaceTxt, True, WHITE)
        NFight(MLvl,EncText)
    else: #DUNGEON
        DFight(FPlace,MLvl)
    return

def PrintPlayerStats(): #Show Player Stats
    HPRect = pygame.Rect(210,608,1,1)
    HPstr = str(PlayerStats[1])
    HPMaxstr = str(PlayerStats[2])
    HPText = HPstr+" / "+HPMaxstr
    HPRend = SmallFont.render(HPText, True, WHITE)
    ManaRect = pygame.Rect(210,633,1,1)
    Manastr = str(PlayerStats[5])
    ManaMaxstr = str(PlayerStats[6])
    ManaText = Manastr+" / "+ManaMaxstr
    ManaRend = SmallFont.render(ManaText, True, WHITE)
    ExpRect = pygame.Rect(210,658,1,1)
    Expstr = str(PlayerStats[8])
    ExpReqstr = str(100*PlayerStats[0]*PlayerStats[0])
    ExpText = Expstr+" / "+ExpReqstr
    ExpRend = SmallFont.render(ExpText, True, WHITE)
    PbarRect = pygame.Rect(20,550,5,5)
    GoldPileRect = pygame.Rect(10, 10, 5, 5)
    GoldRect = pygame.Rect(50, 10, 5, 5)
    GoldText = str(PlayerStats[7])
    GoldRend = LargeFont.render(GoldText, True, GOLD)
    if PlayerStats[3] > 0:
        ShieldRect = pygame.Rect(150, 550, 32, 32)
        wSurf.blit(armoricon,ShieldRect)
        wSurf.blit(MediumFont.render(str(PlayerStats[3]), True, LIGHTBLUE),pygame.Rect(155, 575, 5, 5))
    wSurf.blit(GoldRend,GoldRect)
    wSurf.blit(goldpile,GoldPileRect)
    wSurf.blit(playerbar,PbarRect)
    wSurf.blit(HPRend,HPRect)
    wSurf.blit(ManaRend,ManaRect)
    wSurf.blit(ExpRend,ExpRect)

def PrintMonsterStats(MHP,MDMG,MGOLD,MEXP,MSPEED,MMaxHP): #Show Enemy Stats
    MHPRect = pygame.Rect(720,608,1,1)
    MHPstr = str(MHP)
    MHPMaxstr = str(MMaxHP)
    MHPText = MHPstr+" / "+MHPMaxstr
    MHPRend = SmallFont.render(MHPText, True, WHITE)
    MManaRect = pygame.Rect(720,633,1,1)
    MManastr = '100'
    MManaMaxstr = '100'
    MManaText = MManastr+" / "+MManaMaxstr
    MManaRend = SmallFont.render(MManaText, True, WHITE)
    MExpRect = pygame.Rect(720,658,1,1)
    MExpstr = str(MEXP)
    MExpReqstr = str(MEXP)
    MExpText = MExpstr+" / "+MExpReqstr
    MExpRend = SmallFont.render(MExpText, True, WHITE)

    wSurf.blit(MHPRend,MHPRect)
    wSurf.blit(MManaRend,MManaRect)
    wSurf.blit(MExpRend,MExpRect)

    return

def ChangeTurn(MLvl, R): #Refresh Screen
    RoundRect = pygame.Rect(470, 20, 5, 5)
    mbarrect = pygame.Rect(620,550,5,5)
    wSurf.blit(battleback,BackRect)
    wSurf.blit(battlemenu1,MenuRect)
    Rend = MediumFont.render("Round: "+str(R), True, WHITE)
    wSurf.blit(Rend, Rend.get_rect(center = (HEIGHT/2, 50)))
    if MLvl == 1:
        wSurf.blit(dummybar,mbarrect)
    elif 2 <= MLvl <= 3:
        wSurf.blit(fairybar,mbarrect)
    elif 4 <= MLvl <= 5:
        wSurf.blit(pigbar,mbarrect)
    elif 6 <= MLvl <= 7:
        wSurf.blit(dragonbar,mbarrect)

def UseSkills(MHP,MMaxHP,PATK): #Use skills in fight
    global BLEED
    global STUN
    while True:
        xcord = 450
        ycord = 200
        for Skills in PlayerSkills:
            Rect = pygame.Rect(xcord, ycord,64,64)
            ycord += 64
            Pic = pygame.image.load("Game Images/Pic Fin/Skills/"+Skills[0]+".png")
            wSurf.blit(Pic,Rect)
##            if Rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
##                wSurf.blit(MediumFont.render(Skills[0], True, WHITE), pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1], 5,5))
##                print("Collision")
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if Skills[0] == AvailSkills[0][0] and PlayerStats[5] >= AvailSkills[0][1]: #Pummel
                        PATK = PlayerStats[9] * 2
                        PlayerStats[5] -= AvailSkills[0][1]
                        Text = PName + " used Pummel"
                    elif Skills[0] == AvailSkills[1][0] and PlayerStats[5] >= AvailSkills[1][1]: #Slash
                        BLEED = 6
                        PlayerStats[5] -= AvailSkills[1][1]
                        Text = PName + " used Slash"
                    elif Skills[0] == AvailSkills[2][0] and PlayerStats[5] >= AvailSkills[2][1]: #Bash
                        STUN = 2
                        PlayerStats[5] -= AvailSkills[2][1]
                        Text = PName + "used Bash"
                    elif Skills[0] == AvailSkills[3][0] and MHP <= MMaxHP/5 and PlayerStats[5] >= AvailSkills[3][1]:
                        PATK = PlayerStats[9] * 5
                        PlayerStats[5] -= AvailSkills[3][1]
                        Text = PName + " used Victory Rush"
                    elif Skills[0] == AvailSkills[4][0] and PlayerStats[5] >= AvailSkills[4][1]:
                        PlayerStats[1] += PlayerStats[2]/5
                        if PlayerStats[1] > PlayerStats[2]:
                            PlayerStats[1] = PlayerStats[2]
                        PlayerStats[5] -= AvailSkills[4][1]
                        Text = PName + " used Restoration"
                    elif Skills[0] == AvailSkills[5][0] and PlayerStats[5] >= AvailSkills[5][1]:
                        PlayerStats[3] += PlayerStats[4]/5
                        if PlayerStats[3] > PlayerStats[4]:
                            PlayerStats[3] = PlayerStats[4]
                        PlayerStats[5] -= AvailSkills[5][1]
                        Text = PName + " used Anvil"
                    else:
                        Text = "Cannot do that"
                    wSurf.blit(MediumFont.render(Text, True, RED), TopRect3)
                    return PATK
                pygame.display.update()
        pygame.display.update()

def NFight(MLvl, EncText): #FIGHT
    global INFIGHT
    global STUN
    global BLEED
    global FLEE
    global BOSS
    global FAIL

    INIFGHT = 1
    RDMG = 0
    R = 1
    PDamageRect = pygame.Rect(700, 500, 5, 5)
    EDamageRect = pygame.Rect(200, 500, 5, 5)
    EStatusRect1 = pygame.Rect(650, 550, 32, 32)
    EStatusRect2 = pygame.Rect(700, 550, 32, 32)
    PStatusRect1 = pygame.Rect(200, 550, 32, 32)
    PStatusRect2 = pygame.Rect(240, 550, 32, 32)
    a = True
    while a == True:
        wSurf.blit(battleback,BackRect)
        EncTextRect = pygame.Rect(200, 100, 5, 5)
        wSurf.blit(EncText,EncTextRect)
        BattleRect = pygame.Rect(450, 500, 100, 50)
        wSurf.blit(battlebutton,BattleRect)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if BattleRect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
                    a = False
        pygame.display.update()

    if BOSS == 1:
        MHP = 100*MLvl #Monster Health Points
        MDMG = 10*(MLvl+MLvl) #Monster Damage
        MGOLD = 200*MLvl*MLvl #Monster Gold (PLayer receives if won)
        MEXP = 40*MLvl #Monster Experience (Player receives if won)
        MSPEED = 150 #Monster Speed (Determines who goes first)
        MMaxHP = MHP #Monster Max Health Points
        R = 1 #Rounds
    else:
        MHP = 50*MLvl #Setting up monster stats
        MDMG = 5*(MLvl+MLvl)
        MGOLD = 100*MLvl*MLvl
        MEXP = 20*MLvl
        MSPEED = 75 + (10*MLvl)
        MMaxHP = MHP
        R = 1 #Rounds
    while True:
        
        #Check for events
        PATK = int(0)
        RDMG = int(0)
        
        while PATK <= 0:
            #Print Screen Components
            ChangeTurn(MLvl, R)
            PrintPlayerStats()
            PrintMonsterStats(MHP,MDMG,MGOLD,MEXP,MSPEED,MMaxHP)
            Rend = MediumFont.render("Player Turn", True, GREEN)
            wSurf.blit(Rend, Rend.get_rect(center = (500, 100)))
            SettingsIcon() #Show settings icon
            if STUN > 0:
                wSurf.blit(stunstatus, EStatusRect2)
            if BLEED > 0:
                wSurf.blit(bleedstatus, EStatusRect1)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if 370 <= event.pos[0] <= 620 and 425 <= event.pos[1] <= 470:#Normal Attack
                        PATK = PlayerStats[9] 
                    elif 370 <= event.pos[0] <= 620 and 475 <= event.pos[1] <= 520:#Use skill
                        PATK = UseSkills(MHP,MMaxHP,PATK)
                    elif 370 <= event.pos[0] <= 620 and 533 <= event.pos[1] <= 577:#Use items
                        Equipment() 
                    elif 370 <= event.pos[0] <= 620 and 590 <= event.pos[1] <= 630:#Flee
                        ChangeTurn(MLvl, R)
                        Rend = MediumFont.render("You Fled!", True, RED) 
                        wSurf.blit(Rend, TopRect3)
                        pygame.display.update()
                        pygame.time.delay(1000)
                        INFIGHT = 0
                        FLEE = 1
                        return
                    elif 370 <= event.pos[0] <= 620 and 645 <= event.pos[1] <= 686:
                        print("NOTHING")

            pygame.display.update()

        if random.randint(1,2) == 1: #Check to see if player had a critical hit
            CritText = "CRITICAL HIT. Damage x2"
            CritRend = MediumFont.render(CritText, True, RED)
            wSurf.blit(CritRend,CritRend.get_rect(center = (500, 250))) #Tell player that there was a critical hit
            PATK *= 2 #Double damage when critical hit
            pygame.display.update()
        if BLEED > 0: #Checking if enemy is bleeding
            BleedDMG = PlayerStats[9]*3 / 6
            BleedDMGstr = str(BleedDMG)
            MHP -= BleedDMG
            BleedText = "Boss is bleeding. " + str(BleedDMG) + " damage taken"
            BleedRend = MediumFont.render(BleedText, True, PURPLE)
            wSurf.blit(BleedRend, BleedRend.get_rect(center = (500, 200))) #Show how much bleed damage was caused
            wSurf.blit(bleedstatus, EStatusRect1) #Show bleed icon over enemy health bar

        MHP -= PATK

        if MHP <= 0: #Check for win
            ChangeTurn(MLvl, R)
            PrintPlayerStats()
            PrintMonsterStats(MHP,MDMG,MGOLD,MEXP,MSPEED,MMaxHP)
            WonText = "You Won!" #Tell player the battle was won
            Rend = MediumFont.render(WonText, True, GREEN)
            wSurf.blit(Rend, Rend.get_rect(center = (500, 100)))
            PlayerStats[7] += MGOLD #Player gains gold equal to difficulty of battle
            PlayerStats[8] += MEXP #Player gains experience equal to difficulty of battle
            if PlayerStats[8] >= 100*PlayerStats[0]*PlayerStats[0]: #If player has reached next level
                wSurf.blit(MediumFont.render("Level up", True, GREEN), BottomLeftRect1)
                PlayerStats[0] += 1 #Player level += 1
                PlayerStats[8] = 0 #Player experience = 0
            INFIGHT = 0
            BOSS = 0
            FAIL = 0
            PlayerStats[5] = PlayerStats[6] #Player regains mana
            if len(BAG) <= MaxBagLen: #Check to see if bag is full
                RandomCategory = random.randint(0, len(Armor)-1)
                RandomItem = random.randint(0, len(Armor[RandomCategory])-1)
                Category = Armor[RandomCategory]
                BAG.append(Category[RandomItem][0]) #Player is rewarded a random item
                Text = str(Category[RandomItem][0]) #Tell player what item dropped
            else:
                Text = "Bag is full" #Tell player that bag is full
            Rend = MediumFont.render(Text, True, RED)
            wSurf.blit(Rend, Rend.get_rect(center = (500, 300)))
            pygame.display.update()
            pygame.time.delay(2000)
            return

        wSurf.blit(MediumFont.render("- " + str(PATK), True, RED), PDamageRect)

        pygame.display.update()
        pygame.time.delay(1000)

        ###ENEMY TURN###
        ChangeTurn(MLvl, R)
        PrintPlayerStats()
        PrintMonsterStats(MHP,MDMG,MGOLD,MEXP,MSPEED,MMaxHP)

        Rend = MediumFont.render("Enemy Turn", True, RED)
        wSurf.blit(Rend, Rend.get_rect(center = (500, 100)))
        SettingsIcon() #Show settings icon
        if STUN == 0: #Checking if enemy is stunned
            if PlayerStats[3] > 0: #If player has armor
                PlayerStats[3] = PlayerStats[3] - MDMG
            elif PlayerStats[3] <= 0: #If player armor is depleted
                PlayerStats[1] -= MDMG
            Rend = MediumFont.render("- " + str(MDMG), True, RED)
                
        elif STUN > 0: #If enemy is stunned, tells user.
            Rend = MediumFont.render("Enemy is stunned. No damage taken this round", True, GREEN)
            wSurf.blit(Rend, TopRect3)
            Rend = MediumFont.render("- 0", True, RED)
            wSurf.blit(stunstatus, EStatusRect2) #Show stun icon over enemy health bar
        wSurf.blit(Rend, EDamageRect)

        if PlayerStats[1] <= 0: #Check for defeat
            ChangeTurn(MLvl, R)
            PrintPlayerStats()
            PrintMonsterStats(MHP,MDMG,MGOLD,MEXP,MSPEED,MMaxHP)
            Rend = MediumFont.render("Defeat!", True, RED) #Tell player that the battle was lost
            wSurf.blit(Rend, TopRect1)
            PlayerStats[7] -= MGOLD / 2 #Player loses half of what he would have won
            INFIGHT = 0
            BOSS = 0
            FAIL = 1
            PlayerStats[1] = PlayerStats[2] #Player gains 100% health
            PlayerStats[5] = PlayerStats[6] #Player gains 100% mana
            if PlayerStats[7] < 0: #Player cannot have negative gold
                PlayerStats[7] = 0
            pygame.display.update()
            pygame.time.delay(1000)
            return
        
        if STUN > 0: #If enemy is stunned
            STUN -= 1 #Subtract 1 turn of stun (End of turn)
        if BLEED > 0: #If enemy is bleeding
            BLEED -= 1 #Subtract 1 turn of bleeding (End of turn)
        PlayerStats[5] += 5 #Gain 5 mana after each turn
        if PlayerStats[5] > PlayerStats[6]: #If mana is full
            PlayerStats[5] = PlayerStats[6] #Mana = Max mana
        R += 1 #Round number increases

        pygame.display.update()
        pygame.time.delay(1000)

    return

def DFight(FPlace,MLvl): #Dungeon Fight
    global FLEE
    global BOSS
    global FAIL
    BattleRect = pygame.Rect(450, 500, 100, 50)
    wSurf.blit(dungeonmenu,BackRect)
    if MLvl == 1: #Check which dungeon the player is in
        Text1 = "Welcome to the Training Dummy Dungeon."
    elif 2 <= MLvl <= 3:
        Text1 = "Welcome to the Fairy Dungeon."
    elif 4 <= MLvl <= 5:
        Text1 = "Welcome to the Pig Dungeon."
    elif 6 <= MLvl <= 7:
        Text1 = "Welcome to the Dragon Dungeon."
    Text2 = "You have to clear the whole dungeon to get dungeon specific rewards (Does not include gold and experience)"
    Text3 = "You will encounter 3 enemies and 1 boss in the dungeon"
    wSurf.blit(MediumFont.render(Text1, True, WHITE),TopLeftRect1)
    wSurf.blit(MediumFont.render(Text2, True, WHITE),TopLeftRect5)
    wSurf.blit(MediumFont.render(Text3, True, WHITE),TopLeftRect9)
    pygame.display.update()
    pygame.time.delay(1000)
    Stage = 1
    while Stage < 5:
        wSurf.blit(dungeonmenu,BackRect)
        if Stage <= 3:
            Text1 = "Get ready for stage: " + str(Stage) + "!"
            FType = 1
        elif Stage == 4:
            Text1 = "Get ready for the boss!"
            FType = 2
            BOSS = 1
        wSurf.blit(MediumFont.render(Text1, True, WHITE),LeftRect1)
        wSurf.blit(battlebutton, BattleRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if BattleRect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):  
                    FGen(FPlace, FType)
                    Stage += 1
        if FAIL == 1 or FLEE == 1: #Check for defeat or surrender
            Stage = 5

    #Dungeon is now complete
    if FAIL != 1 and FLEE != 1:
        print("Congratulations. You have completed the Dungeon!")
        if random.randint(1,3) == 1: #Check for a mystery box drop from the dungeon
            print("Wow! You found a mystery box in the dungeon!")
            if len(BAG) <= MaxBagLen:
                BAG.append(Items[2][0])
            else:
                print("Bag is full")
    else:
        print("Dungeon Failed")
        FLEE = 0
        FAIL = 0
        BOSS = 0

    return

def Armory():
    while True:
        wSurf.blit(armorymenu,BackRect)
        PrintPlayerStats()
        SettingsIcon()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 410 <= event.pos[0] <= 640 and 120 <= event.pos[1] <= 175:
                    Equipment()
                elif 410 <= event.pos[0] <= 640 and 192 <= event.pos[1] <= 245:
                    Skills()
##                elif 410 <= event.pos[0] <= 640 and 265 <= event.pos[1] <= 315:
##                    BackPack()
                elif 410 <= event.pos[0] <= 640 and 335 <= event.pos[1] <= 388:
                    return
        pygame.display.update()

def Equipment():
    MouseClick = False
    ShowText = False
    while True:
        wSurf.blit(equipmentmenu, BackRect)
        PrintPlayerStats()
        for x in range(len(PlayerEquipment)):
            Rect = pygame.Rect(EquipmentRect[x][0],EquipmentRect[x][1],80,90)
            Equip = pygame.image.load("Game Images/Pic Fin/Items/" + PlayerEquipment[x] + ".png")
            wSurf.blit(Equip, Rect)
            wSurf.blit(frame, Rect)
            if Rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                ShowText = True
                statstext = PlayerEquipment[x]
                stats = MediumFont.render(statstext, True, WHITE, BLACK)
                Rect = pygame.Rect(pygame.mouse.get_pos()[0]+20,pygame.mouse.get_pos()[1]+50, 5,5)
                if pygame.mouse.get_pos()[0] > 500:
                    Rect = pygame.Rect(500, pygame.mouse.get_pos()[1]+50, 5, 5)
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONUP:
                        MouseClick = True
                        ItemName = PlayerEquipment[x]
                        ChoiceText = "Would you like to unequip this item?"
        xcord = 50
        ycord = 100
        Ite = 0
        for y in range(len(BAG)):
            Rect = pygame.Rect(xcord, ycord,64,64)
            Pic = pygame.image.load("Game Images/Pic Fin/Items/" + BAG[y] + ".png")
            wSurf.blit(Pic, Rect)
            if Rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                ShowText = True
                statstext = BAG[y]
                stats = MediumFont.render(statstext, True, WHITE, BLACK)
                Rect = pygame.Rect(pygame.mouse.get_pos()[0]+20,pygame.mouse.get_pos()[1]+50, 5,5)
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONUP:
                        MouseClick = True
                        ItemName = BAG[y]
                        ChoiceText = "Would you like to equip this item?"                        
                        for x in range(len(Items)):
                            if BAG[y] in Items[x][0]:
                                ChoiceText = "Would you like to use this item?"
            Ite += 1
            if Ite == 5:
                xcord = 50
                ycord += 75
                Ite = 0
            else:
                xcord += 75
        xcord = 50
        ycord = 100
        Ite = 0
        for y in range(MaxBagLen):
            Rect = pygame.Rect(xcord,ycord,64,64)
            wSurf.blit(frame, Rect)
            Ite += 1
            if Ite == 5:
                xcord = 50
                ycord += 75
                Ite = 0
            else:
                xcord += 75
        if ShowText == True:
            Rect = pygame.Rect(pygame.mouse.get_pos()[0]+20,pygame.mouse.get_pos()[1]+50, 5,5)
            wSurf.blit(stats, Rect)
            ShowText = False
        pygame.display.update()
        if MouseClick == True:
            CHOICE = DeciderMenu(ChoiceText)
            MouseClick = False
            if CHOICE == 1:
                CHOICE = 0
                ##The Player Chose YES
                Decider(ChoiceText, ItemName)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 835 <= event.pos[0] <= 977 and 30 <= event.pos[1] <= 80:
                    return

def Decider(ChoiceText, ItemName):
    if ChoiceText == "Would you like to equip this item?": #If user is equipping an item
        EquipGear(ItemName)
    elif ChoiceText == "Would you like to unequip this item?": #If user is unequipping an item
        UnequipGear(ItemName)
    elif ChoiceText == "Would you like to use this item?": #If user is using an item
        UseItem(ItemName)
    elif ChoiceText == "Would you like to buy this item?": #If user is buying an item
        BuyItem(ItemName)
    pygame.display.update()
    pygame.time.delay(1000)

    return

def BuyItem(ItemName):
    for categories in Armor: #Check what category the item is - Categories: Helmets, Shoulders, Chests...
        for x in range(len(categories)): #Check each index in that particular category - info: Helmets[1], Helmets[2], Helmets[3]...
            if ItemName in categories[x]: #If the item is in that particular category - Helmets, Shoulders, Chests...
#                a = info.index(categories) #a = Index of the category in PlayerEquipment
                if categories[x][1] <= PlayerStats[7]: #If player has enough gold PlayerStats[7] = GOLD
                    PlayerStats[7] -= categories[x][1] #Subtract gold from player
                    BAG.append(categories[x][0]) #Add item to bag
                    print("Item has been added to bag") #Tell player that the item has been bought
                else: #If not enough gold
                    print("Not enough money") #Tell player that they don't have enough money

def UnequipGear(ItemName):
    if ItemName not in NoEquipment: #Cannot unequip starter gear
        BAG.append(ItemName) #Add the item to the bag
        a = PlayerEquipment.index(ItemName) #a = index of the item in PlayerEquipment[]
        PlayerEquipment[a] = NoEquipment[a] #Remove the item from equipped and add place holder for the item that was unequipped
        Rend = MediumFont.render("Item has been unequipped", True, RED) #Tell player that the item has been unequipped
        Rect  = pygame.Rect(300, 50, 5, 5)
        wSurf.blit(Rend, Rect)
        for categories in Armor: #Check category of item
            for info in categories: #Check information in that category
                if ItemName in info: #If item is in that category
                    if categories == Weapons: #If item is a weapon
                        PlayerStats[9] -= categories[info.index(ItemName)][2] #Subtract damage from playerstats
                    else: #If item is not a weapon
                        PlayerStats[3] -= categories[info.index(ItemName)][2] #Subtract armor from playerstats
    else: #If player is only wearing starter gear
        Rend = MediumFont.render("You cannot do that", True, RED) #Tell player that it cannot be done
        Rect  = pygame.Rect(300, 50, 5, 5)
        wSurf.blit(Rend, Rect)
    pygame.display.update() #Update Screen
    pygame.time.delay(1000) #Delay code to allow player to read the information

    return
    

def EquipGear(ItemName):
    Rect  = pygame.Rect(300, 50, 5, 5)
    for categories in Armor: #Check category of item
        for x in range(len(categories)): #Check information in that category
            if ItemName in categories[x]: #If item is in that category
                a = Armor.index(categories) #Returns index of the item in that list
                if categories[x][3] <= PlayerStats[0]: #If player level is high enough to equip the item
                    if PlayerEquipment[a] not in NoEquipment and categories == Weapons: #If player is wearing another weapon
                        BAG.append(PlayerEquipment[a]) #Remove the weapon and put it in the bag
                        PlayerStats[9]-= categories[x][2] #Subtract the damage from player stats [9] = Damage
                    elif PlayerEquipment[a] not in NoEquipment and categories != Weapons: #If player is wearing some other equipment
                        BAG.append(PlayerEquipment[a]) #Remove gear and put it in the bag
                        PlayerStats[3]-= categories[x][2] #Subtract armor from player stats [3] = Armor
                    if categories == Weapons: #If item is a weapon
                        PlayerStats[9]+= categories[x][2] #Add damage to player stats
                    else: #If item is not a weapon
                        PlayerStats[3] += categories[x][2] #Add armor to player stats
                        PlayerStats[4] += categories[x][2]
                    PlayerEquipment[a] = ItemName #Equip item
                    BAG.remove(ItemName) #Remove the item from the bag
                    Rend = MediumFont.render("Item has been equipped", True, GREEN) #Tell player item has been equipped
                else:
                    Rend = MediumFont.render("Level is too low", True, RED) #Tell player if his level is too low to equip
    
    wSurf.blit(Rend, Rect) #Add it to the screen
    pygame.display.update() #Update display
    pygame.time.delay(1000) #Delay to allow player to read information
    return

def UseItem(ItemName): #Use an item from the bag
    for x in Items:
        if ItemName in x:
            a = Items.index(x)
    if a == 0: #If item is health potion
        if PlayerStats[1] == PlayerStats[2]:
            Rend = MediumFont.render("Health already full", True, RED)
        else:
            PlayerStats[1] = PlayerStats[2]
            Rend = MediumFont.render("Item has been used", True, RED)
            BAG.remove(ItemName)
    if a == 1: #If item is mana potion
        if PlayerStats[5] == PlayerStats[6]:
            Rend = MediumFont.render("Mana already full", True, RED)
        else:
            PlayerStats[5] = PlayerStats[6]
            Rend = MediumFont.render("Item has been used", True, RED)
            BAG.remove(ItemName)
    if a == 2 or a == 3: #If item is myestery box or key
        if 'Key' in BAG:
            if 'Mystery Box' in BAG:
                OpenMysteryBox()
                Text = "Mystery Box has been opened"
            else:
                Text = "You don't have a mystery box"
        else:
            Text = "You don't have a key"
    wSurf.blit(MediumFont.render(Text, True, RED), TopRect1)
    pygame.display.update()
    pygame.time.delay(1000)
    return

def OpenMysteryBox():
    IndexBox = BAG.index(Items[2][0])
    IndexKey = BAG.index(Items[3][0])
    BAG.remove(Items[2][0])
    BAG.remove(Items[3][0])
    Chance = random.randint(0,100)
    if 0 < Chance <= 20:
        RandomCategory = random.randint(0, len(Armor)-1)
        RandomItem = random.randint(0,100)
        if 0 < RandomItem <= 80:
            BAG.append(Armor[RandomCategory][0][0])
        elif 80 < RandomItem < 90:
            BAG.append(Armor[RandomCategory][-2][0])
        else:
            BAG.append(Armor[RandomCategory][-1][0])
        Text = "You got: "+str(BAG[-1])
    elif 20 < Chance <= 90:
        RandomNumb = random.randint(0,20)
        PlayerStats[7] += RandomNumb*100
        Text = "You got: "+str(RandomNumb*100)+" Gold"
    elif 90 < Chance <= 100:
        RandomNumb = random.randint(0,20)
        PlayerStats[7] += RandomNumb*500
        Text = "You got: "+str(RandomNumb*500)+" Gold"
    wSurf.blit(MediumFont.render(Text,True, RED), TopRect2)
    pygame.display.update()
    return
        

def DeciderMenu(ChoiceText): #Displays a prompt for the player
    Rect = pygame.Rect(300, 250, 5, 5)
    TextRend = HandFont.render(ChoiceText, True, BLACK)
    wSurf.blit(decidermenu, Rect)
    wSurf.blit(TextRend, MiddleRect1)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 320 < event.pos[0] < 403 and 400 < event.pos[1] < 436:
                    CHOICE = 0
                    return CHOICE
                elif 574 < event.pos[0] < 676 and 400 < event.pos[1] < 436:
                    CHOICE = 1
                    return CHOICE

def Skills(): #Let's player read about all the different kinds of skills
    ComingSoon()
    return

##def BackPack():
##    wSurf.blit(backpackmenu, BackRect)
##    PrintPlayerStats()
##    while True:
##        for event in pygame.event.get():
##            if event.type == MOUSEBUTTONUP:
##                if 800 <= event.pos[0] <= 968 and 30 <= event.pos[1] <= 155:
##                    return
##
##        pygame.display.update()

def PrintEquipment(): #Displays equipment on the screen (Under armory --> Equipment menu)
    for x in range(len(EquipmentRect)):
        Rect = pygame.Rect(EquipmentRect[x-1][0],EquipmentRect[x-1][1],5,5)
        Equip = pygame.image.load("Game Images/Pic Fin/Items/" + PlayerEquipment[x-1] + ".png")
        wSurf.blit(Equip, Rect)
        
    return

def Market():
    while True:
        wSurf.blit(marketmenu,BackRect)
        PrintPlayerStats()
        SettingsIcon()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 3 <= event.pos[0] <= 240 and 160 <= event.pos[1] <= 205:
                    WeaponShop()
                    return
##                elif 3 <= event.pos[0] <= 240 and 285 <= event.pos[1] <= 330:
##                    ItemShop()
##                    return
                elif 3 <= event.pos[0] <= 240 and 343 <= event.pos[1] <= 388:
                    BlackSmith()
                    return
                elif 3 <= event.pos[0] <= 240 and 405 <= event.pos[1] <= 450:
                    return

        pygame.display.update()

def WeaponShop():
    while True:
        a = 0
        wSurf.blit(weaponshop, BackRect)
        PrintPlayerStats()
        xcord = 75
        ycord = 200

        for categories in Armor:
            for info in categories:
                Rect = pygame.Rect(xcord, ycord, 64, 64)
                Pic = pygame.image.load("Game Images/Pic Fin/Items/"+info[0]+".png")
                wSurf.blit(Pic,Rect)
                wSurf.blit(frame,Rect)
                ycord += 75
            xcord += 87
            ycord = 200
        xcord = 75
        ycord = 200
        for categories in Armor:
            for info in categories:
                Rect = pygame.Rect(xcord, ycord, 64, 64)
                if Rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONUP:
                            a = 1
                            ItemName = info[0]
                            ChoiceText = "Would you like to buy this item?"
                    stats = MediumFont.render(str(info[0]), True, WHITE, BLACK)
                    xRect = pygame.Rect(pygame.mouse.get_pos()[0]+20,pygame.mouse.get_pos()[1]+50, 5,5)
                    if pygame.mouse.get_pos()[0] > 500:
                        xRect = pygame.Rect(500,pygame.mouse.get_pos()[1]+50, 5,5)
                    wSurf.blit(stats, xRect)
                ycord += 75
            xcord += 87
            ycord = 200
        if a == 1:
            CHOICE = DeciderMenu(ChoiceText)
            if CHOICE == 1:
                Decider(ChoiceText, ItemName)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 21 <= event.pos[0] <= 153 and 33 <= event.pos[1] <= 92:
                    return

def BlackSmith():
    wSurf.blit(blacksmithmenu, BackRect)
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 80 <= event.pos[0] <= 320 and 635 <= event.pos[1] <= 690:
                    wSurf.blit(blacksmithmenu2, BackRect)
                    while True:
                        for event in pygame.event.get():
                            if event.type == MOUSEBUTTONUP:
                                return
                        pygame.display.update()
                if 665 <= event.pos[0] <= 906 and 637 <= event.pos[1] <= 690:
                    BlackSmith2()
                    return
        pygame.display.update()

def BlackSmith2():
    wSurf.blit(blacksmithmenu3, BackRect)
##    pygame.display.update()
##    pygame.time.delay(1000)
##    wSurf.blit(blacksmithmenu2, BackRect)
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                return
        pygame.display.update()

        
        

def Stats():
    a = 55
    wSurf.blit(statsmenu,BackRect)
    for x in range(len(PlayerStats)):
        Rect1 = pygame.Rect(75, a, 5, 5)
        Rect2 = pygame.Rect(500, a, 5, 5)
        Text1 = str(PlayerStatsDef[x-1])
        Text2 = str(PlayerStats[x-1])
        Rend1 = MediumFont.render(Text1, True, WHITE)
        Rend2 = MediumFont.render(Text2, True, WHITE)
        wSurf.blit(Rend1,Rect1)
        wSurf.blit(Rend2,Rect2)
        a += 50
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 777 <= event.pos[0] <= 990 and 10 <= event.pos[1] <= 95:
                    return

        pygame.display.update()
    
                
def SaveMenu():
    file1 = open("Game Files/SaveGame1.txt","r")
    file2 = open("Game Files/SaveGame2.txt","r")
    file3 = open("Game Files/SaveGame3.txt","r")
    Save1 = file1.readlines()
    Save2 = file2.readlines()
    Save3 = file3.readlines()

    print("Which slot would you like to save your game to?")
    SaveText1 = str("1: " + Save1[-1] + " - Player Name: " + Save1[-2])
    SaveText2 = str("2: " + Save2[-1] + " - Player Name: " + Save2[-2])
    SaveText3 = str("3: " + Save3[-1] + " - Player Name: " + Save3[-2])

    file1.close()
    file2.close()
    file3.close()

    SaveRect1 = pygame.Rect(175 , 125, 5, 5)
    SaveRect2 = pygame.Rect(175 , 335, 5, 5)
    SaveRect3 = pygame.Rect(175 , 540, 5, 5)

    SaveRend1 = MediumFont.render(SaveText1, True, WHITE)
    SaveRend2 = MediumFont.render(SaveText2, True, WHITE)
    SaveRend3 = MediumFont.render(SaveText3, True, WHITE)
    
    BackRect = pygame.draw.rect(wSurf, BLACK, (0,0,5,5))
    wSurf.blit(savemenu,BackRect)
    wSurf.blit(SaveRend1, SaveRect1)
    wSurf.blit(SaveRend2, SaveRect2)
    wSurf.blit(SaveRend3, SaveRect3)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 115 <= event.pos[0] <= 887 and 57 <= event.pos[1] <= 222:
                    SaveGame1()
                    print("Save 1")
                    return
                if 115 <= event.pos[0] <= 887 and 267 <= event.pos[1] <= 432:
                    SaveGame2()
                    print("Save 2")
                    return
                elif 3 <= event.pos[0] <= 240 and 477 <= event.pos[1] <= 642:
                    SaveGame3()
                    print("Save 3")
                    return
                else:
                    return

def SaveGame1():
    file = open("Game Files/SaveGame1.txt","w+")
    for x in PlayerStats:
        xstr = str(x)
        file.writelines(xstr)
        file.writelines("\n")
    file.writelines(PName)
    file.writelines("\n")
    file.writelines(SaveGameName)

    file.close()

    return

def SaveGame2():
    file = open("Game Files/SaveGame2.txt","w+")
    for x in PlayerStats:
        xstr = str(x)
        file.writelines(xstr)
        file.writelines("\n")
    file.writelines(PName)
    file.writelines("\n")
    file.writelines(SaveGameName)

    file.close()

    return

def SaveGame3():
    file = open("Game Files/SaveGame3.txt","w+")
    for x in PlayerStats:
        xstr = str(x)
        file.writelines(xstr)
        file.writelines("\n")
    file.writelines(PName)
    file.writelines("\n")
    file.writelines(SaveGameName)

    file.close()

    return
            
def LoadMenu():
    file1 = open("Game Files/SaveGame1.txt","r+")
    file2 = open("Game Files/SaveGame2.txt","r+")
    file3 = open("Game Files/SaveGame3.txt","r+")
    Load1 = file1.readlines()
    Load2 = file2.readlines()
    Load3 = file3.readlines()

    print("Which game would you like to load?")
    SaveText1 = str("1: " + Load1[-1] + " - Player Name: " + Load1[-2])
    SaveText2 = str("2: " + Load2[-1] + " - Player Name: " + Load2[-2])
    SaveText3 = str("3: " + Load3[-1] + " - Player Name: " + Load3[-2])

    file1.close()
    file2.close()
    file3.close()

    SaveRect1 = pygame.Rect(175 , 125, 5, 5)
    SaveRect2 = pygame.Rect(175 , 335, 5, 5)
    SaveRect3 = pygame.Rect(175 , 540, 5, 5)

    SaveRend1 = MediumFont.render(SaveText1, True, WHITE)
    SaveRend2 = MediumFont.render(SaveText2, True, WHITE)
    SaveRend3 = MediumFont.render(SaveText3, True, WHITE)
    
    BackRect = pygame.draw.rect(wSurf, BLACK, (0,0,5,5))
    wSurf.blit(savemenu,BackRect)
    wSurf.blit(SaveRend1, SaveRect1)
    wSurf.blit(SaveRend2, SaveRect2)
    wSurf.blit(SaveRend3, SaveRect3)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 115 <= event.pos[0] <= 887 and 57 <= event.pos[1] <= 222:
                    LoadGame1()
                    return
                elif 115 <= event.pos[0] <= 887 and 267 <= event.pos[1] <= 432:
                    LoadGame2()
                    return
                elif 3 <= event.pos[0] <= 240 and 477 <= event.pos[1] <= 642:
                    LoadGame3()
                    return
                else:
                    return

def LoadGame1():
    global PName
    
    file = open("Game Files/SaveGame1.txt","r+")
    LoadGame = file.readlines()
    
    for x in range(len(PlayerStats)):
        PlayerStats[x] = int(LoadGame[x])
        
    PName = LoadGame[-1]

    file.close()
        
    return

def LoadGame2():
    global PName
    
    file = open("Game Files/SaveGame2.txt","r+")
    LoadGame = file.readlines()
    
    for x in range(len(PlayerStats)):
        PlayerStats[x] = int(LoadGame[x])
        
    PName = LoadGame[-1]

    file.close()
        
    return

def LoadGame3():
    global PName
    
    file = open("Game Files/SaveGame3.txt","r+")
    LoadGame = file.readlines()
    
    for x in range(len(PlayerStats)):
        PlayerStats[x] = int(LoadGame[x])
        
    PName = LoadGame[-1]

    file.close()
        
    return

def EndGame():
    wSurf.blit(endgamemenu, BackRect)
    Rect = pygame.Rect(150, 20, 5, 5)
    Text = "Thanks for Playing. Click anywhere to quit."
    Rend = BigFont.render(Text, True, BLACK)
    wSurf.blit(Rend,Rect)
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def MainMenu():
    while True:
        wSurf.blit(mainmenu,BackRect)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if 560 < event.pos[0] < 725 and 195 < event.pos[1] < 260:
                    return
                elif 560 < event.pos[0] < 725 and 302 < event.pos[1] < 366:
                    SaveMenu()
                elif 560 < event.pos[0] < 725 and 410 < event.pos[1] < 475:
                    LoadMenu()
                elif 560 < event.pos[0] < 725 and 518 < event.pos[1] < 580:
                    pygame.mixer.music.stop()
                    EndGame()
        pygame.display.update()
    return

def ComingSoon():
    wSurf.blit(comingsoonmenu, BackRect)
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                return
        pygame.display.update()

def PlayMusic():
    global PLACE
    pygame.mixer.music.load("Music/"+PLACE+".mp3")
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.play()

def SettingsIcon():
    Rect = pygame.Rect(900, 20, 64, 64)
    wSurf.blit(settings, Rect)
    if Rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                Settings()
    pygame.display.update()
    return

def Settings():
    global MUSIC
    global VOLUME
    while True:
        wSurf.blit(settingsmenu, BackRect)
        VOLUME = pygame.mixer.music.get_volume()
        MusicPlayerRect = pygame.Rect(450, 200, 64, 64)
        MusicPlayer = pygame.image.load("Game Images/Pic Fin/Misc/Music Player.png")
        MusicVolume = LargeFont.render("Volume:  "+str(VOLUME), True, BLACK)
        MusicVolumeRect = pygame.Rect(300, 300, 64, 64)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if MusicPlayerRect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
                    if MUSIC == True:
                        pygame.mixer.music.pause()
                        MUSIC = False
                    elif MUSIC == False:
                        pygame.mixer.music.unpause()
                        MUSIC = True
                elif MusicVolumeRect.collidepoint(pygame.mouse.get_pos()[0]-50, pygame.mouse.get_pos()[1]):
                    pygame.mixer.music.set_volume(VOLUME+0.05)
                elif MusicVolumeRect.collidepoint(pygame.mouse.get_pos()[0]+50, pygame.mouse.get_pos()[1]):
                    pygame.mixer.music.set_volume(VOLUME-0.05)
                elif 900 < event.pos[0] < 1000 and 0 < event.pos[1] < 100:
                    return
        wSurf.blit(MusicPlayer,MusicPlayerRect)
        wSurf.blit(MusicVolume,MusicVolumeRect)
        pygame.display.update()
        print(pygame.mixer.music.get_busy())
    return

def main():
    FileSetup()
#    global PLACE
#    PLACE = 'Main'
#    PlayMusic()
    MainMenu()
    while True:
        PlayMenu()
    pygame.display.update()
    mclock.tick(40)

main()
