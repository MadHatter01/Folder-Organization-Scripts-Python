import os;
import networkx as nx;
import matplotlib.pyplot as plt;


def generate_tree(root, Graph, parent=None):
    try:
        base = os.path.basename(root);
        Graph.add_node(root, label = base)

        if parent:
            Graph.add_edge(parent, root)

        items = os.listdir(root)
        _ne = False

        for item in items:
            _path = os.path.join(root, item)

            if os.path.isdir(_path):
                if generate_tree(_path, Graph, parent = root):
                    _ne = True
        return _ne

    except PermissionError as e:
        print('Permission Error')
        return False


if __name__=="__main__":
    _dir = "C:/Users/Placeholder/Placeholder/"
    if os.path.exists(_dir):
        Graph = nx.DiGraph()
        generate_tree(_dir, Graph)

        _layout = nx.spring_layout(Graph, seed=24)
        labels = nx.get_node_attributes(Graph, 'label')


        plt.figure(figsize=(12,8))
        plt.title("Graph Visualization")
        nx.draw(Graph, _layout, labels=labels, with_labels=False,  node_size=400, font_size=8, font_color='black')
        plt.show()
