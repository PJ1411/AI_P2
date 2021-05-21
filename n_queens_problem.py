class queens_problem:
    def __init__(self,inital_state):
        if(len(inital_state)>0):
            self.queens = inital_state;
        else:
            self.queens = []
        

    def draw(self):
        print()
        for x in range(0,8):
            row = ""
            temp = ""
            for y in range(0,8):
                if(len(self.queens)>y and self.queens[y]==x):
                    row += "| Q "
                elif(x%2==0):
                    if(not y%2==0):
                        row += "| + "
                    else:
                        row += "| - "
                else:
                    if(y%2==0):
                        row += "| + "
                    else:
                        row += "| - "
                temp += "----"
            print(row)
            print(temp)

    def heuristic(self):
        h = 0
        state = self.queens;
        for i in range(0,8):
            for x in range(i+1,8):
                ###check row##
                if(state[i]==state[x]):
                    h += 1;
            ###check diagonal fields##
                if(state[i]<state[x]):
                    if((x-i)+state[i]==state[x]):
                        h += 1;
                if(state[i]>state[x]):
                    if(state[i]-(x-i)==state[x]):
                        h += 1;
        return h;
                    


    
    
