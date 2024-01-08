from typing import Dict
from anytree import Node, PreOrderIter, Walker

from source.utils import parse_file

test_data = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
""".split()


def parse_orbits(lines: [str]) -> dict:
    orbit_map = {}
    for line in lines:
        a, b = line.split(')')
        if a not in orbit_map:
            orbit_map[a] = []
        orbit_map[a].append(b)
    return orbit_map


def build_tree(orbit_map: Dict[str, str]) -> [Node]:
    node_map = {}
    all_node_names = ({key for key in orbit_map.keys()} |
                      {val for sublist in orbit_map.values() for val in sublist})

    for parent in all_node_names:
        node_map[parent] = Node(parent)

    for parent, children in orbit_map.items():
        for child in children:
            node_map[child].parent = node_map[parent]

    return node_map


def get_orbit_counts(orbits: Dict[str, str]) -> int:
    tree: [Node] = build_tree(orbits)
    tree_node = tree['COM']
    depths = [node.depth for node in PreOrderIter(tree_node)]
    return sum(depths)


def get_orbit_traversal(orbits) -> int:
    tree: [Node] = build_tree(orbits)
    w = Walker()
    (u, c, d) = w.walk(tree['YOU'], tree['SAN'])
    return len(u) + 1 + len(d) - 3


__all__ = ['parse_file', 'parse_orbits', 'get_orbit_counts', 'get_orbit_traversal']
