'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 true，
否则返回 false。假设输入的数组的任意两个数字都互不相同。
'''
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        n = len(postorder)

        def helper(left,right,min_val,max_val):
            if left >= right: #只有一个元素 或者没有元素 为真
                return True

            #根节点的值
            root_val = postorder[right]
            idx = right-1

            #寻找右子树
            while idx >= left and postorder[idx] > root_val:
                idx -=1

            #left [left,idx] right [idx+1,right-1] 
            
            for i in range(left,idx+1):
                if (max_val and postorder[i] > max_val) or \
                   (min_val and  postorder[i] < min_val) or \
                   (postorder[i] > root_val):
                    return False

            for i in range(idx+1,right):
                if (max_val and postorder[i] > max_val) or \
                   (min_val and  postorder[i] < min_val) or \
                   (postorder[i] < root_val):
                    return False    

            return helper(left,idx,min_val,root_val) and helper(idx+1,right-1,root_val,max_val)


        return helper(0,n-1,None,None)