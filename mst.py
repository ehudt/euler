# problem 107
# minimal network

import sys
from operator import itemgetter

class MstPrimMatrix(object):
  """Implementation of Prim's MST algorithm for adjacency matrix version.

  Based on a high-level description of this version found in
  http://lcm.csa.iisc.ernet.in/dsa/node183.html.
  """
  def __init__(self):
    super(MstPrimMatrix, self).__init__()

  @staticmethod
  def MatrixFromFile(infile_path):
    matrix = []
    with open(infile_path) as infile:
      for line in infile:
        line = line.strip('\n')
        mapping_func = lambda s: sys.maxint if s is '-' else int(s)
        row = map(mapping_func, line.split(','))
        matrix.append(row)
    return matrix

  @staticmethod
  def RunPrimsAlgorithm(matrix):
    """Run Prim's MST algorithm on the input matrix.
    
    Args:
      matrix: A list of int lists representing an adjacency matrix of a
        weighted connected graph. Each entry [i][j] in the matrix represents
        the weight of the edge between node i and node j. If 2 nodes are not
        connected, their respective edge should have weight sys.maxint
        (This condition applies to self-edges as well).
        Matrix must be of size n*n for some n.

    Return:
      Returns an adjacency matrix form of an MST, where
    """
    n = len(matrix)
    mst_edges = [[sys.maxint for i in xrange(n)] for j in xrange(n)]
    mst_nodes = [0]
    closest = [0 for i in xrange(n)]
    lowcost = [matrix[0][i] for i in xrange(n)]
    while len(mst_nodes) < n:
      next_node, weight = min(enumerate(lowcost), key=itemgetter(1))
      closest_to_next = closest[next_node]
      mst_edges[next_node][closest_to_next] = weight
      mst_edges[closest_to_next][next_node] = weight
      mst_nodes.append(next_node)
      lowcost[next_node] = sys.maxint
      for i in xrange(n):
        if i in mst_nodes: continue
        if matrix[i][next_node] < lowcost[i]:
          lowcost[i] = matrix[i][next_node]
          closest[i] = next_node
    print mst_nodes
    return mst_edges

  @staticmethod
  def GetGraphEdgeWeight(matrix):
    """Return the weight of and MST."""
    total_sum = 0
    for row in matrix:
      total_sum += sum(x for x in row if x != sys.maxint)
    return total_sum/2


matrix = MstPrimMatrix.MatrixFromFile('network.txt')
matrix_weight = MstPrimMatrix.GetGraphEdgeWeight(matrix)
mst = MstPrimMatrix.RunPrimsAlgorithm(matrix)
mst_weight = MstPrimMatrix.GetGraphEdgeWeight(mst)

print matrix_weight - mst_weight

