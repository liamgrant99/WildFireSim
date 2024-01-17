"""
Simulates a forest fire. The number of trees in the forest are based on the density of the forest, and fire spreads
to vertically and horizontally adjacent trees. If the fire reaches the bottom, true is returned, and if it does not false is
returned. 
"""
from Queue import Queue
from Stack import Stack

import random
import dudraw

class Forest:
    def __init__(self, width: int, height: int, d: float) -> None:
        """
        Instantiates the forest class. 
            parameters: 
                width : int - Length of the sub_list
                height : int - Length of 2D list
                d : float - the density of the forest. 
            return: None
        """
        self.the_forest = [[1 if random.random() <= d else 0 for i in range(width)] for j in range(height)]
        
        #Instance variables are created to store the x and y scale of the screen when the forest is drawn.
        self.x_scale = width
        self.y_scale = height

    def __str__(self) -> str:
        """
        Prints the content of the 2D forest list. 
            parameters: 
                None
            return: str
        """
        #Empty string is created
        return_str = ""

        #Each sub_list is traversed in the list
        for list in self.the_forest:
            sub_str = "["

            #Each value is appended to the sub string. 
            for value in list:
                sub_str += str(value) + " "

            #Closing bracket is added to sub string. 
            sub_str += "]\n"
            #Sub string is added to the result string. 
            return_str += sub_str

        #Result string is returned. 
        return return_str
    
    def depth_first_search(self):
        """
        The forest fire is simulated with a stack ADT. 
            parameters: 
                None
            return: bool
        """
        #A stack to store the cells is created. 
        cells_to_explore = Stack()

        #Int value 2 to represent tree on fire. 
        #The tree on fire is pushed to the stack. 
        for i in range(len(self.the_forest[0])):
            if self.the_forest[0][i] == 1:
                self.the_forest[0][i] = 2
                cells_to_explore.push((0,i))

        #While loop runs while the stack has contents. 
        while not cells_to_explore.is_empty():

            self.draw()

            current_cell = cells_to_explore.pop()

            #True is returned if the algorithm reaches the final row of the 2D list. 
            if current_cell[0] == len(self.the_forest)-1:
                return True
            
            
            for i in range(-1,2,2):
                #Horizontally adjacent cells are checked to see if they are trees. If so, the fire spreads to them and the cell is pushed onto the stack.
                if not(i==-1 and current_cell[1]==0) and not(i==1 and current_cell[1]==len(self.the_forest[current_cell[0]])-1):
                    if self.the_forest[current_cell[0]][current_cell[1]+i] == 1:
                        self.the_forest[current_cell[0]][current_cell[1]+i] = 2
                        cells_to_explore.push((current_cell[0], current_cell[1]+i))
                
                #Vertically adjacent cells are checked to see if they are trees. If so, the fire spreads to them and the cell is pushed onto the stack.
                if not(i==-1 and current_cell[0]==0) and not(i==1 and current_cell==len(self.the_forest)-1):
                    if self.the_forest[current_cell[0]+i][current_cell[1]] == 1:
                        self.the_forest[current_cell[0]+i][current_cell[1]] = 2
                        cells_to_explore.push((current_cell[0]+i, current_cell[1]))
            
        #False is returned if the fire does not make it to the final row. 
        return False

    def breadth_first_search(self):
        """
        The forest fire is simulated with a queue ADT. 
            parameters: 
                None
            return: bool
        """
        #A queue is created to store the cells. 
        cells_to_explore = Queue()

        #Int value 2 to represent tree on fire. 
        #The tree on fire is pushed to the stack.
        for i in range(len(self.the_forest[0])):
            if self.the_forest[0][i] == 1:
                self.the_forest[0][i] = 2
                cells_to_explore.enqueque((0,i))

        #While loop runs while the stack has contents.
        while not cells_to_explore.is_empty():

            self.draw()

            current_cell = cells_to_explore.dequeque()

            #True is returned if the algorithm reaches the final row of the 2D list.
            if current_cell[0] == len(self.the_forest)-1:
                return True

            for i in range(-1,2,2):
                #Horizontally adjacent cells are checked to see if they are trees. If so, the fire spreads to them and the cell is pushed onto the stack.
                if not(i==-1 and current_cell[1]==0) and not(i==1 and current_cell[1]==len(self.the_forest[current_cell[0]])-1):
                    if self.the_forest[current_cell[0]][current_cell[1]+i] == 1:
                        self.the_forest[current_cell[0]][current_cell[1]+i] = 2
                        cells_to_explore.enqueque((current_cell[0], current_cell[1]+i))

                #Vertically adjacent cells are checked to see if they are trees. If so, the fire spreads to them and the cell is pushed onto the stack.
                if not(i==-1 and current_cell[0]==0) and not(i==1 and current_cell==len(self.the_forest)-1):
                    if self.the_forest[current_cell[0]+i][current_cell[1]] == 1:
                        self.the_forest[current_cell[0]+i][current_cell[1]] = 2
                        cells_to_explore.enqueque((current_cell[0]+i, current_cell[1]))

        #False is returned if the fire does not make it to the final row. 
        return False


    def draw(self):
        """
        The forest is drawn. 
            parameters: 
                None
            return: bool
        """
        dudraw.clear()

        dudraw.set_x_scale(0,self.x_scale)
        dudraw.set_y_scale(0,self.y_scale)

        #The variables representing the x and y values of the square are set
        x_val = .5
        y_val = self.y_scale - .5

        #The sub lists of the 2d list are iterated over. 
        for list in self.the_forest:
            #x_val is resert to .5
            x_val = .5

            #Each cell is iterated over
            for value in list:
                #If the cell is set to one the pen color is set to Green.
                if value == 1:
                    dudraw.set_pen_color(dudraw.GREEN)

                #If the cell is set to one the pen color is set to Red. 
                elif value == 2:
                    dudraw.set_pen_color(dudraw.RED)

                #If the cell is set to one the pen color is set to Gray. 
                else:
                    dudraw.set_pen_color(dudraw.GRAY)

                #The square is drawn at the x and y value. 
                dudraw.filled_square(x_val, y_val, .5)

                x_val += 1

            y_val -= 1

        #The image is shown for 4 seconds. 
        dudraw.show(1)
        #2500

class FireSpread:
    def probability_fire_spread_dfs(self, d : float, r:int):
        """
        A forest object is created with an inputted density and checked to see if it solves with 
        DFS. This is repeated multiple times and the average is taken to check the probability that 
        a fire spreads in forest with a given density. 
            parameters: 
                d : float - density of the forests to be tested
                r : int - the number of repitions DFS is executed. 
            return: float
        """
        #The number of times a fire spreads is set to 0. 
        fire_spread_count = 0

        #Forest is instantiated and solved multiple times. 
        for i in range(r):
            #A forest object is created. 
            forest = Forest(20,20,d)

            #If the forest solves, one is added to the fire spread count. 
            if forest.depth_first_search():
                fire_spread_count += 1

        #The average is found by dividing the number of times the fire spreads divided by the number of repitions. 
        fire_spread_probability = fire_spread_count/r

        #The average percentage is returned. 
        return fire_spread_probability

    def probability_fire_spread_bfs(self, d : float, r:int):
        """
        A forest object is created with an inputted density and checked to see if it solves with 
        BFS. This is repeated multiple times and the average is taken to check the probability that 
        a fire spreads in forest with a given density. 
            parameters: 
                d : float - density of the forests to be tested
                r : int - the number of repitions BFS is executed. 
            return: float
        """
        #The number of times a fire spreads is set to 0. 
        fire_spread_count = 0
        
        #Forest is instantiated and solved multiple times. 
        for i in range(r):
            #A forest object is created. 
            forest = Forest(20,20,d)

            #If the forest solves, one is added to the fire spread count. 
            if forest.breadth_first_search():
                fire_spread_count += 1

        #The average is found by dividing the number of times the fire spreads divided by the number of repitions. 
        fire_spread_probability = fire_spread_count/r

        #The average percentage is returned. 
        return fire_spread_probability
    
    def highest_density_dfs(self, r:int):
        """
        A binary search is conducted to find the density of a 20X20 forest that results in a 50%
        probability of a forestfire spreading. Uses DFS. 
            parameters: 
                r : int - the number of repitions DFS is executed. 
            return: float
        """
        #Variables are created to represents the low and high variables. 
        low_density = 0
        high_density = 1.0

        #The binary search is conducted 20 times. 
        for i in range(20):
            #The density is set to the midpoint between the high and low. 
            density = (low_density+high_density)/2
           
            #The probability is found with a DFS search. 
            p = self.probability_fire_spread_dfs(density, r)

            #If the probability is less than .5, the low density is increased. 
            if p < .5:
                low_density = density
            #If the probability is greater than .5, the high density is increased. 
            else:
                high_density = density
        
        #If the probability is greater than .5, the high density is increased. 
        return density

    def highest_density_bfs(self, r:int):
        """
        A binary search is conducted to find the density of a 20X20 forest that results in a 50%
        probability of a forestfire spreading. Uses BFS. 
            parameters: 
                r : int - the number of repitions BFS is executed. 
            return: float
        """
        #Variables are created to represents the low and high variables.
        low_density = 0
        high_density = 1.0

        #The binary search is conducted 20 times.
        for i in range(20):
            #The density is set to the midpoint between the high and low.
            density = (low_density+high_density)/2
            
            #The probability is found with a BFS search.
            p = self.probability_fire_spread_bfs(density, r)

            #If the probability is less than .5, the low density is increased.
            if p < .5:
                low_density = density
            #If the probability is greater than .5, the high density is increased.
            else:
                high_density = density

        #If the probability is greater than .5, the high density is increased.
        return density
    
#A fire spread class is created. 
fire_spread = FireSpread()

#The critical probability for BFS and DFS are calculated and printed to the terminal. 
critical_probability_bfs = fire_spread.highest_density_bfs(10000)
critical_probability_dfs = fire_spread.highest_density_dfs(10000)

print(f"Highest density that results in fire spreading with less than 0.5 probability for dfs: {critical_probability_dfs}")
print(f"Highest density that results in fire spreading with less than 0.5 probability for bfs: {critical_probability_bfs}")

#A list to store the probability outcomes is created. 
y_values = []

#Probability of fire spread is calculated for all values between .01 and 1 incremented by .01.
#One is added to the value and appended to the list, so that it matches the x and y scale. 
for i in range(1,101):
    y_values.append((fire_spread.probability_fire_spread_dfs(i/100, 3000)*100)+1)

#The x and y scale are set to the min and max values of the probability data ponits, with extra space for the axises. 
dudraw.set_x_scale(0,101)
dudraw.set_y_scale(0,101)

#The axis lines are drawn
dudraw.set_pen_color(dudraw.BLACK)
dudraw.line(.5,101,.5,0)
dudraw.line(0,.5,101,.5)

#The axis labels are printed 
dudraw.text(56,4,"Tree Density")
dudraw.text(12,51,"Probability of Fire Spread")

#Draw the hashes on the axises of the graph. 
for i in range(100):
    dudraw.line(0,i+.5,1,i+.5)
    dudraw.line(i+.5,0,i+.5,1)

dudraw.set_pen_color(dudraw.RED)
#Draws lines between each of the y value points.
for i in range(len(y_values)-1):
    dudraw.line(i+1,y_values[i], i+2, y_values[i+1])

dudraw.show(100000)
