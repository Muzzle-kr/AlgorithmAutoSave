arr = []
(1..100).each { |i| i.times.each { |_| arr << i } }

n, m = gets.chomp.split.map(&:to_i)
answer = 0

(n..m).each { |i| answer += arr[i-1] }
puts answer
