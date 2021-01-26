# The script of the game goes in this file.

## side portrait versions of the characters, for use during CGs/misc scenarios

# define c_side = Character("Cerise")
# define e_side = Character("Eleanor")
# define f_side = Character("Fiona")
# define s_side = Character("Sofia")
# define a_side = Character("Antigone")



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
    # "Here is a test of the Gallery. We will show the test CGs one by one to unlock them in the gallery (accessible from the game menu at any time)."
    # show cg_1 with dissolve
    # "Here is the first one."
    # hide cg_1
    # show cg_2
    # with dissolve
    # "And the next one..."
    # hide cg_2
    # show cg_3
    # with dissolve
    # "And the third. Check the Gallery to see the status of the unlocks."
    # hide cg_3
    # show cg_4
    # with dissolve
    # "Fourth."
    # hide cg_4
    # show cg_5
    # with dissolve
    # "Fifth."
    # hide cg_5
    # show cg_6
    # with dissolve
    # "Sixth."
    # hide cg_6
    # show cg_7
    # with dissolve
    # "Seventh."
    # hide cg_7
    # show cg_8
    # with dissolve
    # "And the last one (for now)."
    # hide cg_8 with dissolve

    # # Example code for Music Room unlock
    # # First, add the track to the list of tracks defined at the top of extras.rpy
    # # Then simply play the track and it will automatically unlock!
    # "Now let's test the Music Room, which works in a very similar manner. We will play the test tracks one by one to unlock them in the Music Room (accessible from the game menu at any time)."
    # play music "audio/The Superiority_looped.mp3" fadein 0.5
    # "Here is the first one."
    # play music "audio/1. Unbreakable.mp3" fadeout 0.5 fadein 0.5
    # "And the next one..."
    # play music "audio/Abstract Vision #3 (Looped).mp3" fadeout 0.5 fadein 0.5
    # "And the third. Check the Music Room to see the status of the unlocks."
    # play music "audio/Hidden Threat_looped.mp3" fadeout 0.5 fadein 0.5
    # "Fourth."
    # play music "audio/Lift Me Up.mp3" fadeout 0.5 fadein 0.5
    # "Fifth."
    # play music "audio/Magic Within.mp3" fadeout 0.5 fadein 0.5
    # "Sixth."
    # play music "audio/Mystical  Loop #1.mp3" fadeout 0.5 fadein 0.5
    # "Seventh."
    # play music "audio/Soft Relaxing Track (looped).mp3 " fadeout 0.5 fadein 0.5
    # "And the last one (for now)."
    # stop music fadeout 0.5


    ### I want to use the dissolve+ drop in function we discussed before on these narration bubbles but for now I'm just saying "with dissolve"


label opening_narration:

    ### ATL: zoom + pan over silver-valley1 for a few seconds

    #SFX : play music lyric & peaceful (piano ver) , loop first 18 seconds

    narration"Silver Valley..." with dissolve

    ### continue slow pan right to left  for a few seconds

    narration "A beautiful, old town,"
    narration "nestled between two mountain ranges."

    ###ATL Snowflakes swirl over the screen

    ## ATL cross dissolve to silver-valley2
    ### ATL: slow pan-zoom left to right, glittery tones

    narration "In the winter, the town glistens with the frost that gives the valley its name."

    #SFX : play music lyric & peaceful (piano ver) , jump to 0:18


    narration "But, in the heart of the valley..." with dissolve

    #ATL dissolve to silver-valley3
    #ATL: slow pan from left to right

    narration "Hidden away from the eyes of the world outside..." with dissolve


    narration "There lies an eternal garden..." with dissolve

    #stop snow
    #sfx: music cue

    #ATL slow pan upwards on main building ext

    narration "{b}Silver Valley Women's University.{/b}" with dissolve

    #ATL stop pan

    narration "In this prestigious academy,"
    narration "the flowers of love and youth bloom eternal."

    #scene black
    #atl show lily closeup, slowly pan down
    #SFX : play music lyric & peaceful (piano ver) , jump to 1:18

    narration "For every flower there is a season,"
    narration "and for every season, there is another story of love, loss, and passion."

    #ATL: stop pan down over the dewy lily on the lily closeup
    #ATL lily close up sparkle animation

    narration "So it is known to us..."


    narration "{i}The Lilies of Silver Valley.{/i}"

    #show logo with moveinfrom top + dissolve
    #pause 3.0

    #SFX fade out music

    ####Note to self- if you end up going through with an OP, use Two Sides.mp3

    ##scene black
    #play sound subtitle.ogg
    centered "The Snow Queen and the Winter Prince"

    #hold on this until music ends

label LateToAnimeSchool:

        ##scene outside with slideinleft

        ##Date Indicator top right: Wednesday, December 1st.

        ### 'Student' and 'Prof' dialogue, unless otherwise indicated, will have speech bubbles (without tails) in various
        ### places around the screen.

        #play sound walla

        student "Ugh, it's so cold...{nw}"

        student "{i}Ach-oooo!{/i}"

        #stop sound with fadeout 2.0

        student "Professor, do we HAVE to have class outside?"

        e "{i}{size=+10}Ohohohohoho!{/size}{/i}"

        "A familiar, scornful laugh echoed off the snowy flagstones."

        ##show Eleanor laugh at right with hpunch

        ##show Eleanor smile with dissolve

        e "It's hardly the teacher's fault you left your jacket in the dorm."

        e "Now you want to make it {i}our{/i} problem?"

        e "How impudent."

        student "Tch-!"

        student "Teacher's pet."

        #show Eleanor scorn with dissolve

        e "What was that?"
        e "I'm afraid the snow must be muffling your voice."

        ##show Eleanor smile

        e "...Which, if you recall,"
        e "Overcoming such challenges is the entire reason we're having our diction class outside."


        e "Of course, if you can't manage to remember that much..."

        ##show Eleanor vhappy with dissolve

        e "Maybe you should just drop the class."

        student "Why, you-!"
        student "*mutter mutter*"
        student "That Eleanor..."
        student "*mutter*"

        ##show Eleanor with dissolve

        prof "Now, now, ladies, settle down!"

        prof "Miss Silviera is right."
        ##show Eleanor smile

        prof "You've known this presentation was happening for over a week now."

        prof "Now everyone, take a seat on the benches, and we'll get started."

        prof "Miss Silviera, you're up first."

        ##hide Eleanor with dissolve

        prof "And remember, this recitation is a {i}major{/i} part of your grade!"

        ##show Sofia worried at left with dissolve.

        s "(Cece...where are you...?)"

        s "(You're up second to present...)"

        prof "Everyone, quiet!"
        prof "Eleanor, you may begin."

        ##show Eleanor vhappy at right with dissolve

        e "Of course."

        narration "As Eleanor Silviera began her recitation,"

        narration "Sofia Elena continued to glance at her watch."

        ##show Eleanor smile with dissolve
        e "{i}A winter garden in an alder swamp,{/i}"
        ##show Sofia with dissolve
        e "{i}Where conies now come out to sun and romp,{/i}"
        e "{i}As near a paradise as it can be / And not melt snow or start a dormant tree.{/i}"

        student "(Do you see that?)"
        student "(On the river?)"
        ##show Eleanor annoyed
        e "Ah-{i}HEM.{/i}"

        ##show Eleanor with dissolve
        e "{i}It lifts existence on a plane of snow,{/i}"
        e "{i}One level higher than the earth below,{/i}"

        student "(It's getting closer!)"
        #sound ice skates
        ##show Sofia shock

        student "(Where?)"
        student "(I cant see!)"

        prof "Ladies, don't-"

        student "Oh my god, is that Cerise?"
        ##show Eleanor annoyed
        "Just like that, chaos erupted among the gathered students trying to get a look down the river."
        #play sound chatter
        ##show Sofia worried
        s "Oh, dear."
        student "She's skating on the river!"
        student "Is that even safe?!"
        student "She's coming in {i}really fast{/i}!"
        #sfx - wooosh!
        ##hide Eleanor and Sofia

        ##show Cece smile at center with vpunch
        c "(I'm gonna make it!)"
        student "Haha! {p=.2}{i}You go, Mountbatten!{/i}"
        student "How can she have that little drag with all that hair?"
        ##show Cece vhappy with dissolve
        c "G-Good morning, everyone!"
        #multiple student bubbles
        student "Good morning!~~"

        #sfx:ice crack
        ### ATL:cut-in of a tree breaking, the word CRACK!!!

        #sfx: branch falling to ground
        #sfx gasp
        ##show Cece shock
        student "It fell in front of her!"
        student "She's going too fast to stop!"
        student "She's gonna crash- !!"
        student "Oh, I can't look!"
        c "{i}HUP!{/i}"
        ##hide Cece
        #sfx like a twirl noise
        #sfx landing in ice skates
        ##show Sofia shock at left
        ## show Eleanor shock at right
        s "A double axel?!"
        #sfw crowd "WHOAA!", whistles
        ##show Cece sheepish at center
        c "{i}Huff..huff....{/i}"
        c "P-pardon my tardiness!"
        ##hide Sofia with dissolve

        #sfx applause
        ##show Cece surprise
        ##show Eleanor annoyed
        #multiple student bubbles
        student "A perfect ten!"
        student "That was so {i}cool!{/i}"
        ##show Cece vhappy
        student "I totally forgot how cold I even was!"
        c "Thank you..."

        ## show Eleanor mad at right
        e "Mountbatten....!"
        e "{i}AHEM!{/i}"
        ##show Eleanor smile with dissolve
        e "You {i}interrupted{/i} me."
        ##show Cece blush
        c "I- I did?"
        ##show Cece laugh
        c  "Oh-"
        c "{i}{size=+10}Ohohohohoho!{/size}{/i}"
        ##show Eleanor mad
        ###ATL: show cut in of Cece shock
        c "{i}(CRAP...! I did it again...!){/i}"
        ##show Sofia worried at left
        ##show Cece
        ##with dissolve
        s "She's sorry, Miss Silviera."
        s "Cerise-"
        "The professor glowered at Sofia over his glasses."
        s "Pardon, me- {p}{i}Miss Cerise{/i}"
        s "There's have a spot for you to sit right here. Come along, now."
        e "Hmph."
        ##hide Eleanor with dissolve
        ##hide Sofia with dissolve

        prof "All right, ladies! That's quite enough."
        prof "Miss Mountbatten."
        ##show Cece cringe
        c "Y-yes sir?"
        Prof "Please refrain from causing a scene if you're going to be late."
        c "Yes sir."
        prof "Now take your seat, please."
        prof "Miss Silviera, please continue."
        ## fade to black,
        #sfx- class bell rings.

        narration "After Class..."
        ##Show sofia mad at center
        ##show Cece cringe at left
        ##with hpunch
        s "Cerise, what were you {i}thinking{/i}?"
        ## show Sofia worried
        s "Eleanor looked like she was going to absolutely end you!"
        ##show Cece sad with dissolve
        c "I didn't mean to..."
        Sofia "Intentional or not, you {i}need{/i} to stop antagonizing her."
        ##show Sofia frown
        s "Eleanor Silviera isn't someone you want to make an enemy of."
        #### speech bubble from offscreen
        e "You should listen to your friend, Mountbatten."

        label .ellie_intro:
            ####PseudoCG: Eleanor intro.
            #### ATL: Zoom+crop onto Eleanor default sprite.
            #### Lillies and shoujo bubble screentone
            #SFX: sparkle, title sting
            #### Text Displayable: Eleanor Helena Silviera
            #### Text Displayable row 2: Second Year Student
            #pause 3.0
            ####Hide intro text
        ##show Sofia worry
        ##show Cece blush
        ##show Eleanor mad at right
        ##with dissolve

        e "Carol Cerise Mountbatten!"
        e "Don't think I'll let this slide just because you're a transfer student."
        ## Show Eleanor annoyed

        e "If you continue to insist on such unseemly behavior..."
        ## Show Eleanor smile with dissolve
        ##show Sofia frown
        e "I will {i}not{/i} hesitate to put you in your place."
        ## Show Eleanor with dissolve
        e "Mark my words, Carol Mountbatten!"

        ##show Cece sheepish
        c "Um..."
        c "I've been meaning to tell you..."
        c "I actually hate being called 'Carol.'"

        ##show Cece smile
        c "I prefer just 'Cerise.'"
        ## Show Cece vhappy
        c "And my friends all call me Cece."
        ## show Sofia smile

        e "Well,"
        e "{i}Whatever{/i} your name is-"

        ## show Cece sad
        ## show Sofia annoyed

        e "Stay out of my way, and we won't have any problems."
        ##show Eleanor vhappy
        e "Understood?"
        ##hide Eleanor with dissolve

        ##show Cece sad at right with move
        ## show Sofia sigh with dissolve

        s "...Goodness."
        c "Sofiaaaaaa..."

        c "What did I do to make her hate me?"
        c "She's so pretty and talented and cute-"
        ##show Cece cry
        c "BUT SHE HAAAATES MEEEE..."

        s "Oh, Cerise..."
        s "Don't take it personally. Eleanor is like this to pretty much everyone."

        s "Now come on, you need to hurry to your next class."
        ##sadly
        c "Oh- Ohohohoho..."
        c "The buildings are so far apart on this campus..."

        s "I {i}did{/i} warn you about signing up for classes on the northern part of the campus in winter..."
        s "Oh well. It's a mistake every newcomer makes."

        c "It's too bad the river doesn't run past the sciences building..."
        ##show sofia annoyed but smiling

        s "Just leave for class on time!"

        #scene black with dissolve
        #end scene chime


label GirlTalk:
    scene dorm with dissolve
    ### Date indicator: Dec 1st, Night
    ##show sofia and cece's sprites basically on top of each other

    c "Ow ow ow-!"
    c "Sofiaaa, that HURTSS!!"

    s "That's because you didn't take time to stretch {i}before{/i} your little Olympic showcase this morning."

    c "I was gonna be late!"

    s "No buts on this, Cerise."
    s "We're closer to 30 than you think."
    s "You have to take care of yourself now, or you'll regret it later."

    c "Geeeez, don't say that!"
    c "(...Even if it's true.)"

    s "How did you even get this good at skating if your flexibility is {i}this bad?{/i}"

    #sfx whipcrack emph

    c "Hey, I'm SUPER flexible!"
    c "I'm just sore all over."

    s "That's because you didn't stretch."

    c "Thanks, {i}mom.{/i}"

    s "No problem, dear. {image="heart.png"}"

    "Leaning back, Sofia sighed."

    s "That should be good for now."
    s "But don't skip stretching again, got it?"

    c "Yes m'aam."

    #play comfortable, cozy music

    "With a sigh, Cerise climbed into her bed, rolling over the events of the day in her head, while Sofia started to cut out a sewing pattern for the school's drama department."

    c "...Hey Sofia?"

    s "Hmmm?"

    c "Earlier today Eleanor said something about letting my behavior slide because I'm a transfer student..."
    c "What'd she mean by that?"
    c "Are transfers really all that rare here?"

    "Sofia looked up from her work and sighed."


    s "Not as uncommon as it seems, but most of them end up dropping out or transferring to other schools rather quickly."
    s "Beyond the high requirements for acceptance..."
    s "A lot of them just can't adjust to how demanding the school's schedule is."

    s "It's really unusual for transfers to stick around as long as you have, to be honest."

    s "So I think by bringing that up, {p=.5}Eleanor was probably trying to put you in your place."

    c "O-Ohohoho...?"
    c "Y- you mean like,"
    c "{i}'Watch out, freshmeat, you're next'{/i}?"

    "Sofia gave Cerise a doleful smile."

    s "More like,"
    s "{i}'If it weren't for the courtesy I'm expected to extend to someone new, I would have undergone a scorched-earth campaign to make sure you making me look like a fool was the last mistake you ever made at this school.'{/i}"

    c "{i}Ulp...!{/i}"

    s "...Well, that's what I think, at least."

    c "H-has she...done that before...?"

    "Sofia paused mid-cut, and pursed her lips."

    s "...not {i}exactly.{/i}"
    s "She's definitely been involved in a {i}few{/i} cases of people dropping out..."
    s "But most of them cited academic pressures as being the main reason they left."

    c "I can understand why..."
    c "It's a bit of a bizarre setup to for a college to have stuff like homeroom, and requiring students to take a morning class every quarter."
    c "It feels a lot like high school that way."

    c "...Why do we do that, anyway?"


    s "From what I understand, it's because when the school first opened, it was operated by a convent of nuns."
    s "They would have a morning class, then both the students and nuns would gather for morning prayers."
    label .NunHistory:

        ###parallaxing nuns over nuns-bg, pan left to right

        narration "By their exposure to a simple life alongside the Sisters,"
        narration "young women from wealthy families were expected to not only receive a formal education,"

        #dissolve in, zoom+pan slowly down marriage-meeting.png
        narration "but come to possess traits desirable in a wife and heiress."

        #dissolve in, zoom on two seated women in nun-history3, slow pan from lower left to upper right
        narration "Diligence, humility, generosity..."
        narration "And above all, compassion."
        #hide all images, return to dorm

    s "So the structure as we have it now is in honor of that."

    c "Ehhh, really?"
    c "You sure know a whole lot, Sofia."

    s "Ohohoho.{p}It's not all that impressive, really."
    s "It's just some cursory info from some of the school brochures."

    "There was a comfortable silence between the two, the only sound in the dorm being the snip of Sofia's scissors as she worked."

    c "It's pretty crazy to think about, actually."
    c "That a finishing school became one of the top universities in the country..."

    s "It certainly is impressive."
    s "But it's even more impressive that you're adjusting so well, Cece."

    c "Sofia..."

    c "Hehehe."
    c "If it weren't for you, I wouldn't have stood a chance."

    c "Telling me about different teachers..."
    c "Helping me catch up with the foreign language classes..."
    c "Trying to make sure I don't sleep until noon..."

    c "I'm glad you got assigned as my roommate."

    "Rolling over, Cerise reached her hand out to Sofia on the floor, {w=.2}who took it in her own, their fingers interlacing."

    c "{i}Squueeeeeze.{/i}"

    s "Ohohoho.{p}Stop being so cute."

    c "Only if {i}you{/i} stop being so cute."

    s "I asked you first."

    c "Well fine."
    c "I guess we'll both have to keep being cute then."

    s "A burden, for sure."
    s "But I'm sure we can handle it together."

    #at the same time
    s "Ohohoho."
    c "Ohohoho."

    "Sofia, finished cutting her pattern, withdrew her hand and began folding the pieces, carefully placing the tissue-thin paper back into the paper envelope as best as she could."

    "Cerise yawned, rolled onto her side, and pulled the blankets over her head to settle in for the night."

    c "I'm going to bed, okay?"
    s "I'm almost finished here, so I'll get the lights in just a minute."

    c "Good night, Sofia."
    s "Good night, Cece."

    scene black with dissolve
    #sfx scene end chime
    ###Scene end###



    return
