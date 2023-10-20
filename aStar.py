from pyamaze import maze, agent, textLabel, COLOR
from queue import PriorityQueue

def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2
    
    return (abs(x1-x2) + abs(y1-y2))

def getNextCell(d, currCell):
    if d =='E':
        childCell=(currCell[0], currCell[1] + 1)
    elif  d =='W':
        childCell=(currCell[0], currCell[1] - 1)
    elif  d =='N':
        childCell=(currCell[0] - 1, currCell[1])
    elif  d =='S':
        childCell=(currCell[0] + 1, currCell[1])

    return childCell


def aStar(m,start=None):
    if start is None:
        start = (m.rows,m.cols)
    
    if m is None:
        raise ValueError("Maze object cannot be None.")
    
    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))
    aPath = {}

    g_score = {row: float('inf') for row in m.grid}
    g_score[start] = 0
    f_score = {row: float('inf') for row in m.grid}
    f_score[start] = h(start, m._goal)
    
    searchPath = [start]

    while not open.empty():
        currCell = open.get()[2]
        searchPath.append(currCell)
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                childCell = getNextCell(d, currCell)
                   
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(currCell, m._goal)    

                if temp_f_score < f_score[childCell]:
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + h(childCell, m._goal)
                    open.put((f_score[childCell], h(currCell, m._goal), childCell)) 
                    
    fwdPath = {}
    cell= m._goal
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return searchPath, aPath, fwdPath

if __name__=='__main__':
    m = maze(10, 15)
    m.CreateMaze(1,1, loopPercent=100)

    searchPath, aPath, fwdPath = aStar(m, (10,15))
    a = agent(m, 10,15, footprints=True, color=COLOR.blue, filled=True)
    b = agent(m, 1,1, footprints=True, color=COLOR.yellow, filled=True, goal=(10,15))
    c = agent(m, 10,15, footprints=True, color=COLOR.red, goal=(1,1))

    m.tracePath({a:searchPath}, delay=300)
    m.tracePath({b:aPath}, delay=300)
    m.tracePath({c:fwdPath}, delay=300)


    l = textLabel(m, 'A* Path Length', len(fwdPath)+1)
    l = textLabel(m, 'A* Search Length', len(searchPath))

    m.run()
