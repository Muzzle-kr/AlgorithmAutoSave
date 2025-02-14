n = gets.chomp.to_i
map = gets.chomp.split.map(&:to_i)

puts "%d %d" % [map.min, map.max]