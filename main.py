import sys
import xml.etree.ElementTree as ET 

NODES_FILE_SUFFIX = "nodes.csv"
EDGES_FILE_SUFFIX = "edges.csv"

def create_nodes_csv_file(gexf_file_name, nodes_element):
    nodes_csv_file_name = gexf_file_name + "_" + NODES_FILE_SUFFIX
    with open(nodes_csv_file_name, 'w') as file:
        file.write("nodeID,nodeName\n")
        for node in nodes_element: # node = <node id= .. > .. </node>                              
            node_id = node.attrib["id"]
            node_name = node.attrib["label"].encode("utf-8").decode()
            file.write(node_id + "," + node_name + "\n")
    print("{} is created.".format(NODES_FILE_SUFFIX))
    print("Number of nodes: {}".format(len(nodes_element)))

def get_weight_of_edge(edge):
    for attvalues in edge: # attvalues = <attvalues> .. </attvalues>
        for attvalue in attvalues: # attvalue = <attvalue>  .. </attvalue>
            if attvalue.attrib["for"] == "weight":
                return attvalue.attrib["value"]
    return "0"

def create_edges_csv_file(gexf_file_name, edges_element, is_graph_undirected):
    edges_csv_file_name = gexf_file_name + "_" + EDGES_FILE_SUFFIX
    with open(edges_csv_file_name, 'w') as file:
        file.write("SourceID,TargetID,weight\n")
        for edge in edges_element: # edge = <edge source= .. > .. </edge>
            source_id = edge.attrib["source"]
            target_id = edge.attrib["target"]
            weight = get_weight_of_edge(edge)
            file.write(source_id + "," + target_id + "," + weight + "\n")
            if (is_graph_undirected):
                file.write(target_id + "," + source_id + "," + weight + "\n")
    print("{} is created.".format(EDGES_FILE_SUFFIX))
    print("Number of edges: {}".format(len(edges_element)))

def find_element(graph_element, target_element_type):
    for child in graph_element:
        if target_element_type in child.tag:
            return child
    raise Exception("Please specify a valid GEXF file which contains <{}> element.".format(target_element_type))

def get_graph_element(gexf_file_path):
    tree = ET.parse(gexf_file_path)
    root = tree.getroot()
    for child in root:
        if "graph" in child.tag:
            return child
    raise Exception("Please specify a valid GEXF file.")

def create_csv_files(gexf_file_path):
    graph_element = get_graph_element(gexf_file_path)
    is_graph_undirected = graph_element.attrib["defaultedgetype"] == "undirected"

    nodes_element = find_element(graph_element, "nodes") # nodes_element = <nodes> .. </nodes>
    edges_element = find_element(graph_element, "edges") # edges_element = <edges> .. </edges>
    
    gexf_file_name = gexf_file_path.split(".gexf")[0]
    create_nodes_csv_file(gexf_file_name, nodes_element)
    create_edges_csv_file(gexf_file_name, edges_element, is_graph_undirected)

if __name__ == "__main__":
    create_csv_files(sys.argv[1])
