"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import datetime

ON = 255
OFF = 0
vals = [ON, OFF]

#Configurations 
block = np.array([[0,0,0,0],
                      [0,255,255,0],
                      [0,255,255,0],
                      [0,0,0,0]])
beehive = np.array([[0,0,0,0,0,0],
                        [0,0,255,255,0,0],
                        [0,255,0,0,255,0],
                        [0,0,255,255,0,0],
                        [0,0,0,0,0,0]])
loaf = np.array([[0,0,0,0,0,0],
                     [0,0,255,255,0,0],
                     [0,255,0,0,255,0],
                     [0,0,255,0,255,0],
                     [0,0,0,255,0,0],
                     [0,0,0,0,0,0]])
boat = np.array([[0,0,0,0,0],
                     [0,255,255,0,0],
                     [0,255,0,255,0],
                     [0,0,255,0,0],
                     [0,0,0,0,0]])
tub = np.array([[0,0,0,0,0],
                    [0,0,255,0,0],
                    [0,255,0,255,0],
                    [0,0,255,0,0],
                    [0,0,0,0,0]])
blinker1 = np.array([[0,0,0],
                     [0,255,0],
                     [0,255,0],
                     [0,255,0],
                     [0,0,0]])
blinker2 = np.array([[0,0,0,0,0],
                         [0,255,255,255,0],
                         [0,0,0,0,0]])
toad1 = np.array([[0,0,0,0,0,0],
                     [0,0,0,255,0,0],
                     [0,255,0,0,255,0],
                     [0,255,0,0,255,0],
                     [0,0,255,0,0,0],
                     [0,0,0,0,0,0]])
toad2 = np.array([[0,0,0,0,0,0],
                      [0,0,255,255,255,0],
                      [0,255,255,255,0,0],
                      [0,0,0,0,0,0]])
beacon1 = np.array([[0,0,0,0,0,0],
                        [0,255,255,0,0,0],
                        [0,255,255,0,0,0],
                        [0,0,0,255,255,0],
                        [0,0,0,255,255,0],
                        [0,0,0,0,0,0]])
beacon2 = np.array([[0,0,0,0,0,0],
                        [0,255,255,0,0,0],
                        [0,255,0,0,0,0],
                        [0,0,0,0,255,0],
                        [0,0,0,255,255,0],
                        [0,0,0,0,0,0]])
glider1 = np.array([[0,0,0,0,0,0,0],
                        [0,0,0,255,0,0,0],
                        [0,0,0,0,255,0,0],
                        [0,0,255,255,255,0,0],
                        [0,0,0,0,0,0,0]])
glider2 = np.array([[0,0,0,0,0],
                        [0,255,0,255,0],
                        [0,0,255,255,0],
                        [0,0,255,0,0],
                        [0,0,0,0,0,]])
glider3 = np.array([[0,0,0,0,0],
                        [0,0,0,255,0],
                        [0,255,0,255,0],
                        [0,0,255,255,0],
                        [0,0,0,0,0]])
glider4 = np.array([[0,0,0,0,0],
                        [0,255,0,0,0],
                        [0,0,255,255,0],
                        [0,255,255,0,0],
                        [0,0,0,0,0]])
lightweightship1 = np.array([[0,0,0,0,0,0,0],
                                 [0,255,0,0,255,0,0],
                                 [0,0,0,0,0,255,0],
                                 [0,255,0,0,0,255,0],
                                 [0,0,255,255,255,255,0],
                                 [0,0,0,0,0,0,0]])
lightweightship2 = np.array([[0,0,0,0,0,0,0],
                                 [0,0,0,255,255,0,0],
                                 [0,255,255,0,255,255,0],
                                 [0,255,255,255,255,0,0],
                                 [0,0,255,255,0,0,0],
                                 [0,0,0,0,0,0,0]])
lightweightship3 = np.array([[0,0,0,0,0,0,0],
                                 [0,0,255,255,255,255,0],
                                 [0,255,0,0,0,255,0],
                                 [0,0,0,0,0,255,0],
                                 [0,255,0,0,255,0,0],
                                 [0,0,0,0,0,0,0]])
lightweightship4 = np.array([[0,0,0,0,0,0,0],
                                 [0,0,255,255,0,0,0],
                                 [0,255,255,255,255,0,0],
                                 [0,255,255,0, 255,255,0],
                                 [0,0,0,255, 255,0,0],
                                 [0,0,0,0,0,0,0]])

def randomGrid(gridwidth, gridlength):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, gridwidth*gridlength, p=[0.2, 0.8]).reshape(gridwidth, gridlength)

def update(frameNum, img, grid, gridwidth, gridlength, generations):
    if frameNum >= generations: #Stops simulation once it reaches frame 200
        exit()
    newGrid = grid.copy()

    for i in range(gridwidth):
        for j in range(gridlength):
            neighbors = (grid[i, (j-1)%gridlength] + grid[i, (j+1)%gridlength] +
                         grid[(i-1)%gridwidth, j] + grid[(i+1)%gridwidth, j] +
                         grid[(i-1)%gridwidth, (j-1)%gridlength] + grid[(i-1)%gridwidth, (j+1)%gridlength] +
                         grid[(i+1)%gridwidth, (j-1)%gridlength] + grid[(i+1)%gridwidth, (j+1)%gridlength])
            neighbors=neighbors/255
            #Conway's rules
            if grid[i, j]  == ON and (neighbors == 2 or neighbors == 3):
                    newGrid[i, j] = ON
            elif grid[i, j]  == OFF and neighbors == 3:
                    newGrid[i, j] = ON
            else:
                 newGrid[i, j] = OFF

    img.set_data(newGrid)
    grid[:] = newGrid[:]

    gliderc=0
    blockc=0 
    beehivec=0
    loafc=0
    boatc=0
    tubc=0
    blinkerc=0
    toadc=0
    beaconc=0
    lwshipc=0

    #Checks for figures in the Universe.
    for i in range(gridwidth):
        for j in range(gridlength):
             if i+4 <=gridwidth and j+4 <=gridlength: 
                  if(newGrid[i:i+4, j:j+4] == block).all():
                       blockc+=1 #block count
             if i+5 <=gridwidth and j+6 <=gridlength: 
                  if(newGrid[i:i+5, j:j+6] == beehive).all():
                       beehivec+=1 #beehive counter
             if i+5 <=gridwidth and j+5 <=gridlength: 
                  if(newGrid[i:i+5, j:j+5] == glider3).all():
                       gliderc+=1 #glider count
             if i+5 <=gridwidth and j+7 <=gridlength: 
                  if(newGrid[i:i+5, j:j+7] == glider1).all():
                       gliderc+=1  #glider count
             if i+5 <=gridwidth and j+5 <=gridlength: 
                  if(newGrid[i:i+5, j:j+5] == glider2).all():
                       gliderc+=1
             if i+5 <=gridwidth and j+5 <=gridlength: 
                  if(newGrid[i:i+5, j:j+5] == glider4).all():
                       gliderc+=1
             if i+6 <=gridwidth and j+6 <=gridlength: 
                  if(newGrid[i:i+6, j:j+6] == loaf).all():
                       loafc+=1
             if i+5 <=gridwidth and j+5 <=gridlength: 
                  if(newGrid[i:i+5, j:j+5] == boat).all():
                       boatc+=1
             if i+5 <=gridwidth and j+5 <=gridlength: 
                  if(newGrid[i:i+5, j:j+5] == tub).all():
                       tubc+=1
             if i+5 <=gridwidth and j+3 <=gridlength: 
                  if(newGrid[i:i+5, j:j+3] == blinker1).all():
                       blinkerc+=1
             if i+3 <=gridwidth and j+5 <=gridlength: 
                  if(newGrid[i:i+3, j:j+5] == blinker2).all():
                       blinkerc+=1
             if i+6 <=gridwidth and j+6 <=gridlength: 
                  if(newGrid[i:i+6, j:j+6] == toad1).all():
                       toadc+=1
             if i+4 <=gridwidth and j+6 <=gridlength: 
                  if(newGrid[i:i+4, j:j+6] == toad2).all():
                       toadc+=1
             if i+6 <=gridwidth and j+6 <=gridlength: 
                  if(newGrid[i:i+6, j:j+6] == beacon1).all():
                       beaconc+=1
             if i+6 <=gridwidth and j+6 <=gridlength: 
                  if(newGrid[i:i+6, j:j+6] == beacon2).all():
                       beaconc+=1
             if i+6 <=gridwidth and j+7 <=gridlength: 
                  if(newGrid[i:i+6, j:j+7] == lightweightship1).all():
                       lwshipc+=1
             if i+6 <=gridwidth and j+7 <=gridlength: 
                  if(newGrid[i:i+6, j:j+7] == lightweightship2).all():
                       lwshipc+=1
             if i+6 <=gridwidth and j+7 <=gridlength: 
                  if(newGrid[i:i+6, j:j+7] == lightweightship3).all():
                       lwshipc+=1
             if i+6 <=gridwidth and j+7 <=gridlength: 
                  if(newGrid[i:i+6, j:j+7] == lightweightship4).all():
                       lwshipc+=1
     #Write output file
    outputinfo(blockc, gliderc, beehivec, loafc, boatc, tubc, blinkerc, toadc, beaconc, lwshipc,gridwidth, gridlength, frameNum)

               
    return img, 

def outputinfo(blockc, gliderc, beehivec, loafc, boatc, tubc, blinkerc, toadc, beaconc, lwshipc, gridwidth, gridlength, frameNum):
     today=datetime.datetime.now()
     totalCounter=blockc+ gliderc+ beehivec+ loafc+ boatc+ tubc+ blinkerc+ toadc+ beaconc+ lwshipc #Total of configurations per iteration
     blockpercent=(100*blockc)/totalCounter #Percentage of each type of configuration
     gliderpercent=(100*gliderc)/totalCounter
     beehivepercent=(100*beehivec)/totalCounter
     loafpercent=(100*loafc)/totalCounter
     boatpercent=(100*boatc)/totalCounter
     tubpercent=(100*tubc)/totalCounter
     blinkerpercent=(100*blinkerc)/totalCounter
     toadpercent=(100*toadc)/totalCounter
     beaconpercent=(100*beaconc)/totalCounter
     lwshippercent=(100*lwshipc)/totalCounter

     
     with open("output.txt", "a") as file:
          #Output file
          file.write("Simulation: at "+ str(today) +"\n")
          file.write("Universe size " + str(gridwidth) + " x " + str(gridlength)+ "\n")
          file.write("Iteration:    " + str(frameNum+1) + "\n")
          file.write("__________________________________________________" + "\n")
          file.write("             |   Count   |   Percentage  |" + "\n")
          file.write("__________________________________________________" + "\n")
          file.write("Blocks       |     " + str(blockc) + "     |     " + str(blockpercent)+"%" + "\n")
          file.write("Beehives     |     " + str(beehivec) + "     |     " + str(beehivepercent)+"%" +"\n")
          file.write("Loafs        |     " + str(loafc) + "     |     " + str(loafpercent)+"%"+"\n")
          file.write("Boats        |     " + str(boatc) + "     |     " + str(boatpercent)+"%"+"\n")
          file.write("Tubs         |     " + str(tubc) + "     |     " +str(tubpercent)+"%"+"\n")
          file.write("Blinkers     |     " + str(blinkerc) + "     |     " +str(blinkerpercent)+"%"+"\n")
          file.write("Toads        |     " + str(toadc) + "     |     " +str(toadpercent)+"%"+"\n")
          file.write("Beacons      |     " + str(beaconc) + "     |     " +str(beaconpercent)+"%"+"\n")
          file.write("Gliders      |     " + str(gliderc) + "     |     " +str(gliderpercent)+"%"+"\n")
          file.write("Lw spaceships|     " + str(lwshipc) + "     |     " + str(lwshippercent) +"%"+"\n")
          file.write("__________________________________________________" + "\n")
          file.write("Total        |     " + str(totalCounter) + "\n")
          file.write("__________________________________________________" + "\n")
          file.write(""+ "\n")
          
def addGlider(i, j, grid):
    glider1 = np.array([[0,0,0,0,0,0,0],
                        [0,0,0,255,0,0,0],
                        [0,0,0,0,255,0,0],
                        [0,0,255,255,255,0,0],
                        [0,0,0,0,0,0,0]])
    
    grid[i:i+5, j:j+7] = glider1

def addCells(i,j, grid):
     cell=np.array([255])

     grid[i, j] =cell

def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()
    
    # TODO: add arguments
    
    updateInterval = 50
    if args.interval:
        updateInterval= int(args.interval)

    grid = np.array([]) 

    #Input file, amount of generations, width, height and starting configurations are received from here.
    with open("input.txt", "r") as myInput:
        inputList = []
        gridwidth, gridlength = map(int, myInput.readline().strip().split())
        generations = int(myInput.readline().strip())
        lines=myInput.read().splitlines()

        for line in lines:
            positions = line.split()
            for position in positions:
                 thisposition=position.split()
                 inputList.append(thisposition)
    Livecellx=[]#position in x and y for the data collected from the input file 
    Livecelly=[]
    
    grid = np.zeros(gridwidth*gridlength).reshape(gridwidth, gridlength)
    
    for i in range(0, len(inputList)):
          thisnumber=int(inputList[i][0])
          if i%2 == 0:
               Livecellx.append(int(inputList[i][0])) 
          else:
               Livecelly.append(int(inputList[i][0]))

    for i, j in zip(Livecellx,Livecelly):
        addCells(i, j, grid) ##adds the cells from the input file
     
    grid = randomGrid(gridwidth, gridlength)
    addGlider(4,4,grid) ##adds a glider
    addGlider(14,14,grid) ##adds a glider
    addGlider(91,10,grid) ##adds a glider
    addGlider(79,79,grid) ##adds a glider
    addGlider(80,160,grid) ##adds a glider
    addGlider(17,170,grid) ##adds a glider

    #animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, gridwidth, gridlength, generations),
                                  frames = generations,
                                  interval=updateInterval,
                                  save_count=50, repeat=False)
    plt.show()

# call main
if __name__ == '__main__':
    main()