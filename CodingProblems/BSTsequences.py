
class Node:

    def __init__(self,elem=None):

        self.data=elem
        self.left=None
        self.right=None


all_sequences=[]

def sequences(node):
    
    if node.left==None and node.right==None:
        return [[node.data]]

    elif node.left==None and node.right!=None:

        root = node.data
        right_seq = sequences(node.right)
        print(right_seq)
        for each_right_seq in right_seq:
            #print(each_right_seq)
            new_seq=[]
            new_seq.append(root)
            new_seq.extend(each_right_seq[:])
            all_sequences.append(new_seq)

        return all_sequences

    elif node.left!=None and node.right==None:

        root=node.data
        left_seq = sequences(node.left)

        for each_left_seq in left_seq:
                print(each_left_seq)
                new_seq=[]
                new_seq.append(root)
                new_seq.extend(each_left_seq[:])
                all_sequences.append(new_seq)
                
        return all_sequences

    elif node.left!=None and node.right!=None:
        root=node.data
        left_seq = sequences(node.left)
        right_seq = sequences(node.right)

        for each_left_seq in left_seq:
             for each_right_seq in right_seq:
                new_seq=[]
                new_seq.append(root)
                new_seq.extend(each_left_seq[:])
                new_seq.extend(each_right_seq[:])
                all_sequences.append(new_seq)

        for each_right_seq in right_seq:
             for each_left_seq in left_seq:
                new_seq=[]
                new_seq.append(root)
                new_seq.extend(each_right_seq[:])
                new_seq.extend(each_left_seq[:])
                all_sequences.append(new_seq)
                
        return all_sequences


def weaved(first,second,prefix):



    

    

'''root = Node(2)
root.left = Node(1)
root.right = Node(3)'''

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.right = Node(9)
root.right.right.left = Node(8)
root.right.right.right = Node(10)

res = sequences(root)
#print(res)

                        

                
    
