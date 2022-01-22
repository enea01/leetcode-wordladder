class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(wordList) < 1: return 0
            
        graph_list = self.make_graph(wordList + [beginWord])
        if endWord not in graph_list:
            return 0
        steps = self.bfs(graph_list, beginWord, endWord)
        return steps
    
    def make_graph(self,list):
        graph = {}
        graph_list = {}
        for word in list:
            graph_list[word] = []
            for index in range(1,len(word) - 1):
                suba = word[:index]
                subb = word[index + 1:]
                self.append_sub_to_graph(graph, suba, subb, word)
            self.append_sub_to_graph(graph, '', word[1:], word)
            self.append_sub_to_graph(graph, word[:-1], '', word)
        for i in graph:
            for j in graph[i]:
                connected_words = graph[i][j]
                sub_list = {}
                for k in range(len(connected_words)):
                    x = connected_words.pop(0)
                    graph_list[x] = graph_list[x] + connected_words
                    connected_words.append(x)
        return graph_list
                
                
                
            

        
    def append_sub_to_graph(self,graph, suba, subb, word):
        if suba in graph and subb in graph[suba]:
            graph[suba][subb].append(word)
        elif suba in graph and subb not in graph[suba]:
            graph[suba][subb] = [word]
        else:
            graph[suba] = {}
            graph[suba][subb] = [word]
                
    def bfs(self, dic_graph, start, end):
        nexts = [start]
        daddy = {}
        daddy[start] = 'no daddy'
        found = False
        while len(nexts) > 0:
            current = nexts.pop(0)
            if current == end:
                found = True
                break
            for j in dic_graph[current]:
                if j not in daddy:
                    nexts.append(j)
                    daddy[j] = current
        if not found:
            return 0
        current = end
        steps = 1
        while current != start:
            steps += 1
            current = daddy[current]
        return steps
            
                    
                
