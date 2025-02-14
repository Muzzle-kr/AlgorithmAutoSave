def prime_number?(n)
  return false if n == 1 

  (2..Math.sqrt(n).to_i).each do |i|
    return false if (n % i).zero?
  end

  true
end
n = gets.chomp.to_i
m = gets.chomp.to_i


min_prime_number = nil
total_prime_number = 0

(n..m).each do |x|
  if prime_number?(x)
    min_prime_number ||= x
    total_prime_number += x
  end
end

if total_prime_number.zero?
  puts -1
else
  puts total_prime_number
  puts min_prime_number
end
