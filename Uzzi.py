import time  # Imports a module to add a pause

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nUse only A, B, or C\n")  # Cutting down on duplication

sword = 0
score = 0

# The story is broken into sections, starting with "intro"
def intro():
    print("\nAfter being the only survivor in your dragon hunt group,"
          "\nyou wake up in a dark forest."
          "\nYou suddenly hear a growl coming from behind you. Its the dragon that slayed your group."
          "\nYou panic and think of options."
          "\nYou will:")
    time.sleep(1)
    print("""  A. Use your sling shot and shoot a stone
  B. Accept your faith and let the dragon eat you
  C. Sprint as fast as you can""")
    choice = input(">>> ")  # Here is your first choice.
    if choice in answer_A:
        option_sling_shot()
        global score
        score = score + 10
    elif choice in answer_B:
        print("\nWell, that was quick. You will be remembered. May your soul rest in peace. "
              "\n\nYou died!")
        print("Your Score =")
        print(score)
    elif choice in answer_C:
        option_run()
    else:
        print(required)
        intro()


def option_sling_shot():
    print("\nThe dragon is stunned, but regains control. He begins "
          "to blow fire but misses. Will you:")
    time.sleep(1)
    print("""  A. Run
  B. Shoot another stone
  C. Run towards a nearby cave""")
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
        global score
        score = score + 10
    elif choice in answer_B:
        print("\nYou decided to shoot another stone, but it has no effect as the"
              "stone shot did no damage. The stone flew well over the "
              "dragons head. You missed. \n\nYou died! ")
        print("Your Score =")
        print(score)
    elif choice in answer_C:
        score = score + 10
        option_cave()
    else:
        print(required)
        option_sling_shot()

def option_cave():
    print("\nYou were hesitant, since the cave was dark and "
          "ominous.\n Before you fully enter, you notice a shiny sword on "
          "the ground.\n Do you pick up a sword. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        sword = 1  # adds a sword
    elif choice in no:
        global score
        score = score + 10
        print("You are defenceless "
              "\nYou Died!")
        print("Your Score =")
        print(score)
        intro()
    else:
        sword = 0
    print("\nWhat do you do next?")
    time.sleep(1)
    print("""  A. Hide in silence
  B. Fight
  C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nReally? You're going to hide in the dark? I think "
              "dragons can see very well in the dark, right? Not sure, but "
              "I'm going with YES, so...the dragon roasted you\n\nYou died!")
        print("Your Score =")
        print(score)
    elif choice in answer_B:
        if sword > 0:
            score
            score = score + 10
            print("\nYou laid in wait. The shimmering sword attracted "
                  "the dragon, which thought you were no match.\n As he walked "
                  "closer and closer, your heart beat rapidly.\n As the dragon "
                  "reached out to grab the sword with its mouth, you pierced the blade into "
                  "its chest. \nYou survived! You slayed a Dragon!")
            option_dragon()

        else:  # If the user didn't grab the sword
            print("\nYou should have picked up that sword. You're "
                  "defenseless. \n\nYou died!")
            print("Your Score =")
            print(score)
    elif choice in answer_C:
        print("As the dragon enters the dark cave, you sliently "
              "sneak out. You're several feet away, but the dragon turns "
              "around and sees you running.")
        option_run()
    elif choice in no:
        print("You are defenceless "
              "\nYou Died!")
        print("Your Score =")
        print(score)
    else:
        print(required)
        option_cave()


def option_run():
    print("\nYou run as quickly as possible, but the dragons "
          "speed is too great."
          "\nYou will:")
    time.sleep(1)
    print("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
    choice = input(">>> ")
    if choice in answer_A:
        print("The dragon smells you and covers the area with fire "
              "\n\nYou died!")
        global score
        print("Your Score =")
        print(score)


    elif choice in answer_B:
        print("\nYou're no match for a dragon. "
              "\n\nYou died!")
        print("Your Score =")
        print(score)
    elif choice in answer_C:
        score = score + 10
        option_town()
    else:
        print(required)
        option_run()

def option_town():
    print("\nWhile frantically running, you decide to hide behind a wall."
          "\nYou decide that you want to kill the dragon."
          "\nYou find a sword next to you."
          "\nYou decide to:")
    time.sleep(1)
    print("""    A. Pick up the sword and fight the dragon 
    B. Charge at the dragon and try to poke its eyes
    C. Run to the dragons wings and try to tear it""")
    choice = input(">>> ")  # Here is your first choice.
    if choice in answer_A:
        global score
        score = score + 10
        print("\nYou slayed the dragon!")
        option_dragon()
    elif choice in answer_B:
        print("\nThe dragon is to quick for you and you run stright into its mouth. "
              "\nYou Died!")
        print("Your Score =")
        print(score)
    elif choice in answer_C:
        print("\nThe dragon lifts its wing and smashes you"
              "\nYou Died!")
        print("Your Score =")
        print(score)
    else:
        print(required)

# The story is broken into sections, starting with "intro"
def option_dragon():
    print("\nYou are filled with confidence and want to finish dragons once and for all."
          "\nYou decide to head to the mountains and kill the mother of all dragons"
          "\nYou will:")
    time.sleep(1)
    print("""  A. Head stright to the mountains to the dragons den
  B. Think its a bad idea and walk away (End game)
  C. Decide to start a new life(End game)""")
    choice = input(">>> ")  # Here is your first choice.
    if choice in answer_A:
        global score
        score = score + 10
        option_mountains()
    elif choice in answer_B:
        print("\nYou scared of fighting another dragon. Shame on you! "
              "\nThe End")
        print("Your Score =")
        print(score)
    elif choice in answer_C:
        print("\nYou found love and lived happily ever after."
              "\nThe End")
        print("Your Score =")
        print(score)
    else:
        print(required)
        option_dragon()

def option_mountains():
    print("\nYou head to the Mountains and find the Beast Resting"
          "\nWill you:")
    time.sleep(1)
    print("""  A. Sneak up to the dragon and stab it in the heart with your sword
  B. Set the cave on fire and run
  C. Charge at the dragon with all your might!""")
    choice = input(">>> ")
    if choice in answer_A:
        global score
        score = score + 10
        option_kill()
    elif choice in answer_B:
        print("\nDragons are not effected by fire."
              "\nThe dragon awakens and traps you in the cave on fire"
              " \nYou died! You burnt to death")
        print("Your Score =")
        print(score)
    elif choice in answer_C:
        print("\nThe dragon awakens by you noise and attacks you"
              "\nYou Died! The dragon ate you")
        print("Your Score =")
        print(score)
    else:
        print(required)
        option_mountains()


def option_kill():
    print("\nYou sneak up close to the dragon but she smells you and wakes up."
          "\nYou will:")
    time.sleep(1)
    print("""  A. Accept death
  B. Try to flee
  C. Stand your ground be brave and fight""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nYou wasted your time. "
              "\nYou died!")
        global score
        print("Your Score =")
        print(score)
    elif choice in answer_B:
        print("\nThe dragon is to big and quick for you so it smashes you with its tail. "
              "\nYou died!")
        print("Your Score =")
        print(score)
    elif choice in answer_C:

        score = score + 10
        option_win()
    else:
        print(required)
        option_kill()


def option_win():
    print("\nYou find a weak spot at the dragons heart area and strike. you slayed the beast!"
          "\nWhats next:")
    time.sleep(1)
    print("""   A. Go back to the town (End game)
   B. Become a dragon slayer for money
   C. Some things are better left unsaid(End game)""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nYou go back to the town and now looked at as a hero."
              "\nAs part of your bravely you are offered all the towns gold.")
        print("Your Score =")
        print(score)
    elif choice in answer_B:
        print("\nYou become a dragon slayer and the king hires you to kill the most fears dragon in the country named "
              "Immortal."
              "\nHe offers you a task that you take and you decide to get supplies.")
        option_king()
    elif choice in answer_C:
        print("You are a legend and your story goes down in history")
        print("Your Score =")
        print(score)
    else:
        print(required)
        option_win()

def option_king():
    print("\nYou find out that the dragon normally fights while its flying! "
          "\nYou head to the local amory store and purchase:")
    time.sleep(1)
    print("""   A. Sword
   B. X-bow
   C. Shield""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nThe dragon attacks from the sky, there's nothing you can do with the Sword!"
              "\nYou end up Dead!")
        global score
        print("Your Score =")
        print(score)
    elif choice in answer_B:
        score = score + 10
        print("Perfect Choice!"
              "You continue to head in the direction of Immortal")
        option_Immortal()
    elif choice in answer_C:
        print("\nThe shield protects you for a bit but Immortal is to strong and crushes you!"
              "\nYou end up dead!")
        print("Your Score =")
        print(score)
    else:
        print(required)
        option_king()


def option_Immortal():
    print("\nYou are well prepared for the battle and you come face to face with Immortal"
          " by a mountain top.\nThe dragon quickly takes to the air and swoops down towards you."
          "\nYou will:")
    time.sleep(1)
    print("""   A. Use your X-Bow and shoot at the dragon
   B. Jump to the left 
   C. Jump to the right""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\n The dragon is to quick for you and grabs you into hes mouth!"
              "\n You Died!")
        global score
        print("Your Score =")
        print(score)
    elif choice in answer_B:
        print("\nYou jumped to the left to the edge of the mountain and the ground crumbles!"
              "\nYou fall down a rocky path."
              "\nThat was unlucky.You Died!")
        print("Your Score =")
        print(score)
    elif choice in answer_C:
        score = score + 10
        print("\nYou Jump to the right and the dragon misses you!"
              "\nYou Survived the attack")
        option_battle()
    else:
        print(required)
        option_Immortal()

def option_battle():
    print("\nYou find an opportunity and take a shot with your X-bow. "
          "\nYou manage to hit the dragon in the back. The dragon is injured! "
          "\nThe dragon takes to the sky and swoops down towards you."
          "\nYou will:")
    time.sleep(1)
    print("""   A. Hide behind a rock
   B. Use your X-bow and shoot at the dragon 
   C. Try to run""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\n The dragon blows fire and covers you in flames!"
              "\n You Died!")
        global score
        print("Your Score =")
        print(score)
    elif choice in answer_B:
        score = score + 10
        print("\nHit! You plant an arrow in the dragons belly!"
              "\nYou countered the attack")
        option_final()
    elif choice in answer_C:
        print("\nThe dragon is to fast at flying and catches you with ease"
              "\nYou Died!")
        print("Your Score =")
        print(score)
    else:
        print(required)
        option_Immortal()

def option_final():
    print("\nThe dragon lands and hes health is critical! "
          "You have run out of arrows! "
          "\nYou will:")
    time.sleep(1)
    print("""   A. Charge at the dragon
   B. Throw your X-bow at the dragon 
   C. Hide""")
    choice = input(">>> ")
    if choice in answer_A:
        global score
        score = score + 10
        print("\nYou run up to the unexpecting dragon and manage to get onto he's back. "
              "You pull out the arrow in he's back"
              "\n You Survived!")
        option_death()
    elif choice in answer_B:
        print("\nThe X-bow hits the dragon but has no effect. The dragon eats you!"
              "\nThat was a cleaver choice. You Died!")
        print("Your Score =")
        print(score)
    elif choice in answer_C:
        print("\nThe dragon smells you and charges at you. You traped and cant escape."
              "\nThe dragon eat's you, You Died!")
        print("Your Score =")
        print(score)
    else:
        print(required)
        option_final()


def option_death():
    print("\nSitting ontop of the dragon with an arrow in your hand. "
          "\nYou decide to:")
    time.sleep(1)
    print("""   A. Reload your X-bow
   B. Climb to the head of the dragon 
   C. Stab the dragon in the back""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nYou try to put the arrow into the X-bow but dropped it."
              "You are defenceless"
              "\n You Died!")
        global score
        print("Your Score =")
        print(score)
    elif choice in answer_B:
        score = score + 10
        print("\nYou quickly get to the dragons head and stab it through the eye!"
              "\nYou Survived!")
        option_story_End()
    elif choice in answer_C:
        print("\nYou Stab the dragon in the back again and it takes flight."
              "\nYou fell off the dragon in mid air, You Died!")
        print("Your Score =")
        print(score)
    else:
        print(required)
        option_death()

def option_story_End():
    print("\nYou slay the dragon and your quest is complete."
          "\nYou are greatly rewarded by the king."
          "\nYou are the Dragon slayer."
          "\nCONGRATULATIONS!!!!!")
    print("Your Score =")
    print(score)
intro()
