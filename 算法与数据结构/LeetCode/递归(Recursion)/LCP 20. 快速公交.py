'''
小扣打算去秋日市集，由于游客较多，小扣的移动速度受到了人流影响：

小扣从 x 号站点移动至 x + 1 号站点需要花费的时间为 inc；
小扣从 x 号站点移动至 x - 1 号站点需要花费的时间为 dec。
现有 m 辆公交车，编号为 0 到 m-1。小扣也可以通过搭乘编号为 i 的公交车，从 x 号站点移动至 jump[i]*x 号站点，耗时仅为 cost[i]。小扣可以搭乘任意编号的公交车且搭乘公交次数不限。

假定小扣起始站点记作 0，秋日市集站点记作 target，请返回小扣抵达秋日市集最少需要花费多少时间。由于数字较大，最终答案需要对 1000000007 (1e9 + 7) 取模。

注意：小扣可在移动过程中到达编号大于 target 的站点。

'''

class Solution(object):
    def busRapidTransit(self, target, inc, dec, jump, cost):
        """
        :type target: int
        :type inc: int
        :type dec: int
        :type jump: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #自底向上记忆化递推   
        memo = dict() #记忆字典
        def findroute(cur_target):  
            if cur_target==0:     #当前站点已经是0了返回0代价
                return 0
            if cur_target in memo:
                return memo[cur_target]
            mincost = cur_target*inc  #最小代价初始化为直接回终点站，我相信这种情况应该存在

            for i,val in enumerate(jump): #遍历附近的公交站点
                if cur_target>1:#至少得大于1，不然我自己走了还坐个屁公交
                    if cur_target%val==0: #当前站能够坐公交
                        mincost =min(mincost,cost[i]+findroute(cur_target//val)) #递归下一站
                    else:
                        bias = cur_target%val #当前站不能做公交看看需要走几步到达公交站  
                        if cur_target-bias>0: #往前走几步如果没到终点，就该坐公交，递归下一站
                            mincost=min(mincost,bias*inc+cost[i]+findroute(cur_target//val))

                        mincost = min(mincost,(val-bias)*dec+cost[i]+findroute(cur_target//val+1))#往后走几步坐公交递归下一站
            memo[cur_target]=mincost
            return mincost

        return findroute(target)%(1000000007)
