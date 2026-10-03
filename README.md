# Robot-Control-Center-OOP

This project uses several classes to simulate a Robot Fight Club.

there are 3 classes with the Robot class being the parent, hosting the necessary methods
for the subclasses to use and/or build off uptop.

There are 6 options, including exit when entering the control pannel.

One of the options is Battle initialization which sets a battle between 2 bots
One allows you to add a robot to the fleet
One allows you to see Robot statistics
Another allows you to see the Robots ranked 1 to last
One allows you to see the entire robot fleet

The question about choose 1-6 repeats until you choose 6 (exit)

Technical:

There are 2 subclasses of the parent class Robot

Both alter the choose_move and perform_move methods to suit different styles which is what the 
subclasses are based around

The 4th class is InitBattle which is used as a referee to host and overlook battles and pass/calculate information about attacks/moves.

Personal Recomendation:
ALWAYS CHOOOSE GIBBY!!!!!