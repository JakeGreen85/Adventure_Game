#Equipment
NoEquipment = ['no helmet','no shoulders','Old Black Shirt (0 Armor)','no hands','no wrist','no belt','Ripped Leather Pants (0 Armor)','Worn Sandals (0 Armor)','Fists']
EquipmentRect = [[615, 35], [730, 105], [500, 100], [750, 252], [475, 243], [495, 415], [745, 430], [616, 592], [472, 585]]
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
Items = [['Healing Potion (100%)',20],['Mana Potion (100%)',20],['Mystery Box',100],['Key',100]]
BAG = ["Beginner's Sword (DMG 10)(Req. Level 1)"]

#Skills
AvailSkills = ['Pummel (20 Mana)(200% Player Damage)(Req. Level 1)','Slash (15 Mana)(300% Player Damage over 6 rounds)(Req. Level 2)','Bash (30 Mana)(100% Player Damage + Stuns enemy for 2 rounds)(Req. Level 3)','Victory Rush (30 Mana, Enemy health < 20%)(500% Player Damage)(Req. Level 4)','Restoration (20 Mana)(Heals 20% of player health)(Req. Level 5)','Anvil (20 Mana)(Repairs 20% of Player Armor)(Req. Level 6)']
AvailSkillsCost = [20,15,30,30,20,20]
AvailSkillsLvl = [1,2,3,4,5,6]
PlayerSkills = [AvailSkills[0],'none','none']
SkillsCost = [AvailSkillsCost[0],0,0]
#NEW#
AvailSkills = [['Pummel (20 Mana)(200% Player Damage)(Req. Level 1)',20,1],['Slash (15 Mana)(300% Player Damage over 6 rounds)(Req. Level 2)',15,2],['Bash (30 Mana)(100% Player Damage + Stuns enemy for 2 rounds)(Req. Level 3)',30,3],['Victory Rush (30 Mana, Enemy health under 20%)(500% Player Damage)(Req. Level 4)',30,4],['Restoration (20 Mana)(Heals 20% of player health)(Req. Level 5)',20,5],['Anvil (20 Mana)(Repairs 20% of Player Armor)(Req. Level 6)',20,6]]
PlayerSkills = [AvailSkills[0],'none','none']
SkillsCost = [PlayerSkills[0][1],0,0]

#Player
ULvl1 = [" ","Skills: ",AvailSkills[0]," ","Weapons: ",Weapons[0]," ","Equipment: ",Chests[0], Hands[0], Pants[0], Feet[0]]
ULvl2 = [" ","Skills: ",AvailSkills[1]," ","Weapons: ",Weapons[1]]
ULvl3 = [" ","Skills: ",AvailSkills[2]," ","Weapons: ",Weapons[2]," ","Equipment: ",Helmets[0],Shoulders[0],Chests[1],Hands[1],Wrists[0],Belts[0],Pants[1],Feet[1]]
ULvl4 = [" ","Skills: ",AvailSkills[3]," ","Weapons: ",Weapons[3]]
ULvl5 = [" ","Skills: ",AvailSkills[4]," ","Weapons: ",Weapons[4]," ","Equipment: ",Helmets[1],Shoulders[1],Chests[2],Hands[2],Wrists[1],Belts[1],Pants[2],Feet[2]]
ULvl6 = [" ","Skills: ",AvailSkills[5]," ","Weapons: ",Weapons[5]]
UNLOCK = [ULvl1,ULvl2,ULvl3,ULvl4,ULvl5,ULvl6]

Armor = [Helmets,Shoulders,Chests,Hands,Wrists,Belts,Pants,Feet,Weapons,Items] ###What did I use this for in the original code??

#####################################################

#Equipment
NoEquipment = ['no helmet','no shoulders','Old Black Shirt (0 Armor)','no hands','no wrist','no belt','Ripped Leather Pants (0 Armor)','Worn Sandals (0 Armor)','Fists']
EquipmentRect = [[472, 585],[615, 35],[500, 100],[730, 105],[475, 243],[750, 252], [495, 415], [745, 430], [616, 592]]
BagRect = [[55, 100], [150, 100], [250, 100], [340, 100], [55, 220], [150, 220], [250, 220], [340, 220], [55, 335], [150, 335], [250, 335], [340, 335], [55, 450], [150, 450], [250, 450], [340, 450]]
PlayerEquipment = ['no helmet','no shoulders','Old Black Shirt (0 Armor)','no hands','no wrist','no belt','Ripped Leather Pants (0 Armor)','Worn Sandals (0 Armor)','Fists']
PlayerCatArmor = [0,0,0,0,0,0,0,0]
ArmorTypes = ['Helmet','Shoulders','Chest','Hands','Wrists','Belts','Pants','Feet']
Helmets = ["Handcrafted Iron Helmet (50 Armor)(Req. Level 3)","Dragon's Head (150 Armor)(Req. Level 5)"]
PHelmets = [1500,5000]
AHelmets = [50,150]
HelmetsLvl = [3,5]
Shoulders = ["Handcrafted Iron Pads (50 Armor)(Req. Level 3)","Dragon's Scales (150 Armor)"]
PShoulders = [1500,5000]
AShoulders = [50,150]
ShouldersLvl = [3,5]
Chests = ["Leather Chest Plate (10 Armor)(Req. Level 1)","Handcrafted Iron Plate (50 Armor)(Req. Level 3)","Dragon's Chest (150 Armor)(Req. Level 5)"]
PChests = [100,1500,5000]
AChests = [10,50,150]
ChestsLvl = [1,3,5]
Hands = ["Leather Gloves (10 Armor)(Req. Level 1)","Handcrafted Iron Gloves (50 Armor)(Req. Level 3)","Dragon's Claws (150 Armor)(Req. Level 5)"]
PHands = [100,1500,5000]
AHands = [10,50,150]
HandsLvl = [1,3,5]
Wrists = ["Handcrafted Iron Bands (50 Armor)(Req. Level 3)","Dragon's Cuffs (150 Armor)(Req. Level 5)"]
PWrists = [1500,5000]
AWrists = [50,150]
WristsLvl = [3,5]
Belts = ["Handcrafted Iron Plated Belt (50 Armor)(Req. Level 3)","Dragon's Waist (150 Armor)(Req. Level 5)"]
PBelts = [1500,5000]
ABelts = [50,150]
BeltsLvl = [3,5]
Pants = ["Leather Pants (10 Armor)(Req. Level 1)","Handcrafted Iron Pants (50 Armor)(Req. Level 3)","Dragon's Legs (150 Armor)(Req. Level 5)"]
PPants = [100,1500,5000]
APants = [10,50,150]
PantsLvl = [1,3,5]
Feet = ["Leather Sandals (10 Armor)(Req. Level 1)","Handcrafted Iron Shoes (50 Armor)(Req. Level 3)","Dragon's Feet (150 Armor)(Req. Level 5)"]
PFeet = [100,1500,5000]
AFeet = [10,50,150]
FeetLvl = [1,3,5]
PArmor = [PHelmets,PShoulders,PChests,PHands,PWrists,PBelts,PPants,PFeet]
AArmor = [AHelmets,AShoulders,AChests,AHands,AWrists,ABelts,APants,AFeet]
ArmorLvl = [HelmetsLvl,ShouldersLvl,ChestsLvl,HandsLvl,WristsLvl,BeltsLvl,PantsLvl,FeetLvl]

#Skills
AvailSkills = ['Pummel (20 Mana)(200% Player Damage)(Req. Level 1)','Slash (15 Mana)(300% Player Damage over 6 rounds)(Req. Level 2)','Bash (30 Mana)(100% Player Damage + Stuns enemy for 2 rounds)(Req. Level 3)','Victory Rush (30 Mana, Enemy health < 20%)(500% Player Damage)(Req. Level 4)','Restoration (20 Mana)(Heals 20% of player health)(Req. Level 5)','Anvil (20 Mana)(Repairs 20% of Player Armor)(Req. Level 6)']
AvailSkillsCost = [20,15,30,30,20,20]
AvailSkillsLvl = [1,2,3,4,5,6]
PlayerSkills = [AvailSkills[0],'none','none']
SkillsCost = [AvailSkillsCost[0],0,0]

#Weapons
Weapons = ["Beginner's Sword (DMG 10)(Req. Level 1)","Beginner's Axe (DMG 15)(Req. Level 2)","Handcrafted Sword of the Lion (DMG 30)(Req. Level 3)","Handcrafted Axe of the Tiger (DMG 45)(Req. Level 4)","Sword of the Dragon's Tail (DMG 70)(Req. Level 5)","Axe of the Dragon's Tooth (DMG 100)(Req. Level 6)"]
WPrice = [100,200,3000,4500,10000,15000]
WDMG = [10,15,30,45,70,100]
WLvl = [1,2,3,4,5,6]

#Items
Items = ['Healing Potion (100%)','Mana Potion (100%)','Mystery Box','Key']
IPrice = [20,20,100,100]
BAG = []

#Player
ULvl1 = [" ","Skills: ",AvailSkills[0]," ","Weapons: ",Weapons[0]," ","Equipment: ",Chests[0], Hands[0], Pants[0], Feet[0]]
ULvl2 = [" ","Skills: ",AvailSkills[1]," ","Weapons: ",Weapons[1]]
ULvl3 = [" ","Skills: ",AvailSkills[2]," ","Weapons: ",Weapons[2]," ","Equipment: ",Helmets[0],Shoulders[0],Chests[1],Hands[1],Wrists[0],Belts[0],Pants[1],Feet[1]]
ULvl4 = [" ","Skills: ",AvailSkills[3]," ","Weapons: ",Weapons[3]]
ULvl5 = [" ","Skills: ",AvailSkills[4]," ","Weapons: ",Weapons[4]," ","Equipment: ",Helmets[1],Shoulders[1],Chests[2],Hands[2],Wrists[1],Belts[1],Pants[2],Feet[2]]
ULvl6 = [" ","Skills: ",AvailSkills[5]," ","Weapons: ",Weapons[5]]
UNLOCK = [ULvl1,ULvl2,ULvl3,ULvl4,ULvl5,ULvl6]

Armor = [Helmets,Shoulders,Chests,Hands,Wrists,Belts,Pants,Feet,Weapons,Items] ###What did I use this for in the original code??
