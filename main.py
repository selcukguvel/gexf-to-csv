# Converts the specified GEXF file to nodes.csv and edges.csv files.
import sys
import xml.etree.ElementTree as ET 

NODES_FILE = "nodes.csv"
EDGES_FILE = "edges.csv"

def findElement(graphElement,str):
    # Finds either nodesElement or edgesElement which str specifies to.
    element = None
    for child in graphElement:
        if(str in child.tag):
            element = child
        elif(str in child.tag):
            element = child
    if(element == None):
        raise Exception('Unknown file format.')
    return element

def writeNodes(nodesElement):
    # Writes to the nodes.csv file which has two columns: nodeID and nodeName.
    with open(NODES_FILE,'w') as file:
        file.write("nodeID,nodeName\n")
        for node in nodesElement:                              # node   = <node id= .. > .. </node>
            nodeAtr  = node.attrib
            nodeId   = nodeAtr["id"]
            nodeName = nodeAtr["label"]
            file.write(nodeId + "," + nodeName + "\n")    

def writeEdges(edgesElement):
    # Writes to the edges.csv file which has three columns: SourceID, TargetID and weight.
    with open(EDGES_FILE,'w') as file:
        file.write("SourceID,TargetID,weight\n")
        for edge in edgesElement:                              # edge   = <edge source= .. > .. </edge>
            edgeAtr = edge.attrib
            sourceId = edgeAtr["source"]
            targetId = edgeAtr["target"]
            weight   = "0"
            for attvalues in edge:                             # attvalues  = <attvalues> .. </attvalues>
                for attvalue in attvalues:                     # attvalue   = <attvalue>  .. </attvalue>
                    edgeAttr = attvalue.attrib
                    if(edgeAttr['for'] == 'weight'):
                        weight = edgeAttr['value']
            file.write(sourceId + "," + targetId + "," + weight + "\n")

def convert(gexfFile):
    # Converts GEXF to the CSV.
    tree = ET.parse(gexfFile)
    root = tree.getroot()
    for child in root:
        if('graph' in child.tag):
            graphElement = child
    nodesElement = findElement(graphElement,'nodes')           # nodesElement = <nodes> .. </nodes>
    edgesElement = findElement(graphElement,'edges')           # edgesElement = <edges> .. </edges>
    writeNodes(nodesElement)
    writeEdges(edgesElement)
    print(NODES_FILE + " and " + EDGES_FILE + " are created.")
    print("Number of nodes: {}".format(len(nodesElement)))
    print("Number of edges: {}".format(len(edgesElement)))

if __name__ == "__main__":
    convert(sys.argv[1])
