from code import interact
from __init__ import *

class Tree:
    def __init__(self, root, children = []):
        self.parent = None
        self.root = root
        for elem in children:
            elem.parent = self
        self.children = children

    def __str__(self):
        res = '%s'%self.root

        for child in self.children:
            res += ('\n' + str(child)).replace('\n', '\n\t')

        return res

    def find_node(self, elem):
        if root == elem:
            return self

        for child in self.children:
            res = child.find_node(elem)
            if res is not None:
                return res

        return None

    @staticmethod
    def from_koala_syntaxtree(parse_tree):
        if parse_tree.terminal is None:
            pos = parse_tree.getLabel()
            text = ''
            for child in parse_tree:
                children.append(Tree.from_koala_syntaxtree(child))

            return Tree(root, children)

        else: # terminal tree
            pass
        interact(local = locals())

class EdgedTree(Tree):
    def __init__(self, root, children):
        """

        Argument children is a list of 2-tuple, (edge, subtree)
        """

        subtrees = [e[1] for e in children]
        super().__init__(root, subtrees)
        self.tree = Tree(root, [e.tree for e in subtrees])
        self.edged_children = children

    @staticmethod
    def initialize_from_dependencies(lst, debug = False):
        res = Tree(None, [])
        cur = res
        covered_nodes = []
        lst = lst[::-1]

        if debug:
            print(lst)
            print('================')
            flag = 0

        while lst != []:
            if debug:
                print('------------')
            dep = lst.pop()

            if dep.src is None:
                if debug:
                    flag = 1
                res.children.append(Tree(dep.dest))
                cur = res.children[0]
            elif dep.src == covered_nodes[-1]:
                if debug:
                    flag = 2
                    print(cur)
                cur.children.append(Tree(dep.dest))
                if debug:
                    print(cur.children[0].root)
            else:
                if debug:
                    flag = 3
                while cur != dep.src:
                    if cur is None:
                        break
                    cur = cur.parent

                if cur is None:
                    res.children.append(Tree(dep.dest))
                else:
                    cur.children.append(Tree(dep.dest))

            covered_nodes.append(dep.dest)

            if debug:
                print('flag', flag)
                print(dep)
                print(covered_nodes)
                print('cur : \n', cur)
                print('res : \n', res)

        return res

if __name__ == '__main__':
    class A:
        def __init__(self, a, b):
            self.src = a
            self.dest = b
        def __str__(self):
            return '%s, %s'%(self.src, self.dest)
        def __repr__(self):
            return '(%s, %s)'%(self.src, self.dest)


    lst = [A(None, 2),
           A(2, 3),
           A(3, 4),
           A(2, 5),]

    print(Tree(1,
            [Tree(2, [Tree(3), Tree(4)],),
             Tree(4, [Tree(6)])]))

    # print(EdgedTree.initialize_from_dependencies(lst, debug = True))
    t = EdgedTree.initialize_from_dependencies(lst, debug = True)
    interact(local = locals())



