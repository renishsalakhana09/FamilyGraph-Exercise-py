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
#Exercise-2
> *Validate correct people loaded Write a test to validate that you have loaded the expected number of people.*

            
            
            
