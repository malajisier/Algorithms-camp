# 官方题解：详细解释
# 1.当栈不为空时，查看栈的顶部元素，该元素表示为 (parent_node, parent_state) 。
# 2.在遍历 parent_node 的任何子节点之前，我们检查 parent_node 本身是否是 p 或 q 中的一个。
# 3.当我们第一次找到 p 或 q 的时候，设置一个布尔标记，名为 one_node_found 为 true 。
# 还可以通过在变量 LCA_index 中记录栈的顶部索引来跟踪最近的公共祖先。因为栈的所有当前元素都是我们刚刚发现的节点的祖先。
# 4.第二次 parent_node == p or parent_node == q 意味着我们找到了两个节点，我们可以返回 LCA node 。
# 5.每当我们访问 parent_node 的子节点时，我们将 (parent_node, updated_parent_state) 推到栈上。我们更新父级的状态为子级/分支已被访问/处理，并且相应地更改状态。
# 6.当状态变为 BOTH_DONE 时，最终会从栈中弹出一个节点，这意味着左、右子树都被推到栈上并进行处理。
# 如果 one_node_found 是 true 的，那么我们需要检查被弹出的顶部节点是否可能是找到的节点的祖先之一。在这种情况下，我们需要将 LCA_index 减一。因为其中一位祖先被弹出了。
# 7.当同时找到 p 和 q 时，LCA_index 将指向栈中包含 p 和 q 之间所有公共祖先的索引。并且 LCA_index 元素具有 p 和 q 之间的最近公共祖先。


class Solution:
    BOTH_PENDING = 2
    LEFT_DONE = 1
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [(root, Solution.BOTH_PENDING)]
        one_found = False
        LCA_idx = -1

        while stack:
            parent_node, parent_state = stack[-1]

            if parent_state != Solution.BOTH_DONE:
                if parent_state == Solution.BOTH_PENDING:
                    if parent_node == p or parent_node == q:

                        # 已经为True，p、q都已经找到
                        if one_found:
                            return stack[LCA_idx][0]
                        else:
                            # 找到了一个，标记
                            one_found = True
                            LCA_idx = len(stack) - 1


                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                
                # 更新栈顶元素的state
                stack.pop()
                stack.append((child_node, parent_state - 1))
                # 孩子节点压栈
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))

            # 
            else:
                if one_found and LCA_idx == len(stack) - 1:
                    LCA_idx -= 1
                stack.pop()

        return False
