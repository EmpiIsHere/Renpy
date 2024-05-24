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

define grdelf = Character("Elf Guard") 

define elder  = Character("Elfe Elder")

define dwarfgrd=Character("Dwarf Guard")

define durin=Character("Durin")

define k = Character("King Throin")

define min1 = Character("Minion 1")

define min2 = Character("Minion 2")

define c = Character("King Charles")

define dra =Character ("Draythorn")


# The game starts here.

label start:

    scene black
    n"Summer has passed, and another school year is approaching. Students are excited as the new year will embrace them."
    n"Everyone’s busy with their requirements. And there’s one student who made the room a bit odd as she walks on"
    show akemi def
    n"Akemi is an ordinary student. She always wears her jolliest smile."
    n"School Day is done as she makes her way to her favorite spot which is at the library she saw an old book"
    n"Akemi pick it up and try to read it but there is no content of the book only a Riedel"
    a"Hmm there's a Riedel (It lights sometimes; it’s dark sometimes everyone wants to walk all over me. What am I?)?"
    n"As akemi read the riedel she try to answer it "
    a"Moon"
    n"The book glows a wight light and Akemi close her eye"
    n"Akemi hear that someone is calling for her as she slowly open her eyes, she saw this mysterious woman"
    Mysterious"Hero please wake up.."
    a"uh?....waht happen...and who are you"
    Mysterious"Thank you are aright....My name is Aoi i am the daughter of king Charles and from the kingdom of Azurevale"
    pra"May i ask your name Hero"
    a"Hi my name is Akemi....Where am I..."
    pra"Hero Akemi then...you are in the ruins forest this place is used to summoned hero from another world"
    a"Huh i am no hero i am just a regular student"
    n"As Akemi seems confused Princess Aoi try to explain everything as she gradually understands the situation Akemi ask another question."
    a"I see so that's what happened....then why did you summon me here"
    pra"Please help me on my quest to defeat an evil magician that have been terrorizing my Kingdome and my father..."
    pra"please help me"
    n"Akemi have been to honest and always helping someone who needs her help even if she put her sefl in danger."
    a".....Okey ill help you Princess Aoi"
    pra"Really thank you so much hero Akem"
    a"It's fine.... and please stop calling me Hero Akemi it's kind of embarrassing"
    a"Just call me Akemi.. "
    pre"Understood.... Then you can call me Aoi its so nice to meet you"
    a"Yeah nice to meet you too."
label branch_2:
    n"As Akemi and Princess Aoi have decided to start their adventure journey."
    show princess def at left
    pra"Thank you for helping me Akemi..."
    hide princess def
    show akemi def at left
    a"It okey your welcome.... so, are we going straight to kingdom of Azurevale?"
    hide akemi def
    show princess def
    pra"No, Himeko is a powerful magician simple physical and magical attack won't hurt her."
    hide princess def
    show akemi def at left
    a"So how will I be able to beat Himeko then?"
    hide akemi def
    show princess def at left
    pra"We need to get the 3 legendary items that can only be wielded by a hero who came far from our world and that is you. "
    hide princess def
    show akemi def
    a"So, what are these 3 legendary items. Then."
    hide akemi def
    show princess def
    pra"The first is the blade of Ethereal Fang the legend tells that it has been forge and bless by the ancient gods and imbued with the power to pierce through darkness itself."
    pra"The second item is the Necklace of Valor it is made by the most skilled dwarf and has the ability to increase physical and magical power to its full potential."
    hide princess def
    show akemi def 
    a"What about the third item."
    hide akemi def
    show princess def
    pra"Princess Aoi: I can't tell you yet. In order to obtain the last item, you need to have the first two. You need their combined power before you can even attempt to retrieve the third item."
    hide princess def
    show akemi def
    a"I see..."
    hide akemi def
    show princess def
    pra"so which of the two item you want to get first."
    hide princess def
    menu:
        "Blades of Ethernal Fang":
            $ menu_flag = True
            jump branch_3

        "Necklace of Valor":
            $ menu_flag = False
            jump branch_4
 
#Blade of Ethernal Fang
label branch_3:
    n"Ethereal Fang legend speak that it is resting place deep within the heart of mystical forest known as the Whispering Woods and the location of the forest is only know the elder elf wich is located at Faewood."
    #Princess aoi
    show princess def
    pra"We must travel deep in the forest to meet the elf elder and ask the Whispering woods."
    n"Upon reaching the guard gates of the Faewood they met with a vigilant sentry, wary of outsider. "
    grdelf"Stop right there, who are you and state your buisness."
    n"With Aoi regal presence lending credibility and royal etiquette"
    pra"Good day to you sir, I am Princess Aoi from the kingdom of Azurevale, we humbly ask request to meet and ask guidance of the elf elder."
    grdelf"Wait here i will ask for the chef of the village."
    n"As the time Akemi and Princess Aoi for the approval of the chef village."
    grdelf"You may enter and be careful"
    n"As the they both enter the elf village akemi is amaze to the scenery of the elf village and the center have this giant tree"
    hide princess def
    show akemi def
    a"Wow look at that tree, it looks bigger than the biggest building in my hometown."
    n" As they enter inside the giant tree, they are great by the elder of the elf village"
    elder"Greetings Princess Aoi you have grown"
    pra"It's nice to see you all again."
    elder"Hmm. Princess Aoi are you doing okey, we heard what happen about your father and your kingdom, as you know that we are a friend to your ancestor and your father, we are sorry to hear it."
    hide akemi def
    pra"Thank you for your concern, allow me to introduce you to Akemi the hero i brought to this world to defeat Himeko."
    a"Hello, it's so nice to meet you all."
    elder"Hmmm. We guest that you are here to ask us the location of the Blade of Ethereal Fang yes."
    pra"Yes, we would like to use it to deafet Himeko."
    elder"We will tell you the location, but it's very dangerous in the forest, and many monsters have been wandering there do you still want to know."
    pra"Yes"
    elder"And how about you, are you prepared to fight such a monster."
    n"As as they look at akemi waiting to her response"
    a"Yes, because I made a promised to aoi to help her."
    elder"Very well then, the location of the sword is located at the center of Whispering Woods west from here."
    elder" but recently there's a giant snake wandering and we try everything we can but the monster can heal itself easily,"
    elder "Princess Aoi be careful you and hero Akemi Please look after her, and one more thing go to the center ofthe forest monster won't go near the location of the sword"
    a"Yes"
    pra"We will be careful and thank you"
    n"As they start their quest to get the sword Akemi ask Princess Aoi."
    a"Aoi, why did Himeko attack and claim your kingdom."
    pra"Himeko is also a magic caster like me but instead of helping others, she used it for her personal gain and Himeko is obsessed with gaining more power and she fell into the darkness and wanted to control others through fear and power."
    a"So, she's really obsesses in gaining more power huh."
    n"As Akemi and princess aoi got closer to their destination suddenly an angry giant snake attack them."
    a"Ahh!" 
    pra" Ahh!"
    a"Are you okey Aoi!" 
    pra"Yes, I am fine"
    n"As the dodge the attack of the giant snake Akemi suddenly got stumble by a tree"
    a"Ahhh!"
    n"As the snake notice the snake suddenly release a purple smoke and release it Akemi suddenly feel dizzy and feel weak and the giant snake saw Akemi lie down on the ground the snake tries to attack again."
    pra"Akemi, Look out!!"
    n"As Princess Aoi saw Akemi can't move, she used her magic and attack the snake with fire."
    pra"FireBall"
    n"As the Giant snake got attack by a fire it got distracted and Princess Aoi used the chance to go see Akemi condirtion"
    pra"Are you alright Akemi."
    a" Yeah I am fine...just a little dizzy."
    pra" Let's retreat for now."
    a"Yeah, you're right."
    n"As they retreat far away from the monster for now, they rest for a bit."
    pra"Are you okey Akemi?."
    n"As Princess Aoi asked Akemi if she is okey she didn't get a respond. "
    pra"Akemi,Akemi hey are you okey!"
    n"Princess Aoi shake Akemi and notice something is strange on Akemi"
    pra"Huh!? Poison."
    pra"that is the content of the purple smoke that the snake release earlier"
    pra" I must do something."
    n" As soon as Princess Aoi knows that it is a poison, she began sight an incantation for magic"
    pra"Heal!.....Yes, it works, Akemi are okey?"
    a"Aoi, what happened?"
    pra"Thank goodness you're okay...are you still injured."
    a"No i think i am fine...What happend anyway"
    pra"You got poison."
    a"I see thank you for helping me"
    pra"Its okey, don't mention it"
    n"As they rest for a bit Akemi notices something rustelling in the forest, the giant snake appears again."
    a"Aoi look out!"
    pra"Ahh!"
    n"Princess Aoi and Akemi were able to dodge the snake attack."
    pra"Be careful Akemi"
    a"Yeah, we need to run deep in the forest."
    pra"Yeah, you're right the monster won't go near the location of the sword."
    pra"Akemi i will cast a support magic on you and can you give me sometime i will use my magic."
    a"Okey got it."
    n" As Akemi tries to distract the giant snake Princess Aoi is preparing her magic."
    pra"I am ready Akemi."
    a"okey!."
    pra"Mega Flare!!"
    n"As the snake got attacked again by fire Akemi rush toward on Princess Aoi."
    a"We did it lets go."
    pra"Yeah, but i can’t run fast i used all my magic power on that attack. "
    a"Okey then il carry you lets go."
    pra"Thank you Akemi."
    a"Its okey."
    n"Akemi carries Princess Aoi and ran fast at the center of the forest as soon as they see the center Akemi go toward it."
    a"AAHHH! We made it!"
    pra"Yeah."
    n"As they both got in the center of the forest Akemi look at the sword "
    a"So that is the Blade of Ethereal Fang"
    pra"Yes, go on Akemi try to pull it."
    a"Yeah..Okey lest do this."
    n"As Akemi Approach the sword, she can feel its power wondering if this is the reason why no monster won't go near it, as Akemi hold the sword, she felt warm feeling all over her body." 
    a "Here’s got nothing."
    n"As soon as akemi tried to pull the sword she felt it was too light."
    a"Yes!, Look Aoi i did it i pulled the sword."
    n"Princess Aoi looks at Akemi and smiles. "
    pra" Yes, you did it."
    a"let's rest here for a while, are you still tired."
    pra"Yes, thank you for asking."
    n"Akemi and Princess Aoi finally got rest for a bit they are now trying to go back to the elf village once again."
    a"Finaly We got the Blade of Ethereal Fang we are close in saving your Kingdome Aoi"
    pra" Yes."
    n"Akemi and Princess Aoi chatting, the snake appears again it their way."
    a"Aoi be careful let's defeat this giant snake for real this time."
    pra"Right"
    n"Akemi and Princess Aoi prepare to fight the giant snake and Akemi proposes a plan."
    a"Use your magic and support and i will draw its attention try to use fire magic only "
    pra"Okey"
    n"Akemi draw the attention of the snake and princess aoi used fire magic to make the giant snake more confused, Because of this the giant snake try to use the purple Princess used her support magic to make Akemi resistance to poised for a short amount of time."
    pra"Now is your chance Akemi."
    a"Right,HYAAAA!!."
    n"Akemi jumps high and goes directly to attack the head of the snake. As she swings her sword to the head, Akemi lands and the giant snake's head."
    a"Wow this sword cut it like paper...we did it Aoi."
    pra"Yeah....that was amaizing Akemi."
    a"Let's go back to the elf village."
    pra"Yeah."
    n"Akemi and Princess Aoi got Infront of the elf village they are surprised to see that Akemi is holding the Blade of Ethereal Fang"
    elder"We are glad you are safe Princess Aoi and Akemi. "
    pra"Thank you."
    n"Akemi and Princess Aoi explain what happened, they are relief and surprised because they were able to slay the giant snake and the Elf elder explains about that giant snake."
    elder"We have been for long time..that snake suddenly appear out of knowhere and releasing a purple smoke."
    pra"Himeko must be the one behind it. She must be trying to stop someone who will search for the sword."
    elder"It must be.... but the sword can’t be pulled by a normal person, Akemi."
    a"Yes"
    elder"The sword chooses you to be its user please use it only for good."
    a"I will."
    elder"We assume that the two of you will continue your journey, we will pray for your success and safety, good luck Akemi and Princess Aoi."
    a"Thank you"
    pra"Thank you."
    n"Akemi and Princess Aoi say goodbye to the elf village they are now off on their next journey."

    if menu_flag == False:
        jump branch_5
    elif menu_flag == True:
        jump branch_4



#Necklace of Valor
label branch_4:
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
    
    pra"Look at the busy street Aoi, there are a lot of markets and lot of weapons on display and a lot of beautiful jewelry and shining armor its really like a fantasy."
    
    pra"Yes, there's a lot of people than the last time i visit here."
    
    n"As they approach the imposing gate of the royal castle, Akemi and Princess aoi was able to meet King Throin."
    
    k"Welcome, it an honor to meet you once more and to meet your esteemed companion"
    
    pra"t's an honor to meet you to king Throin allow me to introduce my companion, her name is Akemi she is the hero i summon"
    
    pra"It's a pleasure to meet you, King Throin."
    
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

    n"With a final, resounding clash, General Ragnor fell to the ground, defeated. The cavern echoed with the silence of their victory, and fo deep in the minning cave Akemi and Princess Aoi was
    surprise the beautiful of the gem infornt of them."

    pra"Akemi, look! Over there, deep in the mining cave. It's the Mystic Lunar, shimmering in a radiant sky blue. It's truly breathtaking... Our journey was not in vain, this gem holds the key to our kingdom's salvation."

    a"Yeah, Aoi I've never seen anything so beautiful. It's like the heavens themselves have descended into this cave. With this gem, we can forge the Necklace of Valor and bring hope back to your people."

    n"As Akemi and Princess Aoi return, King Throin greeted them with gratitude. He thanked both of them for their bravery and informed us that General Ragnor had been defeated. It seems our victory has weakened our enemy's forces"

    a"Thank you, King Throin. We're honored to have helped. Our encounter with General Ragnor was challenging, but with Princess Aoi's leadership, we prevailed."

    k"Your bravery has brought light to our kingdom in these dark times. With the Mystic Lunar in our possession, we can now forge a necklace stronger than ever before. Guards, prepare the forge and summon our most skilled smith. The Necklace of Valor shall rise again!"

    pra"Akemi, our journey together has been filled with danger and uncertainty, but seeing the Mystic Lunar fills me with hope."

    a"Aoi it's been an honor to fight by your side. Your courage and determination inspire me. Together, we've overcome every obstacle, and I have no doubt that we'll continue to do so."

    pra"hank you, Akemi. Your strength and loyalty have been invaluable to our cause. Let us go forth and ensure that the Necklace of Valor is forged with the same determination that brought us here."

    n"As Akemi and Priccess Aoi rest for a few day to finish the forge of Necklace of Valor Akemi notice somting is worrying Princess Aoi."

    a"Aoi is something bothering you I can see the worry in your eyes."

    pra"Thank you Akemi, I am just worry about my father and the people of Azurevale"

    a"I see...But for now, let us focus on the task at hand. We have the gem, and soon we will have the necklace. With its power, we will be better equipped to face whatever challenges lie ahead"

    pra"Yes..your right,we must stay focused on our mission"

    n"As they awaited the necklace's completion, Akemi and Princess Aoi spent their days in the dwarven kingdom, assisting those in need. Though outwardly brave, the weight of their responsibilities grew heavier, intensifying their sense of urgency."

    n"On the day of completion, King Throin presented the finished necklace to Akemi and Princess Aoi"

    k"This necklace is a testament to your bravery and determination. May it serve you well in your quest to bring peace to your kingdom."

    pra"Thank you King Throin"

    a"Thank you"

    n"As they set their next journey,the grand halls of the royal palace, they were greeted with cheers and applause from the dwarven citizens, who hailed them as heroes."

    if menu_flag == False:
        jump branch_3
    elif menu_flag == True:
        jump branch_5

label branch_5:

    n"Akemi and Princess Aoi continue and prepare their journey and Princess Aoi turned to Akemi with a determined look in her eyes."

    pra"Akemi, there is one final item we need to retrieve to defeat Himeko once and for all."

    n"he explained, her voice filled with resolve"

    pra"t is the Crimson Radiance Ring, said to protect its wearer from even the most powerful of attacks. However, it is in the realm of one of the Heavenly Dragons, guarded for millennia, awaiting the true and worthy hero to retrieve it."

    n"Akemi nodded, understanding the gravity of their task." 
    a "Then we must journey to the realm of the Heavenly Dragon and prove ourselves worthy of the Crimson Radiance Ring."
    n"She replied, her voice steady with determination"
    a"Together, we will face whatever challenges lie ahead and emerge victorious."
    n"With their hearts set on their next quest, Akemi and Princess Aoi, their minds filled with thoughts of the trials and tribulations that awaited them."
    n"As one of the minions of General Ragnor escaped from the kingdom of the dwarves, he wasted no time in delivering his message to Himeko. Rage consumed her as she learned of Princess Aoi and Akemi's involvement."
    min1"Your Majesty General Ragnor was defeated by a Princess Aoi and a girl named Akemi."
    h"What...they defeated Ragnor what Ragnor is supposed to be strong, and he was defeated."
    min1"What should we do you Majesty. "
    h"Bring me King Charles (king of Azurevale) from his cell now!"
    min2"Yes, your Majesty."
    n"The Minion brings King Charles to Himeko and asks him the location of the Crimson Radiance Ring."
    h"Hmmm...I want you to tell me something and don't think of lying to me! "
    c"Hmmm... "
    h"Tell me the location of the Crimson  of Radiance Ring."
    c"Hmmm...I won't tell you even if you threat to kill me"
    h"hmm....If you don't tell me the location of the Crimson radiance ring i will kill ever person in this castle HAHAHHAHAH!"
    h"And that's not all I will also kill your beloved daughter"
    c"You monster don't you dare to hurt her...or-"
    h"AHAHAHAH!...Or what haha what can you possible do in your current state...I make you a deal, I will order my Servant to only capture Princess Aoi and return her to you safe and sound if you tell me the location of the ring."
    c"Hmmm....I want you to give me your word that you won't hurt my daughter and my people."
    h"Hehe, Fine i give you my word"
    c"The location of the Crimson Radiance Ring is in the Heavenly Dragon Mountain."
    h"Was that hard to say, take him back to his cell. "
    n"With King Charles returning to back to his cell his heart heavy with guilt and despair, he hoped to protect his people and Princess Aoi from her wrath."
    n"But as soon as the information was in her grasp, Himeko's true intentions were revealed. With a wicked grin, she ordered her minion to return the king to his cell, his fate sealed for daring to defy her."
    h"Heavenly Dragons Mountain huh....Let's see if this time they will survive HAHAHAAHAH!."
    n"Himeko concocted a sinister plan to ensure Akemi and Princess Aoi's demise. Harnessing her dark powers, she formed a purple orb infused with her malevolent energy."
    h"Come my servant i want to give you a special quest right now you are my general I need you to deliver this in the heavenly dragons Mountain now, "
    min1": I am honored your majesty."
    n"The orb contains some of Himeko power and it will realease  a purple smoke that will make any living creature to go berserk and becomes Himekos pawn,meanwhile Akemi and Princess Aoi continue their journey. "
    a"So thats the heavenly Mountain Dragon."
    pra"Yes..theirs also a dragon living there"
    a"Really thats amazing, wait if there is a dragon living there then we will get attacked by it"
    pra"No its okey the dragon thats been living there is actually a kind dragon he never go attack human as long as it doesnt bother him."
    a"Really then were safe..as long as we dont bother him okey seems easy."
    pra"Yes"
    n"As Akemi and Princess Aoi continue their walk a violent wind suddenly whipped around them."
    a"Aoi, AAHHHH!"
    pra"Akemi, AAHHHH!"
    a"Why you!!"
    n"As the dragon poised itself for another strike, Akemi leaped high into the air, carrying Princess Aoi to safety."
    a"Are you okey Aoi. "
    pra"Yes, i am fine, Thank you."
    a"Stay here i deal with the dragon."
    n"Akemi drew her sword, ready to face the formidable foe. With a swift and precise strike, she lunged at the dragon, but to her astonishment, her blade had no effect. "
    a"What...It didn’t work, what's going on?"
    n"Princess Aoi uses her magic to strike the dragons wing and to Akemi is surprised that magic is working. She also try to use it."
    a"So magic works huh..then let's see you try to take this."
    n"The sword lights fire and Akemi try to slash the dragon but as soon as Akemi is about to attack Princess Aoi stops her."
    pra"Wait Akemi!!"
    a"Huh,why whats wrong."
    n"As soon as Akemi got stopped by princess Aoi the dragon raise up and started to fire a multipe fireball."
    a"Whooo!, Thats was close."
    pra"Akemi lets hide for now, trust me. "
    a"Really, Okey if you say so."
    n"Akemi and princess Ai ran deep to the forest were the stumble a lake and Princess Aoi explained to Akemi what she noticed."
    a"Whats, why did you stop me. "
    pra"That dragon seems in pain and under an influence of something like there is something controlling it against its will."
    a"Then what should we do."
    pra"I know that i am asking too much, but can we save it. "
    a"Okey if that's what you want so how we will help it."
    pra"Hmmmmm...how about we investigate his lair maybe we can find somethig there or we can try to make it unconscious and see what is going on to him Whats your choice?"

menu:
        "Investiagte the cause":
            $ menu_flag = True
            jump invest_dragon

        "Fight the dragon":
            $ menu_flag = False
            jump fight_dragon

label invest_dragon:
    a"We should investigate it then" 
    pra"Okey then "
    n"As they try to hide from the trees to go look for the dragon lair Princess Aoi saw something."
    pra"Hmm,whats that, Akemi come over here"
    a"What did you saw."
    pra"There's seemed to be a cave over theirs seem to be a purple fog inside it."
    a"We Should go and see it."
    pra"Okey, but first i will cast a spell to prevent us from that purple smoke. "
    n"Narrator: Akemi and Princess Aoi enter the cave the saw a purple orb that is releasing purple smoke. "
    a"What is that should we go and see it."
    pra"Okey, but lest be carefull"
    n"Akemi and Himeko got closer to the purple orb Princess Aoi looks it and realize that this is Himeko’s doing."
    pra"I see now Himeko must have used this purple orb to control the dragon. "
    a"Should we destroy it then?"
    pra"Wait if we just destroy it the smoke will get more powerful  "
    a"So What should we do"
    pra"We need to purify it by chaneling light magic maybe it will stop the smoke but my magic it not enough to purify it but I think you can do it  Akemi you Blade of Ethereal Fang to cast the light magic and necklace of valor to boost your magic."
    a"Okey, i will try"
    n"Akemi try to focus with the help of the elder of the elf Akemi is able to cast magic into the sword and as the sword lights all the smoke slowly vanishes, and the purple orb suddenly turns gray. "
    a"HMMMMMM!!!! "
    pra"Yes thats it Akemi you did it now we should see what the condition of the dragon is outside "
    n"Akemi saw the dragon fall sleep nearby when the purple smoke is gone. "


label fight_dragon:

    a"We should fight it if we dont try to stop in now the dragon might attack an innocent"
    pra"Okey, I understand."
    pra"First we need plan, magic is the only thing to hurt him and we have to knock him down so i will be able to observe what is wrong with him, "
    a"I Have an idea Aoi."
    pra"Okey lets hear it. "
    a"First I will draw its attention and you try to attack him with magic and once he is down i will try to use a bind magic so he mont be able to move"
    pra"Okey I,got it."
    n" As Akemi try to shout loudly to lure the dragon."
    a"HYYAAAAAAAAAAA!!"
    n" A violent wind dash through Akemi as see observe where will it attack Akemi. "
    a"Hmmm,Over there, aoi get ready."
    pra"On it."
    n"Narator As akemi draw the attention of the dragon princess Aoi used this chance to fire at the dragon."
    pra"FireBall"
    n"As the dragon got hit Akemi used a binding magic to seal the movement of the dragon while Princess Aoi notice the purple aura raleasing n the body of the dragon"
    pra"Akemi I got it we need to use light magic to remove the purple aura but my magic is not enough."
    a"I will do it i will used the Blade of Ethereal Fang to cast the light magic and necklace of valor to boost your magic"
    n"As Akemi concentrate in casting light magic the sword light and the necklace glow and the purple aura is slowly fading and making the dragon fall sleep"


label outcome:
    n"Exhausted from the Akemi and Princess Aoi shared a triumphant smile, knowing they had succeeded in freeing the dragon from Himeko's control, As minutes passed, the dragon stirred awake, its eyes filled with remorse for its actions. "
    a"Hi are you okey?"
    pra"How are you feeling?"
    Dragon"Yes and thank you for saving me."
    pra"My name is Aoi and this is my companion Akemi."
    a"Hi whats your name."
    Dragon"Akei and Aoi.....My name is Draythorn" 
    n"As they rest for bit, Draythorn asks what are they doing here in heavenly mountain?"
    pra" We are looking for the Crimson of Radiance Ring."
    dra"So you are also looking for it too?" 
    a"What do you mean by that "
    dra"When i was under the influence of that purple smoke a keep hearing a female voice to destroy someone and bring her the ring."
    pra"Its Himeko again."
    a"Yeah and she is probably trying to get the ring for herself."
    dra" So that's her name huh, it's true that i have the ring but it won't work if I don't give my magic to power to it, I will give you the ring as a reward for helping me and promise me this Akemi and Princess Aoi to defeat Himeko."
    a" I Promise"
    pra" I Promise"
    n"Draythorn gave Crimson Radiance Ring. Akemi donned the ring, feeling its power course through her veins, and to their surprise, Draythorn blessed the ring, imbuing it with even greater strength. "
    n"With their mission accomplished, Draythorn offers Princes Aoi and Akemi a ride. As they soared towards the edge of the forest, they bid farewell to Draythorn, expressing their gratitude for his aid and the swift ride, With the Crimson Radiance Ring in their possession and Draythorn's blessing, Akemi and Princess Aoi continued their quest with renewed determination"
    




















with dissolve
return

