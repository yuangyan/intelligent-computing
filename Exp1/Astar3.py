import random
from PIL import Image, ImageDraw
SIZE = 25
BLOCK_RATIO = 0.2

Map = [1] * SIZE * SIZE
blocks = list(range(SIZE * SIZE))
img =Image.new('RGB',(1000,1000), (255,255,255))
h,w = img.size
draw = ImageDraw.Draw(img)

def CoordiateConvert(t) :
    x = t // SIZE
    y = t % SIZE
    return x, y

def GenerateMap() :
    global blocks
    random.shuffle(blocks)
    blocknum = round(SIZE * SIZE * BLOCK_RATIO)
    blocks = blocks[0 : blocknum - 1]
    for b in blocks :
        Map[b] = 0

def PaintPoint(t, color) :
    x, y = CoordiateConvert(t)
    draw.rectangle((x * w / SIZE, y * h / SIZE, (x + 1) * w / SIZE, (y + 1) * h / SIZE), fill = color)

def PaintMap() :
    for b in blocks :
        PaintPoint(b, (0, 0, 0))

class Point :
    def __init__(self) :
        self.x, self.y, self.t = 0, 0, 0
        self.covereddistance = 0
        self.estimateddistance = 0
        self.previous = list()

    def ToLeft(self) :
        x, y = self.x - 1, self.y
        if(x < 0) :
            return None
        t = x * SIZE + y
        if Map[t] == 0 :
            return None
        c = Point()
        c.x, c.y, c.t, c.covereddistance = x, y, t, self.covereddistance + 1
        c.estimateddistance = c.EstimatedDistance()
        c.previous = self.previous.copy()
        c.previous.append(self.t)
        return c
        

    def ToRight(self) :
        x, y = self.x + 1, self.y
        if(x >= SIZE) :
            return None
        t = x * SIZE + y
        if Map[t] == 0 :
            return None
        c = Point()
        c.x, c.y, c.t, c.covereddistance = x, y, t, self.covereddistance + 1
        c.estimateddistance = c.EstimatedDistance()
        c.previous = self.previous.copy()
        c.previous.append(self.t)
        return c
        

    def Down(self) :
        x, y = self.x, self.y - 1
        if(y < 0) :
            return None
        t = x * SIZE + y
        if Map[t] == 0 :
            return None
        c = Point()
        c.x, c.y, c.t, c.covereddistance = x, y, t, self.covereddistance + 1
        c.estimateddistance = c.EstimatedDistance()
        c.previous = self.previous.copy()
        c.previous.append(self.t)
        return c
        

    def Up(self) :
        x, y = self.x, self.y + 1
        if(y >= SIZE) :
            return None
        t = x * SIZE + y
        if Map[t] == 0 :
            return None
        
        c = Point()
        c.x, c.y, c.t, c.covereddistance = x, y, t, self.covereddistance + 1
        c.estimateddistance = c.EstimatedDistance()
        c.previous = self.previous.copy()
        c.previous.append(self.t)
        return c
        

    def ManhattanDistance(self) :
        return SIZE - 1 - self.x + SIZE - 1 - self.y

    def EstimatedDistance(self) :
        return self.ManhattanDistance() + self.covereddistance

GenerateMap()
PaintMap()
img.show()

solutionlist = list()
solutionlist.append(Point())
solution = Point()
iters = 0
while (solutionlist != []):
    iters += 1
    currentPoint = solutionlist[0]
    for p in solutionlist :
        if p.estimateddistance < currentPoint.estimateddistance :
            currentPoint = p
    tmp = currentPoint
    currentPoint = solutionlist[-1]
    solutionlist[-1] = tmp
    solutionlist.pop()
    
    solution = currentPoint
    print(str(iters) + ' ' + str(len(solutionlist)) + ' ' + str(currentPoint.ManhattanDistance()))
    if currentPoint.t == SIZE * SIZE - 1 :
        break
    r, l, u, d = currentPoint.ToRight(), currentPoint.ToLeft(), currentPoint.Up(), currentPoint.Down()
    if currentPoint.previous == [] :
        if r != None: solutionlist.append(r)
        if l != None: solutionlist.append(l)
        if u != None: solutionlist.append(u)
        if d != None: solutionlist.append(d)
    else :
        if r != None and ((r in currentPoint.previous) == False): solutionlist.append(r)
        if l != None and ((l in currentPoint.previous) == False): solutionlist.append(l)
        if u != None and ((u in currentPoint.previous) == False): solutionlist.append(u)
        if d != None and ((d in currentPoint.previous) == False): solutionlist.append(d)



    
for t in solution.previous :
    PaintPoint(t, (0, 255, 0))
    PaintPoint(solution.t, (0, 255, 0))

img.show()
img.save('demo.png')


