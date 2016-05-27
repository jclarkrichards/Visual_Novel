
label week02:
    scene bg classroom 
    with fade
    
    
    scene bg classroom
    with fade
    n ""
    show aryan neutral with dissolve:
        zoom 2
        xpos -75 ypos 50
    
    a ""
    n ""
    menu:
        "":
            $aryan_affection +=0
        "":
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
            jump week02_lecture
        "*Daydream about Unicorns.*":
            n "A pink, fluffy unicorn runs in a field at velocity v, it then applies a force, F, to throw a fairy into the air..."
            jump week02_concept
    
label week02_lecture:
    i "Let\'s get started with the lecture then."
    n "The teacher wrote on the whiteboard."
    i "Today, we\'re going to go over kinematics.  This is a special case of motion with a constant acceleration"
    i "A constant acceleration means that the acceleration doesn\'t change as time goes on.  We could draw a graph of acceleration on the y or vertical axis, and time on the x or horizontal axis.  In other words, we can draw acceleration \"as a function of time\"."
    i "Sometimes this can written in an equation as a(t)=(Delta v)\/(Delta t).  This doesn\'t mean a times t, but instead means that a is a function of t."
    i "When we draw acceleration as a function of time, we get a straight horizontal line if the acceleration is constant.  For any value of time, t, the acceleration as the same value."
    show week01_lecture01_02:
        zoom 0.36
        xpos 59 ypos 60
    i "We can also draw velocity as a function of time.  If the acceleration is constant, then the velocity will be a straight line.  The slope of that line is the magnitude of the acceleration."
    i "We can see that by drawing a right-triangle.  The line representing the velocity as a function of time will be the hypotenuse.  The change in velocity is the height, and the change in time is the wdith.  The slope of the hypotenuse is the change in velocity divided by the change in time, or the acceleration."
    i "We can compare this graph of the velocity as a function of time to equation for a straight line of y as a function of x; y(x)=mx+b.  Where y(x) is the value of y at a particular value of x, m is the slope of the line, and b is the value of y when x=0.  Or where the line crosses the vertical axis."
    hide week02_lecture01_02
    show week02_lecture01_03:
        zoom 0.36
        xpos 59 ypos 60
    i "We can then translate this velcity.  Writing our velocity as a line equation.  Velocity, v, at some time t, is equal to the slope, the acceleration, times time t, plus the velocity at time equal to zero.  "
    hide week02_lecture01_03
    show week02_lecture01_04:
        zoom 0.36
        xpos 59 ypos 60
    i ""
    hide week02_lecture01_04
    show week02_lecture01_05:
        zoom 0.36
        xpos 59 ypos 60
    i ""
    n "Yuichi raised his hand immediately."
    n "He seemed pretty confident for a guy who had messed up the homework assignment."
    menu:
        "*I don\'t know the answer.":
            i "Yes... You with the anime hair."
            show yuichi neutral with dissolve:
                zoom 2
                xpos -75 ypos 50
            y ""
            i "Yes, good job."
            yuichi_concept+=1
            hide yuichi
            jump week02_concept_a_explain
        "*I think I know the answer.*":
            menu:
                "*Let Yuichi answer.*":
                    i "Yes... You with the anime hair."
                    show yuichi neutral with dissolve:
                        zoom 2
                        xpos -75 ypos 50
                    z ""
                    i "Very good."
                    $yuichi_concept+=1
                    hide yuichi
                    jump week02_continue_lecture01
                "*Raise your hand*":
                    if concept>=zeke_concept:
                        $zeke_affection-=1
                    n "The instructor looked past Yuichi to me."
                    i "Yes..?"
                    menu:
                        "":
                            i "No...\n Actually ..."
                            jump week02_concept_a_explain
                        "":
                            i "No...\n Actually ..."
                            jump week02_concept_a_explain
                        "":
                            $concept+=1
                            $yuichi_affection+=1
                            i "Very good."
                            jump week02_continue_lecture01
                        "Your Mom":
                            $aryan_affection+=1
                            i "No...\n Actually ..."
                            jump week02_concept_a_explain
                
label week02_concept_a_explain:
    i ""
    hide week01_lecture01_04
    show week01_lecture01_03:
        zoom 0.5
        xpos 59 ypos 60
    i ""
    jump week02_continue_lecture01
label week02_continue_lecture01:
    hide week01_lecture01_04
    hide week01_lecture01_03
    show week01_lecture01_05:
        zoom 0.36
        xpos 59 ypos 60
    i ""
    hide week01_lecture01_05
    show week01_lecture01_06:
        zoom 0.36
        xpos 59 ypos 60
    i ""

    i ""
    n ""
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
    i ""
    jump week02_concept
label week02_concept:
    hide week01_lecture01
    show week01_lecture01_07:
        zoom 0.36
        xpos 59 ypos 60
    i ""
    menu:
        "*You know the answer*":
            menu:
                "*Let Aryan answer.*":
                    i "OK... boy with the hair in the white shirt."
                    show aryan sad with dissolve:
                        zoom 2
                        xpos -75 ypos 50
                    a "Um...."
                    
                    i "Yes. That\'s close enough."
                    show aryan neutral with dissolve:
                        zoom 2
                        xpos -75 ypos 50
                    a "Nailed it!"
                    hide aryan
                    jump week01_concept_explanation
                "*Raise your hand.*":
                    n "The instructor looked straight at me. Why?  It\'s like I stick out or something..."
                    i "Yes... Y"
                    menu:
                        "":
                            i "Um... not quite."
                            jump week01_concept_explanation
                        "":
                            i "Close, but not quite."
                            jump week01_concept_explanation
                        "":
                            $aryan_affection+=1
                            i "Um... no."
                            jump week01_concept_explanation
                        "":
                            $concept+=1
                            $zeke_affection-=1
                            i "Good job.\n Glad someone was paying attention."
                            jump week01_end_of_class
                        "":
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
            i "OK... boy with the hair in the white shirt."
                    show aryan sad with dissolve:
                        zoom 2
                        xpos -75 ypos 50
                    a "Um...."
                    
                    i "Yes. That\'s close enough."
                    show aryan neutral with dissolve:
                        zoom 2
                        xpos -75 ypos 50
                    a "Nailed it!"
                    hide aryan
                    
            jump week01_concept_explanation
label week02_concept_explanation:
    hide week01_lecture01_07
    show week01_lecture01:
        zoom 0.5
        xpos 59 ypos 60
    i ""
    hide week01_lecture01
    jump week01_end_of_class
label week02_end_of_class:
    hide week01_lecture01_07
    i "OK, that does it for today."
    show week02_hw01:
        zoom 0.36
        xpos 59 ypos 60
    i "Here is your homework assignment."
    i ""
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
            jump week02_hw_z_explain
        "No, I got it.  Thanks.":
            jump week02_hw
    jump week02_hw
label week02_hw:
    hide aryan
    hide zeke
    hide miguel
    hide yuichi
    show week02_hw01:
        zoom 0.36
        xpos 59 ypos 60
    "A stationary block with with mass, m, is pushed with force, F= 10 N, on a frictionless surface.  The final velocity of the block is v = 2 m//s after time, t = 5 s, of pushing."
    pause
    menu:
        "A stationary block with with mass, m, is pushed with force, F= 10 N, on a frictionless surface.  The final velocity of the block is v = 2 m//s after time, t = 5 s, of pushing."
        "a":
            jump week02_end
        "b":
            $grade+=1
            jump week02_end
        "c":
            jump week02_end
        "d":
            jump week02_end
        "*Hm... maybe I should ask someone for help.*":
            jump week02_help
        "*I got this, but maybe someone needs help":
            jump week02_help
        "*I need a closer look at the board.*":
            jump week02_hw
label week02_help:
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
                    jump week_02_hw_me_explain
                "Um... no, I thought you could explain it to me.":
                    a "That\'s fine."
                    mc "Sorry."
                    jump week02_help
                    
        "Zeke":
            z "Haha, changed your mind, huh?"
            $zeke_affection+=1
            jump week02_hw_z_explanation
        "Yuichi":
            y "Sure, we can do the homework together."
            $yuichi_affection+=1
            jump week02_hw_y_explanation
        "Miguel":
            $miguel_affection+=1
            m "Hey, you seem like you unddertand this, could you help me out?"
            menu:
                "Sure, no problem.":
                    jump week_02_hw_me_explain
                "Um... no, I thought you could explain it to me.":
                    m "That\'s fine."
                    mc "Sorry."
                    jump week02_help
    

label week02_hw_z_explanation:
    hide zeke
    hide yuichi
    hide aryan
    hide miguel
    hide week02_hw01
    show week02_hw01_z:
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
            hide week02_hw01_z
            jump week02_hw
        "Um... I still don\'t get it, but thanks for the answer.":
            $zeke_affection+=1
            hide week02_hw01_z
            jump week02_hw
        "Not quite...":
            jump week02_hw_z_explanation
            
label week02_hw_y_explanation:
    hide zeke
    hide yuichi
    hide aryan
    hide miguel
    hide week01_hw02
    show week01_hw02_y:
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
            hide week02_hw02_y
            jump week02_hw
        "Um... I still don\'t get it, but thanks for the answer.":
            $zeke_affection+=1
            hide week02_hw01_y
            jump week02_hw
        "Not quite...":
            jump week02_hw_y_explanation
    
    
label week_02_hw_me_explain:
    hide zeke
    hide yuichi
    hide aryan
    hide miguel
    hide week01_hw02
    show week01_hw02_me:
        zoom 0.36
        xpos 59 ypos 60
    mc "First we know that Force is mass times acceleration.  We were given force, but not acceleration, and we are told to find mass."
    mc "But from the lesson, we know that acceleration is the final velocity minus the initial velocty all divided by the amount of time.  We can put that into the equation replacing acceleration, and know we know everything except for the mass." 

    jump week02_hw
label week02_end:
    
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
                        jump week02_score
                    "*Pretend to not notice.*":
                        hide aryan
                        jump week02_end
                        
            a "This is a fun class, huh?"
            hide aryan
            jump week02_end
            
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
                        jump week02_score
                    "*Ignore him.*":
                        hide zeke
                        jump week02_end
            m "This class seems a little easy.  I\'m glad I won\'t have to work too hard."
            hide zeke
            jump week02_end
                    
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
                        jump week02_score
                    "*Ignore him.*":
                        hide yuichi
                        jump week02_end
            m "I think I know all this stuff... But I\'m going to study when I get home."
            hide yuichi
            jump week02_end
            
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
                        jump week02_score
                    "*Ignore him.*":
                        hide miguel
                        jump week02_end
            m "What do you think of the class?\n It seems a little hard to me, but I can just study more."
            hide miguel
            jump week02_end
                    
                                        
                    
        "*I should really just go straight home and study.*\n*Or maybe just watch TV.*":
          jump week02_score
          
label week02_score:
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