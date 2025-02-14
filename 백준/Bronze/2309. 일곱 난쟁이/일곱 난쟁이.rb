def bt (idx, man, height, arr, answer)
  return if man > 7

  if height == 100 && man == 7
    answer.sort_by! { |x| x }.each { |x| puts x}
    exit(0)
  end

  return if idx == 9

  bt(idx+1, man, height, arr, answer)
  bt(idx+1, man + 1, height + arr[idx], arr, answer + [arr[idx]])
end

arr = []

for i in 1...10
  arr << gets.chomp.to_i
end


bt(0, 0, 0, arr, [])