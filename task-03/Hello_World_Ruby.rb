num = gets.strip.to_i

if num <= 1
    exit
end

puts 2
for i in 2..num do
    for j in 2..i do
        if i%j == 0
            break
        else
            puts i
            break
        end
    end
end