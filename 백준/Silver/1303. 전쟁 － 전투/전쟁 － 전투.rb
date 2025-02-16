m, n = gets.chomp.split.map(&:to_i)
grid = n.times.map { gets.chomp }

# 인덱스는 0부터 시작하므로, n x m 크기의 배열 생성
@visited = Array.new(n) { Array.new(m, false) }

# 인스턴스 변수에 저장해서 bfs 함수에서 접근 가능하도록 함
@n = n
@m = m
@grid = grid

# 네 방향 (오른쪽, 왼쪽, 아래, 위)
@dx = [0, 0, 1, -1]
@dy = [1, -1, 0, 0]

# BFS를 통해 시작 좌표 (i, j)와 같은 팀의 연결된 영역 크기를 반환하는 함수
def bfs(i, j)
  team = @grid[i][j]
  queue = [[i, j]]
  @visited[i][j] = true
  count = 1

  while !queue.empty?
    x, y = queue.shift   # FIFO 방식의 큐: shift로 맨 앞 요소 추출

    (0...4).each do |k|
      nx = x + @dx[k]
      ny = y + @dy[k]

      if nx >= 0 && nx < @n && ny >= 0 && ny < @m
        if !@visited[nx][ny] && @grid[nx][ny] == team
          @visited[nx][ny] = true
          queue << [nx, ny]
          count += 1
        end
      end
    end
  end

  count
end

w_power = 0
c_power = 0

# 0부터 n-1, 0부터 m-1로 순회
(0...n).each do |i|
  (0...m).each do |j|
    unless @visited[i][j]
      count = bfs(i, j)
      # 'W' 팀이면 w_power, 아니라면 ('B' 등) c_power에 더함
      if @grid[i][j] == "W"
        w_power += count ** 2
      else
        c_power += count ** 2
      end
    end
  end
end

puts "#{w_power} #{c_power}"
