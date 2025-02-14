a, b = gets.split.map(&:to_i)


def gcd(a, b)
  return b if a % b == 0
  return gcd(b, a % b)  
end

puts gcd(a, b)
puts a * b / gcd(a, b)