def setup():
    size(450,450) #parameters
    r= random(0, 250)
    stroke (100,255,0)
    fill(15)
    leaf = 255
    triangle (120,300,232,80,344,300) #size of triangle
    fill(r)  #color for the triangle
    stroke(0,0,0)
    ellipse(230,225,150,70)# The first one 
    fill(leaf)
    ellipse(230,225,60,40)#the second one 
    ellipse(230,225,3,3)#the thhird one
    stroke(0,leaf,0)#color for the line
    line(0,50, 450, 50)
    stroke(0,leaf,0)
    line(3,350, 450, 350)
    sometext="KB"
    text(sometext,leaf,250)
    



    
   
    
    
    
