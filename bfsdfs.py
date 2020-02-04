#WAPto reach a goal value of 5 using both BFS and DFS 
root = {'value' : 1, 'depth' : 1}
def succ(node):
    if node['value'] == 5:
        return []
    elif node['value'] == 4:
        return [{'value':5, 'depth': node['depth']+1}]
    else:
        return [{'value':node['value']+1, 'depth': node['depth']+1},
        {'value':node['value']+2, 'depth': node['depth']+1}]
def bfs_tree(root):
    nodes_to_visit = [root]
    visited_nodes = []
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop()
        visited_nodes.append(current_node)
        nodes_to_visit.extend(succ(current_node))
    return visited_nodes
print(bfs_tree(root))
