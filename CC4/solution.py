from __future__ import annotations
from typing import List
import math


class Node:
    """Node that contains value, index and left and right pointers."""
    def __init__(self, val: int, left: Node = None, right: Node = None, index: int = 0):
        self.val = val
        self.index = index
        self.left = left
        self.right = right

def inorder(root, ret_val_list, ret_ind_list) -> List[int]:
    if root is None:
        return []

    inorder(root.left, ret_val_list, ret_ind_list)

    if root is not None:
        ret_val_list.append(root.val)
        ret_ind_list.append(root.index)

    inorder(root.right, ret_val_list, ret_ind_list)

    return ret_val_list, ret_ind_list

def smaller_product(root: Node) -> List[int]:
   """
    docstring: PLEASE fill this out or you will lose points
    Check CC1 for an example
    """
   
   ret_val = []
   ret_idx = []
   product_list = []

   if root is None:
       return []
   if root and root.left is None and root.right is None:
       return [None]

   ret_val, ret_idx = inorder(root=root, ret_val_list=ret_val, ret_ind_list=ret_idx)

   product_list = [0] * len(ret_idx)

   for i in range(len(ret_val)):
        if i == 0:
            product_list[ret_idx[i]] = None  # No smaller elements for the smallest node
        else:
            product = 1
            for j in range(i):
                product *= ret_val[j]
                
            product_list[ret_idx[i]] = product

   return product_list
          
   
   

   
       
   


   
   






