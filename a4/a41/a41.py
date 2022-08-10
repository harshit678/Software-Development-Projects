
# coding: utf-8

# In[33]:


#!/usr/bin/env python
"""Assignment 4 Part 1 template"""
print(__doc__)

from typing import IO


class Circle:
    """Circle class"""
    def __init__(self, cir: tuple, col: tuple) -> None:
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
            
class Rectangle:
    """Rectangle class"""
    def __init__(self, cir: tuple, col: tuple) -> None:
        self.x: int = cir[0]
        self.y: int = cir[1]
        self.width: int = cir[2]
        self.height: int = cir[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]        
        self.op: float = col[2]

class ProEpilogue:
    """Writes Prologue and Epilogue for HTMl script """
    def __init__(self,x)->None:
        self.x:int = x 
   
def writeHTMLcomment(f: IO[str], t: int, com: str) -> None:
    """writeHTMLcomment method"""
    ts: str = "   " * t
    f.write(f"{ts}<!--{com}-->\n")
        
def drawCircleLine(f: IO[str], t: int, c: Circle) -> None:
    """drawCircle method"""
    ts: str = "   " * t
    line1: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" '
    line2: str = f'fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
    f.write(f"{ts}{line1+line2}\n")
    
def drawRecLine(f: IO[str], t: int, c: Rectangle) -> None:
        """drawRec method"""
        ts: str = "   " * t
        line1: str = f'<rect x="{c.x}" y="{c.y}" width="{c.width}" height="{c.height}" '
        line2: str = f'style="fill:rgb({c.red}, {c.green}, {c.blue}); fill-opacity={c.op}"></rect>'
        f.write(f"{ts}{line1+line2}\n")
        
def genArt(f: IO[str], t: int) -> None:
   """genART method"""
   
   drawRecLine(f, t, Rectangle((0,125,100,50), (255,0,0,1.0)))
   drawRecLine(f, t, Rectangle((100,125,100,50), (0,255,0,1.0)))
   drawRecLine(f, t, Rectangle((200,125,100,50), (0,0,255,1.0)))
   drawRecLine(f, t, Rectangle((300,125,100,50), (255,0,255,1.0)))
   drawRecLine(f, t, Rectangle((400,125,100,50), (255,255,0,1.0)))
   drawRecLine(f, t, Rectangle((500,125,100,50), (255,200,150,1.0)))
   drawRecLine(f, t, Rectangle((0,325,100,50), (255,0,0,1.0)))
   drawRecLine(f, t, Rectangle((100,325,100,50), (0,255,0,1.0)))
   drawRecLine(f, t, Rectangle((200,325,100,50), (0,0,255,1.0)))
   drawRecLine(f, t, Rectangle((300,325,100,50), (255,0,255,1.0)))
   drawRecLine(f, t, Rectangle((400,325,100,50), (255,255,0,1.0)))
   drawRecLine(f, t, Rectangle((500,325,100,50), (255,200,150,1.0)))
   drawCircleLine(f, t, Circle((50,50,50), (255,0,0,1.0)))
   drawCircleLine(f, t, Circle((150,50,50), (0,255,0,1.0)))
   drawCircleLine(f, t, Circle((250,50,50), (0,0,255,1.0)))
   drawCircleLine(f, t, Circle((350,50,50), (255,0,255,1.0)))
   drawCircleLine(f, t, Circle((450,50,50), (255,255,0,1.0)))
   drawCircleLine(f, t, Circle((550,50,50), (255,200,150,1.0)))
   drawCircleLine(f, t, Circle((50,250,50), (255,0,0,1.0)))
   drawCircleLine(f, t, Circle((150,250,50), (0,255,0,1.0)))
   drawCircleLine(f, t, Circle((250,250,50), (0,0,255,1.0)))
   drawCircleLine(f, t, Circle((350,250,50), (255,0,255,1.0)))
   drawCircleLine(f, t, Circle((450,250,50), (255,255,0,1.0)))
   drawCircleLine(f, t, Circle((550,250,50), (255,200,150,1.0)))
        
def openSVGcanvas(f: IO[str], t: int, canvas: tuple) -> None:
     """openSVGcanvas method"""
     ts: str = "   " * t
     writeHTMLcomment(f, t, "Define SVG drawing box")
     f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

def closeSVGcanvas(f: IO[str], t: int) -> None:
    """closeSVGcanvas method"""
    ts: str = "   " * t
    f.write(f"{ts}</svg>\n")
    f.write(f"</body>\n")
    f.write(f"</html>\n")

def writeHTMLline(f: IO[str], t: int, line: str) -> None:
     """writeLineHTML method"""
     ts = "   " * t
     f.write(f"{ts}{line}\n")

def writeHTMLHeader(f: IO[str], winTitle: str) -> None:
    """writeHeadHTML method"""
    writeHTMLline(f, 0, "<html>")
    writeHTMLline(f, 0, "<head>")
    writeHTMLline(f, 1, f"<title>{winTitle}</title>")
    writeHTMLline(f, 0, "</head>")
    writeHTMLline(f, 0, "<body>")

def writeHTMLfile() -> None:
    """writeHTMLfile method"""
    fnam: str = "myPart1Art.html"
    winTitle = "My Art"
    f: IO[str] = open(fnam, "w")
    writeHTMLHeader(f, winTitle)
    openSVGcanvas(f, 1, (900,900))
    genArt(f, 2)
    closeSVGcanvas(f, 1)
    f.close()
    

def main() -> None:
    """main method"""
    writeHTMLfile()

if __name__ == "__main__":
    main()

