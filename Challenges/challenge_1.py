# class Vertex():
#     def __init__():
#         self.name = name
#         self.neighbors = []


class Graph():
    """
    
    """
    def __init__(self, graph_file):
        """
        Initializes graph and loads file to read from. 
        """
        self.file = graph_file

    def vertex_count(self):
        """
        Input: None; reads from self.file
        Output: Number of vertices present in graph
        """
        vertices = 0
        with open(self.file, 'r') as file:
            for line in file.readlines():
                if line[0].isalnum() and line[0] != 'G' and line != 'D':
                    return len(line.split(','))
            return vertices

    def edge_count(self):
        """
        Input: None; reads from self.file 
        Ouput: Number of edges present in graph
        """
        edges = 0
        with open(self.file, 'r') as file:
            for line in file.readlines():
                if line[0] == '(' and len(line) >= 5:
                    edges += 1
            return edges

    def edge_list(self):
        """
        Input: None; reads from self.file
        Output: List of tuples with edges and (if necessary) weights
        """
        edges = []
        with open(self.file, 'r') as file:
            for line in file.readlines():
                if line[0] == '(' and len(line) >= 5:
                    edges.append((line.strip('\n')))
        return self.clean_edges(edges)

    def clean_edges(self, edges):
        """
        Input: string representation of list of edges
        Output: Actual list representation of list of edges
        """
        import ast

        clean_edges = []
        for edge in edges: 
            clean_edges.append(ast.literal_eval(edge))
        return clean_edges

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
