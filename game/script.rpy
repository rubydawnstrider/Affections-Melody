####################################################################
##           /\      .-. .-.                                      ##
##       _  / |     / -'/ -'           /  .-.                     ##
##      (  /  |  .-/---/--.-.  .-. ---/---`-'.-._..  .-.     .    ##
##       `/.__|_.'/   / ./.-'_(      /   /  (   )  )/   )   / \   ##
##   .:' /    |`.' `.'  (__.'  `---'/ _.(__. `-'  '/   (   / ._)  ##
##  (__.' .-. `-'         .          .                  `-/       ##
##          /|/|         /          /                             ##
##         /   |  .-.   / .-._..-../ .    .-.                     ##
##        /    |./.-'_ / (   )(   /   )  /                        ##
##   .-' /     |(__.'_/_.-`-'  `-'-..(_.'                         ##
##  (__.'      `.                  ..-._)                         ##
####################################################################

# Declare characters used by this game.
init:
    image ctc_blink = Animation("gui/ctc.png", 0.7, "gui/ctc2.png", 0.5)
define ser = Character('Serena', what_slow_cps=25, color="#FF00CC", ctc="ctc_blink", ctc_position="nestled")
define serThought = Character('Serena', what_prefix="{i}", what_suffix="{/i}", what_slow_cps=25, color="#FF00CC", ctc="ctc_blink", ctc_position="nestled")
define sel = DynamicCharacter("seleneName", what_slow_cps=25, ctc="ctc_blink", ctc_position="nestled")
define a = DynamicCharacter("armaneName", what_slow_cps=25, ctc="ctc_blink", ctc_position="nestled")
define t = DynamicCharacter("tristaName", what_slow_cps=25, ctc="ctc_blink", ctc_position="nestled")
define h = Character('Himeko', what_slow_cps=25, ctc="ctc_blink", ctc_position="nestled")
define n = DynamicCharacter("nurseName", what_slow_cps=25, ctc="ctc_blink", ctc_position="nestled")
define m = Character('Mina', what_slow_cps=25, ctc="ctc_blink", ctc_position="nestled")
define an = Character('Andrea', what_slow_cps=25, ctc="ctc_blink", ctc_position="nestled")
define teach = Character('teacher', what_slow_cps=25, ctc="ctc_blink", ctc_position="nestled")
define non = Character(None, window_background="gui/textbox.png", ctc="ctc_blink", ctc_position="nestled")
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
    # for organization purpose, I moved the main script files into the script folder.
    # to get renpy to go to those, i made a label called 'final_start' in the start.rpy file
    # that's where we'll set all the variables (like affection points with the various girls) up
    # it's also where we'll control what do we're going to.
    # there's notes in start.rpy to help explain it.
    #
    # I wanted to move aaallllll the script files into the script folder but renpy expects there
    # to be a script.rpy file in the game folder >n< boo
    #  -rw
    jump final_start
    
    # Also, I think I'll try to remember to sign more explain-y comments with "-rw" for "ruby walker"
    #  So you can see that it's stuff I left vs stuff you leave. You could sign with -LG if you want...
