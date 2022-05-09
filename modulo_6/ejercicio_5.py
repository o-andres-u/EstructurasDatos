import heapq

song_duration = int(input())
tones = int(input())
song = []
heapq.heapify(song)
for tone in range(tones):
    values = list(map(int, input().split()))
    code = values[0]
    initial = values[1]
    frequency = values[2]
    heapq.heappush(song, (initial, frequency))
turn = heapq.heappop(song)
time = turn[0]
while song_duration >= time:
    print(time)
    heapq.heappush(song, (turn[0] + turn[1], turn[1]))
    turn = heapq.heappop(song)
    time = turn[0]
