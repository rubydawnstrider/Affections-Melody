# TO DO LOOK UP HOW TO SEPERATE SCRIPT INTO MULTIPLE FILES
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
define an = Character('Andrea', what_slow_cps=25)
define teach = Character('teacher', what_slow_cps=25)
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
    hide serenity with moveoutright
    
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
    titles "{w=1.0}End Day 1{w=3.0}"

    #################################################################
    ##
    ## DAY 2
    ##
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
    titles "{w=1.0}End Day 2{w=3.0}"
    
    #################################################################
    ##
    ## DAY 3
    ##
    scene school with fade
    show armane normal at left
    show serena normal at center
    ser "I still don’t get yours and Himeko’s fascination with me and Selene."
    a "Cause its new!"
    show serena irritated
    ser "Glad to know I can entertain you."
    a "Yep! And it's great. Hey how was the tour yesterday?"
    show serena normal
    ser "It went fine until I got hit in the head with a volleyball by Mina Anoi in the gym."
    a "Ouch. Are you ok?"
    ser "Yeah, Selene took me to see Nurse Redford right away."
    a "That’s good. I’m glad you aren’t hurt."
    show selene normal at right with moveinright
    sel "As am I. Serena I’d like to talk to you for a moment if you don’t mind?"
    ser "No of course not."
    a "See you in class Serena, be careful."
    ser "See you soon."
    hide armane with moveoutleft
    show selene smile
    sel "I was wondering if meeting in the courtyard would be alright again for after school?"
    ser "Oh yes it is."
    show serena smile
    sel "Ok good I’ll see you at lunch then."
    #todo bell rings
    ser "Oh! I’ll see you later Selene."
    
    scene school_courtyard with fade
    show selene smile at right
    show serena normal at center with moveinleft
    ser "Sorry I’m late. Armane kept asking me questions."
    sel "It’s ok. What kind of questions?"
    menu:
        "She kept asking why I keep hanging out with you.":
            $ menuChoice = 1
        "She just asked me stuff.":
            $ menuChoice = 2
        "It was nonsense stuff. It doesn’t matter.":
            $ menuChoice = 3
    if menuChoice == 1:
        $ seleneAffinity += 5
        sel "I’m sorry if she’s bothering you."
        ser "No I think in her own weird way she is trying to just look out for me. That and I guess she can’t understand why I hang out with you."
        sel "Why do you? Continue to hang out with me I mean."
        ser "Because you are one of the nicest people I have met at this school and I like being around you. If that makes sense..."
        show serena blush
        show selene smile
        sel "No it does make sense and thank you. It’s been a long time since someone has enjoyed being in my company. I quite like being around you as well. You are very cute when you blush do you know that?"
        show serena shock
    elif menuChoice == 2:
        sel "Oh? Like what?"
        ser "Just things like why I hang out with you.  I told her  I hang out with you is because you are nice to me and I haven't seen anything that holds true to the rumors or the Ice Princess title. Sorry does that even make sense?"
        show serena blush
        show selene smile
        sel "No it does make sense and thank you. It’s been a long time since someone has enjoyed being in my company. I quite like being around you as well. You are very cute when you blush do you know that?"
        show serena shock
    elif menuChoice == 3:
        $ seleneAffinity -= 5
        sel "Oh ok..."
        ser "She just doesn’t see that you are fun to be around its why I like being with you and you are nothing like an Ice Princess. If that makes sense?..."
        sel "No it does make sense and thank you. It’s been a long time since someone has enjoyed being in my company. I quite like being around you as well."
    ser "Thank you that is very nice of you to say."
    show serena normal
    sel "But it is true. So where would you like to go after classes?"
    ser "I haven’t been to the library yet. And it would be safer of course unless the books decide to fall and hit me in the head."
    sel "Let’s hope not I don’t want to have to take you to Nurse Redford’s office two days in a row."
    ser "I'll be careful."
    show selene normal
    sel "What are you doing here Cross?"
    show himeko irritated at left with moveinleft
    h "Serenity wouldn’t tell me what was going on so I had to find out for myself!"
    show selene angry
    sel "So you decided to spy on us?! I thought you would have learned your lesson last time! But I see you didn’t!"
    show serena shock
    serThought "Whoa! Selene is kind of scary when she’s mad. Her voice is like ice and her eyes are so cold... Nothing like the warm ones she was looking at me with. What do I do?!"
    show himeko angry
    h "You’re new {i}girlfriend{/i} left me no choice. I’m merely keeping my promise {i}President{/i}."
    sel "Leave her out of this you know she has nothing to do with our issues Cross!"
    scene black with fade
    #todo bam sign on screen?
    
    scene school_courtyard with fade
    show himeko shock at left
    show selene shock at right
    show serena stern at center
    h "Y-you pushed me! You little bitch!"
    show serena close_eyes
    serThought "I shut my eyes reflexively waiting for the blow from Himeko’s raised hand there was the sound of flesh hitting flesh but I felt no pain. {nw}"
    $ renpy.play('sfx/punch.wav')
    with hpunch
    show selene normal
    extend "Se-Selene grabbed Himeko’s wrist stopping her!"
    show serena shock
    ser "S-Selene..."
    sel "Enough Himeko. Get back to class now or I’ll report you to admissions office for foul language during school hours and attempt of physical assault on another student. {nw}"
    hide himeko at moveoutleft
    show selene small_smile
    extend "Are you alright Serena?"
    show serena normal
    ser "I should be the one asking you that! Are you ok?"
    show selene smile
    sel "I’m fine. What were you thinking? Shoving another student can get you in serious trouble at Akiria."
    show serena sad
    ser "I know I just couldn’t let her continue on. It’s not fair what she’s doing trying to get gossip on you."
    sel "She’s been trying since we started Akiria."
    show serena normal
    ser "Why?"
    sel "It’s a long story and I don’t think now is the time. Class is going to start soon. I’ll meet you here after class."
    
    scene classroomday with fade
    show armane angry at left
    show trista normal at center
    show serena sad at right
    t "Let her talk Armane!"
    a "No! I should have known her hanging around Selene was a bad idea!"
    ser "If you would just listen for a moment I could explain."
    a "What is there to explain?! You shoved Ko!"
    t "Shut up Armane, let Serena talk."
    show armane irritated
    a "Fine but make it quick."
    ser "Selene caught her spying on us. Then Himeko started talking about how she had to because I wouldn’t talk to her, that just upset Selene more! {nw}"
    show serena cry
    extend "I didn’t know what to do! I just wanted them to stop shouting at each other. so I pushed her and she stumbled back a step. Then she called me a bitch and tried to slap me."
    show armane angry
    show trista shock
    show serena sad
    a "She tried to hit you for making her stumble a step?! She said you pushed her to the ground! She had dirt on her clothes!"
    ser "The only reason she didn’t succeed is because Selene caught her wrist before she could."
    show armane sad
    show trista sad
    a "I’m so sorry Serena. It’s just when Ko told me I got mad. It comes with the girlfriend territory."
    ser "I understand but next time, wait and hear both sides of the story first?"
    show serena normal
    a "Yeah. Hey I’m going to go. I need to have a long discussion with Ko."
    show armane stern
    show trista normal
    ser "I need to get going to Selene and I are going to finish my tour."
    a "Have fun. Tell mom I’ll be home by dinner ok Trista?"
    t "Yeah I’ll tell Aunt Maggie. Bye Serena see you tomorrow."
    
    scene school_courtyard with fade
    show selene normal at left
    show serena normal at center
    sel "So... Are you ok? I heard what happened with Armane and Cross."
    ser "Yeah I’m ok. Armane listened to my side and we are still friends. Thanks again for saving me. Again..."
    show selene small_smile
    sel "Any time. Now I believe you have a tour to finish."
    ser "Lead the way President Morigana."
    show serena silly
    sel "Ha ha ha. I didn’t know you were funny."
    show selene smile
    ser "I can be from time to time."
    show serena smile
    sel "Well, come on funny girl we have a tour to finish."
    ser "Right behind you."
    scene library with fade
    show selene normal at right
    show serena normal at center
    sel "This is the library the section to the left is nonfiction the right is fiction."
    show andrea normal at left with moveinleft
    an "Hello President Morigana... What brings you here?..."
    sel "Hello Andrea. I’m showing the new girl, Serenity Anders around today."
    an "Oh... Ok. Well, I’ll see you later President Morigana, Miss Anders."
    hide andrea with moveoutleft
    ser "She seems rather shy."
    sel "She is she doesn’t really interact with other students to well and prefers it here in the library."
    ser "Oh? I guess it makes sense books make wonderful companions."
    sel "You like reading?"
    show selene small_smile
    ser "Very much so although I have a soft spot for fantasy over the other genres."
    sel "Really? {nw}"
    show selene vHappy
    extend "I do too!"
    ser "Shh! we are in a library."
    show selene blush
    sel "Sorry I just got excited."
    show selene smile
    ser "Well, you’ve shown me the school now. Want to get out of here so we can talk at a normal volume?"
    sel "Sure courtyard ok?"
    ser "Mhmm."
    
    scene school_courtyard with fade
    show selene small_smile at center
    show serena normal at left
    sel "Thank you for letting me show you around it was fun even if it took two days to get it done."
    ser "No. Thank you for showing me. And I don’t mind that it took two days. "
    sel "That’s good. So... Would you like to make lunch a regular thing?..."
    ser "You sure you want to have lunch with me every school day?"
    show selene smile
    sel "Yes I’m sure."
    ser "Then who am I to deny you? I’d love to make lunch a regular thing."
    sel "Great! I’ll see you here then tomorrow?"
    ser "Yes. Selene?"
    sel "Hmm?"
    ser "Would you like to hang out before class with me?"
    sel "I’d like that. Here?"
    ser "Yes."
    sel "Ok. I’ll see you here first thing tomorrow morning."
    ser "Mmkay. See you tomorrow."
    hide selene with moveoutright
    show serena close_eyes
    serThought "Wow I can’t believe today. What was going on between Himeko and Selene? And why do I feel so happy when I’m around her? I was so happy when she held me yesterday and today she saved me again. {nw}"
    show serena smile
    extend "How can they call her Ice Princess she's been nothing but sweet and caring to me. She's more a normal princess than anything else."
    
    scene black with fade
    titles "{w=1.0}End Day 3{w=3.0}"
    
    #################################################################
    ##
    ## DAY 4
    ##
    scene school_courtyard with fade
    show selene normal at right
    sel "You came."
    show serena smile at center with moveinleft
    ser "Of course I did. Why wouldn’t I?"
    sel "Well after what Himeko tried..."
    ser "You thought I’d not come?"
    sel "Maybe?..."
    show selene blush
    ser "Well no need to fret I’m here."
    show selene smile
    sel "Thank you for coming."
    ser "Your welcome. I’m glad I came. Hey did you understand the last problem in the bio homework?"
    sel "Yeah. Here let me see what you have so far."
    ser "Ok. I got stuck at the identifying homo habilis."
    sel "Homo habilis traits are chapter three."
    ser "Oh? I thought it was chapter two no wonder I couldn’t find them. Thanks Selene."
    sel "You’re welcome."
    show himeko stern at left with moveinleft
    show selene normal
    show serena stern
    ser "Himeko? What are you doing?"
    h "I'm sorry..."
    sel "What?..."
    h "I’m sorry for spying on you two and I’m sorry for trying to hit you Serena. I was out of line."
    sel "Why are you apologizing now? In all the years i've known you. You've never cared."
    h "Armane. Well, I've don'e what I had to."
    hide himeko with moveoutleft
    sel "wonderful that just made things worse."
    ser "..."
    sel "What?"
    ser "Uhm... why did her apologizing make things worse? Isn’t Himeko’s apology a good thing?"
    sel "No. All it’s done is make Himeko hate me more. She will want to get back at me eventually."
    ser "How do you know she won’t just let it go?"
    sel "People like Himeko don’t let things go."
    ser "Oh..."
    #todo bell ring
    
    scene classroomday with fade
    show serena close_eyes at center
    serThought "I wonder why Himeko and Selene don’t get along? What happened to cause them to get at each other like that? Did it have something to do with Naomi?"
    show teacher angry at left with moveinleft
    teach "Miss Anders?... Miss Anders... MISS ANDERS!"
    show serena shock
    ser "Wha?"
    show serena blush
    teach "Nice of you to join us Miss Anders. Pay attention or you will be taking a trip to the admissions office."
    show serena sad
    ser "Yes Ma’am."
    show serena normal
    #todo bell ring
    teach "And that's all for History. Have a good lunch everyone."
    hide teacher with moveoutleft
    show armane normal at right with moveinright
    show trista normal at left with moveinleft
    a "Wow Serena what’s got you so flighty today?"
    ser "Nothing just thinking. Well I’m off to see Selene."
    t "Ok see you for Algebra. I’m going to the cafeteria coming Armane?"
    a "Right behind you."
    hide trista with moveoutleft
    hide armane with moveoutleft
    show himeko irritated at left with moveinleft
    h "Going to see the {i}Ice Princess{/i}?"
    ser "She has a name."
    h "Who cares?"
    show serena angry
    ser "I do! She’s nice and nothing like that nickname!"
    show himeko angry
    h "You don’t even know anything about her! How can you know?!"
    show serena sad
    ser "It doesn’t matter! She has never treated me poorly or coldly! She has been nothing but sweet and caring!"
    h "Puh-lease! It’s just because your new!"
    show selene angry at right with moveinright
    sel "What’s going on in here?!"
    h "Nothing that concerns you {i}president{/i}."
    show selene normal
    sel "Get out. I’ll deal with you later. {nw}"
    hide himeko with moveoutright
    extend "Serena are you ok?"
    show serena stern
    ser "I’m fine."
    sel "Are you sure?"
    ser "Yes. Selene why does she seem to hate you so much?..."
    sel "...Theres many reasons for Himeko’s hate. The biggest I suppose is Naomi."
    show serena sad
    ser "Naomi? Trista told me about her."
    sel "She was my best friend. She moved last year her dad got transferred."
    ser "What has that to do with Himeko?"
    sel "Himeko was originally vice president of student council with Naomi as president."
    ser "But Trista said you were made president in Naomi’s place..."
    sel "I was. It’s part of why Himeko hates me so much. She feels as though I stole what was rightfully hers. Himeko wasn’t right for student council president according to the school."
    ser "Oh..."
    sel "Serena?"
    ser "Yes?"
    sel "Promise me if she tries anything like this again tell me ok?"
    ser "Ok."
    sel "Thank you. Now let’s go and eat lunch."
    show serena normal
    ser "Ok."
    show selene small_smile
    sel "There. You look so much cuter when you smile."
    show serena blush
    ser "Thank you. You look cuter when you smile too. Why do you call me cute?"
    show selene smile
    sel "Because you are."
    ser "Ok..."
    
    scene school_courtyard with fade
    show serena normal at center 
    show selene smile at left
    sel "I’m sorry Himeko went after you."
    ser "It’s ok you couldn’t have known. And you were there to stop her before something bad happened."
    show selene normal
    sel "I guess… But I promise I will do my best to make sure she doesn’t do anything more to you."
    show serena smile
    ser "I know you will."
    show selene smile
    sel "... Serena?"
    ser "Yes?..."
    sel "Do you have plans after school tomorrow?"
    ser "No I don’t think I do."
    sel "Would you like to go into the shopping district with me? We could go to one of the cafés or something..."
    show serena vHappy
    ser "I’d like that! Very much."
    show selene blush
    sel "Great. I’ll meet you at the front gates after school then?..."
    show serena smile
    show selene smile
    ser "That sounds good to me."
    #todo bell ring
    
    scene classroomday with fade
    show teacher normal at left
    show serena normal at center
    teach "That's all for today have a good afternoon. I'll see you tomorrow."
    hide teacher with moveoutleft
    show armane normal at right with moveinright
    a "What did Himeko do to you?"
    ser "Nothing just got mad at me for hanging with Selene."
    a "I don’t know what’s wrong with her. I tried talking to her but she obviously didn’t listen."
    ser "It’s ok Selene came in and nothing bad happened."
    a "Still..."
    ser "Don’t worry about it. So she told me about why she and Himeko don’t get along."
    show armane shock
    a "Really?! Wow!... so what is it?"
    ser "Well, what I got was Himeko hates Selene because she became student council president instead."
    a "Really? That’s it?!"
    ser "Yeah. Oh! Also Selene and I are going out tomorrow after classes. I’m excited we are going to the shopping district."
    show armane normal
    a "Wow first week here and you have a date with the most wanted girl in school."
    show serena blush
    ser "Wh-What?! Most- most wanted girl?! But you call her that name."
    a "Part of it is. She's never really dated any girl in this school and she doesn’t have a boyfriend at another school like Trista. And she just turns down anyone who asks her out."
    ser "She was actually the one who brought up the hanging out after school... Do you think she thinks it’s a date?"
    a "I’m not sure maybe? Why don’t you bring an extra set of clothes to change into after class?"
    ser "I don’t know wouldn’t that be weird?"
    a "I don’t think so."
    ser "Ok I’ll do it then."
    show serena smile
    a "Cool! Well, I have to go find Trista see you tomorrow Serena."
    ser "Bye Armane."
    
    scene hallwayday with fade
    serThought "I wonder if what Armane said is true? I wonder if Selene thinks it’s a date?... Huh is that Selene?... {nw}"
    show selene irritated at center
    extend "and Himeko?!"
    show himeko angry at left
    show serena shock at right with moveinright
    sel "I told you to stop this!"
    h "Now why would I do that? It’s much more fun to see you finally react for once!"
    show selene angry
    sel "I don’t care what you do to me. But I won’t stand for you hurting Serena she has done nothing."
    h "No but she interacts with you. And I made a promise {i}President{/i}. I’m going to make you suffer for taking {i}my place{/i}."
    serThought "What do I do?!"
    menu:
        "*stay where you are*":
            $ menuChoice = 1
        "*intervene*":
            $ menuChoice = 2
        "*leave*":
            $ menuChoice = 3
    if menuChoice == 1:
        h "Well, I guess it doesn’t matter anyway. {nw}"
        show himeko smile
        extend "Hello Serena."
        ser "Serena?!"
        show selene shock
        sel "Why do you? Continue to hang out with me I mean."
        ser "Because you are one of the nicest people I have met at this school and I like being around you. If that makes sense..."
        show serena blush
        show selene smile
        sel "No it does make sense and thank you. It’s been a long time since someone has enjoyed being in my company. I quite like being around you as well. You are very cute when you blush do you know that?"
        show serena shock
    elif menuChoice == 2:
        $ seleneAffinity -= 5
        show serena stern
        ser "Hey! What’s going on?!"
        show himeko angry
        h "None of your business!"
        show selene normal
    elif menuChoice == 3:
        $ seleneAffinity += 5
        serThought "I shouldn’t hear this I’ll just go."
        h "Well, well, well... {nw}"
        show himeko smile
        extend "Look who’s here."
        show selene shock
        sel "Serena?!"
    h "Well, my work here is done. Toodles."
    show selene sad
    hide himeko with moveoutleft
    show serena normal
    ser "Selene... Are you alright?"
    sel "I’m fine. I’m sorry… I didn’t want you to see that."
    ser "It’s ok you were just trying to help get her to leave me alone."
    show selene small_smile
    sel "Yeah but it didn’t work. I’m sorry."
    ser "Hey, I’m a big girl I can take care of myself. So don’t worry ok?"
    sel "Alright. Well I should get home. I’ll see you tomorrow morning?"
    ser "At the gate."
    hide selene with moveoutleft
    serThought "Wow. I'm more confused than ever. I don't understand Himeko and Selene's angers and is tomorrow a date? With Selene? Why does that make my heart flutter so?"
    
    scene black with fade
    titles "{w=1.0}End Day 4{w=3.0}"     
    
     #################################################################
    ##
    ## DAY 5
    ##
    scene school with fade
    show serena close_eyes at center
    serThough "Wow I can’t wait to for school to be over and it hasn’t even started. I wonder if this is a date? I hope Selene doesn’t mind that I brought a change of clothes."
    show armane normal at right with moveinright
    a "Serena?... Serena… SERENA!"
    show serena shock
    ser "What?! What is it?! What happened?!"
    a "Geez you were hard to wake up. So what were you day dreaming about? Selene?"
    show serena blush
    ser "N-No! O-of course not!"
    a "Suuurrre."
    show serena normal
    show trista normal at left with moveinleft
    t "Leave Serena and her daydreams about her girlfriend alone Armane. You get like that too when you think about Himeko."
    show armane blush
    a "Sh-shut up!"
    show trista happy
    t "So I’m right then? I knew it!"
    a "Whatever! I’m going to find Ko at least she doesn’t tease me!"
    hide armane blush with moveoutright
    t "So you were day dreaming about Selene then?"
    ser "I wasn’t day dreaming about Selene!"
    show selene normal at right with moveinright
    sel "What about me?"
    ser "Nothing! Nothing!"
    show serena blush
    sel "Oh really now?"
    show selene small_smile
    show trista blush
    t "Ok... Well, I’ll see you in class Serena, President."
    hide trista with moveoutleft
    return
