import sys

input = sys.stdin.readline
def main():
    inf = 0x3f3f3f3f
    n, m, k = map(int, input().split())
    edges, dist, backup= [], [inf] * (n + 10), [inf] * (n + 10)
    
    for i in range(m):
        a, b, c = map(int, input().split())
        edges[i] = (a, b, c)
    
    def Bellmford():
        dist[1] = 0
        for i in range(k):
            backup = dist[0:n + 1]
            for a, b, c in edges:
                if dist[b] > backup[a] + c:
                    dist[b] = backup[a] + c

        if dist[n] > inf / 2:
            print('impossible')
        else:
            print(dist[n])
    
    

    Bellmford()


    return 


if __name__ == '__main__':
    main()