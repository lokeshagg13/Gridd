from Node import Node
import random

class Grid: 
    def __init__(self):
        self.gridmap = [] 
        self.rows = 0
        self.columns = 0

    def getEmptyGrid(self, rows, columns):
        self.rows = rows
        self.columns = columns
       
        for i in range(rows):
            col = []
            for j in range(columns):
                cell = Node(i,j,True)
                col.append(cell)
            self.gridmap.append(col)

    def displayGrid(self):
        print('\n\n\n')
        for i in range(self.rows):
            for j in range(self.columns):
                cell = self.gridmap[i][j]
                if(cell.walkable):
                    print(1, end = '')
                else:
                    print(0, end = '')
            print()

    # Create a function to create an automatic random grid (atleast 4*4) with num_obs obstacles,
    # each obstacle must have random size with rows as (1<= obstacle_row <= grid_row/2-1)

    def createGrid(self, rows, columns, num_obs):

        if(rows < 4 or columns < 4):
            print('Grid must be atleast 4 * 4')

        self.getEmptyGrid(rows, columns)
        
        i_obs = 0

        while(i_obs < num_obs):
            obstacle_rows = random.randint(1, rows/2-1)
            obstacle_columns = random.randint(1, rows/2-1)

            obs_top = random.randint(0, rows-obstacle_rows)
            obs_left = random.randint(0, columns-obstacle_columns)

            for i in range(obstacle_rows):
                for j in range(obstacle_columns):
                    gm = self.gridmap[obs_top+i][obs_left+j]
                    if(gm.walkable == True):
                        gm.walkable = False
                    else:
                        continue
            
            i_obs += 1

            self.displayGrid()

if __name__ == '__main__':
    g = Grid()
    g.createGrid(10,10,2)

    