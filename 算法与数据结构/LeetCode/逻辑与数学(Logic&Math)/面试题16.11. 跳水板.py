from typing import List
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        return [] if k == 0 else [shorter*k] if shorter == longer else [ shorter*(k-i)+longer*i for i in range(0,k+1)]