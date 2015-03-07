# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define ser = Character('Serena', what_slow_cps=25, color="#FF00CC")
define serThought = Character('Serena', what_prefix="{i}", what_suffix="{/i}", what_slow_cps=25, color="#FF00CC")
define sel = DynamicCharacter("seleneName", what_slow_cps=25)
define a = DynamicCharacter("armaneName", what_slow_cps=25)
define t = DynamicCharacter("tristaName", what_slow_cps=25)
define h = Character('Himeko', what_slow_cps=25)
define n = DynamicCharacter("nurseName", what_slow_cps=25)
define m = Character('Mina', what_slow_cps=25)
define non = Character(None, window_background="gui/textbox.png")
define titles = Character(None,
                          color="#F0BCEC",
                          what_size=20, #Font size
                          what_xalign=0.5, #Centers text within the window
                          window_xalign=0.5, #Centers the window horizontally
                          window_yalign=0.5, #Centers the window vertically
                          text_align=0.5, #Centers text within the window, just in case
                          window_background=None,#Removes the window, so only the text shows
                          window_xfill=False,
                          what_slow_cps=25 #Speed at which the text appears (slow)
                         ) 

# The game starts here.
label start:
    $seleneName = 'girl'
    $armaneName = 'girl'
    $tristaName = 'girl'
    $nurseName = 'nurse'
    $menuChoice = 1
    $seleneAffinity = 0
    
    scene roomday
    show serena ouch at center
    ser "Geez!"
    ser "I can't believe I overslept! I can't be late on my first day!"
    hide serena ouch with moveoutright
    
    scene black with fade
    $ renpy.pause(2.0)
    ser "Oof!"
    serThought "Warm and soft?... What did I run into?"
    scene school with fade
    show serena ouch at left
    show selene shock at center
    $ renpy.pause(1.0)
    show selene normal
    ser "I'm so sorry! Are you alright?{nw}"
    show selene small_smile
    extend "{p=0.5}"
    show selene normal
    sel "Yes I'm fine. Are you? You seemed like you were in quite the rush."
    show serena normal
    ser "I am. I thought I was going to be late for my first day of class-"
    sel "And ran into me."
    show serena sad
    ser "Again, I'm sorry about that."
    #todo play school bell
    hide selene with moveoutright
    show serena close_eyes
    serThought "Well {b}that{/b} certainly wasn't how I wanted to start my life at Akira. Oh well.{nw}"
    show serena normal
    extend " I doubt I'll see that girl again."
    #todo change serenity to thoughtful/normnal after "oh well"?
    
    scene classroomday with fade
    show serena normal at left
    show armane normal at center with moveinright
    a "Psst!{p=1.0}Psst!{p=1.0}Hey new girl. Is it true that you ran into the Ice Princess?"
    a "I'm Armane by the way. Armane Talier."
    $ armaneName = 'Armane'
    ser "Serenity Anders."
    show serena smile
    ser "What do you mean \"Ice Princess\"?"
    show armane shock
    a "You don't know yet?!"
    ser "Know what?"
    a "Selene Morigana! {b}That{/b} Ice Princess!"
    $ seleneName = 'Selene'
    show serena normal
    show armane normal
    ser "I'm sorry but I have no clue who you are talking about."
    a "Didn't you run into a girl with short black hair and blue eyes? Or did Himeko just see wrong?"
    ser "No, I did. I just never got her name. It's Selene Morigana then?"
    show armane stern
    a "Yes, and you'd better hope you don't run into her again!"
    ser "Why? She seemed nice enough."
    show armane vHappy
    a "Yeah right! She's as cold as they come! Why do you think everyone calls her Ice Princess?"
    show armane normal
    ser "I don't know and honestly I don't care." #ouch. cold. new ice princess here
    a "Really? Well in any case be careful. The last girl who got Ice Princess pissed ended up transferring to another school all the way across the country."
    ser "Across the country? Seriously?"
    a "Yep!"
    t "Are you spreading rumors about Morigana already, Armane?"
    show trista stern at right with moveinright
    t "Hi. I'm Trista Talier, Armane's cousin."
    show trista normal
    $ tristaName = 'Trista'
    ser "Hi I'm-{w=0.5}{nw}"
    t "Serenity Anders. Everyone knows who you are. We don't get transfers at the second term very often."
    t "You're the talk of the school, altough it seems not by everyone."
    show armane angry
    a "They aren't rumors! I heard them from Himeko!"
    t "So that makes them true? Listen Serenity, don't listen to whatever it is Armane is telling you, ok?"
    show armane normal
    ser "You guys can call me Serena. It's what my friends call me."
    ser "Well I'm going to go try to familiarize myself with the school's layout. See you later Trista, Armane."
    hide serenity with moveoutright
    
    scene hallwayday with fade
    show serena close_eyes at center
    serThought "Wow those two are kind of strange but they seem nice. It looks like I'll have two friends here at least."
    sel "So we meet again."
    show selene normal at left with moveinleft
    ser "Huh? {w=0.3}{nw}"
    show serena normal
    extend "Oh. It's you. I'm sorry for running into you earlier Ms. Morigana." # todo Morigana-san?
    sel "So someone told you about me hmm? Must have been Armane."
    menu:
        sel "Tell me. What did they say about me?"
        "*Play dumb*":
            $ menuChoice = 1
        "Mention the \"Ice Princess\" thing":
            $ menuChoice = 2
        "Just her name":
            $ menuChoice = 3
    if menuChoice == 1:
        $ seleneAffinity += 5
        ser "...What do you mean?"
        sel "Really? She didn't tell you anything about my Ice Princess nickname?"
        ser "She may have mentioned it. Why? Is is a problem? It's not like I believe it."
        sel "Really? You don't? Why not?"
    elif menuChoice == 2:
        ser "She told me your name and called you Ice Princess."
        sel "I should have known the little blabber mouth was going to start spouting lies to the new girl as soon as she could."
        ser "I'm sure she didn't mean anything by it. And I don't believe her anyway."
        sel "Really? You don't? Why not?"
    elif menuChoice == 3:
        $ seleneAffinity -= 5
        ser "Just your name. That's all."
        sel "Good at least she knows to keep her mouth shut about things that don't concern her."
        ser "Even if she had told me something, it's not like I would believe her anyway."
        sel "Really? You wouldn't? Why not?"
    ser "Because when I met you outside before school you seemed nice and you seem nice now so why should I listen to rumors when I have no evidence of them being factual?" #whoa there missy. take a breath!
    ser "It'd seem silly if you ask me."
    show selene smile
    sel "So if you don't care about rumors, how would you like to have lunch with me tomorow? Meet me in the courtyard at lunch, ok?"
    ser "Huh?...{w=0.5}Oh! Yes! I'll see you tomorrow then?"
    sel "Yes."
    hide selene with moveoutright
    $ renpy.pause(0.5)
    show serena close_eyes
    serThought "Well this certainly was an interesting first day. I wonder how Selene got that nickname Ice Princess anyway?"
    show serena normal
    serThought "Maybe I'll get answers tomorrow. I'd best head home now."
    hide serena with moveoutright

    scene black with fade
    titles "{w=1.0}End Day 1{w=3.0}"

    #################################################################
    ##
    ## DAY 2
    ##
    scene school with fade
    serThought"I wonder what today will be like. Well hopefully I won't knock into anyone else today"
    show armane normal at left
    a "Hey Serena over here!"
    show serena normal at center with moveinright
    show trista normal at right with moveinright
    t "Must you be so loud the entire school probably heard you."
    ser "Hey Armane, Trista how are you this morning?"
    a "Not as good as you. I heard you are meeting the Ice Princess at lunch."
    ser "How do you know that?"
    t "It's all over school you are the first person since Naomi to be seen with her when it's not for class or student council business."
    ser "Student council business? Who's Naomi?"
    a "Selene is the student council president. And she hates having to be around others. She is super cold to everyone! Well everyone but you that is. I knocked into her once and she gave me the darkest iciest glare ever!"
    ser "Did you apologize? And you still haven't told me who Naomi is."
    t "Ignore Armane she likes gossiping with Himeko. Naomi was a student here till last spring. But that's all I can really tell you since it's not really my place."
    ser "Oh. Ok then." 
    # todo bell ringing sound

    scene classroomday with fade
    show serena normal at left
    ser "I just don't see what the big deal is... I'm just eating lunch with Selene."
    show armane normal at center with moveinright
    a "Himeko tell Serenity it's a bad idea. I don't want the Ice Princess to hurt her." 
    #how do I make himeko's chatacter??? h=himeko
    show himeko normal at right with moveinright
    h "Really Armane its fine it will give me more to talk about. I'm all for Serenity to go."
    a "Thanks Ko thanks."
    ser "Well I'm off then see you after lunch."

    scene school_courtyard with fade
    show selene normal at right
    sel "So you actually came huh?"
    show serena normal at center with moveinleft
    menu:
        sel "So you actually came, huh?"
        "Do you ever just say hello? And yes I did.":
            $ menuChoice = 1
        "I did.":
            $ menuChoice = 2
        "Why? Is it that surprising?":
            $ menuChoice = 3
    if menuChoice == 1:
        $ seleneAffinity += 5
        show selene smile
    elif menuChoice == 2:
        show selene small_smile
    elif menuChoice == 3:
        $ seleneAffinity -= 5
    sel "How do you like Akiria Academy?"
    ser "Well I like it so far, but it's only my second day so I'm not sure I can make a good judgment yet."
    sel "What have you seen so far?"
    ser "I've been to the admissions office, my classroom, the quad, and this court yard."
    sel "Did you not get a tour?"
    ser "No, not yet."
    sel "Would you like one?"
    ser "Yes, that'd be nice." 
    # serena smiles
    sel "Alright meet me here after school and I'll give you a tour of Akiria."
    ser "Thank you Selene."
    # selene smiles
    sel "Well it is part of my job as student council president but you already know that. I heard Armane talking to you this morning by the front gates."
    ser "I'm sorry..."
    sel "Don't be at least this time what she said was true."
    #todo bell ringing

    scene classroomday with fade
    show himeko normal at left
    show serena normal at center with moveinright
    ser "Lunch was fine and that's all I'm telling you."
    h "But that's nothing to work with Serenity!"
    ser "Exactly. I'm not a fan of having my personal interactions out there for everyone."
    h "You're no fun."
    show armane normal at right with moveinright
    a "Leave her be Ko you knew getting into this she wasn't going to talk." 
    #himeko stern face
    h "Fine be that way I'm done with you!"
    hide himeko with moveoutleft
    ser "Is she always like that when she doesn't get her way?"
    a "Unfortunately. She's a really nice person most of the time..."
    ser "If you say so."
    a "So how was lunch really?"
    ser "It was nice we talked. And Selene is giving me a tour in a few minutes. I am to meet her in the court yard."
    # armane smirks
    a "Oh an afterhours tour huh?"
    ser "What?"
    a "Never mind. Just go to the court yard so Ice Princess doesn't think you stood her up and causes you to move across the country to get away from her ok?"
    ser "Yeah... I'll see you later tell Trista bye for me?"
    a "Sure. See you tomorrow."

    scene school_courtyard with fade
    show selene normal at left
    show serena normal at center with moveinleft
    sel "Hello Serenity. Ready for your tour?"
    # serena smiles
    ser "Hi Selene and you can call me Serena. So where do we start?"
    sel "Well how about we start with the gym its closest and you should be starting P.E. tomorrow." 
    ser "Yeah I think we are playing basketball."

    scene gym with fade
    show selene normal at left
    sel "This is the gym and over there on the left is the girls changing rooms." 
    #Bam apears somewhere on screen with sound maybe???

    scene black with fade
    serThought "What just happened? Why do I suddenly smell Lilac? I feel warm too. I wonder why?" 

    scene gym with fade
    show selene normal at center
    serThought "Selene is holding me?!?! Wow her eyes are so pretty..."
    sel "Serena? Serena?..."
    show serena normal at left
    ser "Uhh... Wha?..."
    sel "Great job, Mina."
    show mina normal at right with moveinright #m=mina
    m "Hey it's not my fault! How was I supposed to know you were giving the new girl a tour Ice Princess?"
    #Selene pissed face 
    sel "Watch it, Mina."
    ser "Selene, what happened?"
    #selene normal face
    sel "Anoi here hit you in the head with a volley ball. Are you ok?"
    ser "I think so." 
    m "I'm sorry for hitting you..."
    ser "It's ok it's not like you did it on purpose."
    sel "Come on Serena. I'm going to take you to the nurses office to make sure you are ok."
    ser "Ok. Well I guess I'll see you later, Mina."
    m "My name is Mina. Mina Anoi. You can call me Mina Serena."
    ser "I'm Serenity Anders. Bye Mina."

    scene officeday with fade
    show nurse normal at left #n=nurse
    show selene normal at center
    n "What seems to be the problem miss Morigana?"
    sel "Serena got hit in the head with a volley ball and passed out."
    n "Oh dear well come over and sit down on the bed."
    show serena normal at right with moveinright
    ser "Yes, ma'am." 
    n "Well you look ok just if you get any headaches or feel dizzy go see your doctor right away. If you are at school you can come here alright?"
    ser "Ok. Thank you." 
    sel "Thank you for looking at her Nurse Redford." #show nurse as nurse Redford from now on
    $ nurseName = 'Nurse Redford'
    n "Of course, miss Morigana. Now you two best head on home before it gets to be to late."
    "Serena and Selene" "We will."

    scene school_courtyard with fade
    show selene normal at left
    show serena normal at center
    ser "Thank you for today Selene. I'm sorry the tour got cut short."
    sel "Don't be we can continue tomorrow after classes. We can meet in the court yard for lunch again too if you'd like."
    #selene small smile 
    ser "Yes I'd like that very much."
    #serena smiles big
    sel "Well I will leave you here then and I will see you tomorrow."
    ser "Yes and thank you for waiting with me at the nurses office."
    sel "It's no trouble. Goodbye, Serena."
    ser "Bye, Selene."
    hide selene with moveoutleft
    serThought "Wow, I can't believe Selene is so caring! She's kind of like a real princess. Still, she didn't need to wait with me at the nurses office. I still can't get over how long it took."
    serThought "Once we were done there we had to part ways. Oh well Selene wants to have lunch again with me tomorrow and show me the rest of the school after classes too."
    hide serena with moveoutright

    scene black with fade
    titles "{w=1.0}End Day 2{w=3.0}"

    return
