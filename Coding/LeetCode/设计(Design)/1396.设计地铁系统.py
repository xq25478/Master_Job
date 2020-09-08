#
# @lc app=leetcode.cn id=1396 lang=python3
#
# [1396] 设计地铁系统
#

# @lc code=start
class UndergroundSystem:
    
    def __init__(self):
        self.user_station = {} #[id:[in,t1,out,t2]]
        self.average_station = {} #(in,out):(average,cnt)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # # 之前已经进站 但没出站 无法进站
        # if id in self.user_station and 0 < len(self.user_station[id]) < 3:
        #     return 

        # 之前不存在
        if id not in self.user_station:
            self.user_station[id] = []
        
        if self.user_station[id]:
            return 

        self.user_station[id].extend([stationName,t])
    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # 还未进站或者不存在
        if ( id in self.user_station and len(self.user_station[id]) == 0 ) or (id not in self.user_station):
            return 
        
        self.user_station[id].extend([stationName,t])

        if (self.user_station[id][0],self.user_station[id][2]) not in self.average_station:
            self.average_station[(self.user_station[id][0],self.user_station[id][2])] = [0.0,0.0]

        old_aver = self.average_station[(self.user_station[id][0],self.user_station[id][2])][0]
        old_cnt = self.average_station[(self.user_station[id][0],self.user_station[id][2])][1]

        new_aver = (old_aver*old_cnt + int(self.user_station[id][3]) - int(self.user_station[id][1]))/(old_cnt+1)
        new_cnt = old_cnt + 1

        self.average_station[(self.user_station[id][0],self.user_station[id][2])] = [new_aver,new_cnt]

        #出完站 清空用户信息
        self.user_station[id] = []

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation,endStation) not in self.average_station:
            self.average_station[(startStation,endStation)] = [0.0,0.0]
            return 0.0
        
        if self.average_station[(startStation,endStation)][1] == 0:
            return 

        return  self.average_station[(startStation,endStation)][0]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

