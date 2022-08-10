
# coding: utf-8

# In[177]:


import a41 as one
import a42 as two
import random


# In[184]:



def RandArt(f):
        cnt:int = 0
        while(cnt<500):
                cls = two.GenRandom((random.randint(0,1600),random.randint(0,1600),random.randint(0,100)), 
                      (random.randint(10,100),random.randint(10,100)),
                      (random.randint(10,30),random.randint(10,30)),
                      (random.randint(0,255),random.randint(0,255),random.randint(0,255),random.random()))
                circ = one.Circle((cls.x,cls.y,cls.rad),(cls.red,cls.green,cls.blue,cls.op))
                rec = one.Rectangle((cls.x,cls.y,cls.width,cls.height),(cls.red,cls.green,cls.blue,cls.op))
                one.drawCircleLine(f,1,circ)
                one.drawRecLine(f,1,rec)
                cnt = cnt + 1


# In[185]:


def GenRanArt():
    fnam: str = "myPart3Art.html"
    winTitle = "MyArt"
    f: IO[str] = open(fnam, "w")
    one.writeHTMLHeader(f, winTitle)
    one.openSVGcanvas(f, 1, (1600,800))
    RandArt(f)
    one.closeSVGcanvas(f, 1)
    f.close()


# In[186]:


def main() -> None:
    """main method"""
    GenRanArt()

if __name__ == "__main__":
    main()


