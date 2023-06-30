def build_tree_list(root):
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []

    node_repr = str(root.value)

    new_root_width = gap_size = len(node_repr)

    l_cell, l_cell_width, l_root_start, l_root_end = build_tree_list(
        root.left)
    r_cell, r_cell_width, r_root_start, r_root_end = build_tree_list(
        root.right)

    if l_cell_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(" " * (l_root + 1))
        line1.append("_" * (l_cell_width - l_root))
        line2.append(" " * l_root + "/")
        line2.append(" " * (l_cell_width - l_root))
        new_root_start = l_cell_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    line1.append(node_repr)
    line2.append(" " * new_root_width)

    if r_cell_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append("_" * r_root)
        line1.append(" " * (r_cell_width - r_root + 1))
        line2.append(" " * r_root + "\\")
        line2.append(" " * (r_cell_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    gap = " " * gap_size
    new_cell = ["".join(line1), "".join(line2)]
    for i in range(max(len(l_cell), len(r_cell))):
        temp_l_line = l_cell[i] if i < len(l_cell) else " " * l_cell_width
        temp_r_line = r_cell[i] if i < len(r_cell) else " " * r_cell_width
        new_cell.append(temp_l_line + gap + temp_r_line)

    return new_cell, len(new_cell[0]), new_root_start, new_root_end


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        lines = build_tree_list(self)[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))


first = Node(1)
first.left = Node(2)
first.right = Node(3)
first.left.left = Node(4)
first.left.right = Node(5)
first.right.left = Node(6)
first.right.right = Node(7)
first.right.left.left = Node(8)
first.right.left.right = Node(9)
first.right.left.right.left = Node(10)
first.right.left.right.right = Node(11)

print(first)
