##################################################
##  ██████╗  █████╗ ██╗   ██╗    ██████╗        ##
##  ██╔══██╗██╔══██╗╚██╗ ██╔╝    ╚════██╗       ##
##  ██║  ██║███████║ ╚████╔╝      █████╔╝       ##
##  ██║  ██║██╔══██║  ╚██╔╝       ╚═══██╗       ##
##  ██████╔╝██║  ██║   ██║       ██████╔╝       ##
##  ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═════╝        ##
##################################################
label day3_label:
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
    titles "{w=1.0}End Day 3{w=3.0}{nw}"
    
    jump end_day3