# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define ser = Character('Serenity', what_slow_cps=20, color="#FF00CC")
define serThought = Character('Serenity', what_prefix="{i}", what_suffix="{/i}", what_slow_cps=20, color="#FF00CC")
define sel = DynamicCharacter("seleneName", what_slow_cps=20)
define a = DynamicCharacter("armaneName", what_slow_cps=20)
define t = DynamicCharacter("tristaName", what_slow_cps=20)
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
                          what_slow_cps=20 #Speed at which the text appears (slow)
                          ) 


# The game starts here.
label start:
    $seleneName = 'girl'
    $armaneName = 'girl'
    $tristaName = 'girl'
    $menuChoice = 1
    $seleneAffinity = 0
    
    scene roomday
    show serenity casual_ouch at center
    ser "Geez!"
    ser "I can't believe I overslept! I can't be late on my first day!"
    hide serenity casual_ouch with moveoutright
    
    scene black with fade
    $ renpy.pause(2.0)
    ser "Oof!"
    serThought "Warm and soft?... What did I run into?"
    scene school with fade
    show serenity school_ouch at left
    show selene school_shock at center
    $ renpy.pause(1.0)
    show selene school_normal
    ser "I'm so sorry! Are you alright?{nw}"
    show selene school_small_smile
    extend "{p=0.5}"
    show selene school_normal
    sel "Yes I’m fine. Are you? You seemed like you were in quite the rush."
    show serenity school_normal
    ser "I am. I thought I was going to be late for my first day of class-"
    sel "And ran into me."
    show serenity school_sad
    ser "Again, I'm sorry about that."
    #todo play school bell
    hide selene with moveoutright
    show serenity school_close_eyes
    serThought "Well {b}that{/b} certainly wasn't how I wanted to start my life at Akira. Oh well.{nw}"
    show serenity school_normal
    extend " I doubt I'll see that girl again."
    #todo change serenity to thoughtful/normnal after "oh well"?
    
    scene classroomday with fade
    show serenity school_normal at left
    show armane school_normal at center with moveinright
    a "Psst!{p=1.0}Psst!{p=1.0}Hey new girl. Is it true that you ran into the Ice Princess?"
    a "I'm Armane by the way. Armane Talier."
    $ armaneName = 'Armane'
    ser "Serenity Anders."
    show serenity school_smile
    ser "What do you mean \"Ice Princess\"?"
    show armane school_shock
    a "You don't know yet?!"
    ser "Know what?"
    a "Selene Morigana! {b}That{/b} Ice Princess!"
    $ seleneName = 'Selene'
    show serenity school_normal
    show armane school_normal
    ser "I'm sorry but I have no clue who you are talking about."
    a "Didn't you run into a girl with short black hair and blue eyes? Or did Himeko just see wrong?"
    ser "No, I did. I just never got her name. It's Selene Morigana then?"
    show armane school_stern
    a "Yes, and you'd better hope you don't run into her again!"
    ser "Why? She seemed nice enough."
    show armane school_vHappy
    a "Yeah right! She's as cold as they come! Why do you think everyone calls her Ice Princess?"
    show armane school_normal
    ser "I don't know and honestly I don't care." #ouch. cold. new ice princess here
    a "Really? Well in any case be careful. The last girl who got Ice Princess pissed ended up transferring to another school all the way across the country."
    ser "Across the country? Seriously?"
    a "Yep!"
    t "Are you spreading rumors about Morigana already, Armane?"
    show trista school_stern at right with moveinright
    t "Hi. I'm Trista Talier, Armane's cousin."
    show trista school_normal
    $ tristaName = 'Trista'
    ser "Hi I'm-{w=0.5}{nw}"
    t "Serenity Anders. Everyone knows who you are. We don't get transfers at the second term very often."
    t "You're the talk of the school, altough it seems not by everyone."
    show armane school_angry
    a "They aren't rumors! I heard them from Himeko!"
    t "So that makes them true? Listen Serenity, don't listen to whatever it is Armane is telling you, ok?"
    show armane school_normal
    ser "You guys can call me Serena. It's what my friends call me."
    ser "Well I'm going to go try to familiarize myself with the school's layout. See you later Trista, Armane."
    hide serenity with moveoutright
    
    scene hallwayday with fade
    show serenity school_close_eyes at center
    serThought "Wow those two are kind of strange but they seem nice. It looks like I'll have two friends here at least."
    sel "So we meet again."
    show selene school_normal at left with moveinleft
    ser "Huh? {w=0.3}{nw}"
    show serenity school_normal
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
    show selene school_smile
    sel "So if you don't care about rumors, how would you like to have lunch with me tomorow? Meet me in the courtyard at lunch, ok?"
    ser "Huh?...{w=0.5}Oh! Yes! I'll see you tomorrow then?"
    sel "Yes."
    hide selene with moveoutright
    $ renpy.pause(0.5)
    show serenity school_close_eyes
    serThought "Well this certainly was an interesting first day. I wonder how Selene got that nickname Ice Princess anyway?"
    show serenity school_normal
    serThought "Maybe I'll get answers tomorrow. I'd best head home now."
    hide serenity with moveoutright

    scene black with fade
    titles "{w=1.0}End Day 1{w=3.0}"
    
    return
