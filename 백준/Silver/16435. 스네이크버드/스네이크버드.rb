n, l = gets.chomp.split.map(&:to_i)
arr = gets.split.map(&:to_i)
arr.sort!

arr.each do |fruit|
    l += 1 if l >= fruit
end

puts l