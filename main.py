from collections import deque
from heapq import heappush, heappop 
from functools import reduce

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO


    def short_short_help(visited, frontier, graph):
      if len(frontier) == 0:
        return visited
      else:
        node = heappop(frontier)
        distance = node[0]
        edge = node[1]
        my_char = node[2]
        if my_char in visited:
          return short_short_help(visited, frontier, graph)
        else:
          visited[my_char] = (distance, edge)

          for neigh, weight in graph[my_char]:
            heappush(frontier, (distance + weight, edge + 1, neigh))
          return short_short_help(visited, frontier, graph)

    frontier = []
    visited = dict()
    myno = (0, 0, source)
    heappush(frontier, myno)
    
    return short_short_help(visited, frontier, graph)


#returning 0 instead of (0,0)
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):

  all_d = dict()
  #visited = set()
  frontier = set([source])

  if len(frontier) == 0:
    return all_d
  else:
    while len(frontier) > 0:

      node = frontier.pop()

      for val in graph[node]:
        if val[0] not in all_d.keys():
          all_d[val[0]] = node
          frontier.add(val[0])

  return all_d
  
   # return bfs_helper_d(visited, frontier, 0, all_d)
   
  """
  def bfs_helper_d(visited, frontier, current_d, all_d):
        if len(frontier) == 0:
          return all_d
        else:
          new_visit = visited | frontier
        
          for ed in new_visit - visited:
            all_d[ed] = current_d

          visited = new_visit
          #frontier_neigh = set()
          frontier_neigh = reduce(set.union, [graph[n] for n in frontier])
          frontier = set(frontier_neigh) - visited
          return bfs_helper_d(visited, frontier, current_d + 1, all_d)

    all_d = dict()
    visited = set()
    frontier = set([source])
    return bfs_helper_d(visited, frontier, 0, all_d)
 

  """

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    my_return = ""
    if destination in parents:
      return get_path(parents,parents[destination]) + parents[destination]
    else:
      return my_return


    # this is currently returning sbacd, not sbc
    # need to determine how to isolate the necessary values
  
  
    #pass

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'




"""""
Extra ideas for bfs

 Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
  def bfs_helper(visited, frontier):
    if len(frontier) == 0:
          return visited
    else:
          node = frontier.popleft()
          visited.add(node)
          frontier.extend(filter(lambda n: n not in visited, graph[node]))
          return bfs_helper(visited, frontier)


  frontier = deque()
  frontier.append(source)
  visited = set()
  return bfs_helper(visited, frontier)

  """

  