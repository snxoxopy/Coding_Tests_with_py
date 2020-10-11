"""
2020-10-11
Floyd-Warshall Algorithm
O(N^3)
"""

n, m = map(int, input().split())
INF = int(1e9)

#1. 2차원 그래프 선언, 무한 값으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

#2. 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#3. 간선 정보를 입력 받아 그래프 값을 비용으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

#4. 최단 거리 테이블 갱신
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b], end=" ")
    print()