# class Vertex():
#     def __init__():
#         self.name = name
        # self.neighbors = []

class Graph():
    def __init__(self, graph_file):
        self.file = graph_file

    def vertex_count(self):
        vertices = 0
        with open(self.file, 'r') as file:
            for line in file.readlines():
                if line[0] == '(' and len(line) >= 5:
                    vertices += 1
            return vertices

    def edge_count(self):
        edges = 0
        with open(self.file, 'r') as file:
            for line in file.readlines():
                if line[0] == '(' and len(line) >= 5:
                    edges += 1
            return edges

    def edge_list(self):
        edges = 0
        with open(self.file, 'r') as file:
            for line in file.readlines():
                if line[0] == '(' and len(line) >= 5:
                    edges += 1
            return edges

def main():
    import sys 
    args = sys.argv[1:]

    if len(args) == 1: 
        text = args[0]
        g = Graph(text)
        print("Number of Vertices:", g.vertex_count())
        print("Number of Edges:", g.edge_count())
        print("Edge List:", g.edge_list())
    else: 
        print("Please provide a text file at the command line.\n")
        print("Example: python3 challenge_1.py graph_data.txt")
if __name__ == "__main__":
    main()