"""
입력 조건
1) 1 <= 노드 N/K, 간선 M <= 100
2) 공백으로 구분
3) 연결된 두 회사(노드)가 공백으로 구분
출력 조건
1) A->K->X 최소 이동 시간 출력
2) X번 회사에 도달할 수 없다면 -1 출력
"""


n, m = map(int, input().split())
INF = int(1e9)
graph = [ [INF] * (n+1) for _ in range(n+1) ]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
x, k = map(int, input().split())
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


distance = graph[1][k] + graph[k][x]

if distance == INF:
    distance = -1
    print(distance)
else:
    print(distance)
print()