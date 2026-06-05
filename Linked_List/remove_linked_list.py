
class ListNode(object):
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head


def array_to_linked_list(arr):
     
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))

# Example usage

arr = [1, 1, 2, 3, 3, 4, 5, 5, 5]
head = array_to_linked_list(arr)

print("Original list:")
print_linked_list(head)

result = deleteDuplicates(head)

print("After removing duplicates:")
print_linked_list(result)