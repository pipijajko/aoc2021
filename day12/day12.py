
test_input_ = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".split("\n")
# lowercase - small cave, uppercase - big cave
#So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

test_input2_ = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".split("\n")


test_input3_ = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""".split("\n")



from collections import defaultdict
def parse_graph(source):
    source = [li.strip() for li in source if li.strip()]
    graph = defaultdict(list) #A->[B,C,D]
    for connection in source:
        A,_,B = connection.strip().partition("-")
        if A == "end" or B == "start":
            A,B=B,A
        #symmetric connections
        graph[A].append(B)
        if A != "start" and B != "end": #don't allow to return to start or exit from exit ;)
            graph[B].append(A)
    return graph




def dfs_paths(graph, node_name, paths, curpath=()):
    curpath = curpath + (node_name,)
    if node_name == "end":
        #print(curpath)
        paths.append(curpath)
        return
    children = graph[node_name]
    for child in children:
        if child.lower() == child and child in curpath:
            #Lowercase nodes can only be visited once
            continue
        else:
            dfs_paths(graph, child, paths, curpath)
    return



def dfs_paths_revisit(graph, node_name, paths, curpath=()):
    #blows up stack
    curpath = curpath + (node_name,)
    visited_small_caves = [x for x in curpath if x.lower() == x and x not in ("start", "end")]
    revisited = len(visited_small_caves) == len(set(visited_small_caves)) + 1
    #print(curpath, revisited, visited_small_caves)
    if node_name == "end":
        #print(curpath)
        paths.append(curpath)
        return
    children = graph[node_name]
    for child in children:
        if child.lower() == child and child in curpath and revisited:
            #Lowercase nodes can only be visited once
            continue
        else:
            dfs_paths_revisit(graph, child, paths, curpath)
    return


# def dfs_paths_revisit(graph, paths):
#     node = graph["start"]


    
    
#     #blows up stack
#     curpath = curpath + (node_name,)
#     visited_small_caves = [x for x in curpath if x.lower() == x and x not in ("start", "end")]
#     revisited = len(visited_small_caves) == len(set(visited_small_caves)) + 1
#     #print(curpath, revisited, visited_small_caves)
#     if node_name == "end":
#         #print(curpath)
#         paths.append(curpath)
#         return
#     children = graph[node_name]
#     for child in children:
#         if child.lower() == child and child in curpath and revisited:
#             #Lowercase nodes can only be visited once
#             continue
#         else:
#             dfs_paths_revisit(graph, child, paths, curpath)
#     return




def cave_explorer(source, revisit_once=False):
    g = parse_graph(source)
    paths = []
    print(g)
    if revisit_once:
        dfs_paths_revisit(g, "start", paths)
    else:
        dfs_paths(g, "start", paths)
    print("len=", len(paths))
    return len(paths)




def main(filename):
    with open(filename) as fp:
        x= cave_explorer(fp)
        print("simple: ", x)
    with open(filename) as fp:
        y=cave_explorer(fp, True)
        print("adv: ", y)
    

if __name__ == "__main__":
    # assert cave_explorer(test_input_) == 10
    # assert cave_explorer(test_input2_) == 19
    # assert cave_explorer(test_input3_) == 226
    # assert cave_explorer(test_input_, True) == 36
    assert cave_explorer(test_input2_, True) == 103
    # assert cave_explorer(test_input3_, True) == 3509

    main("input.txt")
