# gexf-to-csv

In order to convert a `GEXF` (Graph Exchange XML Format) file to the `nodes` and `edges` `CSV` files, you can use the command:

`python main.py {yourFileName}.gexf`

## Output CSV Files

### {yourFileName}\_nodes.csv

This file has two columns: `nodeID` and `nodeName`.

### {yourFileName}\_edges.csv

This file has three columns: `SourceID`, `TargetID` and `weight`.

`SourceID` and `TargetID` represents the id of the source and target nodes.
`weight` represents the weight of the edge.

If the graph is undirected (has attribute `defaultedgetype` as `undirected` in the `GEXF` file), the edges `CSV` file will contain two edge rows for each edge specified in the `GEXF` file.
