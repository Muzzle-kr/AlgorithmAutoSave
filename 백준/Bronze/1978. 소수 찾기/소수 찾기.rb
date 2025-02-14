# 4
# 1 3 5 7
# 3

def prime_number?(number)
  return false if number == 1

  (2..(number**0.5).to_i).each { |i| return false if (number % i).zero? }

  true
end

n = gets.chomp.to_i
arr = gets.split.map(&:to_i)

count = 0
arr.each { |a| count += 1 if prime_number?(a) }
puts count
