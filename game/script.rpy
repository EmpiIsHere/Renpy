# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#Code for resize character.

#akemi character
image akemi def = im.Scale("akemi_def.png", 679, 900)
image akemi 2 = im.Scale("akemi_2.png", 679, 900)
image akemi 3 = im.Scale("akemi_3.png", 679, 900)
image akemi 4 = im.Scale("akemi_4.png", 679, 900)
# Princess aoi
image princess def = im.Scale("princess_def.png", 679, 900)
image princess 1= im.Scale("princess_1.png", 679, 900)
image princess 2 = im.Scale("princess_2.png", 679, 900)
image princess 3 = im.Scale("princess_3.png", 679, 900)
# Himeko
image himiko def = im.Scale("himiko_def.png", 679, 900)
image himiko 1= im.Scale("himiko_1.png", 679, 900)
image himiko 2 = im.Scale("himiko_2.png", 679, 900)
image himiko 3 = im.Scale("himiko_3.png", 679, 900)
define n = Character("Narrator")

#background
image bg forest1 = "forest1.png"
image bg deepforest = "deepforest.png"
image bg deepforestsword = "deepforestsword.png"
image bg cave1 = "cave.png"
image bg meetingelf ="meetingelf.png"
image bg incavegold ="incavegold.png"
image bg mountain = "mountain.png"
image bg dcave = "dwarf_deep cave.png"


#asset
image bg ring = "ring_final.png"
image bg sword = "sword_final.png"

define a = Character("Akemi",color="546569") 

define p = Character("Aoi") 

define pra = Character("Princess Aoi",color="d8aec5") 

define h = Character("Himeko",color="546569") 

define n = Character("Narrator") 

define k = Character("King Throin") 

define s = Character("Scholar") 

define g = Character("General Ragnor") 

define grdelf  = Character("Elf Guard") 

define dwarfgrd=Character("Dwarf Guard")

define durin=Character("Durin")

define k= = Character("King Throin")

define min1 = Character("Minion 1")

define min2 = Character("Minion 2")



# The game starts here.

label start:

scene black
n"Summer has passed, and another school year is approaching. Students are excited as the new year will embrace them."
n"Everyone’s busy with their requirements. And there’s one student who made the room a bit odd as she walks on"
show akemi def
n"Akemi is an ordinary student. She always wears her jolliest smile."

label branch_2:




label branch_3:
n"As Akemi and Princess Aoi have decided to start their adventure journey."
show princess def
pra"Thank you for helping me Akemi..."
hide princess def
show akemi def
a"It okey your welcome.... so, are we going straight to kingdom of Azurevale?"
hide akemi def
pra"No, Himeko is a powerful magician simple physical and magical attack won't hurt her."
a"So how will I be able to beat Himeko then?"
pra"We need to get the 3 legendary items that can only be wielded by a hero who came far from our world and that is you. "
a"So, what are these 3 legendary items. Then."
pra"The first is the blade of Ethereal Fang the legend tells that it has been forge and bless by the ancient gods and imbued with the power to pierce through darkness itself."
pra"The second item is the Necklace of Valor it is made by the most skilled dwarf and has the ability to increase physical and magical power to its full potential."
a"What about the third item."
pra"Princess Aoi: I can't tell you yet. In order to obtain the last item, you need to have the first two. You need their combined power before you can even attempt to retrieve the third item."
a"I see..."
pra"    so witch of the two item you want to get first. "
    menu:
        "Blades of Ethernal Fang ":
            jump choice1_yes

        "Necklace of Valor":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

    jump branch_4

    label choice1_no:

        $ menu_flag = False

    jump branch_5
 
#Blade of Ethernal Fang
label branch_4:
n"Ethereal Fang legend speak that it is resting place deep within the heart of mystical forest known as the Whispering Woods and the location of the forest is only know the elder elf wich is located at Faewood."
#Princess aoi
show princess def
pra"We must travel deep in the forest to meet the elf elder and ask the Whispering woods."
hide princess def
n"Upon reaching the guard gates of the Faewood they met with a vigilant sentry, wary of outsider. "
grdelf"Stop right there, who are you and state your buisness."
n"With Aoi regal presence lending credibility and royal etiquette"
show princess def
pra"Good day to you sir, I am Princess Aoi from the kingdom of Azurevale, we humbly ask request to meet and ask guidance of the elf elder."
grdelf"Wait here i will ask for the chef of the village."
n"As the time Akemi and Princess Aoi for the approval of the chef village. "
grdelf"You may enter and be careful"



#Necklace of Valor
label branch_5:
n"As Akemi and Princess Aoi set their journey to get the Necklace of Valor from the dwarf and the name of the kingdom is Ironforge."
show princess def
pra"We need to travel to the Ironspine mountain and go to the Ironforge kingdom and meet their king his name is King Throin. "
    pra"We can easily  go inside the and meet King Throin because my father and King Throin are friends."
    hide princess def
    show akemi def
    a"I am excited to enter the kingdowm of dwarfs, its like a real fantasy. "
    hide akemi
    show princess def
    pra"Yes, and i also have a friend in the kingdom."
    hide princess def
    n"Akemi and Princess Aoi got closer to the entrance of the the dwarf kingdom."
    show princess def
    pra"Here we are the Ironforge Kingdom."
    hide  princess def
    show akime def
    a"Wow look at the size of the wall and the gate is so huge."
    hide akemi def
    n"As Akemi and princess aoi got closer one of the guards recognise princess Aoi."
    
    dwarfgrd"Princess Aoi is that you thank god your safe its been to long"
    
    n"Princess Aoi smiled with relief as she explained their quest to retrieve the Necklace of Valor and save her kingdom from Himeko's darkness."
    
    pra"It has been too long indeed Durin."
    
    durin"What brings you here in Ironforge, Is she your companion."

    pra"Yes she is and she is also my friend and the hero the is summoned."
    
    a"Hello nice to meet you Durin."
    
    durin"Nice to meet you too."
    
    pra" We came hoping to meet King Throin and ask for the Necklace of Valor to help me and the hero to defeat Himeko that invaded their Kingdome."
    
    n"Durin nods and promise to Princess Aoi"
    
    durin"Fear not, Princess Aoi. As your friend and ally, I shall see to it that you and your companion are granted an audience with King Throin. "
    
    pra"Thank you Durin."
    
    n"With Durins guidance Akemi and Princess Aoi are escorted through the bustling street of ironforge."
    
    a"Look at the busy street Aoi, there are a lot of markets and lot of weapons on display and a lot of beautiful jewelry and shining armor its really like a fantasy."
    
    pra"Yes, there's a lot of people than the last time i visit here."
    
    n"As they approach the imposing gate of the royal castle, Akemi and Princess aoi was able to meet King Throin."
    
    k"Welcome, it an honor to meet you once more and to meet your esteemed companion"
    
    pra"t's an honor to meet you to king Throin allow me to introduce my companion, her name is Akemi she is the hero i summon"
    
    a"It's a pleasure to meet you, King Throin."
    
    n"King Throin regarded Akemi with a solemn gaze, acknowledging the hero's presence with a hint of respect."
    
    k"Akemi, It's an honor to meet you."
    
    n"Princess Aoi continued her tone urgently."
    
    pra"Your Majesty, we seek you aid in offering us the Neklace of valor. "
    
    k"I fear I must deliver grim tidings"
    
    n"The king tell them with a heavy sorrow."
    
    k"The Necklace of Valor was stolen and destroyed form us by one of Himeko men in the past few months by General Ragnor a cunnig and ruthless adversary."
    
    n"Princess Aoi heart sank at the news, but before she could despair King Throin spoke again, his tine resolute."
    
    k"However, There’s another way. We can forge a new necklace, one that is more powerful than its predecessor."
    
    n"A glimmer of hope sparked in Princess Aoi’s heart, but their joy was short-lived as the ground trembled, signaling impending danger."
    
    dwarfgrd" We are under attack!"
    
    n"One of the guards shouted, with resolved in their hearts Akemi and Princess Aoi rushed to defense of Ironforge their swords drawn and their magic ablaze."
    
    n"Outside the castle walls, they were met with a horde of monstrous creatures, their eyes filled with malice and hunger for battle."
    
    n"As Akemi and Princess Aoi fought bravely against the onslaught, King Throin approached them with a grim expression."
    
    k"Our enemies seek the gemstone needed to forge the new necklace."
    
    k"It lies deep within the mining caves, but the entrance is heavily guarded by General Ragnor's minions."
    
    n"Narator: Princess Aoi's determination burned brighter than ever as she turned to Akemi, her eyes shining with resolve."
    
    pra"We must retrieve the gemstone, no matter the cost." 
    
    n"  With the king's blessing and the support of the dwarven warriors, Akemi and Princess Aoi ventured into the mining caves, their hearts ablaze with courage and hope."
    
    n"Akemi and Princess Aoi set forth into the depths of the mining caves, their hearts set ablaze with the fires of courage and hope."
    
    a"We have faced greater dangers before, Princess. Together, we can overcome any obstacle."
    
    pra"You're right, Akemi. With the strength of our friendship and the bravery of the dwarves, we will prevail."
    
    n"The resolve in their voices strengthened as they ventured deeper into the darkness"

    n"Suddenly, shadows shifted, revealing General Ragnor's minions ready to attack."

    g"Foolish mortals! You will go no further!"

    pra"Stand your ground, Akemi! We can do this!"

    a"For the dwarves! For our people!"

#fight DIALOG
    min1"You won't leave here alive!"

    a"We'll see about that! *Clashes swords with Minion*"

    pra"*Dodging and providing cover* Your reign of terror ends here!"

    min2"Charging at Aoi* You'll regret those words!"

    a"*Defeating Minion 1* Aoi, stay behind me!"

    pra"*Swiftly blocking Minion 2's attack and providing a shield* I’ve got your back, Akemi!"

    n": As they defeated the minions, a menacing figure stepped out from the shadows General Ragnor himself."

    g"Impressive, but now you face me!"

    a"The real challenge begins. Ready, Princess?"

    pra"I’ll support you, Akemi. Let’s end this!"

    g"You have courage, but it will not save you from my wrath!"

    a"We have more than courage we have each other"
    
    pra"And we fight for a just cause! (Casts a protective spell on Akemi)"

    g"(Deflects Aoi's attack with a powerful swing)Foolish girl"

    a"(Flanking Ragnor) Over here, brute! (trikes at Ragnor's side)"

    g"(Roars in anger) You will pay for that! (Swings his massive axe at Akemi)"

    pra"Akemi, look out! (Uses her shield to block the axe)"

    n"The battle intensifies, with Akemi and Aoi coordinating their attacks, wearing Ragnor down"

    g"(Breathing heavily) This... this cannot be!"

    a"It's over, Ragnor. Surrender"

    g"Never! (Lunges desperately)"

    pra"(Providing a final spell boost to Akemi) Now, Akemi!"

    a"(With a final, powerful strike) For the dwarves! For our people!"

    n"With a final clash, General Ragnor fell defeated. The cavern echoed in victory's silence."
    n"With the gem secured, Akemi and Princess Aoi returned triumphant."
    n"Cheers and applause greeted them in the royal halls, hailed as heroes by the dwarven citizens."




label branch_6:





with dissolve
return

