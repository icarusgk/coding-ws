family = {  
  uncles: ["bob", "joe", "steve"],
  sisters: ["jane", "jill", "beth"],
  brothers: ["frank","rob","david"], 
  aunts: ["mary","sally","susan"]
}

family.each_key do |key| p key end
family.each_value do |value| p value end

family.each do |k, v| puts "#{k}: #{v}" end

p family.fetch :uncles

p family.key? :uncles
p family.key? :mom

p family.empty?

immediate_family = family.select do |k, v|
  k == :sisters || k == :brothers
end

arr = immediate_family.values.flatten

p arr


cat = { name: "Whiskas" }
weight = { weight: "10 lbs" }


p cat.merge weight

cat.merge! weight

p cat