from CLI_Full import CLI
import time

banner = r"""
  ______                           _        ____                              
 |  ____|                         | |      |  _ \                             
 | |__  __  ____ _ _ __ ___  _ __ | | ___  | |_) | __ _ _ __  _ __   ___ _ __ 
 |  __| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \ |  _ < / _` | '_ \| '_ \ / _ \ '__|
 | |____ >  < (_| | | | | | | |_) | |  __/ | |_) | (_| | | | | | | |  __/ |   
 |______/_/\_\__,_|_| |_| |_| .__/|_|\___| |____/ \__,_|_| |_|_| |_|\___|_|   
                            | |                                               
                            |_|                                               
"""

# Print the Banner
# Das Banner in der Konsole zeigen

CLI.prepare_banner(banner)

# Write something
# Etwas Schreiben

CLI.write("This is a Example Text!")

time.sleep(3)

# You can change the Color and Duration dont know what that means? Just look!
# Du kannst sogar die Farbe und Dauer ändern. Was das heißt? Guck einfach!

CLI.write("This is a Colorfull Text!", rgb=(250,120,0),duration=2)

# And the user Input is even more Important (Not really but eh)
# Natürlich darf der User Input nicht fehlen!

text = CLI.get_input()
CLI.write(text=text)

time.sleep(3)

# But thats not it! Look you can Customize the Prompt and Color
# Aber das war es noch lange nicht du kannst die Farbe und den Prompt ändern!

text = CLI.get_input(prompt="Make a decision: ", rgb=(51,26,0))
CLI.write(text=text)

time.sleep(3)

# Do you know that? You want the user to really see a text? Well here is the Solution
# Kennst du das? Du wolltest das der User deinen Text richtig sieht? Hier ist die Lösung

CLI.present("Wow look at me!!")

time.sleep(3)

# But that wasnt it just look what we can do!
# Aber das war es noch nicht guck mal was du machen kannst!

# rgb1 = text
# rgb2 = borders
# offset = extra borders (must be even)

CLI.present("Wow this is really cool!!", rgb1=(200,200,0), rgb2=(0,200,200), offset=6)