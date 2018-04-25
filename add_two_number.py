"""
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    l1_tmp = l1
    l2_tmp = l2
    len_l1, len_l2 = 0, 0
    while l1_tmp != None:
        len_l1 += 1
        l1_tmp = l1_tmp.next
    while l2_tmp != None:
        len_l2 += 1
        l2_tmp = l2_tmp.next

    max_len = max(len_l1, len_l2)
    carry = 0  # 前一位相加后的进位
    result_head = ListNode(-1)
    before = result_head
    after = before
    for i in range(max_len):
        cur_l1, cur_l2 = 0, 0
        if i < len_l1:
            cur_l1 = l1.val
            l1 = l1.next
        if i < len_l2:
            cur_l2 = l2.val
            l2 = l2.next
        cur_sum = cur_l1 + cur_l2 + carry
        carry = cur_sum // 10
        cur_num = cur_sum % 10
        after = ListNode(cur_num)
        before.next = after
        before = after

    if carry > 0:
        after = ListNode(carry)
        before.next = after
    if result_head.next:
        result_head = result_head.next
    return result_head


d1 = ListNode(1)
d2 = ListNode(8)
d3 = ListNode(9)
d1.next = d2
d2.next = d3

d4 = ListNode(0)
d5 = ListNode(9)
d6 = ListNode(9)
d4.next = d5
d5.next = d6

result = add_two_numbers(d1, d4)
result_temp = result
result_len = 0
while result_temp:
    result_len += 1
    result_temp = result_temp.next
for i in range(result_len):
    print(result.val)
    result = result.next
