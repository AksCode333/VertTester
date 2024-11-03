ExampleDataSet = [[0, 0, 0, 1],[0, 0, 0,2],[0, 1, 0, 3],[0, 1, 0, 4],[0, 0, 0, 5],[0, 0, 0, 6],[0, 0, 0, 7],[0, 0, 0, 8],[0, 0, 1, 9],[0, 0, 0, 10],[0, 0, 0, 11]]
#print(ExampleDataSet[2])
onGroundValue = []
for i in ExampleDataSet: #goes through every data point
    if (i[0] or i[1] or i[2] == 1): # If the foot is seen at any point
        onGroundValue.append([True, i[3]]) # make it true
    else:
        onGroundValue.append([False, i[3]])#false
    
print(onGroundValue)
start = []

def startOfJump():
    for i in onGroundValue: #checks every value to see if the foot is seen
        if i[0] == True: #fidns the first place the foot is seen with the time stamp
            start.append(i)
            firstFoot = i[1]
            onGroundValue.remove(i)
            for i in onGroundValue: #goes through it again to find when the foot leaves the ground
                if i[1] < firstFoot:
                    onGroundValue.remove(i)
                else:
                    return i #first frame after the foot leaves the ground
        else:
            print('')
            #onGroundValue.remove(i) #Removes all non valid data poitns BEFORE the first
            
def endOfJump():
    for i in onGroundValue:
        if i[1] <= beg[1]:
            onGroundValue.remove(i)
    onGroundValue.remove(onGroundValue[0])
    return(onGroundValue)
            
beg = startOfJump()


print("the first time the foot was seen was ", start)
print("the last time the foot was seen the first time was", beg)
print("end of the jump", endOfJump())
