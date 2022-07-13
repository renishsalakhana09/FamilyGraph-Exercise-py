# FamilyGraph-Exercise-py
#### :black_square_button:Building a graph of people, and their relationships with each other  :family:
#### :black_square_button:For Detail Explanation of Problem please refer pdf attached [click Here](README.pdf)

### :arrow_forward: You will find all necessary function and code at `FamilyGraph.py` 

#### :heavy_check_mark:Exercise is completed in `Python` only

#### :heavy_check_mark:All things will run smoothly on py `jupyter notebook` to know more and steps to install jupyter notebook [click Here](https://www.geeksforgeeks.org/how-to-install-jupyter-notebook-in-windows/)


> ![image](https://user-images.githubusercontent.com/104903815/178730491-33003657-6065-449d-a792-e0add2c7470e.png = 50x50)


> `CSV files that are used in this program`

##### people.csv 

| Names     | Email         | Id |                  
| ------------- |:-------------:| -----:|
| Bob | bob@bob.com | 31 |
| Derek | derek@bob.com | 25 |
| Anna | anna@clothes.com | 25 |
| Jenny | jenny@toys.com | 52 |
| Pete | pete@timber.com | 57 |
| kerry | kerry@oilcompany.org | 29 |
| joe| joe@construction.net | 28 |
| Nigel | nigel@marketing.com | 40 |
| Amber | amber@gmail.com | 12 |
| Finn | finn@gmail.com | 15 |
| Alan | alan@lonely.org | 23 |
| Dave | dave@dentists.com | 49 |

#### relationships.csv 


| Email1    | Relation        | Email2 |                  
| ------------- |:-------------:| -----:|
| bob@bob.com | FAMILY | finn@gmail.com |
| bob@bob.com | FAMILY | amber@gmail.com |
| bob@bob.com | FAMILY | anna@clothes.com |
| anna@clothes.com | FAMILY | finn@gmail.com |
| anna@clothes.com | FAMILY | amber@gmail.com |
| amber@gmail.com | FAMILY | finn@gmail.com |
| anna@clothes.com | FRIEND | jenny@toys.com |
| jenny@toys.com | FAMILY | pete@timber.com |
| jenny@toys.com | FAMILY | kerry@oilcompany.org |
| pete@timber.com | FAMILY | kerry@oilcompany.org |
| dave@dentists.com | FAMILY | pete@timber.com |
| kerry@oilcompany.org | FRIEND | joe@construction.net |
| joe@construction.net | FAMILY | nigel@marketing.com |
| nigel@marketing.com | FRIEND | derek@bob.com |
|derek@bob.com| FRIEND | bob@bob.com |
|derek@bob.com| FRIEND | pete@timber.com |





## Exercise-1
> *:heavy_check_mark:Please implement code and data structures that read the files:*
> *and use them to build an in-memory data structure that represents the people in the file and their relationships with each other.*

Create necessary python function

> *:heavy_check_mark:importing the `csv` module's*

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
## Exercise-2
> *:heavy_check_mark:Validate correct people loaded Write a test to validate that you have loaded the expected number of people.*

```python
for person in people:
            for relation in relationship:
                if person[1] == relation[0]: 
                    name = relation[2]
                    name2 = name[0: + name.index('@')]
                
                    print(person[0].lower() + " & " + str(name2) + " are " + relation[1])
```
## Exercise 3 - Validate correct relationships loaded
>*:heavy_check_mark:Write a test to validate that the following people have the correct expected number of connections to other people*
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


## Exercise 4 - Write a method that calculates the size of the extended family :family:
>*:heavy_check_mark:Write a method which, when passed the object representing a particular person, returns an int representing the size of their extended family including themselves. Their extended family includes anyone connected to them by a chain of family relationships of any length, so your solution will need to work for arbitrarily deep extended families. It `should not count their friends` Write tests that validate this returns the correct result for the families of:*
>
>- *Jenny (4 family members)*
>- *Bob (4 family members)*

```python
def search_family_relations():
    with open('people(1).csv') as people_file, open('relationships.csv') as relative_file:
        people = list(csv.reader(people_file,delimiter=','))
        relationship = list(csv.reader(relative_file,delimiter=','))
          
        #making lists 
        family_relation_list = list()
        family_members = [];
	
        for person in people:
            for relation in relationship:
                name = relation[2]
                name2 = name[0: + name.index('@')]
                if ((person[1] == relation[0] ) and relation[1] == 'FAMILY'):
                    
                    print(person[0].lower() + " & " + str(name2) + " are " + relation[1])
		    
        for person in people:
            for relation in relationship:
                name = relation[2]
                name2 = name[0: + name.index('@')]
                if ( (person[1] == relation[0]) and relation[1] == 'FAMILY' ):
                    family_relation_list.append(person[0].lower())
                    
                    family_relation_list.append(str(name2))
                
        print("\n")
        print("---family_relation_list---")
        print(family_relation_list)    
            
        i=0
        my_relation_list = {}
        for i in family_relation_list:
            if i in my_relation_list:
                my_relation_list[i]+=1
            else:
                my_relation_list[i] = 2
                
        total_family_relation = my_relation_list.items()
        print("\n")
        print("---Total family relations---")
        print(total_family_relation)
```

            
            
            
