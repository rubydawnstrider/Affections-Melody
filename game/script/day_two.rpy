##################################################
##  ██████╗  █████╗ ██╗   ██╗    ██████╗        ##
##  ██╔══██╗██╔══██╗╚██╗ ██╔╝    ╚════██╗       ##
##  ██║  ██║███████║ ╚████╔╝      █████╔╝       ##
##  ██║  ██║██╔══██║  ╚██╔╝      ██╔═══╝        ##
##  ██████╔╝██║  ██║   ██║       ███████╗       ##
##  ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝       ##
##################################################
label day2_label:
    scene school with fade
    serThought"I wonder what today will be like. Well, hopefully I won't knock into anyone else today."
    show armane normal at left
    a "Hey Serena over here!"
    show serena normal at center with moveinright
    show trista normal at right with moveinright
    t "Must you be so loud? The entire school probably heard you."
    ser "Hey Armane, Trista how are you this morning?"
    a "Not as good as you. I heard you are meeting the Ice Princess at lunch."
    ser "How do you know that?"
    t "It's all over school you are the first person since Naomi to be seen with her when it's not for class or student council business."
    ser "Student council business? Who's Naomi?"
    a "Selene is the student council president. And she hates having to be around others. She is super cold to everyone! Well, everyone but you that is. I knocked into her once and she gave me the darkest iciest glare ever!"
    ser "Did you apologize? And you still haven't told me who Naomi is."
    t "Ignore Armane she likes gossiping with Himeko. Naomi was a student here till last year. She was president and when she left Selene was made president in her place. But that's all I can really tell you, since it's not really my place."
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
    a "Thanks Ko, thanks."
    ser "Well, I'm off then see you after lunch."

    scene school_courtyard with fade
    show selene normal at right
    sel "So you actually came, huh?"
    show serena normal at center with moveinleft
    menu:
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
    ser "Well, I like it so far, but it's only my second day so I'm not sure I can make a good judgment yet."
    sel "What have you seen so far?"
    ser "I've been to the admissions office, my classroom, the quad, and this court yard."
    sel "Did you not get a tour?"
    ser "No, not yet."
    sel "Would you like one?"
    ser "Yes, that'd be nice." 
    show serena smile
    sel "Alright meet me here after school and I'll give you a tour of Akiria."
    ser "Thank you Selene."
    show selene smile
    sel "It is part of my job as student council president but you already know that. I heard Armane talking to you this morning by the front gates."
    ser "I'm sorry..."
    sel "Don't be at least this time what she said was true."
    #todo bell ringing

    scene classroomday with fade
    show himeko normal at left
    show serena normal at center with moveinright
    ser "Lunch was fine and that's all I'm telling you."
    show himeko irritated
    h "But that's nothing to work with Serenity!"
    ser "Exactly. I'm not a fan of having my personal interactions out there for everyone."
    h "You're no fun."
    show armane normal at right with moveinright
    a "Leave her be Ko you knew getting into this she wasn't going to talk." 
    h "Fine be that way I'm done with you!"
    hide himeko with moveoutleft
    ser "Is she always like that when she doesn't get her way?"
    a "Unfortunately. She's a really nice person most of the time..."
    ser "If you say so."
    a "So how was lunch really?"
    ser "It was nice we talked. And Selene is giving me a tour in a few minutes. I am to meet her in the court yard."
    a "Oh an afterhours tour huh?"
    ser "What?"
    a "Never mind. Just go to the court yard so Ice Princess doesn't think you stood her up, and causes you to move across the country to get away from her ok?"
    ser "Yeah... I'll see you later tell Trista bye for me?"
    a "Sure. See you tomorrow."

    scene school_courtyard with fade
    show selene normal at left
    show serena normal at center with moveinleft
    sel "Hello Serenity. Ready for your tour?"
    show serena smile
    ser "Hi Selene and you can call me Serena. So where do we start?"
    sel "How about we start with the gym its closest and you should be starting P.E. tomorrow." 
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
    show serena ouch at left
    ser "Uhh... Wha?..."
    sel "Great job, Mina."
    show mina gym_normal at right with moveinright #m=mina
    show serena normal
    m "Hey it's not my fault! How was I supposed to know you were giving the new girl a tour Ice Princess?"
    show selene angry
    sel "Watch it, Mina."
    show selene normal
    ser "Selene, what happened?"
    sel "Mina here hit you in the head with a volley ball. Are you ok?"
    ser "I think so." 
    m "I'm sorry for hitting you..."
    ser "It's ok it's not like you did it on purpose."
    sel "Come on Serena. I'm going to take you to the nurses office to make sure you are ok."
    ser "Ok. I guess I'll see you later, Mina."
    m "My name is Mina. Mina Anoi. You can call me Mina Serena."
    ser "I'm Serenity Anders. Bye Mina."

    scene officeday with fade
    show nurse normal at left #n=nurse
    show selene normal at center
    n "What seems to be the problem miss Morigana?"
    sel "Serena got hit in the head with a volley ball and passed out."
    n "Oh dear, well come over and sit down on the bed."
    show serena normal at right with moveinright
    ser "Yes, ma'am." 
    n "You look ok just if you get any headaches or feel dizzy go see your doctor right away. If you are at school you can come here alright?"
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
    show selene small_smile
    ser "Yes I'd like that very much."
    show serena smile
    sel "I will leave you here then and I will see you tomorrow."
    ser "Yes and thank you for waiting with me at the nurses office."
    sel "It's no trouble. Goodbye, Serena."
    ser "Bye, Selene."
    hide selene with moveoutleft
    serThought "Wow, I can't believe Selene is so caring! She's kind of like a real princess. Still, she didn't need to wait with me at the nurses office. I still can't get over how long it took."
    serThought "Once we were done there we had to part ways. Oh well, Selene wants to have lunch again with me tomorrow and show me the rest of the school after classes too."
    hide serena with moveoutright

    scene black with fade
    titles "{w=1.0}End Day 2{w=3.0}{nw}"

    jump end_day2