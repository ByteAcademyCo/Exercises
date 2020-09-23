# Command Line Workflow: Star Wars

## Spoilers: Star Wars Episode IV: A New Hope
* This exercise contains spoilers for the 1977 film Star Wars (retitled as "Star Wars: Episode IV: A New Hope). While it has been over four decades, you have been warned.

## Problem Description
* Navigating your computer through terminal is an extremely important, practically required skill to be a programmer. The following is an assignment where you will make / delete folders and files to help you get used to navigating your terminal and manipulating your files with bash commands. Perform all commands within the *solution* directory (there is no `solution.py` here, you'll be creating all necessary files.)

### Use bash to perform the following commands, in order:
* Navigate into the "star_wars" folder
* Create a folder called "the_empire"
* Create a folder called "the_rebellion"
* Make the following folders
	* "tatooine"
	* "millenium_falcon"
	* "death_star"
	* "x_wing"
	* "tie_fighter"
* Make the following text files (.txt) ***Make Sure to have the .txt extension on these files***
	* "luke_skywalker"
	* "old_man_ben"
	* "han_solo"
	* "chewbacca"
	* "leia_organa"
	* "darth_vader"
	* "emperor_palpatine"
* Open the darth_vader text file and add the text "Darth Vader"
	* **Bonus points** if you add the text without opening the file
* Move the emperor and darth vader into the folder "the_empire"
* Move "luke_skywalker" and "old_man_ben" to the "tatooine" folder
* Luke has found out old man ben is actually Obi Wan Kenobi. Change the name of "old_man_ben" to "obi_wan_kenobi"
* Now they need to escape tatooine. Move "han_solo" and "chewbacca" into "tatooine"
* While all this is happening the Sith lords are sitting nice and cozy inside their giant metal moon. Move "darth_vader" and "emperor_palpatine" inside the "death_star"
* Back on tatooine the characters get on the fastest ship in the galaxy and take off to save the princess. Move all four files from tatooine into the millenium falcon
* The princess is also on the death star. Move "leia_organa" to the "death_star"
* Our heroes sneak onto the Death Star. Move all the files inside the "millenium_falcon" onto the "death_star" 
* They found the princess! but in the process Obi Wan was struck down by Darth Vader. Delete the "obi_wan_kenobi" file 
* Our other heroes retreat in anger. Move Luke, Leia, Han, and Chewbacca into the "millenium_falcon"
* Alright the rebels have regrouped and come up with a plan to destroy the death star. Luke gets into an x-wing to use his sweet piloting skills. Move "leia" into the "the_rebellion" directory. Move Luke into the "x_wing"
* Vader, also a legendary pilot, gets into the tie fighter to defend the death star. Move "darth_vader" out of the death_star and into the "tie_fighter"
* Luke uses those sweet farm boy desert skills and fires some torpedos into the core of the death star, destroying it. **CAREFULLY** Delete the folder "death_star"
	* Remember that deletion of a directory is a high-stake operation
	* **DO NOT** do this without checking your command for correctness

## Testing
* to test your solution, type 'pytest' within the **solutions** subdirectory. It will use python to make sure your final directory/file structure is correct.

## Submission
* Submit your answer in the *solution* subdirectory in this directory. Your "answer" will be the structure of the folders/files you created at the end of the exercise
