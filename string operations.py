# len
text = "python"
print(len(text))


# slicing
print(text[:2:-1])

s = "PYTHONPROGRAMMING"
print(s[2:15:3])
s = "datascience"
print(s[-1:-10:-2])
s = "ABCDEFGHIJK"
print(s[:: -1][2:8])
s = "python_slicing_test"
print(s[7::-1])
s = "programming"
print(s[1:10][::-2])
s = "COMPLEXITY" # doubt came
print(s[3:8:2] + s[:3:-3])
s = "INTERVIEWQUESTION"
print(s[5::-1] + s[:5:-1])
s = "slicingpython"
print(s[-6:3:-1])
s = "EDGECASES"
print(s[1::2][::-1])
s = "abcdefgh"
print(s[::-2][2:5])


# concatenation
name = "gagan"
surname = " mishra"
name = name + surname
print(name)


# replication
laugh = "Haha "
print(laugh * 10)
