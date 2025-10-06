class EnrollmentRecord:
    def __init__(self, enrollment_id, name):
        self.enrollment_id = enrollment_id
        self.name = name
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
def insert(self, root, enrollment_id, name):
        if not root:
            return EnrollmentRecord(enrollment_id, name)

        if enrollment_id < root.enrollment_id:
            root.left = self.insert(root.left, enrollment_id, name)
        elif enrollment_id > root.enrollment_id:
            root.right = self.insert(root.right, enrollment_id, name)
        else:
            print("Enrollment ID already exists.")
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and enrollment_id < root.left.enrollment_id:
            return self.right_rotate(root)
        if balance < -1 and enrollment_id > root.right.enrollment_id:
            return self.left_rotate(root)
        if balance > 1 and enrollment_id > root.left.enrollment_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and enrollment_id < root.right.enrollment_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, enrollment_id):
        if not root:
            return root

        if enrollment_id < root.enrollment_id:
            root.left = self.delete(root.left, enrollment_id)
        elif enrollment_id > root.enrollment_id:
            root.right = self.delete(root.right, enrollment_id)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.enrollment_id = temp.enrollment_id
            root.name = temp.name
            root.course = temp.course
            root.right = self.delete(root.right, temp.enrollment_id)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, enrollment_id):
        if root is None or root.enrollment_id == enrollment_id:
            return root
        if enrollment_id < root.enrollment_id:
            return self.search(root.left, enrollment_id)
        else:
            return self.search(root.right, enrollment_id)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(f"ID: {root.enrollment_id}, Name: {root.name}, Course: {root.course}")
            self.inorder_traversal(root.right)

    def count_nodes(self, root):
        if not root:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


def main():
    tree = AVLTree()

    while True:
        print("\n====== Enrollment System Menu ======")
        print("1. Insert Enrollment Record")
        print("2. Delete Enrollment Record")
        print("3. Search Enrollment Record")
        print("4. Show All Enrollments (In-Order)")
        print("5. Count Total Enrollments")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            try:
                enrollment_id = int(input("Enter Enrollment ID: "))
                name = input("Enter Student Name: ")
                tree.root = tree.insert(tree.root, enrollment_id, name)
                print(" Record inserted.")
            except ValueError:
                print(" Invalid input. Please enter numeric Enrollment ID.")
        elif choice == '2':
            try:
                enrollment_id = int(input("Enter Enrollment ID to delete: "))
                tree.root = tree.delete(tree.root, enrollment_id)
                print(" Record deleted (if existed).")
            except ValueError:
                print("Invalid input.")
        elif choice == '3':
            try:
                enrollment_id = int(input("Enter Enrollment ID to search: "))
                result = tree.search(tree.root, enrollment_id)
                if result:
                    print(f"Found: ID: {result.enrollment_id}, Name: {result.name}")
                else:
                    print("Enrollment ID not found.")
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            print(" All Enrollments (In-Order):")
            tree.inorder_traversal(tree.root)
        elif choice == '5':
            count = tree.count_nodes(tree.root)
            print(f" Total Enrollments: {count}")
        elif choice == '6':
            print(" Exiting. Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
