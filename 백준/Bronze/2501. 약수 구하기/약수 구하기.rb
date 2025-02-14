a, b = gets.split.map(&:to_i)
arr = []

(1..a + 1).each do |i|
    if a % i == 0
        arr << i
    end
end

if arr.length >= b
    puts arr[b-1]
else
    puts 0
end