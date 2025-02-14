t = gets.chomp.to_i

t.times do
  x = gets.chomp.to_i
  s = ""
  
  while x > 1
    if x % 2 == 0
      s = "0" + s
    else
      s = "1" + s
    end

    x = x / 2
  end

  if x == 1
    s = "1" + s
  else
    s = "0" + s
  end
  
  arr = []
  (s.length - 1).downto(0) do |i|
    if s[i] == "1"
      arr << (i - s.length + 1).abs
    end
  end
  
  puts arr.join(" ")
end
