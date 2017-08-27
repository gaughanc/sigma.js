import random
from create_lin_list import create_lin_list
from get_lists_test import get_genera, get_g_oxygen
from get_species_lists import get_species, get_s_oxygen

#create or define all needed lists
lins = create_lin_list()
genera = get_genera()
species = get_species()
g_oxygen = get_g_oxygen()
s_oxygen = get_s_oxygen()
nodes = []
edges = []

#define colors
dark_blue = "#27258c" 
blue = "#216fb2"
light_blue = "#beddf7"
purple = "#9868d8"
light_purple = "#d6bbf9"
maroon = "#9b1b1b"
red = "#ec5148"
pink = "#fccff7"
grey = "#e0d8d5"
black = "#000000"

#for each genus
for i, genus in enumerate(genera):
    for j, spec in enumerate(species[i]):
        o = s_oxygen[i][j]
        if o == "aerobe":
            color = dark_blue
        elif o == "facultative anaerobe":
            color = purple
        elif o == "microaerobe":
            color = light_blue
        elif o == "obligate anaerobe":
            color = maroon
        elif o == "anaerobe (unspecified)":
            color = red
        elif o == "microaerobe or anaerobe":
            color = light_purple
        elif o == "microaerobe or aerobe":
            color = blue
        elif o == "aerotolerant":
            color = pink
        elif o == "variable":
            color = dark_grey
        else:
            color = grey
        #create a node for each of its species
        nodes.append({"id":"sn"+str(i)+str(j), "label":spec, "x":10*i-10+j, "y":random.randint(850,1000), "size":5, "color":color})
        #create an edge from the genus to each of its species
        edges.append({"id":"se"+str(i)+str(j), "source":"gn"+str(i), "target":"sn"+str(i)+str(j),"size":20,"color":black})
    o = g_oxygen[i]
    if o == "aerobe":
        color = dark_blue
    elif o == "facultative aerobe":
        color = purple
    elif o == "microaerobe":
        color = light_blue
    elif o == "obligate anaerobe":
        color = maroon
    elif o == "anaerobe (unspecified)":
        color = red
    elif o == "microaerobe or anaerobe":
        color = light_purple
    elif o == "microaerobe or aerobe":
        color = blue
    elif o == "aerotolerant":
        color = pink
    elif o == "variable":
        color = dark_grey
    else:
        color = grey
    #create a node for the genus
    nodes.append({"id":"gn"+str(i), "label":genus, "x":10*i, "y":random.randint(600,800), "size":15, "color":color})
    #for each lineadge
    for lin in lins:
        if len(lin) == 6:
            #if the genus appears
            if lin[5] == genus:
                xs = [10*i+10, 10*i, 11*i, 11*i+10, 700]
                ys = [random.randint(400,500), random.randint(200,300), random.randint(90,100), 0, -300]
                sizes = [20, 25, 30, 35, 40]
                for j, n in enumerate([4, 3, 2, 1, 0]):
                    #if one of its taxon levels does not have a node, create one
                    if not any(node["label"] == lin[n] for node in nodes):
                        nodes.append({"id":"tn"+str(n)+str(i), "label":lin[n], "x":xs[j], "y":ys[j], "size":sizes[j], "color":grey})
                #for each node
                for node in nodes:
                    #if its label belongs to the genus' family, connect the node to the genus
                    if node["label"] == lin[4]:
                        edges.append({"id":"fe"+str(i), "source":"gn"+str(i), "target":node["id"],"size":20,"color":black})
                        #mark the family node
                        source = node["id"]
                        #for each node
                        for node in nodes:
                            #if its label belongs to the genus' order, connect the  node to the family
                            if node["label"] == lin[3]:
                                edges.append({"id":"oe"+str(i), "source":source, "target":node["id"],"size":20,"color":black})
                                #mark the order node
                                source = node["id"]
                                #for each node
                                for node in nodes:
                                    #if its label belongs to the genus' class, connect the node to the order
                                    if node["label"] == lin[2]:
                                        edges.append({"id":"ce"+str(i), "source":source, "target":node["id"],"size":20,"color":black})
                                        #mark the class node
                                        source = node["id"]
                                        #for each node
                                        for node in nodes:
                                            #if its label belongs to the genus' phylum, connect the node to the class
                                            if node["label"] == lin[1]:
                                                edges.append({"id":"pe"+str(i), "source":source, "target":node["id"],"size":20,"color":black})
                                                #mark the class node
                                                source = node["id"]
                                                #for each node
                                                for node in nodes:
                                                    #if its label belongs to the genus' domain, connect the node to the phylum
                                                    if node["label"] == lin[0]:
                                                        edges.append({"id":"de"+str(i), "source":source, "target":node["id"],"size":20,"color":black})
                break

scripta = """<!-- START SIGMA IMPORTS -->
<script src="../src/sigma.core.js"></script>
<script src="../src/conrad.js"></script>
<script src="../src/utils/sigma.utils.js"></script>
<script src="../src/utils/sigma.polyfills.js"></script>
<script src="../src/sigma.settings.js"></script>
<script src="../src/classes/sigma.classes.dispatcher.js"></script>
<script src="../src/classes/sigma.classes.configurable.js"></script>
<script src="../src/classes/sigma.classes.graph.js"></script>
<script src="../src/classes/sigma.classes.camera.js"></script>
<script src="../src/classes/sigma.classes.quad.js"></script>
<script src="../src/classes/sigma.classes.edgequad.js"></script>
<script src="../src/captors/sigma.captors.mouse.js"></script>
<script src="../src/captors/sigma.captors.touch.js"></script>
<script src="../src/renderers/sigma.renderers.canvas.js"></script>
<script src="../src/renderers/sigma.renderers.webgl.js"></script
<script src="../src/renderers/sigma.renderers.svg.js"></script>
<script src="../src/renderers/sigma.renderers.def.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.nodes.def.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.nodes.fast.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.edges.def.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.edges.fast.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.edges.arrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.labels.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.hovers.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.nodes.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.curve.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.arrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.curvedArrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.curve.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.arrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.curvedArrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.extremities.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.utils.js"></script>
<script src="../src/renderers/svg/sigma.svg.nodes.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.edges.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.edges.curve.js"></script>
<script src="../src/renderers/svg/sigma.svg.labels.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.hovers.def.js"></script>
<script src="../src/middlewares/sigma.middlewares.rescale.js"></script>
<script src="../src/middlewares/sigma.middlewares.copy.js"></script>
<script src="../src/misc/sigma.misc.animation.js"></script>
<script src="../src/misc/sigma.misc.bindEvents.js"></script>
<script src="../src/misc/sigma.misc.bindDOMEvents.js"></script>
<script src="../src/misc/sigma.misc.drawHovers.js"></script>
<!-- END SIGMA IMPORTS -->
<div id="container">
  <style>
    #graph-container {
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      position: absolute;
    }
  </style>
  <div id="graph-container"></div>
</div>

<script>
var g = {
      nodes: [],
      edges: []
    };

// Generate a graph:"""
scriptb = "g.nodes.push(" + str(nodes)[1:-1] + ")"

scriptc = ""

scriptd = "g.edges.push(" + str(edges)[1:-1] + ")"

scripte = """
// Instantiate sigma:
s = new sigma({
  graph: g,
  container: 'graph-container',
});
</script>"""

print(scripta, scriptb, scriptc, scriptd, scripte, sep="\n")
