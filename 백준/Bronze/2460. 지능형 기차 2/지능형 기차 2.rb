max_num = 0
current_num = 0

(0...10).each do
  a, b = gets.chomp.split.map(&:to_i)
  current_num -= a
  current_num += b
  max_num = [max_num, current_num].max
end

puts max_num