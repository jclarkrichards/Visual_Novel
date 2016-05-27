# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg classroom = "classroom01.png"

image yuichi neutral ="yuichi_neutral.png"
image yuichi angry 1 ="yuichi_angry01.png"
image yuichi angry 2 ="yuichi_angry02.png"
image yuichi sad ="yuichi_sad.png"

image aryan neutral ="aryan_neutral.png"
image aryan angry 1 ="aryan_angry01.png"
image aryan happy ="aryan_happy.png"
image aryan sad ="aryan_sad.png"

image miguel neutral ="miguel_neutral.png"
image miguel angry="miguel_angry.png"
image miguel sad ="miguel_sad.png"

image zeke neutral ="zeke_neutral.png"
image zeke angry ="zeke_angry03.png"
image zeke sad ="zeke_sad02.png"

# Declare characters used by this game.
define y = Character('Yuichi', color="#c8ffc8")
define a = Character('Aryan', color="#c8ffc8") #,show_side_image=Image("aryan_neutral.png"), zoom = 0.25, xalign=0.0, yalign=1.0)
define m = Character('Miguel', color="#c8ffc8")
define z = Character('Zeke', color="#c8ffc8")
define mc = Character('Me', color="#c8ffc8")
define n = Character(None, color="#c8ffc8")
define i = Character('Instructor', color="#c8ffc8")
define score = Character(None, color="#c8ffc8", kind=nvl)

# The game starts here.
label start:
    $yuichi_affection=0
    $aryan_affection=0
    $miguel_affection=0
    $zeke_affection=0
    $grade=0
    $concept=0
    
    jump week01
    
label week01:

    scene bg classroom
    with fade
    n "I signed for up a ten-week intensive physics course."
    n "I didn\'t really think too much about it at the time.\n I just thought it would be fun."
    n "But once I got to the classroom and sat down, I started to feel nervous."
    n "Like maybe I had made a mistake."
    n "I smiled at the boy sitting next to me."
    show aryan neutral with dissolve:
        zoom 2
        xpos -75 ypos 50
    
    a "Hi, I'm Aryan.  Are you in this class?"
    n "I shrugged."
    menu:
        "I guess so.":
            $aryan_affection +=0
        "I am here aren\'t I?":
            $aryan_affection+=1
            a "Haha."
            a "Guess that was a stupid question."
            
    
    hide aryan
    show aryan neutral:
        zoom 2
        xpos -200 ypos 50
    show zeke neutral:
        zoom 2
        xpos 100 ypos 50
    with dissolve
    n "The boy on my other side leaned over to talk to us."
    z "This is Intro to Physics intensive."
    menu:
        "Yeah, that\'s what I signed up for.":
            $zeke_affection-=1
        "*Laugh*":
            $zeke_affection+=1
        
    z "Ha, I was just joking."
    z "I\'m Zeke. \n Just let me know if you need any help."
    hide aryan
    hide zeke
    show aryan neutral:
        zoom 2
        xpos -250 ypos 50
    show zeke neutral:
        zoom 2
        xpos 0 ypos 50
    show yuichi neutral with dissolve:
        zoom 2
        xpos 225 ypos 50
    n "The boy sitting behind Zeke spoke up."
    y "Do you guys feel good about this class?"
    z "I took AP Physics at my old school."
    menu:
        ". . .":
            $zeke_affection+=0
        "Your old school?":
            z "Yeah, it was for gifted students."
            menu:
                "That\'s impressive!":
                    $zeke_affection+=1
                    $miguel_affection-=1
                "Oh...":
                    $zeke_affection +=0
        
        
    a "So did I, but my teacher wasn\'t a physics-person."
    a "But it should be OK."
    y "Did you take AP Physics?"
    menu:
        "Yeah, I did.":
            $yuichi_affection +=1
        "No... that\'s why I signed up for the intro class...":
            $aryan_affection+=1
            $miguel_affection+=1
    n "The boy behind me joined in the conversation."
    hide aryan
    hide zeke
    hide yuichi
    show aryan neutral with dissolve:
        zoom 1.75
        xpos -300 ypos 50
    show zeke neutral with dissolve:
        zoom 1.75
        xpos -75 ypos 50
    show yuichi neutral with dissolve:
        zoom 1.75
        xpos 170 ypos 50
    show miguel neutral with dissolve:
        zoom 1.75
        xpos 355 ypos 50
    m "I didn\'t take any AP courses."
    m "I think you\'ll be fine either way.  \n As long as you study."
    menu:
        "I don\'t know ... \n physics is so hard...":
            $miguel_affection-=1
        "*smile*":
            $miguel_affection+=1
    hide aryan
    hide zeke
    hide yuichi
    hide miguel
    
    i "OK, everyone time to start class."
    menu: 
        "*Pay attention to lecture.*":
            jump week01_lecture
        "*Daydream about boys.*":
            jump week01_concept
    
label week01_lecture:
    i "Welcome to Introduction to Physics.  \n This course is designed to be you\'re very first introduction to physics."
    i "The only prerequisite is algebra."
    i "Let\'s get started with the \"Force\""
    n "The teacher wrote on the whiteboard."
    show physics_whiteboard_01_02:
        zoom 0.5
        xpos 59 ypos 60
    pause
    menu:
        "*Laugh*":
            $aryan_affection+=1
        "*Roll your eyes*":
            $aryan_affection-=1
    hide physics_whiteboard_01_02
    i "Isaac Newton formulated  3 Laws of Motion. \n We are going to focus on the first law and second law today."
    i "The first law is that an object at rest will stay at rest and an object in motion will stay in motion..."
    i "...unless acted upon by an outside force."
    show week01_lecture01_01:
        zoom 0.5
        xpos 59 ypos 60
    i "The square will stay at rest unless a \"force\" acts upon it."
    i "That force will cause the square to now be in motion."
    hide week01_lecture01_01
    show week01_lecture01_02:
        zoom 0.5
        xpos 59 ypos 60
    i "Motion simply means that an object is moving."
    i "That means that the object\'s position is changing with time.\n We call the change in position divided by the change in time \"velocity\""
    i "I will write velocity as a \"v\", and consider the position to be represented by \"x\", and time to be represented as \"t\".  So my velocity is defined as v = \"Delta\" x divided by \"Delta\" t."
    hide week01_lecture01_02
    show week01_lecture01_03:
        zoom 0.5
        xpos 59 ypos 60
    i "\"Delta\" is a shorthand way of saying \"change in\".  \n I could also write the final position minus the initial position.  But that\'s just too long and I\'m just too lazy."
    i "And speaking of lazy... \n I see of a lot of vacant faces out there.\n so how\'s about a question."
    hide week01_lecture01_03
    show week01_lecture01_04:
        zoom 0.5
        xpos 59 ypos 60
    i "If an object is at rest... What does \"Delta\" x equal....?"
    n "Zeke raised his hand immediately."
    n "Everyone else seems to be thinking about it. \n He must be really confident and know the answer."
    menu:
        "*I don\'t know the answer.":
            i "Yes... Um..."
            show zeke neutral with dissolve:
                zoom 2
                xpos -75 ypos 50
            z "Zeke.\n Delta x equals 0."
            i "Yes, good job."
            hide zeke 
            jump concept_a_explain
        "*I think I know the answer.*":
            menu:
                "*Let Zeke answer.*":
                    i "Yes... Um..."
                    show zeke neutral with dissolve:
                        zoom 2
                        xpos -75 ypos 50
                    z "Zeke.\n Delta x equals 0."
                    i "Very good.  Delta x is zero because the object is not moving.  \n So the final position would equal the initial position."
                    hide zeke 
                    jump continue_lecture01
                "*Raise your hand*":
                    $zeke_affection-=1
                    n "The instructor looked straight at me, ignoring Zeke."
                    i "Yes..? What does Delta x equal if the object is at rest?"
                    menu:
                        "Delta x = 37":
                            i "No...\n Actually ..."
                            jump concept_a_explain
                        "Delta x = Delta t":
                            i "No...\n Actually ..."
                            jump concept_a_explain
                        "Delta x = 0":
                            $concept+=1
                            $yuichi_affection+=1
                            i "Very good.  Delta x is zero because the object is not moving.  \n So the final position would equal the initial position."
                            jump continue_lecture01
                        "Delta x = Your Mom":
                            $aryan_affection+=1
                            i "No...\n Actually ..."
                            jump concept_a_explain
                
label concept_a_explain:
    i "Delta x would be zero in this case."
    hide week01_lecture01_04
    show week01_lecture01_03:
        zoom 0.5
        xpos 59 ypos 60
    i "If the object is at rest, then the final position is the same as the initial position.  Meaning that since Delta x is the final position minus the initial posion, we would end up subtracted the same value from itself."
    i "And we would get zero."
    jump continue_lecture01
label continue_lecture01:
    hide week01_lecture01_04
    hide week01_lecture01_03
    show week01_lecture01_05:
        zoom 0.36
        xpos 59 ypos 60
    i "Let\'s talk briefly about units."
    i "x is position, and that has units of meters, kilometers, millimeters, etc.  That is a distance. \n it measures how far away something is."
    i "t is time, which has units of seconds, minutes, hours, years, etc.  This measures how long something takes."
    i "And v is velocity, which is change in position divided by change in time.  So the units are the units of position divided by the units of time.\n This is usually meters divided by seconds, but could be kilometers divided by hours, etc."
    i "And what if the velocity changes over time?"
    i "That is called \"acceleration\", which is the change in velocity divided by the change in time. \n Or acceleration \"a\" equals Delta v divided by Delta t."
    i "This means that accerlation has the units of velocity divided by time.  \n Typically, this is meters divided by seconds-squared."
    hide week01_lecture01_05
    show week01_lecture01_06:
        zoom 0.36
        xpos 59 ypos 60
    i "You probably are wondering what all of this has to do with force?"
    i "Well that brings us to Newton's second law.\n Newton defined \"force\" and something applied to an object to make it move."
    i "An \"object\" is anything with mass. \n Mass is measured in grams, kilograms, tons, etc.  But usually kilograms."

    i "The more mass an object has, the more force you need to make it move."
    i "If a small force is needed to move an object, then the mass is small too."
    i "If a large force is needed to move an object, then the mass is large.\n Or the mass is \"massive\"."
    n "Aryan laughed loudly at the instructor\'s terrible pun."
    menu:
        "*Laugh as well*":
            $aryan_affection+=1
        "*Roll your eyes*":
            $aryan_affection-=1
        "*Ignore the pun AND the idiot laughing at it*":
            pass
    hide week01_lecture01_06
    show week01_lecture01:
        zoom 0.5
        xpos 59 ypos 60
    i "Since making an object move means changing it\'s velocity from zero to something that is not zero, then applying a force to an object means that a mass, or \"m\", has an acceraltion."
    i "This is Newton\'s second law:\n Force equals a mass times the acceleration."
    jump week01_concept
label week01_concept:
    hide week01_lecture01
    show week01_lecture01_07:
        zoom 0.36
        xpos 59 ypos 60
    i "You guys looks really bored.  I think you need a question."
    i "Force equals mass times acceleration.  We call the units of force \"Newtons\", what is a \"Newton\" in fundamental units?"
    n "Miguel raised his hand tentatively."
    menu:
        "*You know the answer*":
            menu:
                "*Let Miguel answer.*":
                    i "OK... boy in the white tank top..."
                    show miguel sad with dissolve:
                        zoom 2
                        xpos -75 ypos 50
                    m "Um...."
                    m "..."
                    i "That\'s fine."
                    hide miguel
                    jump week01_concept_explanation
                "*Raise your hand.*":
                    n "The instructor looked straight at me. Why?  It\'s like I stick out or something..."
                    i "Yes... You can tell what a Newton is in fundamental units?"
                    menu:
                        "Kilograms":
                            i "Um... not quite."
                            jump week01_concept_explanation
                        "Seconds-squared divided by kilograms times meters":
                            i "Close, but not quite."
                            jump week01_concept_explanation
                        "Your Mom":
                            $aryan_affection+=1
                            i "Um... no."
                            jump week01_concept_explanation
                        "Kilograms times meters divided seconds-squared.":
                            $concept+=1
                            $zeke_affection-=1
                            i "Good job.\n Glad someone was paying attention."
                            jump week01_end_of_class
                        "A cookie":
                            $aryan_affection+=1
                            n "The instructor does not look amused."
                            i "Haha, never heard that one before."
                            jump week01_concept_explanation
        "*You don\'t know the answer.*":
            menu:
                n "If I could back in time to the beginning of the lecture, would I?"
                "Yes.":
                    hide week01_lecture01_07
                    jump week01_lecture
                "No.":
                    pass
            i "OK... boy in the white tank top..."
            show miguel sad with dissolve:
                zoom 2
                xpos -75 ypos 50
            m "Um...."
            m "..."
            i "That\'s fine."
            hide miguel
            jump week01_concept_explanation
label week01_concept_explanation:
    hide week01_lecture01_07
    show week01_lecture01:
        zoom 0.5
        xpos 59 ypos 60
    i "So the force equals the mass times the accerleration.  So it has the units of mass, kilograms, times the units of accerleration, meters divided by seconds-squared."
    hide week01_lecture01
    jump week01_end_of_class
label week01_end_of_class:
    hide week01_lecture01_07
    i "OK, that does it for today."
    show week01_hw01:
        zoom 0.36
        xpos 59 ypos 60
    i "Here is your homework assignment."
    i "Because of magic, you will know instantly if your answer is correct or not.\n Your homework scores will instantly be added to your grade."
    i "Guess, I should\'ve mentioned this first, but be carefull of your grade.  \n If your grade drops below 0.25\%, you\'ll have to leave the classe."
    i "You are allowed to work together on the hoemworks. \n This can not only help your grade, but it also might help you make friends."
    n "It seemed like the teacher gave me pointed look."
    n "I looked around, but it didn\'t seem like anyone else noticed."
    i "I\'ll see you later."
    n "The instrcutor left the room.  All the other students filed out slowly except for the boys I talked to before class started."
    #show aryan neutral with dissolve:
    #    zoom 1.75
    #    xpos -300 ypos 50
    show zeke neutral with dissolve:
        zoom 2
        xpos -75 ypos 50
    #show yuichi neutral with dissolve:
    #    zoom 1.75
    #    xpos 170 ypos 50
    #show miguel neutral with dissolve:
    #    zoom 1.75
    #    xpos 355 ypos 50
    z "*Yawn*  That was so boring.\n I just daydreamed the whole time."
    menu:
        "Same.  I knew all that stuff.":
            $yuichi_affection+=1
        "I paid attention the whole time":
            $miguel_affection+=1
    show yuichi neutral with dissolve:
        zoom 2
        xpos 170 ypos 50
    y "Yeah, I zoned out too.  I already knew all that stuff."
    z "Do you need help with the homework?"
    menu:
        "Definitely, I didn't get that all.":
            $zeke_affection+=1
        "I think I got it, but I could use a little help.":
            jump week01_hw_z_explanation
        "No, I got it.  Thanks.":
            jump week01_hw
    jump week01_hw
label week01_hw:
    hide aryan
    hide zeke
    hide miguel
    hide yuichi
    show week01_hw01:
        zoom 0.36
        xpos 59 ypos 60
    "A stationary block with with mass, m, is pushed with force, F= 10 N, on a frictionless surface.  The final velocity of the block is v = 2 m//s after time, t = 5 s, of pushing."
    pause
    menu:
        "A stationary block with with mass, m, is pushed with force, F= 10 N, on a frictionless surface.  The final velocity of the block is v = 2 m//s after time, t = 5 s, of pushing."
        "a":
            jump week01_end
        "b":
            $grade+=1
            jump week01_end
        "c":
            jump week01_end
        "d":
            jump week01_end
        "*Hm... maybe I should ask someone for help.*":
            jump week01_help
        "*I got this, but maybe someone needs help":
            jump week01_help
        "*I need a closer look at the board.*":
            jump week01_hw
label week01_help:
    show aryan sad with dissolve:
        zoom 1.75
        xpos -300 ypos 50
    show zeke neutral with dissolve:
        zoom 1.75
        xpos -75 ypos 50
    show yuichi neutral with dissolve:
        zoom 1.75
        xpos 170 ypos 50
    show miguel sad with dissolve:
        zoom 1.75
        xpos 355 ypos 50

    menu:
        n "But who should I ask?"
        "Aryan":
            a "Um... I\'m not sure I get this, could you explain it to me?"
            menu:
                "Sure, no problem.":
                    $aryan_affection+1
                    jump week_01_hw_me_explain
                "Um... no, I thought you could explain it to me.":
                    a "That\'s fine."
                    mc "Sorry."
                    jump week01_help
                    
        "Zeke":
            z "Haha, changed your mind, huh?"
            $zeke_affection+=1
            jump week01_hw_z_explanation
        "Yuichi":
            y "Sure, we can do the homework together."
            $yuichi_affection+=1
            jump week01_hw_y_explanation
        "Miguel":
            $miguel_affection+=1
            m "Hey, you seem like you unddertand this, could you help me out?"
            menu:
                "Sure, no problem.":
                    jump week_01_hw_me_explain
                "Um... no, I thought you could explain it to me.":
                    m "That\'s fine."
                    mc "Sorry."
                    jump week01_help
    

label week01_hw_z_explanation:
    hide zeke
    hide yuichi
    hide aryan
    hide miguel
    hide week01_hw01
    show week01_hw01_z:
        zoom 0.36
        xpos 59 ypos 60
    z "You have to look for what they give you in the problem.  We know the force, but we don\'t know the mass or the acceleration."
    z "But since they gave us the final veloctiy and the block was at rest to start with, we can figure out Delta v.  The final velocity is 2 meters per second minus 0 meters per second, so 2 meters per second."
    z "Since acceleration is Delta v divided by Delta t, we should also have Delta t.  And we do, it is 5 seconds."
    z "So we put that all together, and we get the answer."
    show zeke neutral with dissolve:
        zoom 2
        xpos 0 ypos 50
    menu:
        z "Do you get it?"
        "Yeah, that made a lot of sense, thanks.":
            hide week01_hw01_z
            jump week01_hw
        "Um... I still don\'t get it, but thanks for the answer.":
            $zeke_affection+=1
            hide week01_hw01_z
            jump week01_hw
        "Not quite...":
            jump week01_hw_z_explanation
            
label week01_hw_y_explanation:
    hide zeke
    hide yuichi
    hide aryan
    hide miguel
    hide week01_hw01
    show week01_hw01_y:
        zoom 0.36
        xpos 59 ypos 60
    y "Um... Well, we know that force is mass times acceleration.  So we just do that."
    y "So... we have a force of 10 Netwons, and um... 2 meters per second.  So, I guess we just divide those like that."
    show yuichi sad with dissolve:
        zoom 2
        xpos 0 ypos 50
    menu:
        y "Do you get it?"
        "Yeah, that made a lot of sense, thanks.":
            hide week01_hw01_y
            jump week01_hw
        "Um... I still don\'t get it, but thanks for the answer.":
            $zeke_affection+=1
            hide week01_hw01_y
            jump week01_hw
        "Not quite...":
            jump week01_hw_y_explanation
    
    
label week_01_hw_me_explain:
    hide zeke
    hide yuichi
    hide aryan
    hide miguel
    hide week01_hw01
    show week01_hw01_me:
        zoom 0.36
        xpos 59 ypos 60
    mc "First we know that Force is mass times acceleration.  We were given force, but not acceleration, and we are told to find mass."
    mc "But from the lesson, we know that acceleration is the final velocity minus the initial velocty all divided by the amount of time.  We can put that into the equation replacing acceleration, and know we know everything except for the mass." 

    jump week01_hw
label week01_end:
    
    show aryan neutral with dissolve:
        zoom 1.75
        xpos -300 ypos 50
    show zeke neutral with dissolve:
        zoom 1.75
        xpos -75 ypos 50
    show yuichi neutral with dissolve:
        zoom 1.75
        xpos 170 ypos 50
    show miguel neutral with dissolve:
        zoom 1.75
        xpos 355 ypos 50
    
    n "After class, I wondered what I should do?"
    menu:
        "*Talk to Aryan.*":
            hide aryan
            hide zeke
            hide miguel
            hide yuichi
            show aryan neutral with dissolve:
                zoom 2
                xpos 0 ypos 50
            if aryan_affection>=5:
                a "You\'re really funny."
                a "I think this is going to ne be a fun class"
                menu:
                    "Aryan looks like he wants to hang out."
                    "*Spend time with Aryan after class.*":
                        $aryan_affection+=2
                        n "I spent some time getting to know Aryan after class."
                        n "He isn\'t a really serious student, or a serious person at all.  But he seems to enjoy the class so far."
                        jump week01_score
                    "*Pretend to not notice.*":
                        hide aryan
                        jump week01_end
                        
            a "This is a fun class, huh?"
            hide aryan
            jump week01_end
            
        "*Talk to Zeke.*":
            hide aryan
            hide zeke
            hide miguel
            hide yuichi
            show zeke neutral with dissolve:
                zoom 2
                xpos 0 ypos 50
            if zeke_affection>=5:
                menu:
                    "Zeke looks like he wants to talk to me."
                    "*Spend time with Zeke after class.*":
                        $zeke_affection+=2
                        n "I spent some time with Zeke after class."
                        n "We talked about his former school.  He seems a little sad that he left."
                        n "He doesn\'t seem to want to talk about other things, even if the subject makes him sad."
                        jump week01_score
                    "*Ignore him.*":
                        hide zeke
                        jump week01_end
            m "This class seems a little easy.  I\'m glad I won\'t have to work too hard."
            hide zeke
            jump week01_end
                    
        "*Talk to Yuichi.*":
            hide aryan
            hide zeke
            hide miguel
            hide yuichi
            show yuichi neutral with dissolve:
                zoom 2
                xpos 0 ypos 50
            if yuichi_affection>=5:
                menu:
                    "Yuichi looks like he wants to hang out."
                    "*Spend time with Yuichi after class.*":
                        $yuichi_affection+=2
                        n "I spent some time with Yuichi after class."
                        n "We talked a lot about school.  Yuichi\'s parents are really strict.  His mom keeps his WiiU locked in a case and only unlocks after he studies for at least 3 hours."
                        jump week01_score
                    "*Ignore him.*":
                        hide yuichi
                        jump week01_end
            m "I think I know all this stuff... But I\'m going to study when I get home."
            hide yuichi
            jump week01_end
            
        "*Talk to Miguel.*":
            hide aryan
            hide zeke
            hide miguel
            hide yuichi
            show miguel neutral with dissolve:
                zoom 2
                xpos 0 ypos 50
            $miguel_affection+=1
            if miguel_affection>=5:
                menu:
                    "Miguel looks like he wants to talk to me."
                    "*Spend time with Miguel after class.*":
                        $miguel_affection+=2
                        n "I spent some time with Miguel after class."
                        n "We talked a lot about physics, but he had to leave to go to work."
                        jump week01_score
                    "*Ignore him.*":
                        hide miguel
                        jump week01_end
            m "What do you think of the class?\n It seems a little hard to me, but I can just study more."
            hide miguel
            jump week01_end
                    
                                        
                    
        "*I should really just go straight home and study.*\n*Or maybe just watch TV.*":
          jump week01_score
          
label week01_score:
    $aryan_score=float(aryan_affection)
    $miguel_score=float(miguel_affection)
    $yuichi_score=float(yuichi_affection)
    $zeke_score=float(zeke_affection)
    $concept_score=float(concept)
    $grade_score=float(grade)/1 *100
    hide zeke
    hide miguel
    hide yuichi
    hide aryan
    scene bg blank
    n "I wonder how I\'m doing in class so far."
    n "I checked the online grades."
    "You have a %(grade_score).2f \% "
    if grade_score<=0.25:
        n "I really need to try harder."
        n "Maybe I can ask for help too."
    
    n "I wonder what the other students think of me?"
    " Aryan = %(aryan_score)0.2f \n Zeke = %(zeke_score)0.2f \n Yuichi = %(yuichi_score)0.2f \n Miguel = %(miguel_score)0.2f \n " 
    n "That\'s really weird.  I wonder what those numbers mean?"
    n "I decided to go to bed, since I was clearly so tired I had started to hallucinate."
    $aryan_grade=1
    $zeke_grade=1
    $yuichi_grade=0
    $miguel_grade=0
    $aryan_concept=0
    $zeke_concept=1
    $yuichi_concept=0
    $miguel_concept=0
    
    
    jump week02
#---------------------------------------------------------------------------------------------


    

    return
