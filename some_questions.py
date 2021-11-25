def DFS(graph, node, visited):
    """
    Running a graph using DFS
    :param graph: the graph
    :param node: current node to running from
    :param visited: array of true/false to indicate if we visit in the graph
    """
    visited[node] = True
    for i in range(len(graph)):
        if graph[node][i] and not visited[i]:
            DFS(graph, i, visited)


def BFS(graph, node, visited):
    """
    Running a graph using BFS
    :param graph: the graph
    :param node: current node to running from
    :param visited: array of true/false to indicate if we visit in the graph
    """
    visited[node] = True
    queue = []
    queue.append(node)
    while queue:
        u = queue.pop(0)
        for i, item in enumerate(graph[u]):
            if not visited[i] and item == 1:
                visited[i] = True
                queue.append(i)


def can_visit_all_rooms(rooms):
    """
    (from leetCode)
    There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
    Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

    When you visit a room, you may find a set of distinct keys in it.
    Each key has a number on it, denoting which room it unlocks,
    and you can take all of them with you to unlock the other rooms.

    Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
    return true if you can visit all the rooms, or false otherwise.

    example 1:
        Input: rooms = [[1],[2],[3],[]]
        Output: true
        Explanation:
            We visit room 0 and pick up key 1.
            We then visit room 1 and pick up key 2.
            We then visit room 2 and pick up key 3.
            We then visit room 3.
            Since we were able to visit every room, we return true.

    example 2:
        Input: rooms = [[1,3],[3,0,1],[2],[0]]
        Output: false
        Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

    in my solution I use in BFS method

    """
    visit = [False] * len(rooms)
    queue = [0]
    keys = set()
    while len(queue) > 0:
        u = queue.pop(0)
        keys.add(u)
        if len(keys) == len(rooms):
            return True
        for key in rooms[u]:
            if not visit[key]:
                visit[key] = True
                queue.append(key)
    return False


def findCircleNum(isConnected):
    """
    (from leetCode)
    There are n cities. Some of them are connected, while some are not.
    If city a is connected directly with city b, and city b is connected directly with city c,
    then city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cities and no other cities outside of the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
    connected, and isConnected[i][j] = 0 otherwise.

    Return the total number of provinces.

    example 1:
        Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        Output: 2

    example 2:
        Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        Output: 3

    in my solution I use in BFS method
    """
    for i in range(len(isConnected)):
        for j in range(len(isConnected)):
            if isConnected[i][j]:
                isConnected[j][i] = isConnected[i][j]
    c = 0
    visit = [False] * len(isConnected)
    for i in range(len(isConnected)):
        if not visit[i]:
            c += 1
            BFS(isConnected, i, visit)
    return c

def clocke_angle(time):
    """
    The angle between the hour hand and the minute hand
    :param time: A string that represent a time for example 06:17
    """
    split_time = time.split(":")
    hour = int(split_time[0])
    minute = int(split_time[1])
    minute_angle = 360 * minute/60
    hour_angle = 360 * (hour % 12) / 12 + 360 * (minute/60) * 1/12
    angle = (hour_angle - minute_angle) % 360
    return 360 - angle



