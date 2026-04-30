class CountSquares:

    def __init__(self):
        #count of points with same coordinate, key is tuple(point)
        # key cannot be list type, this is needed because same points are treated as different
        self.ptsCount = defaultdict(int) 
        self.pts = [] # list to store the points(dups allowed)

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point[0], point[1]
        for x, y in self.pts:
            # first look for diagonal point with query point
            # skip  if not diagonal or same point
            if abs(qx - x) != abs(qy - y) or x == qx or y == qy:
                continue
            res += (self.ptsCount[(x, qy)] * self.ptsCount[(qx, y)])
        return res
        
