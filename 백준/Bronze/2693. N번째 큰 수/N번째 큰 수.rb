t = gets.chomp.to_i

(1..t).each {|_|
  arr = gets.chomp.split.map(&:to_i)
  arr.sort!.reverse!
  puts arr[2]
}
