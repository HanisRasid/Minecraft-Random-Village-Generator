# Development Diary
This is a *template* for your dev diary in PS2.
Feel free to edit as you see fit e.g., based on your progress updates, hurdles encountered and circumvented.
Make sure to log one comprehensive update per student, per each week of our teaching term.
Please, get in touch with teaching staff for any questions around this or otherwise post on Microsoft Teams.

# Mandatory Student's contributions
Please, specify your individual contributions to the project **as a percentage**. 
Default is a *25% contribution for each student*. However, please modify as necessary, if that is not the case.

# Development Diary Activities
Please, report your key activities in each week this assignment is running.  

**Week 1**
* Hanis - s3781755
    * Setup Minecraft and the API
    * Implement basic houses and test out different blocks and their variants. Started to notice the drawbacks of the API, mainly that some objects were not present in the API and that some blocks act weirdly after being placed through script.
    * Finished one of the houses to be used in our randomised village. I tried to make it look slightly different from the average minecraft house by modernising it and shifting around some things such as having a balcony pool instead of the reccommended backyard pool. Nevertheless, I ensured aesthetics were on point!

* Henry - s3905838
    * Setup the Minecraft Python API and the MCspigot Server
    * Finished code that produces a double story house with a fenced pool, pitched roof and has furniture. The material of the house is randomized between wood planks, brick and stone brick. 

* Laskaris Dionyssopoulos - s3845221
    * Read chapter 2 on textbook
    * Setup VS Code, and Minecraft on Windows
    * Implemented Hello Minecraft!
    * Implemented house template design, a basic and more advanced design were created

* Patrick - s3721043
    * Read chapter 1 & 2 on textbook
    * Setup VS Code on Windows, as well as Minecraft Java and MCspigot server
    * Implemented Hello Minecraft!
    * The code required to produce a house, with a pool and a pitched roof has been completed. The house randomizes the materials used each time.

**Week 2**
* Hanis - s3781755
    * Implementing the roads for the village and attempting to randomise the direction of the roads in the x and z planes. The randomisation will be between going straight, right or left with every direction having its own class and functions.
    * Updated hanishouse to have an extra variation and randomised between the versions. The new version is a three storey house that has an added room with furniture inside it.
    * Updating roads script to climb over natural hills and elevation by rewriting the code so that the road is checked row by row before being placed. The height of each individual block is checked so that there are no inconsistencies in the road, ensuring that players are able to walk on the road without any potholes of any sort.

* Henry - s3905838
    * Made some adjustment to the script so the house's shape will be random.
    * Created a landscape script for the village to be set on
    * Created lamp posts that will randomly spawn next to the roads


* Laskaris Dionyssopoulos - s3845221
    * Re-wrote house code to be more procedually generated with randomness, such as the size of the house, and changing rooms
    * Created objects that can be placed around the village, such as the farm and the tree
    * Implemented function in the main file, which allows a house object to be created
    * Started creating a function to connect the houses to the pre-existing roads that have been placed

* Patrick - s3721043
    * Finished the code to generate a two-storey house
    * Included a connected pool to the house, with furnishings like a table and a bookshelf.
    * Included a way to randomize the building materials
    * Begun work on randomized placement of houses on the landscape.
    

**Week 3**
* Hanis - s3781755
    * Working on improving my house with added aesthetics. This includes adding hedges which have to be adjacent to a wood block so that the leaves do not wither.
    * Sketched out a simple script for the video so that we remember to cover all the important aspects of our village
    * Creating a forge to make the village more lively and appealing. The forge will cycle through different blocks so that each generation is randomised.
    * Linked the forge and church to the road system with help from Laskaris through the use of roads functions already present.

* Henry - s3905838
    * Added some more random features to the house such as, random furiture and randomised rooms.
    * Implemented a hill that will spawn in the centre of the landscape 
    * Created a script to spawn plants around the landscape
    * Created a script to spawn a well in the centre of the foundation
    * Adjusted the main script so the houses will randomly spawn at different heights.

* Patrick - s3721043
    * Worked on the placement of the elements of the village, including the houses, the farms, a centred well.
    * Optimising the order of placement of the different elements to ensure no bugs or errant placement of buildings occurs.
    * Making small adjustment to certain parts of the code to allow for a better village generation (changing the length of the randomized path)
    * The creation of a church building to add to the village

* Laskaris Dionyssopoulos - s3845221
    * Finished function to connect the houses to the pre-existing roads and continuously modified it to improve the code and make it workable in certain conditions, 
      including wrapping around the house if the road's endpoint was behind the house.
    * Continued to test the village generation and made small code changes if neccessary
.....
