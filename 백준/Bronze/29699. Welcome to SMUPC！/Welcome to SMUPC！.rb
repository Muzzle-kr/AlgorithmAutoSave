n = gets.chomp.to_i
string = "WelcomeToSMUPC"

idx = n % string.length
puts string[idx-1]