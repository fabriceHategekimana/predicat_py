from pyvis.network import Network
import random


def getRandomColor():
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number = "#" + hex_number[2:]
    return hex_number


def getColumn(num, mylist):
    return [x[num] for x in mylist]


def unique(mylist):
    return list(set(mylist))


def addNodes(net, facts):
    nodeList = unique(getColumn(0, facts) + getColumn(2, facts))
    net.add_nodes(nodeList)


def addEdges(net, facts):
    d = {}  # on crée un dictionnaire qui assignera à chaque type de noeud une couleur
    uniqueLinks = unique(getColumn(1, facts))
    for u in uniqueLinks:
        d[u] = getRandomColor()
    for f in facts:
        net.add_edge(f[0], f[2], label=f[1], color=d[f[1]])


def displayNetwork(tab):
    net = Network(
        bgcolor="#333333",
        font_color="white",
        height="100%",
        width="100%",
        directed=True,
    )
    addNodes(net, tab)
    addEdges(net, tab)

    net.set_options(
        '{ "manipulation": { "enabled": true }, "physics": { "enabled": false }, "interaction": { "multiselect": true, "navigationButtons": true }, "configure": { "enabled": true, "filter": "layout,physics", "showButton": true }, "edges": { "smooth": { "enabled": false } } }'
    )
    net.show("network.html")
