import random
class GenRandom:
    """Stores Random Input"""
    def __init__(self, cir: tuple, rec: tuple, elip: tuple, col: tuple) -> None:
        self.sha: int = random.randint(0,2)
        self.x: int = cir[0]
        self.y: int = cir[1]
        self.width: int = rec[0]
        self.height: int = rec[1]
        self.rad: int = cir[2]
        self.rx: int = elip[0]
        self.ry: int = elip[1]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

class ArtConfig:            
    """Generates random Input"""
    @classmethod
    def RandomNumber(cls):
        """class method"""
            
        Table = GenRandom((random.randint(0,900),random.randint(0,900),random.randint(0,900)), 
                  (random.randint(10,100),random.randint(10,100)),
                  (random.randint(10,30),random.randint(10,30)),
                  (random.randint(0,255),random.randint(0,255),random.randint(0,255),random.random()))
        return Table

def PrintTable()-> None:
    cnt:int = 0
    ch: str = "   " 
    cl = ArtConfig()
    print(f"CNT{ch}SHA{ch}X{ch}Y{ch}RAD{ch}RX{ch}RY{ch}W{ch}H{ch}R{ch}G{ch}B{ch}OP\n")
    while(cnt<10):
        c = cl.RandomNumber()
        print(f"{cnt}{ch}{ch}{c.sha}{ch}{c.x:3d} {c.y:3d}  {c.rad:3d}{ch}{c.rx:2d}{ch}{c.ry:2d} {c.width:3d} {c.height:3d}  {c.red:3d} {c.green:3d} {c.blue:3d} {c.op:.1f}\n")
        cnt = cnt + 1
        
def main() -> None:
    """main method"""
    PrintTable()

if __name__ == "__main__":
    main()

