                 ###               DICTIONARY AND SETS :                  ####

dict={
    "name": "Ramkiran",
    "CGPA": 9.6,
    "marks": 59,
    }
print(dict)
print(type(dict))

NESTED DICTIONARY :

student={
    "name": "Ramkiran",
    "age": 20,
    "subjects":{
        "phy":97,
        "chem":99,
        "maths":100,
    }
}
print(student)
print(student["subjects"]["chem"])



DICTIONARY METHODS :

1) mydict.keys() #returns all keys :

student={
    "name": "Ramkiran",
    "age": 20,
    "subjects":{
        "phy":97,
        "chem":99,
        "maths":100,
    }
}
print(list(student.keys()))

2) mydict.values() #returns all values :

student={
    "name": "Ramkiran",
    "age": 20,
    "subjects":{
        "phy":97,
        "chem":99,
        "maths":100,
    }
}
# print(student.values())
print(list(student.values()))

3) mydict.items() #returns all (key,val) pairs as tuples :

student={
    "name": "Ramkiran",
    "age": 20,
    "subjects":{
        "phy":97,
        "chem":99,
        "maths":100,
    }
}
print(student.items())
print(list(student.items()))

4) mydict.get("keys") #returns the key according to the values :

student={
    "name": "Ramkiran",
    "CGPA": 9.6,
    "marks": 59,
    }
print(student.get("name"))
print(student.get("CGPA"))
print(student.get("marks"))
print(list(student.keys()))

5) mydict.update(new dict) #insert the specified items to the dictionary :

student={
    "name": "Ramkiran",
    "CGPA": 9.6,
    "marks": 59,
    }
students=student.update()
print(students)




   SETS  :

collection={1,2,3,4,3,2,4,5,}
print(collection)

For empty set we use :

collection=set()
print(collection)
print(type(collection))


SETS METHODS :

1) set.add(elements) # adds the elements :

collection=set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("Ramkiran")
collection.add("java Developer")

print(list(collection))

2) set.remove(elements) # removes the elements :

collection={1,2,3,4,5,6,7,1,2}
collection.add(10)
print(collection)
collection.remove(1)
print(collection)

3) set.clear() # empites the set :

collection={1,2,3,4,5,2,3,4,5,3,4,5,4,5,5}
print(collection)
collection.clear()
print(collection)
collection.add(1)
collection.add("Ramkiran")
collection.add("Java Developer")
print(collection)

4) set.pop() # removes the random values :

collection={1,2,3,4,5,2,3,4,5,3,4,5,4,5,5}
print(collection)
collection.clear()
print(collection)
collection.add(1)
collection.add("Ramkiran")
collection.add("Java Developer")
print(collection)
collection.pop()
print(collection)

5) set.union(set2) #combines both set values and return new :

collection={1,2,3,4,5,2,3,4,5,3,4,5,4,5,5}
set2= {1,3,5,10,11,12,13}
set=collection.union(set2)
print(set)

6) set.intersection(set1) # combines common values and return new :

collection={1,2,3,4,5,2,3,4,5,3,4,5,4,5,5}
set2= {1,3,5,10,11,12,13}
uno=collection.union(set2)
inter=collection.intersection(set2)
print(uno)
print(inter)

PRACTICE QUESTIONS :

1) store following meaning in a python  dictionary :
table: "a piece of furniture","list of facts and figures "
cat: "a small animal."

dictonary={
    "cat": "a small animal.",
    "table":["a piece of furniture.","list of facts and figures."]
}
print(dictonary)



2) question :

subjects={
    "python","java","c++","python","java","c","c++","python"
}
print(subjects)
print(len(subjects))

3) Questions :

marks={}
x=int(input("enter phy :"))
marks.update({"phy":x})

x=int(input("enter chem :"))
marks.update({"chem":x})

x=int(input("enter maths :"))
marks.update({"maths":x})

print(marks)


Question 4 :

values={
    "float":9.0,
    "int":9
}
print(values)
