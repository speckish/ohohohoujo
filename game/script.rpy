# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

#custom positions for displaying sprites
transform nearleft:
    xalign 0.25
    yalign 1.0
transform nearright:
    xalign 0.75
    yalign 1.0

# The game starts here.

label start:

    # Example code for Gallery unlock
    # First, add the image to the list of CGs defined at the top of extras.rpy
    # Then simply show the image and it will automatically unlock!
    "Here is a test of the Gallery. We will show the test CGs one by one to unlock them in the gallery (accessible from the game menu at any time)."
    show cg_1 with dissolve
    "Here is the first one."
    hide cg_1
    show cg_2
    with dissolve
    "And the next one..."
    hide cg_2
    show cg_3
    with dissolve
    "And the third. Check the Gallery to see the status of the unlocks."
    hide cg_3
    show cg_4
    with dissolve
    "Fourth."
    hide cg_4
    show cg_5
    with dissolve
    "Fifth."
    hide cg_5
    show cg_6
    with dissolve
    "Sixth."
    hide cg_6
    show cg_7
    with dissolve
    "Seventh."
    hide cg_7
    show cg_8
    with dissolve
    "And the last one (for now)."
    hide cg_8 with dissolve

    # Example code for Music Room unlock
    # First, add the track to the list of tracks defined at the top of extras.rpy
    # Then simply play the track and it will automatically unlock!
    "Now let's test the Music Room, which works in a very similar manner. We will play the test tracks one by one to unlock them in the Music Room (accessible from the game menu at any time)."
    play music "audio/The Superiority_looped.mp3" fadein 0.5
    "Here is the first one."
    play music "audio/1. Unbreakable.mp3" fadeout 0.5 fadein 0.5
    "And the next one..."
    play music "audio/Abstract Vision #3 (Looped).mp3" fadeout 0.5 fadein 0.5
    "And the third. Check the Music Room to see the status of the unlocks."
    play music "audio/Hidden Threat_looped.mp3" fadeout 0.5 fadein 0.5
    "Fourth."
    play music "audio/Lift Me Up.mp3" fadeout 0.5 fadein 0.5
    "Fifth."
    play music "audio/Magic Within.mp3" fadeout 0.5 fadein 0.5
    "Sixth."
    play music "audio/Mystical  Loop #1.mp3" fadeout 0.5 fadein 0.5
    "Seventh."
    play music "audio/Soft Relaxing Track (looped).mp3 " fadeout 0.5 fadein 0.5
    "And the last one (for now)."
    stop music fadeout 0.5
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show amber at left
    show kaori at right

    # These display lines of dialogue.

    call speech_bubble_example
    # This ends the game.

    return
