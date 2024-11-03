ExampleDataSet = [[0, 0, 0, 1],[0, 0, 0,2],[0, 1, 0, 3],[0, 1, 0, 4],[0, 0, 0, 5],[0, 0, 0, 6],[0, 0, 0, 7],[0, 0, 0, 8],[0, 0, 1, 9]]
#print(ExampleDataSet[2])
onGroundValue = []
for i in ExampleDataSet:
    if (i[0] or i[1] or i[2] == 1):
        onGroundValue.append([True, i[3]])
    else:
        onGroundValue.append([False, i[3]])
    
print(onGroundValue)
start = []
def startOfJump():
    for i in onGroundValue: #checks every value to see if the foot is seen
        if i[0] == True: #fidns the first place the foot is seen with the time stamp
            start.append(i)
            onGroundValue.remove(i)
            for i in onGroundValue: #goes through it again to find when the foot leaves the ground
                if i[0] == True:
                    onGroundValue.remove(i)
                else:
                    return i #first frame after the foot leaves the ground
        else:
            onGroundValue.remove(i) #Removes all non valid data poitns BEFORE the first
            
def endOfJump():
    for i in onGroundValue:
        if i[0] == True:
            print("not done yet")
            
            
beg = startOfJump();


print("the first time the foot was seen was ", start)
print("the last time the foot was seen the first time was", beg)
print(onGroundValue)
