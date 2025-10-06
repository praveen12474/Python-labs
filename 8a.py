class Node:
    def __init__(self,name,time,purpose):
        self.name=name
        self.time=time
        self.purpose=purpose
        self.left=None
        self.right=None

    def insert(root,name,time,purpose):
        if root is None:
            return Node(name,time,purpose)
        if name.lower()<root.name.lower():
            root.left=Node.insert(root.left,name,time,purpose)
        else:
            root.right=Node.insert(root.right,name,time,purpose)
        return root

    def search(root,name):
        if root is None or root.name.lower()==name.lower():
            return root
        if name.lower()<root.name.lower():
            return Node.search(root.left,name)
        return Node.search(root.right,name)

    def find_min(root):
      while root.left:
          root=root.left
      return root

    def delete(root,name):
        if root is None:
            return root
        if name.lower()<root.name.lower():
            root.left=Node.delete(root.left,name)
        elif  name.lower()>root.name.lower():
            root.right=Node.delete(root.right,name)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp=Node.find_min(root.right)
root.name,root.time,root.purpose=temp.name,temp.time,temp.purpose
            root.right=Node.delete(root.right,temp.name)
        return root

    def inorder(root):
        if root:
            Node.inorder(root.left)
            print("",root.name,",",root.time,"," ,root.purpose,"")
           
            Node.inorder(root.right)
           
    def preorder(root):
        if root:
            Node.inorder(root.left)
            print("",root.name,",",root.time,"," ,root.purpose,"")
            Node.preorder(root.right)


    def postorder(root):
          if root:
            Node.postorder(root.left)
            Node.postorder(root.right)
            print("",root.name,",",root.time,",",root.purpose,"")

    def count(root):
        if root is None:
            return 0
        return 1+Node.count(root.left)+Node.count(root.right)

root=None
while True:
    print("---LOG BOOK MENU---")
    print("1.Insert logentry")
    print("2.Delete")
    print("3.Search")
    print("4.Inorder")
    print("5.Postorder")
    print("6.Preorder")
    print("7.Count")
    print("8.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        name=input("Enter the name:")
        time=input("Enter the time:")
        purpose=input("Enter the purpose:")
        root=Node.insert(root,name,time,purpose)
    elif choice=="2":
        name=input("Enter the name:")
        root=Node.delete(root,name)
    elif choice=="3":
        name=input("Enter the name to search:")
        res=Node.search(root,name)
    if res:
           print(f"Found: {res.name}, {res.time}, {res.purpose}")

        else:
            print("NOT FOUND")
    elif choice=="4":
        print("Inorder Traversal:")
        Node.inorder(root)
    elif choice=="5":
        print("Postorder Traversal:")
        Node.postorder(root)
    elif choice=="6":
        print("preorder Traversal:")
        Node.preorder(root)
    elif choice=="7":
        total=Node.count(root)
        print("Total entries:{total}")
    elif choice=="8":
        print("Exiting---")
    else:
        print("Invalid choice")
