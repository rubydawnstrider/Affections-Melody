##################################################
##  ██████╗  █████╗ ██╗   ██╗     ██╗           ##
##  ██╔══██╗██╔══██╗╚██╗ ██╔╝    ███║           ##
##  ██║  ██║███████║ ╚████╔╝     ╚██║           ##
##  ██║  ██║██╔══██║  ╚██╔╝       ██║           ##
##  ██████╔╝██║  ██║   ██║        ██║           ##
##  ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═╝           ##
##################################################

# I cheated for the fancy day 1 banner up top. I added the ##### around it, but i got the rest from:
#  http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=
# make sure to use the 'ANSI Shadow' font.
# I also just copy the line of just #'s from this file for the other files' banners so they're all the same length total
#  -rw

# When you make a new file, use the 'File > New Tab' from the menu, or hit CTRL+N or double-click in the little blank space to the right of the tabs for the open files.
# Make sure to do two things when you save it the first time:
#  * save it with a name so we know what the file has in it, you can see I've been naming the day files as 'day_[day number as a word]'
#  * make sure you save the file as filename.rpy
#    # that ".rpy" is important cuz it tells renpy "hey. this is a renpy file. use it, kay?"
#  -rw

# This is where that 'jump day1_label' heads to. 
# If you think it would be helpful(for searching and editing purposes), you can even put labels for the start of a new scene on a day.
# Like the scene where serena bumps into selene the first time, you could label it put 'label day1_meet_selene:' before 
#  the 'scene black with fade' line (currently it's line 27 in this file)
# I'd name the helper labels as 'day#_label_want_to_use' to help keep them organized. and use underscores for spaces since a label has to be one "word".
#  -rw
label day1_label:
    scene roomday
    show serena ouch at center
    ser "Geez!"
    ser "I can't believe I overslept! I can't be late on my first day!"
    hide serena ouch with moveoutright
    
    scene black with fade
    # start with a 1-second pause
    $ renpy.pause(1.0)
    # wait for a second after the text appears. if user doesn't click to advance by then, move on. otherwise the punch doesnt make sense
    ser "{cps=0}Oof!{/cps}{w=1.0}{nw}"
    # {cps=some number} changes text speed. cps of zero instantly displays the text
    $ renpy.play('sfx/punch.wav')
    with hpunch
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
    serThought "Well, {b}that{/b} certainly wasn't how I wanted to start my life at Akira. Oh well.{nw}"
    show serena normal
    extend " I doubt I'll see that girl again."
    #todo change serenity to thoughtful/normnal after "oh well"?
    
    scene classroomday with fade
    show serena normal at left
    show armane normal at center with moveinright
    a "Psst!{p=1.0}Psst!{p=1.0}Hey, new girl is it true that you ran into the Ice Princess?"
    a "I'm Armane, by the way. Armane Talier."
    $ armaneName = 'Armane'
    ser "Serenity Anders."
    show serena smile
    ser "What do you mean, \"Ice Princess\"?"
    show armane shock
    a "You don't know yet?!"
    ser "Know what?"
    a "Selene Morigana! {b}That{/b} Ice Princess!"
    $ seleneName = 'Selene'
    show serena normal
    show armane normal
    ser "I'm sorry, but I have no clue who you are talking about."
    a "Didn't you run into a girl with short blue hair and grey eyes? Or did Himeko just see wrong?"
    ser "No, I did. I just never got her name. It's Selene Morigana then?"
    show armane stern
    a "Yes, and you'd better hope you don't run into her again!"
    ser "Why? She seemed nice enough."
    show armane vHappy
    a "Yeah right! She's as cold as they come! Why do you think everyone calls her Ice Princess?"
    show armane normal
    ser "I don't know, and honestly, I don't care." #ouch. cold. new ice princess here
    a "Really? Well, in any case be careful. The last girl who got Ice Princess pissed ended up transferring to another school- all the way across the country."
    ser "Across the country? Seriously?"
    a "Yep!"
    t "Are you spreading rumors about Morigana already, Armane?"
    show trista stern at right with moveinright
    t "Hi. I'm Trista Talier, Armane's cousin."
    show trista normal
    $ tristaName = 'Trista'
    ser "Hi I'm-{w=0.5}{nw}"
    t "Serenity Anders. Everyone knows who you are. We don't get transfers in the second term very often."
    t "You're the talk of the school, with almost everyone, it seems."
    show armane angry
    a "They aren't rumors! I heard them from Himeko!"
    t "So that makes them true? Listen Serenity, don't listen to whatever it is Armane is telling you, ok?"
    show armane normal
    ser "You guys can call me Serena. It's what my friends call me."
    ser "Well, I'm going to go try to familiarize myself with the school's layout. See you later Trista, Armane."
    hide serena with moveoutright
    
    scene hallwayday with fade
    show serena close_eyes at center
    serThought "Wow those two are kind of strange but... It looks like I'll have at least two friends here."
    sel "So we meet again."
    show selene normal at left with moveinleft
    ser "Huh? {w=0.3}{nw}"
    show serena normal
    extend "Oh. It's you. I'm sorry for running into you earlier, Ms. Morigana." # todo Morigana-san?
    sel "So someone told you about me hmm? Must have been Armane."
    menu:
        sel "Tell me. What did they say about me, hmm?"
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
    ser "Because when I met you outside before school you seemed nice, and you seem nice now. Why should I listen to rumors when I have no evidence of them being factual?" #whoa there missy. take a breath!
    ser "It'd seem silly, if you ask me."
    show selene smile
    sel "So, if you don't care about rumors, how would you like to have lunch with me tomorow? Meet me in the courtyard at lunch, ok?"
    ser "Huh?...{w=0.5}Oh! Yes! I'll see you tomorrow then?"
    sel "Yes."
    hide selene with moveoutright
    $ renpy.pause(0.5)
    show serena close_eyes
    serThought "Well, this certainly was an interesting first day. I wonder how Selene got that nickname Ice Princess, anyway?"
    show serena normal
    serThought "Maybe I'll get answers tomorrow. I'd best head home now."
    hide serena with moveoutright

    scene black with fade
    titles "{w=1.0}End Day 1{w=3.0}{nw}"
    # added a no-wait after the tree seconds cuz if the user doesn't realize they need to click to go on, they 
    #  might just wait there. the {nw} will automatically go on after the 3 second pause. -rw

    # We kinda need to jump back to the main script. I don't like this and there's gotta be a better way.
    # For now, we'll just put an 'end_day#' label after each day since it works...
    #  -rw
    jump end_day1