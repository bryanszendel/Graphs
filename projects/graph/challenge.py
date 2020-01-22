"""
  Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
  Only one letter can be changed at a time.

  Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

  Note: Return None if there is no such transformation sequence.

  All words contain only lowercase alphabetic characters.
  You may assume no duplicates in the word list.
  You may assume begin_word and end_word are non-empty and are not the same.

  Sample:
  begin_word = "hit"
  end_word = "cog"
  return: ['hit', 'hot', 'cot', 'cog']
  begin_word = "sail"
  end_word = "boat"
  ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
  beginWord = "hungry"
  endWord = "happy"
  None
"""

from graph import Graph
import time
f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()
def shortest_transformation(word1, word2):
    if len(word1) != len(word2):
        raise Exception("Word lengths not equal")
    possibilities = [word.lower() for word in words if len(word) == len(word1)]
    graph = Graph()
    for word in possibilities:
        graph.add_vertex(word)
    for word in possibilities:
        for comparator in possibilities:
            distance = 0
            for i in range(len(word)):
                if word[i] == comparator[i]:
                    distance += 1
            if distance == len(word) - 1:
                graph.add_edge(word, comparator)
    return graph.bfs(word1, word2)
start_time = time.time()
print(shortest_transformation('hit', 'cog'))
end_time = time.time()
print("Time elapsed for 'hit' and 'cog':", end_time - start_time)
start_time = time.time()
print(shortest_transformation('sail', 'boat'))
end_time = time.time()
print("\nTime elapsed for 'sail' and 'boat':", end_time - start_time)