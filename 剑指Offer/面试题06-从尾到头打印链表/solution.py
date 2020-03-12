# 题目描述：
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。


# 递归法：
# （1）递归阶段：每次传入 head.next ，以 head == None（即走过链表尾部节点）为递归终止条件，此时返回空列表 [] 。
# （2）回溯阶段： 利用 Python 语言特性，递归回溯时每次返回 当前 list + 当前节点值 [head.val] ，即可实现节点的倒序输出
# TC:O(n),  SC:O(n)
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []


# 辅助栈法 
# TC:O(n), 入栈出栈一共为n
# SC:O(n)
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []

        while head:
            stack.append(head.val)
            head = head.next
        
        return stack[::-1]