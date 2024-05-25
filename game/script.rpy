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
# Himiko
image himiko def = im.Scale("himiko_def.png", 679, 900)
image himiko 1= im.Scale("himiko_1.png", 679, 900)
image himiko 2 = im.Scale("himiko_2.png", 679, 900)
image himiko 3 = im.Scale("himiko_3.png", 679, 900)
define n = Character("Narrator")

#background
image bg forest1 = "forest1.png"
image bg deepforest = "deepforest.png"
image bg deepforestsword = "deepforestsword.png"
image bg cave1 = "caved.png"
image bg meetingelf ="meetingelf.png"
image bg incavegold ="incavegold.png"
image bg mountain = "mountain.png"
image bg dcave = "Deepcave.png"
image bg library1="library1.png"
image bg library2="library2 w door"
image bg outc = "outsidecastle.png"
image bg ruins = "ruin door.png"
image bg throne2 = "throne 2.png"
image bg throne1 = "king chair.png"
image bg smith = "blacksmith.png"
image bg cc = "crystalcave.png"
image bg ctr = "crystalnobg.png"
image bg dayelf= "dayelfvillage.png"
image bg nightelf= "nightelfvillage.png"
image bg fgdwarf = "frontgatedwarf.png"
image bg gatedwarf= "gatedwarf.png"
image bg outsidek = "outcastle.png"
image bg cavepurple = "incavegoldpurplesmoke.png"
image bg gcave ="incavegold.png"




#asset
image bg ring = "ring_final.png"
image bg sword = "sword.png"

define a = Character("Akemi",color="546569") 

define p = Character("Aoi") 

define pra = Character("Princess Aoi",color="d8aec5") 

define h = Character("Himiko",color="546569") 

define n = Character("Narrator") 

define k = Character("King Throin") 

define s = Character("Scholar") 

define g = Character("General Ragnor") 

define grdelf = Character("Elf Guard") 

define elder  = Character("Elfe Elder")

define dwarfgrd=Character("Dwarf Guard")

define durin=Character("Durin")

define k = Character("King Throin")

define min1 = Character("Minion 1")

define min2 = Character("Minion 2")

define c = Character("King Charles")

define dra =Character ("Draythorn")

define dragon =Character("Dragon")


# The game starts here.

label start:

    scene black
    n"Summer has passed, and another school year is approaching. Students are excited as the new year will embrace them."
    n"Everyone’s busy with their requirements. And there’s one student who made the room a bit odd as she walks on"
    show akemi def
    n"Akemi is an ordinary student. She always wears her jolliest smile."
    scene black
    with Dissolve(.5)
    pause .5
    scene black
    with Dissolve(.5)
 
    
    scene bg library1
    n"School Day is done as she makes her way to her favorite spot which is at the library she saw an old book"
    show akemi 4
    n"Akemi pick it up and try to read it but there is no content of the book only a riddle"
    a"Hmm there's a Riedel (It lights sometimes; it’s dark sometimes everyone wants to walk all over me. What am I?)?"
    n"As akemi read the riedel she try to answer it "
    show akemi 3
    a"Hmmmmmm....Moon"
    with fade
    scene white 
    hide akemi def 
    n"The book glows a wight light and Akemi close her eye"
    n"Akemi hear that someone is calling for her as she slowly open her eyes, she saw this mysterious woman"
    scene bg ruins
    show princess 3
    "Mysterious" "Hero please wake up.."
    hide princess def
    show akemi 3
    a"uh?....what happen...and who are you"
    hide akemi def
    show princess 1
    "Mysterious" "Thank god are you alright....My name is Aoi i am the daughter of king Charles and from the kingdom of Azurevale"
    pra"May i ask your name Hero"
    hide princess def
    show akemi 3
    a"Hi my name is Akemi....Where am I..."
    hide akemi def
    show princess def
    pra"Hero Akemi then...you are in the ruins forest this place is used to summoned hero from another world"
    hide princess def
    show akemi 3
    a"Huh i am no hero i am just a regular student"
    n"As Akemi seems confused Princess Aoi try to explain everything as she gradually understands the situation Akemi ask another question."
    a"I see so that's what happened....then why did you summon me here"
    hide akemi def
    show princess 3
    pra"Please help me on my quest to defeat an evil magician that have been terrorizing my Kingdome and my father..."
    pra"please help me"
    hide princess def
    show akemi def
    n"Akemi have been to honest and always helping someone who needs her help even if she put her sefl in danger."
    show akemi 2
    a".....Okey I'll help you Princess Aoi"
    hide akemi def
    show princess 2
    pra"Really thank you so much hero Akem"
    hide princess def
    show akemi 3
    a"It's fine.... and please stop calling me Hero Akemi it's kind of embarrassing"
    a"Just call me Akemi.. "
    hide akemi def
    show princess 2
    pra"Understood.... Then you can call me Aoi its so nice to meet you"
    hide princess def
    show akemi 2
    a"Yeah nice to meet you too."
    hide akemi def
    with dissolve
label branch_2:
    scene bg forest1
    n"As Akemi and Princess Aoi have decided to start their adventure journey."
    show princess def at left
    pra"Thank you for helping me Akemi..."
    hide princess def
    show akemi def at left
    a"It okey your welcome.... so, are we going straight to kingdom of Azurevale?"
    hide akemi def
    show princess 3
    pra"No, Himiko is a powerful magician simple physical and magical attack won't hurt her."
    hide princess def
    show akemi 3 at left
    a"So how will I be able to beat Himiko then?"
    hide akemi def
    show princess def at left
    pra"We need to get the 3 legendary items that can only be wielded by a hero who came far from our world and that is you. "
    hide princess def
    show akemi 2
    a"So, what are these 3 legendary items. Then."
    hide akemi def
    show princess 2
    pra"The first is the blade of Ethereal Fang the legend tells that it has been forge and bless by the ancient gods and imbued with the power to pierce through darkness itself."
    pra"The second item is the Necklace of Valor it is made by the most skilled dwarf and has the ability to increase physical and magical power to its full potential."
    hide princess def
    show akemi 3
    a"What about the third item."
    hide akemi def
    show princess 3
    pra"I can't tell you yet. In order to obtain the last item, you need to have the first two. You need their combined power before you can even attempt to retrieve the third item."
    hide princess def
    show akemi def
    a"I see..."
    hide akemi def
    show princess 1
    pra"so which of the two item you want to get first."
    hide princess def
    menu:
        "Blades of Ethernal Fang":
            $ menu_flag = True
            jump branch_3

        "Necklace of Valor":
            $ menu_flag = False
            jump branch_4
with dissolve
#Blade of Ethernal Fang
label branch_3:
    scene bg forest1
    n"Ethereal Fang legend speak that it is resting place deep within the heart of mystical forest known as the Whispering Woods and the location of the forest is only know the elder elf wich is located at Faewood."
    #Princess aoi
    show princess 2 at left
    pra"We must travel deep in the forest to meet the elf elder and ask the Whispering woods."
    n"Upon reaching the guard gates of the Faewood they met with a vigilant sentry, wary of outsider. "
    with dissolve
    scene bg dayelf
    show princess 2 at left
    grdelf"Stop right there, who are you and state your buisness."
    n"With Aoi regal presence lending credibility and royal etiquette"
    pra"Good day to you sir, I am Princess Aoi from the kingdom of Azurevale, we humbly ask request to meet and ask guidance of the elf elder."
    grdelf"Wait here i will ask for the chef of the village."
    n"As the time Akemi and Princess Aoi for the approval of the chef village."
    grdelf"You may enter and be careful"
    n"As the they both enter the elf village akemi is amaze to the scenery of the elf village and the center have this giant tree"
    hide princess def
    with dissolve
    show akemi 2
    a"Wow look at that tree, it looks bigger than the biggest building in my hometown."
    with fade
    scene bg meetingelf
    n" As they enter inside the giant tree, they are great by the elder of the elf village"
    elder"Greetings Princess Aoi you have grown"
    hide akemi def
    show princess 2
    pra"It's nice to see you all again."
    elder"Hmm. Princess Aoi are you doing okey, we heard what happen about your father and your kingdom, as you know that we are a friend to your ancestor and your father, we are sorry to hear it."
    show princess 3
    show princess 1
    pra"Thank you for your concern, allow me to introduce you to Akemi the hero i brought to this world to defeat Himiko."
    hide princess def
    show akemi 2
    a"Hello, it's so nice to meet you all."
    elder"Hmmm. We guest that you are here to ask us the location of the Blade of Ethereal Fang yes."
    hide akemi def
    show princess 2
    pra"Yes, we would like to use it to deafet Himiko."
    elder"We will tell you the location, but it's very dangerous in the forest, and many monsters have been wandering there do you still want to know."
    pra"Yes, I am prepared to face any danger to save my father and my people."
    elder"And how about you, are you prepared to fight such a monster."
    hide princess def
    with dissolve
    n"As as they look at akemi waiting to her response"
    show akemi 2
    a"Yes, because I made a promised to aoi to help her."
    elder"Very well then, the location of the sword is located at the center of Whispering Woods west from here."
    elder" but recently there's a giant snake wandering and we try everything we can but the monster can heal itself easily,"
    elder "Princess Aoi be careful you and hero Akemi Please look after her, and one more thing go to the center ofthe forest monster won't go near the location of the sword"
    a"Yes"
    hide akemi def
    show princess 1
    pra"We will be careful and thank you"
    hide princess def
    with dissolve
    scene bg forest1
    n"As they start their quest to get the sword Akemi ask Princess Aoi."
    show akemi 3
    a"Aoi, why did Himiko attack and claim your kingdom."
    hide akemi def
    show princess 3 at left
    show himiko def at right 
    pra"Himiko is also a magic caster like me but instead of helping others, she used it for her personal gain and Himiko is obsessed with gaining more power and she fell into the darkness and wanted to control others through fear and power."
    hide princess def
    hide himiko def
    show akemi 3 
    a"So, she's really obsesses in gaining more power huh."
    n"As Akemi and princess aoi got closer to their destination suddenly an angry giant snake attack them."
    a"Ahh!" 
    hide akemi 3
    show princess 3
    pra" Ahh!"
    hide princess def
    show akemi 3
    a"Are you okey Aoi!"
    hide akemi def
    show princess 3
    pra"Yes, I am fine"
    hide princess def
    n"As they dodge the attack of the giant snake Akemi suddenly got stumble by a tree root"
    show akemi 3
    a"Ahhh!"
    n"As the snake notice the snake suddenly release a purple smoke and release it Akemi suddenly feel dizzy and feel weak and the giant snake saw Akemi lie down on the ground the snake tries to attack again."
    hide akemi def
    show princess 3
    pra"Akemi, Look out!!"
    n"As Princess Aoi saw Akemi can't move, she used her magic and attack the snake with fire."
    pra"FireBall"
    n"As the Giant snake got attack by a fire it got distracted and Princess Aoi used the chance to go see Akemi condirtion"
    pra"Are you alright Akemi."
    hide princess def
    show akemi 3
    a" Yeah I am fine...just a little dizzy."
    hide akemi def
    show princess 3
    pra" Let's retreat for now."
    hide princess def
    show akemi 3 
    a"Yeah, you're right."
    n"As they retreat far away from the monster for now, they rest for a bit."
    hide akemi 3
    show princess 3
    pra"Are you okey Akemi?."
    n"As Princess Aoi asked Akemi if she is okey she didn't get a respond. "
    pra"Akemi,Akemi hey are you okey!"
    n"Princess Aoi shake Akemi and notice something is strange on Akemi"
    pra"Huh!? Poison."
    pra"that is the content of the purple smoke that the snake release earlier"
    pra" I must do something."
    n" As soon as Princess Aoi knows that it is a poison, she began sight an incantation for magic"
    pra"Heal!.....Yes, it works, Akemi are okey?"
    hide princess def
    show akemi 3
    a"Aoi, what happened?"
    hide akemi def
    show princess 2
    pra"Thank goodness you're okay...are you still injured."
    hide princess def
    show akemi 2
    a"No i think i am fine...What happend anyway"
    hide akemi def
    show princess 3
    pra"You got poison."
    hide princess def
    show akemi 2
    a"I see thank you for helping me"
    hide akemi def
    show princess 1
    pra"Its okey, don't mention it"
    n"As they rest for a bit Akemi notices something rustelling in the forest, the giant snake appears again."
    hide princess def
    show akemi 4
    a"Aoi look out!"
    hide akemi def
    show princess def
    pra"Ahh!"
    n"Princess Aoi and Akemi were able to dodge the snake attack."
    pra"Be careful Akemi"
    hide princess def
    show akemi 3
    a"Yeah, we need to run deep in the forest."
    hide akemi def
    show princess def
    pra"Yeah, you're right the monster won't go near the location of the sword."
    pra"Akemi i will cast a support magic on you and can you give me sometime i will use my magic."
    hide princess def
    show akemi 3
    a"Okey got it."
    n" As Akemi tries to distract the giant snake Princess Aoi is preparing her magic."
    hide akemi_def
    show princess def
    pra"I am ready Akemi."
    hide princess def
    show akemi 3
    a"okey!."
    hide akemi def
    show princess def
    pra"Mega Flare!!"
    n"As the snake got attacked again by fire Akemi rush toward on Princess Aoi."
    hide princess def
    show akemi 3
    a"We did it lets go."
    hide akemi_def
    show princess 3
    pra"Yeah, but i can’t run fast i used all my magic power on that attack."
    hide princess def
    show akemi 3
    a"Okey then ill carry you lets go."
    hide akemi 3
    show princess def
    pra"Thank you Akemi."
    hide princess def
    show akemi 2
    a"Its okey."
    n"Akemi carries Princess Aoi and ran fast at the center of the forest as soon as they see the center Akemi go toward it."
    hide akemi_def
    with dissolve
    scene bg deepforestsword
    show akemi 3
    a"AAHHH! We made it!"
    hide akemi def
    show princess def
    pra"Yeah."
    n"As they both got in the center of the forest Akemi look at the sword "
    hide princess def
    show akemi 4
    a"So that's the Blade of Ethereal Fang"
    hide akemi def
    show princess def
    pra"Yes, go on Akemi try to pull it."
    hide princess def
    show akemi 2
    a"Yeah..Okey lest do this."
    n"As Akemi Approach the sword, she can feel its power wondering if this is the reason why no monster won't go near it, as Akemi hold the sword, she felt warm feeling all over her body." 
    a "Here’s got nothing."
    hide akemi def
    with fade
    scene bg sword
    n"As soon as akemi tried to pull the sword she felt it was too light."
    with fade
    show akemi 2
    a"Yes!, Look Aoi i did it i pulled the sword."
    
    n"Princess Aoi looks at Akemi and smiles. "
    hide akemi def
    show princess 1
    pra" Yes, you did it."
    a"let's rest here for a while, are you still tired."
    show princess def
    pra"Yes, thank you for asking."
    n"Akemi and Princess Aoi finally got rest for a bit they are now trying to go back to the elf village once again."
    hide princess def
    with fade
    scene bg forest1
    show akemi def
    a"Finaly We got the Blade of Ethereal Fang we are close in saving your Kingdome Aoi"
    hide akemi def
    show princess def
    pra" Yes."
    n"Akemi and Princess Aoi chatting, the snake appears again it their way."
    hide princess def
    show akemi def
    a"Aoi be careful let's defeat this giant snake for real this time."
    hide akemi def
    show princess def
    pra"Right"
    n"Akemi and Princess Aoi prepare to fight the giant snake and Akemi proposes a plan."
    hide princess def
    show akemi def
    a"Use your magic and support and i will draw its attention try to use fire magic only "
    hide akemi def
    show princess def
    pra"Okey"
    n"Akemi draw the attention of the snake and princess aoi used fire magic to make the giant snake more confused, Because of this the giant snake try to use the purple Princess used her support magic to make Akemi resistance to poised for a short amount of time."
    pra"Now is your chance Akemi."
    hide princess def
    show akemi 2
    a"Right,HYAAAA!!."
    n"Akemi jumps high and goes directly to attack the head of the snake. As she swings her sword to the head, Akemi lands and the giant snake's head."
    a"Wow this sword cut it like paper...we did it Aoi."
    hide akemi def
    show princess def
    pra"Yeah....that was amaizing Akemi."
    hide princess def
    show akemi def 
    a"Let's go back to the elf village."
    hide akemi def
    show princess def
    pra"Yeah."
    with dissolve
    scene bg nightelf
    n"Akemi and Princess Aoi got Infront of the elf village they are surprised to see that Akemi is holding the Blade of Ethereal Fang"
    elder"We are glad you are safe Princess Aoi and Akemi. "
    show princess def
    pra"Thank you."
    n"Akemi and Princess Aoi explain what happened, they are relief and surprised because they were able to slay the giant snake and the Elf elder explains about that giant snake."
    elder"We have been here for long time..that snake suddenly appear out of knowhere and releasing a purple smoke."
    pra"Himiko must be the one behind it. She must be trying to stop someone who will search for the sword."
    elder"It must be.... but the sword can’t be pulled by a normal person, Akemi."
    hide princess def
    show akemi def 
    a"Yes"
    elder"The sword chooses you to be its user please use it only for good."
    a"I will."
    elder"We assume that the two of you will continue your journey, we will pray for your success and safety, good luck Akemi and Princess Aoi."
    a"Thank you"
    hide akemi def
    show princess def
    pra"Thank you."
    n"Akemi and Princess Aoi say goodbye to the elf village they are now off on their next journey."
    hide princess def
    if menu_flag == False:
        jump branch_5
    elif menu_flag == True:
        jump branch_4
with dissolve
#Necklace of Valor
label branch_4:
    scene black
    n"As Akemi and Princess Aoi set their journey to get the Necklace of Valor from the dwarf and the name of the kingdom is Ironforge."
    with dissolve

    scene bg fgdwarf
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
    with dissolve
    scene bg gatedwarf
    show princess def
    pra"Here we are the Ironforge Kingdom."
    hide  princess def
    show akemi def
    a"Wow look at the size of the wall and the gate is so huge."
    n"As Akemi and princess aoi got closer one of the guards recognise princess Aoi."
    
    dwarfgrd"Princess Aoi is that you thank god your safe its been to long"

    n"Princess Aoi smiled with relief as she explained their quest to retrieve the Necklace of Valor and save her kingdom from Himiko's darkness."
    hide akemi def
    show princess def
    pra"It has been too long indeed Durin."
    
    durin"What brings you here in Ironforge, Is she your companion."

    pra"Yes she is and she is also my friend and the hero the is summoned."
    hide princess def
    show akemi def 
    a"Hello nice to meet you Durin."
    
    durin"Nice to meet you too."
    hide akemi def
    show princess def
    pra" We came hoping to meet King Throin and ask for the Necklace of Valor to help me and the hero to defeat Himiko that invaded their Kingdome."
    
    n"Durin nods and promise to Princess Aoi"
    
    durin"Fear not, Princess Aoi. As your friend and ally, I shall see to it that you and your companion are granted an audience with King Throin. "
    
    pra"Thank you Durin."
    with dissolve
    scene bg outsidek
    n"With Durins guidance Akemi and Princess Aoi are escorted through the bustling street of ironforge."
    hide princess def
    show akemi def
    a"Look at the busy street Aoi, there are a lot of markets and lot of weapons on display and a lot of beautiful jewelry and shining armor its really like a fantasy."
    hide akemi def
    show princess def
    pra"Yes, there's a lot of people than the last time i visit here."
    with dissolve
    scene bg throne2
    n"As they approach the imposing gate of the royal castle, Akemi and Princess aoi was able to meet King Throin."
    
    k"Welcome, it an honor to meet you once more and to meet your esteemed companion"
    show princess def
    pra"It's an honor to meet you to king Throin allow me to introduce my companion, her name is Akemi she is the hero i summon"
    
    pra"It's a pleasure to meet you, King Throin."
    
    n"King Throin regarded Akemi with a solemn gaze, acknowledging the hero's presence with a hint of respect."
    
    k"Akemi, It's an honor to meet you."
    hide princess def
    show akemi def
    a"It's also my honor King Throin"
    hide akemi def
    show princess def
    n"Princess Aoi continued her tone urgently."
    
    pra"Your Majesty, we seek you aid in offering us the Neklace of valor. "
    
    k"I fear I must deliver grim tidings"
    
    n"The king tell them with a heavy sorrow."
    
    k"The Necklace of Valor was stolen and destroyed form us by one of Himiko men in the past few months by General Ragnor a cunnig and ruthless adversary."
    hide princess def
    show princess 3
    n"Princess Aoi heart sank at the news, but before she could despair King Throin spoke again, his tine resolute."
    
    k"However, There’s another way. We can forge a new necklace, one that is more powerful than its predecessor."
    hide princess def
    show princess 2
    n"A glimmer of hope sparked in Princess Aoi’s heart, but their joy was short-lived as the ground trembled, signaling impending danger."
    hide princess def
    show akemi 3
    dwarfgrd" We are under attack!"
    
    n"One of the guards shouted, with resolved in their hearts Akemi and Princess Aoi rushed to defense of Ironforge their swords drawn and their magic ablaze."
    
    n"Outside the castle walls, they were met with a horde of monstrous creatures, their eyes filled with malice and hunger for battle."
    
    n"As Akemi and Princess Aoi fought bravely against the onslaught, King Throin approached them with a grim expression."
    
    k"Our enemies seek the gemstone needed to forge the new necklace."
    
    k"It lies deep within the mining caves, but the entrance is heavily guarded by General Ragnor's minions."
    hide akemi def
    scene bg dcave
    show princess def
    n"Princess Aoi's determination burned brighter than ever as she turned to Akemi, her eyes shining with resolve."
    
    pra"We must retrieve the gemstone, no matter the cost." 
    
    n"  With the king's blessing and the support of the dwarven warriors, Akemi and Princess Aoi ventured into the mining caves, their hearts ablaze with courage and hope."
    
    n"Akemi and Princess Aoi set forth into the depths of the mining caves, their hearts set ablaze with the fires of courage and hope."
    hide princess def
    show akemi def
    a"We have faced greater dangers before, Princess. Together, we can overcome any obstacle."
    hide akemi def
    show princess def
    pra"You're right, Akemi. With the strength of our friendship and the bravery of the dwarves, we will prevail."
    
    n"The resolve in their voices strengthened as they ventured deeper into the darkness"

    n"Suddenly, shadows shifted, revealing General Ragnor's minions ready to attack."

    g"Foolish mortals! You will go no further!"

    pra"Stand your ground, Akemi! We can do this!"
    hide princess def
    show akemi def
    a"For the dwarves! For our people!"
    hide akemi def
    with fade
#fight DIALOG
    scene bg dcave
    min1"You won't leave here alive!"
    show akemi def
    a"We'll see about that! *Clashes swords with Minion*"
    hide akemi def
    show princess def
    pra"Your reign of terror ends here!"

    min2"Charging at Aoi* You'll regret those words!"
    hide princess def
    show akemi def 
    a"*Defeating Minion 1* Aoi, stay behind me!"
    hide akemi def
    show princess def
    pra"*Swiftly blocking Minion 2's attack and providing a shield* I’ve got your back, Akemi!"

    n"As they defeated the minions, a menacing figure stepped out from the shadows General Ragnor himself."

    g"Impressive, but now you face me!"

    a"The real challenge begins. Ready, Princess?"

    pra"I’ll support you, Akemi. Let’s end this!"

    g"You have courage, but it will not save you from my wrath!"
    hide princess def
    show akemi def 
    a"We have more than courage we have each other"
    hide akemi def
    show princess def
    pra"And we fight for a just cause! (Casts a protective spell on Akemi)"

    g"(Deflects Aoi's attack with a powerful swing)Foolish girl"
    hide princess def
    show akemi def
    a"(Flanking Ragnor) Over here, brute! (trikes at Ragnor's side)"

    g"(Roars in anger) You will pay for that! (Swings his massive axe at Akemi)"
    hide akemi def
    show princess def
    pra"Akemi, look out! (Uses her shield to block the axe)"

    n"The battle intensifies, with Akemi and Aoi coordinating their attacks, wearing Ragnor down"

    g"(Breathing heavily) This... this cannot be!"

    a"It's over, Ragnor. Surrender"

    g"Never! (Lunges desperately)"

    pra"(Providing a final spell boost to Akemi) Now, Akemi!"
    hide princess def
    show akemi def
    a"(With a final, powerful strike) For the dwarves! For our people!"
    
    n"With a final, resounding clash, General Ragnor fell to the ground, defeated. The cavern echoed with the silence of their victory, and fo deep in the minning cave Akemi and Princess Aoi was
    surprise the beautiful of the gem infornt of them."
    hide akemi def
    with dissolve
    scene bg cc
    show princess def
    pra"Akemi, look! Over there, deep in the mining cave. It's the Mystic Lunar, shimmering in a radiant sky blue. It's truly breathtaking... Our journey was not in vain, this gem holds the key to our kingdom's salvation."
    hide princess def
    show akemi def 
    a"Yeah, Aoi I've never seen anything so beautiful. It's like the heavens themselves have descended into this cave. With this gem, we can forge the Necklace of Valor and bring hope back to your people."
    with dissolve
    scene black
    show bg ctr
    with fade
    n"As Akemi and Princess Aoi return, King Throin greeted them with gratitude. He thanked both of them for their bravery and informed us that General Ragnor had been defeated. It seems our victory has weakened our enemy's forces"
    with dissolve
    scene bg throne1
    a"Thank you, King Throin. We're honored to have helped. Our encounter with General Ragnor was challenging, but with Princess Aoi's leadership, we prevailed."

    k"Your bravery has brought light to our kingdom in these dark times. With the Mystic Lunar in our possession, we can now forge a necklace stronger than ever before. Guards, prepare the forge and summon our most skilled smith. The Necklace of Valor shall rise again!"
    hide akemi def
    show princess def
    pra"Akemi, our journey together has been filled with danger and uncertainty, but seeing the Mystic Lunar fills me with hope."
    hide princess def
    show akemi def 
    a"Aoi it's been an honor to fight by your side. Your courage and determination inspire me. Together, we've overcome every obstacle, and I have no doubt that we'll continue to do so."
    hide akemi def
    show princess def
    pra"Thank you, Akemi. Your strength and loyalty have been invaluable to our cause. Let us go forth and ensure that the Necklace of Valor is forged with the same determination that brought us here."
    n"As Akemi and Priccess Aoi rest for a few day to finish the forge of Necklace of Valor Akemi notice somting is worrying Princess Aoi."
    hide princess def
    show akemi def
    a"Aoi is something bothering you I can see the worry in your eyes."
    hide akemi def
    show princess def
    pra"Thank you Akemi, I am just worry about my father and the people of Azurevale"
    hide princess def
    show akemi def
    a"I see...But for now, let us focus on the task at hand. We have the gem, and soon we will have the necklace. With its power, we will be better equipped to face whatever challenges lie ahead"
    hide akemi def
    show princess def
    pra"Yes..your right,we must stay focused on our mission"
    with dissolve
    scene black
    n"As they awaited the necklace's completion, Akemi and Princess Aoi spent their days in the dwarven kingdom, assisting those in need. Though outwardly brave, the weight of their responsibilities grew heavier, intensifying their sense of urgency."

    n"On the day of completion, King Throin presented the finished necklace to Akemi and Princess Aoi"
    with fade
    scene bg throne1
    k"This necklace is a testament to your bravery and determination. May it serve you well in your quest to bring peace to your kingdom."

    pra"Thank you King Throin"
    hide princess def
    show akemi def
    a"Thank you"

    n"As they set their next journey,the grand halls of the royal palace, they were greeted with cheers and applause from the dwarven citizens, who hailed them as heroes."

    if menu_flag == False:
        jump branch_3
    elif menu_flag == True:
        jump branch_5

label branch_5:
    scene black
    n"Akemi and Princess Aoi continue and prepare their journey and Princess Aoi turned to Akemi with a determined look in her eyes."
    with fade
    scene bg deepforest
    show princess def
    pra"Akemi, there is one final item we need to retrieve to defeat Himiko once and for all."
    n"she explained, her voice filled with resolve"
    pra"The Crimson Radiance Ring, said to protect its wearer from even the most powerful of attacks. However, it is in the realm of one of the Heavenly Dragons, guarded for millennia, awaiting the true and worthy hero to retrieve it."
    hide princess def
    show akemi def
    n"Akemi nodded, understanding the gravity of their task." 
    a "Then we must journey to the realm of the Heavenly Dragon and prove ourselves worthy of the Crimson Radiance Ring."
    n"She replied, her voice steady with determination"
    a"Together, we will face whatever challenges lie ahead and emerge victorious."
    hide akemi def
   
    n"With their hearts set on their next quest, Akemi and Princess Aoi, their minds filled with thoughts of the trials and tribulations that awaited them."
    with dissolve
    scene black 
    #black screen
    n"As one of the minions of General Ragnor escaped from the kingdom of the dwarves, he wasted no time in delivering his message to Himiko. Rage consumed her as she learned of Princess Aoi and Akemi's involvement."
    with fade
    scene bg throne2
    show himiko def 
    min1"Your Majesty General Ragnor was defeated by a Princess Aoi and a girl named Akemi."
    hide Himiko def
    show himiko 3
    h"What...they defeated Ragnor what Ragnor is supposed to be strong, and he was defeated."
    min1"What should we do you Majesty."
    h"Bring me King Charles (king of Azurevale) from his cell now!"
    min2"Yes, your Majesty."
    n"The Minion brings King Charles to Himiko and asks him the location of the Crimson Radiance Ring."
    hide himiko 3
    show himiko 1
    h"Hmmm...I want you to tell me something and don't think of lying to me! "
    c"Hmmm... "
    h"Tell me the location of the Crimson  of Radiance Ring."
    c"Hmmm...I won't tell you even if you threat to kill me"
    h"hmm....If you don't tell me the location of the Crimson radiance ring i will kill ever person in this castle HAHAHHAHAH!"
    h"And that's not all I will also kill your beloved daughter"
    c"You monster don't you dare to hurt her...or-"
    hide himiko 1
    show himiko 2
    h"AHAHAHAH!...Or what haha what can you possible do in your current state...I make you a deal, I will order my Servant to only capture Princess Aoi and return her to you safe and sound if you tell me the location of the ring."
    c"Hmmm....I want you to give me your word that you won't hurt my daughter and my people."
    h"Hehe, Fine i give you my word"
    c"The location of the Crimson Radiance Ring is in the Heavenly Dragon Mountain."
    hide himiko 2
    show himiko 1
    h"Was that hard to say, take him back to his cell. "
    n"With King Charles returning to back to his cell his heart heavy with guilt and despair, he hoped to protect his people and Princess Aoi from her wrath."
    n"But as soon as the information was in her grasp, Himiko's true intentions were revealed. With a wicked grin, she ordered her minion to return the king to his cell, his fate sealed for daring to defy her."
    h"Heavenly Dragons Mountain huh....Let's see if this time they will survive HAHAHAAHAH!."
    n"Himiko concocted a sinister plan to ensure Akemi and Princess Aoi's demise. Harnessing her dark powers, she formed a purple orb infused with her malevolent energy."
    h"Come my servant i want to give you a special quest right now you are my general I need you to deliver this in the heavenly dragons Mountain now, "
    min1" I am honored your majesty."
    n"The orb contains some of Himiko power and it will realease  a purple smoke that will make any living creature to go berserk and becomes Himikos pawn,meanwhile Akemi and Princess Aoi continue their journey. "
    hide himiko def
    with dissolve
    scene black
    h"HAHAHAHAHAHAHHA!"
    with fade
    #Next Scene for akemi and aio  ot heavenly dragon mountain
    scene bg mountain
    show akemi def 
    a"So thats the heavenly Mountain Dragon."
    hide akemi def
    show princess def
    pra"Yes..theirs also a dragon living there"
    hide princess def
    show akemi def
    a"Really thats amazing, wait if there is a dragon living there then we will get attacked by it"
    hide akemi def
    show princess def
    pra"No its okey the dragon thats been living there is actually a kind dragon he never go attack human as long as it doesnt bother him."
    hide princess def
    show akemi def
    a"Really then were safe..as long as we dont bother him okey seems easy."
    hide akemi def
    show princess def
    pra"Yes"
    dragon"(Roar)RAWWWWWWW!!!!"
    n"As Akemi and Princess Aoi continue their walk a violent wind suddenly whipped around them."
    hide princess def
    show akemi def
    a"Aoi, AAHHHH!"
    hide akemi def
    show princess def
    pra"Akemi, AAHHHH!"
    hide princess def
    show akemi def
    a"It's the Dragon...Be careful Aoi.!!"
    n"As the dragon poised itself for another strike, Akemi leaped high into the air, carrying Princess Aoi to safety."
    a"Are you okey Aoi. "
    hide akemi def
    show princess def
    pra"Yes, i am fine, Thank you."
    hide princess def
    show akemi def
    a"Stay here i deal with the dragon."
    n"Akemi drew her sword, ready to face the formidable foe. With a swift and precise strike, she lunged at the dragon, but to her astonishment, her blade had no effect. "
    a"What...It didn’t work, what's going on?"
    n"Princess Aoi uses her magic to strike the dragons wing and to Akemi is surprised that magic is working. She also try to use it."
    a"So magic works huh..then let's see you try to take this."
    n"The sword lights fire and Akemi try to slash the dragon but as soon as Akemi is about to attack Princess Aoi stops her."
    hide akemi def
    show princess def
    pra"Wait Akemi!!"
    hide princess def
    show akemi def 
    a"Huh,why whats wrong."
    n"As soon as Akemi got stopped by princess Aoi the dragon raise up and started to fire a multipe fireball."
    a"Whooo!, Thats was close."
    hide akemi def
    show princess def
    pra"Akemi lets hide for now, trust me. "
    hide princess def
    show akemi def 
    a"Really, Okey if you say so."
    with fade
    scene bg deepforest
    n"Akemi and princess Ai ran deep to the forest were the stumble a lake and Princess Aoi explained to Akemi what she noticed."
    show akemi 3
    a"What happen why did you stop me. "
    hide akemi def
    show princess def
    pra"That dragon seems in pain and under an influence of something like there is something controlling it against its will."
    hide princess def
    show akemi def 
    a"Then what should we do."
    hide akemi def
    show princess def
    pra"I know that i am asking too much, but can we save it. "
    hide princess def
    show akemi def
    a"Okey if that's what you want so how we will help it."
    hide akemi def
    show princess def
    pra"Hmmmmm...how about we investigate his lair maybe we can find somethig there or."
    pra"We can try to make it unconscious and see what is going on to him Whats your choice?"
menu:
        "Investiagte the cause":
            $ menu_flag = True
            jump invest_dragon

        "Fight the dragon":
            $ menu_flag = False
            jump fight_dragon

label invest_dragon:
    hide princess def
    show akemi def
    a"We should investigate it then" 
    hide akemi def
    show princess def
    pra"Okey then "
    with dissolve
    n"As they try to hide from the trees to go look for the dragon lair Princess Aoi saw something."
    scene bg cave1 
    pra"Hmm,whats that, Akemi come over here"
    hide princess def
    show akemi def
    a"What did you saw."
    hide akemi def
    show princess def
    pra"There's seemed to be a cave over theirs seem to be a purple fog inside it."
    hide princess def
    show akemi def 
    a"We Should go and see it."
    hide akemi def
    show princess def
    pra"Okey, but first i will cast a spell to prevent us from that purple smoke."
    with dissolve
    scene bg cavepurple
    n"Akemi and Princess Aoi enter the cave the saw a purple orb that is releasing purple smoke. "
    hide princess def
    show akemi def
    a"What is that should we go and see it."
    hide akemi def
    show princess def
    pra"Okey, but lest be carefull"
    n"Akemi and Aoi got closer to the purple orb Princess Aoi looks it and realize that this is Himiko’s doing."
    pra"I see now Himiko must have used this purple orb to control the dragon. "
    hide princess def
    show akemi def 
    a"Should we destroy it then?"
    hide akemi def
    show princess def
    pra"Wait if we just destroy it the smoke will get more powerful  "
    hide princess def
    show akemi def
    a"So What should we do"
    hide akemi def
    show princess def
    pra"We need to purify it by chaneling light magic maybe it will stop the smoke but my magic it not enough to purify it but I think you can do it  Akemi you Blade of Ethereal Fang to cast the light magic and necklace of valor to boost your magic."
    hide princess def
    show akemi def
    a"Okey, i will try"
    n"Akemi try to focus with the help of the elder of the elf Akemi is able to cast magic into the sword and as the sword lights all the smoke slowly vanishes, and the purple orb suddenly turns gray. "
    a"HMMMMMM!!!! "
    hide akemi def
    with dissolve
    scene bg gcave
    n"Princess Aoi notice that the purple smoke gradually fading and the orb is turning into a gray orb"
    show princess def
    pra"Yes thats it Akemi you did it now we should see what the condition of the dragon is outside"
    n"Akemi saw the dragon fall sleep nearby when the purple smoke is gone."
    with fade
    jump outcome



label fight_dragon:
    hide princess def
    scene bg deepforest
    show akemi def 
    a"We should fight it if we dont try to stop in now the dragon might attack an innocent"
    hide akemi def
    show princess def
    pra"Okey, I understand."
    pra"First we need plan, magic is the only thing to hurt him and we have to knock him down so i will be able to observe what is wrong with him, "
    hide princess def
    show akemi def
    a"I Have an idea Aoi."
    hide akemi def
    show princess def
    pra"Okey lets hear it."
    hide princess def
    show akemi def 
    a"First I will draw its attention and you try to attack him with magic and once he is down i will try to use a bind magic so he mont be able to move"
    hide akemi def
    show princess def
    pra"Okey I,got it."
    n" As Akemi try to shout loudly to lure the dragon."
    hide princess def
    show akemi def 
    a"HYYAAAAAAAAAAA!!"
    n" A violent wind dash through Akemi as see observe where will it attack Akemi."
    a"Hmmm,Over there, aoi get ready."
    hide akemi def
    show princess def
    pra"On it."
    n"Narator As akemi draw the attention of the dragon princess Aoi used this chance to fire at the dragon."
    pra"FireBall"
    n"As the dragon got hit Akemi used a binding magic to seal the movement of the dragon while Princess Aoi notice the purple aura raleasing n the body of the dragon"
    pra"Akemi I got it we need to use light magic to remove the purple aura but my magic is not enough."
    hide princess def
    show akemi def 
    a"I will do it i will used the Blade of Ethereal Fang to cast the light magic and necklace of valor to boost your magic"
    n"As Akemi concentrate in casting light magic the sword light and the necklace glow and the purple aura is slowly fading and making the dragon fall sleep"
    jump outcome

#Same ending for branch 6
label outcome:
    scene bg deepforest
    n"Exhausted from the Akemi and Princess Aoi shared a triumphant smile, knowing they had succeeded in freeing the dragon from Himiko's control, As minutes passed, the dragon stirred awake, its eyes filled with remorse for its actions. "
    show akemi def 
    a"Hi are you okey?"
    hide akemi def
    show princess def
    pra"How are you feeling?"
    hide princess def
    dragon"Yes and thank you for saving me."
    pra"My name is Aoi and this is my companion Akemi."
    show akemi def
    a"Hi whats your name."
    dragon"Akemi and Aoi it's a pleasure to meet you...My name is Draythorn" 
    n"As they rest for bit, Draythorn asks what are they doing here in heavenly mountain?"
    hide akemi def
    show princess def
    pra" We are looking for the Crimson of Radiance Ring."
    dra"So you are also looking for it too?" 
    hide princess def
    show akemi def 
    a"What do you mean by that "
    dra"When i was under the influence of that purple smoke a keep hearing a female voice to destroy someone and bring her the ring."
    hide akemi def
    show princess def
    pra"Its Himiko again."
    hide princess def
    show akemi def
    a"Yeah and she is probably trying to get the ring for herself."
    dra" So that's her name huh, it's true that i have the ring but it won't work if I don't give my magic to power to it, I will give you the ring as a reward for helping me and promise me this Akemi and Princess Aoi to defeat Himiko."
    a" I Promise"
    hide akemi def
    show princess def
    pra" I Promise"

    n"Draythorn gave Crimson Radiance Ring. Akemi donned the ring, feeling its power course through her veins, and to their surprise, Draythorn blessed the ring, imbuing it with even greater strength. "
    n"With their mission accomplished, Draythorn offers Princes Aoi and Akemi a ride. As they soared towards the edge of the forest"
    n"they bid farewell to Draythorn, expressing their gratitude for his aid and the swift ride, With the Crimson Radiance Ring in their possession"
    n"and Draythorn's blessing, Akemi and Princess Aoi continued their quest with renewed determination"
    





label branch_6:
    pra "Now that we have gathered everything we finally have all of the necessary items we need to defeat Himeko!"

    a "Lead the way princess towards the Kingdom of Azurevale"

    pra "Draythorn dropped us at the outskirts of the Kingdom it will only take us half a day on foot to reach Azurevale, As long as we follow this path we should be fine"

    a "Then lets get going then"

    n "Akemi and Aoi sets off to the kingdom of Azurevale"

    n "As they follow the path towards the kingdom their surrounding was filled with destruction and despair as they see villages nearby abandoned, natural resources destroyed and dead bodies scattered in the area"

    n "Fear soon filled the air as the duo witness the results of their evil thinking how bad it is at the heart of it all"

    pra "This is one of the villages that are outside of the Azurevale. I know Himeko is evil but it is worse than I thought"

    pra "All of the villagers that have met their untimely demise, the houses are all in ruins, even the farms and surrounding forest is reduced to ashes"

    pra "*tries not to puke at the sight she saw* Can we really win this fight against Himeko?"

    pra "Was calling you from the other world a big mistake?"

    pra "If this is what happened to the outskirts of the kingdom how bad is it at the castle?"

    pra "I am afraid we are too late to take action!"

    pra "What should we do?"
    menu:
        "Comfort Aoi":
            jump option_1

        "Leave Aoi alone":
            jump option_2
    

    

label option_1:

    a "Aoi you are the Princess of Azurevale, the one who helped me through this journey to get the necessary items to defeat Himeko, and the one who will free your people from Himeko"

    a "We may not be able to save everyone but there are still people who are waiting to be save and if we don’t stop her then she will continue destroying everything"

    pra "You are right, defeat is never an option we must continue forwards"

    pra "I will support you with all I got Akemi together we will defeat Himeko!"

    n "The duo continued its way towards the kingdom but as they get closer and closer to their destination the sound of demons screaming and the undead growling can be heard getting louder and louder"

    n "Then they saw it, outside of the kingdom a massive horde of demons and undead scattered outside ravaging everything from houses to the land scape itself"

    n "The once beautiful kingdom was turn into a desolate place by the army"

    n "As the both of them are shocked at what they saw Akemi filled with self-doubt asked Aoi"

    a "With all these demons and undead are we able to fight this head on?"

    pra "Although the legendary item’s are powerful, they only protect you and an ambush from Himeko herself can easily be the death of both of us"

    pra "Our best bet is to avoid conflict against the whole army and sneak our way in and…"

    h "That’s a brilliant idea princess! *Binds the princess*"

    h "You may have the legendary items *points at Akemi* but the princess doesn’t have anything!"

    n "Akemi surprised of what happened angerly tried to attack Himeko but was swiftly block by Himeko’s demons."

    h "What will you do now that you lost your partner? Are you really going to fight me and my army all on your own?"

    a "What should I do? Why is she here? Can I even defeat her with her army? Am I ..."

    pra "Stop doubting yourself!"

    pra "We have come this far just to give up! We got everything we need you can do it Akemi!"

    pra "You have all you need to defeat her!"

    a "You are right princess!"

    a "Himeko! If you are really that powerful then you can defeat me all by yourself! Stop hiding behind your minions like a coward and fight me in a duel! Just you and me!"

    h "And what makes you think I would accept that? You are the one who is surrounded here and I can easily command my army to attack you all at once"

    h "What gave you the authority to challenge me in a duel"

    a "If you truly are as powerful as you say then there’s nothing to fear about the duel. At the very least if I fail to defeat you I can have an honorable departure"

    h "You amuse me your name is Akemi correct?"

    a "Yes I am Akemi the Outworlder that will defeat you once and for all!"

    h "You amuse me Akemi, I will accept your duel so that you will have a much more humiliating defeat! I want to see you beg as you wish you fought my army instead of me!"

    h "Take the princess to the dungeon with the rest of the people and do not interfere with our fight!"

    n "Himeko started chanting as she prepares to transport both herself and Akemi to the throne room"

    h "Will this be a suitable place for the duel? Also for our audience we have the King himself!"

    jump himeko_fight
    

    

label option_2: 

    a "I am afraid that something bad may happen to you princess so I must fight her alone"

    pra "What are you saying that’s suicide!"

    a "I know it may be suicide but what will happen when we fail to defeat Himeko and you didn’t survive? What will happen if we won but at the cost of your life? Who will lead you people? Who will look for help from other kingdoms when things don’t go our way?"

    a "I will continue to take this path alone please go back or stay at a safe place"

    a "I will be back when everything is done and if I don’t come back ask the other kingdoms for help"

    n "As Aoi process and thinks about everything Akemi heads of towards the Azurevale"

    n "As Akemi gets closer and closer to her destination the sound of demons screaming and the undead growling can be heard getting louder and louder"

    n "Then she saw it, Outside of the kingdom a massive horde of demons and undead scattered outside ravaging everything from houses to the land scape itself"

    n "The once beautiful kingdom was turn into a desolate place by the army"

    n " With determination in her heart, she continued her path and was met by someone unfamiliar"

    h "Are you the hero they keep on talking about? Where is the princess? Did she ran away like the coward she is? Hahahahaha"

    a "So you must be Himeko the reason why the kingdom is in ruins."

    h "The one and only!"

    a "If you are really that powerful then you can defeat me all by yourself! I challenge you in a duel! Just you and me!"

    h "And what makes you think I would accept that? You are the one who is outnumbered here and I can easily command my army to attack you all at once."

    h "What gave you the authority to challenge me in a duel"

    a "If you truly are as powerful as you say then there’s nothing to fear about the duel. At the very least if I fail to defeat you I can have an honorable departure."

    h "You amuse me, what is your name?"

    a "I am Akemi the Outworlder that will defeat you once and for all!"

    h "You amuse me Akemi, I will accept your duel so that you will have a much more humiliating defeat! I want to see you beg as you wish you fought my army instead of me!"

    h "Take the princess to the dungeon with the rest of the people and do not interfere with our fight!"

    n "Himeko started chanting as she prepares to transport both herself and Akemi to the throne room."

    h "Will this be a suitable place for the duel? Also for our audience we have the King himself!"

    jump himeko_fight

label himeko_fight:

    a "What just happened? Where are we? *Looks around*"

    h "We are in the Throne Room of the castle where you will rest as the king watches you suffer"

    a "*Looks towards the throne and saw the king* What have you done to the king?"

    h "Nothing really, He was very reluctant at giving me his Kingdom so I made sure he wont change his mind"

    a "By chaining him at the throne? This is torture!"

    h "That’s what he wanted now shall we commence the duel?"

    n "As the king holds on to his life, so does the castle where the pillars and walls that became the foundation of the castle where now damaged and barely able to support the ceiling"

    n "This will be Akemi's final battle!"

    a "*nods as she prepares for battle, took a deep breathe, calmed her nerves and took a stance*"

    n "As Akemi was preparing and taking a stance Himeko immediately launched an attack towards Akemi hitting her on her left side while a cloud of dust covered Akemi as the attack also hits the floor"

    h "Is it already over? And here I thought I would be able to torture her som…"

    n "As the dust settled Himeko saw Akemi still standing"

    h "So you were able to surviv…"

    n "Himeko paused as she noticed that Akemi only received a scratch"

    h "That attack only scratched you? Just how powerful are these items!"

    a "That didn’t really hurt too much! So this must be the power of the ring with this I have a chance to defeat Himeko!"

    h "How powerful can these legendary items be? To think that attack will only leave a scratch!"

    n "Akemi with her new found confidence charged at Himeko preparing an attack"

    h "That attack is nothing *waves hand to try deflect the attack* A magician defense must not be… *spell slowly breaks and forced Himeko to retreat* These items the power it holds is really impressive if I don’t get serious, I may lose this battle"

    h "How are you able to get all 3 Legendary Items especially the necklace since it was broken?"

    n "Akemi didn’t respond as she is too focused on the fight as one wrong step may lead to her demise"

    h "So you are going to be quiet about everything then so be it! *launches a volley of attacks with different elements*"

    n "Akemi although amazed at how powerful Himeko us was un able to say anything as she is too focus on dodging while inching closer and closer towards Himeko waiting for the right opportunity to strike!"

    a "I finally got close enough to you *lunges at her preparing for an attack*"

    h "A magician doesn’t just only specialize in long range *As she says that a power spell that was prepared for the opportune moment was launched at Akemi hitting her directly*"

    n "The hit was so powerful the it launched Akemi towards the wall!"

    n "Akemi visible hurt from the blast and impact was bleeding but still able to stand and fight"

    h "Still not giving up? Then you will suffer some more!"

    n "a barrage of spells continued to target Akemi as she tries to dodge and inch forward."

    a "What should I do? getting closer to her is no problem but I am not fast enough to dodge the attack up close!"

    n "Akemi thinks of a way and wished she had a shield to block the spell to create an opening"

    n "An idea popped up in her head and gathered all her courage because she knew if she fails she will meet death"

    h "You may be strong because of the items but in terms of experience you are no match for me! A simple girl with no sword training is nothing compared to me!"

    n "Himeko knowing Akemi defense is strong prepared a spell with all of her power and focusing it on one point, a spell strong enough to piece anything. As she does that, she continued her volley of attack not letting Akemi gain any room to rest"

    h "With this will be enough no matter how strong her defense is this spell will pierce through it!"

    n "As Akemi is a meter away from Himeko, Himeko unleashed the magic circle where a huge spike burst through with a lot of speed"

    n "This was the opportunity Akemi was waiting for as she clashed with the spell head on with the spell. Both attacks clashed to see which one is more powerful!"

    h "Give it up Akemi! If you apologize and grovel now, I'll let you live and be a part of my army or maybe even bring you back home"

    a "I don’t need your pity for I will be the victor here!"

    n "With all their might, the clashed continued until the spell broke surprising Himeko as the slash was able to connect to Himeko"

    n "Himeko collapsed as Akemi points her sword towards her"

    a "You lose Himeko, surrender and get rid of all of the demons and undead in the kingdom!"

    h "So, this is the power of the legendary items? With this power even if my army ambushed you, you will be able to wipe them out"

    h "I was supposed to let my demons ambush you but it is too late now. I will honor our duel and let my army retreat. For I was defeated with honor"

    n "As she used her last bit of energy to order her army to retreat, Himeko has met her end"

    n "The battle was done and Akemi was the victor!"

    n "Akemi released the king and with the help of the was able to free all of the prisoners"

    n "Aoi then reunites with Akemi"

    pra "You did it you won! You saved us all from Himeko! Our kingdom is once again free!"
















with dissolve
return

