fibonacci = [0, 1]

for i in 2..20 do
  fibonacci << fibonacci[i-1] + fibonacci[i-2]
end

n = gets.chomp.to_i
puts fibonacci[n]