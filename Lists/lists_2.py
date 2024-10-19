diller = ["python","C#","JAVA","JavaScript"]

sonuc = diller

print(sonuc) # ['python', 'C#', 'JAVA', 'JavaScript']

print(sonuc[0]) # python

print(sonuc[:3]) # ['python', 'C#', 'JAVA']

print(sonuc[-1]) # JavaScript

print(sonuc[-4:-1]) # ['python', 'C#', 'JAVA']


diller[0] = "HTML"
print(diller) # ['HTML', 'C#', 'JAVA', 'JavaScript']

print(len(diller)) # 4

sonuc = diller + ["angular","vueJs"]
print(sonuc) # ['HTML', 'C#', 'JAVA', 'JavaScript', 'angular', 'vueJs']

#if blocks
if "python" in diller:
    print("python liste içinde var.") 
else:
    print("python içinde yok")

    
#loops (for)
for i in range(len(diller)):
    print(diller[i]) 

del diller[0]
print(diller) # ['C#', 'JAVA', 'JavaScript']




