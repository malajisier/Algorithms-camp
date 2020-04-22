# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS实现， TC:O(N), SC:O(N)
class Codec:
    # 最简版的递归
    def serialize(self, root):
        def helper(node):
            if node:
                res.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                res.append("#")
        
        res = []
        helper(root)
        return ",".join(res)
    
    def deserialize(self, data):
        def helper():
            val = next(vals)
            if val == "#":
                return None
            
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        
        vals = iter(data.split(","))
        return helper()


    # 前序遍历来序列化字符串，用逗号隔开
    # def serialize(self, root):
    #     def recSerialize(root, string):
    #         if root is None:
    #             string += "None,"
    #         else:
    #             string += str(root.val) + ','
    #             string = recSerialize(root.left, string)
    #             string = recSerialize(root.right, string)
    #         return string
        
    #     return recSerialize(root, '')
            
        
    # def deserialize(self, data):
    #     def recDeserialize(s):
    #         if s[0] == 'None':
    #             s.pop(0)
    #             return None
            
    #         root = TreeNode(s[0])
    #         s.pop(0)
    #         root.left = recDeserialize(s)
    #         root.right = recDeserialize(s)
    #         return root

    #     slist = data.split(',')
    #     root = recDeserialize(slist)
    #     return root

# # 使用list和迭代器的递归   
# def serialize(self, root):
#         res = []
#         def preorder(root):
#             if not root:
#                 res.append('#')
#                 return 
#             res.append(str(root.val))
#             preorder(root.left)
#             preorder(root.right)
        
#         preorder(root)
#         return ",".join(res)
        

#     def deserialize(self, data):
#         # 使用了迭代器
#         iterator = iter(data.split(','))
#         def helper():
#             s = next(iterator)
#             if s == "#":
#                 return 
            
#             node = TreeNode(int(s))
#             node.left = helper()
#             node.right = helper()
#             return node

#         return helper()