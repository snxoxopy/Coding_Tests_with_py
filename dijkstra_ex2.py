"""
2020-10-11
개선된 다익스트라 알고리즘 소스코드
Elog(V); E=간선개수, V=노드개수
"""

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
# 각 노드에 대한 리스트 생성
graph = [ [] for i in range(n+1) ]
#2. 최단 거리 테이블 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    #1. 출발 노드 설정, 큐에 삽입 (시작 노드로 가기 위한 최단 경로는 0으로 설정)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 큐가 비어있을 때까지
    while q:
        #3. 최단 거리 선택(꺼내기)
        dist, now = heapq.heappop(q)
        #3. 방문한 경우 무시
        if distance[now] < dist:
            continue
        #3.방문하지 않은 경우
        for i in graph[now]:
            #4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산
            cost = dist + i[1]
            #4. 최단 거리 테이블 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 각 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance [i] == INF:
        print("INFINITY")
    else:
        print(distance[i])