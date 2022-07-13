# FamilyGraph-Exercise-py
- Building a graph of people, and their relationships with each other 
- For Detail Explanation of Problem please refer pdf attached <button>
    <a href="README.pdf"> Go to </a>
</button>

> Exercise is completed in `Python` only 
> 
> [![N|Solid](https://user-images.githubusercontent.com/104903815/178705703-b8842343-cded-4e49-be09-933d13e4e618.png)


# Exercise-1
> *Please implement code and data structures that read the files:*
> *and use them to build an in-memory data structure that represents the people in the file and their relationships with each other.*

Create necessary python function

> *importing the `csv` module's*

```python
import csv
```
> *`def read_people_csv` for display the people csv file:*
> 
> *`def read_relationships_csv` for display the relationships csv file:*
> 
```python
 def read_people_csv():
    with open("people(1).csv",'r') as obj:
        fobj = csv.reader(obj)
        for item in fobj:
            print (item)
```

```python
def read_relationship_csv():
    with open("relationships.csv",'r') as obj:
        fobj = csv.reader(obj)
        for item in fobj:
            print (item)
```
# Exercise-2
> *Validate correct people loaded Write a test to validate that you have loaded the expected number of people.*

```python
for person in people:
            for relation in relationship:
                if person[1] == relation[0]: 
                    name = relation[2]
                    name2 = name[0: + name.index('@')]
                
                    print(person[0].lower() + " & " + str(name2) + " are " + relation[1])
```
# Exercise 3 - Validate correct relationships loaded
>*Write a test to validate that the following people have the correct expected number of connections to other people*
>
>- *Bob (4 relationships)*
>- *Jenny (3 relationships)*
>- *Nigel (2 relationships)*
>- *Alan (0 relationships)*

```python
print("-----------Display the total relationship with each other------------")
def show_total_relations():
    with open('people(1).csv') as people_file, open('relationships.csv') as relative_file:
        
        people = list(csv.reader(people_file,delimiter=','))   #making list of people.csv file
    
        relationship = list(csv.reader(relative_file,delimiter=',')) #making list of relationship.csv file
        
        #Making lists  
        
        person_name_list1 = list()
        
    
        #to show the relationships of all people's with each others with validated excepted numbers of people's:
        
        for person in people:
            for relation in relationship:
                if person[1] == relation[0]: 
                    name = relation[2]
                    name2 = name[0: + name.index('@')]
                
                    print(person[0].lower() + " & " + str(name2) + " are " + relation[1]) 
            
         for person in people:
            for relation in relationship:
                if person[1] == relation[0]:
                    name = relation[2]
                    name2 = name[0: + name.index('@')]
                    person_name_list1.append(str(name2))
                    
         for person in people:
            for relation in relationship:
                if person[1] == relation[0]:
                    person_name_list1.append(person[0].lower())
                    
        print("\n") 
        print("---List of names of people's and Relationships---")
        print(person_name_list1)
    
        total_member_list = {}
        
        for i in person_name_list1:
            if i in total_member_list:
                total_member_list[i] = total_member_list[i] + 1
            else:
                total_member_list[i] = 1
                
        
        k= 'alan'
        for i in person_name_list1:
            total_member_list[k] = 0
                
                
        total_people_relation =  total_member_list.items()
        print("\n")
        print("--- 3rd Exercise Solution --- :\nTotal relations of people's with each others and Validated correct relationships loaded---")
        print("\n")
        print(total_people_relation)
		
```

            
            
            
