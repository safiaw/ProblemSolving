

def robotinagrid(r,c,x,y):
    
    if x==r-1 and y==c-1:
        print("(%d,%d)\n" %(x,y))
        #return([(x,y)])
        return
        
    #path=[]
    print("(%d,%d)," %(x,y))
    #path.append((x,y))
    if x < r-1:
        robotinagrid(r,c,x+1,y)
        #path.extend(robotinagrid(r,c,x+1,y))
        #return path
    if y < c-1:
        robotinagrid(r,c,x,y+1)
        #path.extend(robotinagrid(r,c,x,y+1))
        #return path


def revrobotinagrid(r,c,x,y,path):
    
    if x==r-1 and y==c-1:
        #print("(%d,%d)\n" %(x,y))
        #return([(x,y)])
        path.append([(x,y)])
        print(path)
        return
        
    #path=[]
    #print("(%d,%d)," %(x,y))
    path.append((x,y))
    if x < r-1:
        revrobotinagrid(r,c,x+1,y,path)
        #path.extend(robotinagrid(r,c,x+1,y))
        #return path
    if y < c-1:
        revrobotinagrid(r,c,x,y+1,path)
        #path.extend(robotinagrid(r,c,x,y+1))
        #return path


r=3
c=3
x=0
y=0
path=[]
revrobotinagrid(r,c,x,y,path)
        
