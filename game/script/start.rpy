# Here's where we'll finish any new game setup, like creating all the variables we need to 
#  be able to save, like what the girls's names are.
# We'll also use this file as a kind of traffic controller to decide which day to go to.
#  -rw

label final_start:
    $seleneName = 'girl'
    $armaneName = 'girl'
    $tristaName = 'girl'
    $nurseName = 'nurse'
    $menuChoice = 1
    $seleneAffinity = 0
    
    # We don't actually need the label name to have "label" in it. 
    # The labels do have to be unique each time though.
    # I just figured by naming them "something_label", it would be easier to find them
    #  later if we need to and have multiple labels in one file
    # You use the following code to go to a specific label:
    #       jump labelname
    # where [labelname] is the name of a label.
    #  -rw
    
    # You can set up a label basically wherever you want (which is why we can put them 
    #  in separate files and they work okay with renpy.
    # You define a label like the following (a label get /NO\ indentation):
    #        label labelname:
    # Don't forget the colon after or renpy gets all kerfuffled.
    # [labelname] can be whatever you want. I has to be unique though. 
    # You can't have two different labels called "go_here". 
    # Renpy won't be able to tell which one you want.
    #  -rw
    
    jump day1_label
label end_day1:
# Renpy was being difficult and didn't like returning here on it's own.
# Once it finished the script in day1, it was all "no more. must be end of game lol"
# I'm looking into if there's a good way to avoid that other than using a jump to a second label like I'm currently using.
#  -rw
    jump day2_label
label end_day2:
    jump day3_label
label end_day3:
    jump day4_label
label end_day4:
    #todo looks like day 5 is only partially started - rw
    jump day5_label
label end_day5:
    
    # Technically, we don't need all the jump statements here.
    # We could just put the jump for day 2 at the end of the day_one file.
    # I like them being here because it makes it easier to see which day we're working on.
    # We could probably add little todo notes above each day for things we need to fix or work on and 
    #  then we have a nice summary in one place (if we remember to keep it up-to-date) for
    #  stuff to still do
    # We /could/ also use this to manage exactly what day we want to go to, like if we start doing 
    #  more complicated routes, we could make a selene_day_one file and an andrea_day_one file for 
    #  separating the two routes. Not sure we need /that/ but it's an option :P
    #  -rw

    # we'll leave the final 'return' call here to tell renpy that "the game is complete. go back to the start menu"
    return