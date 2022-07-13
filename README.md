# FamilyGraph-Exercise-py
- Building a graph of people, and their relationships with each other 
- For Detail Explanation of Problem please refer pdf attached <button>
    <a href="README.pdf"> Go to </a>
</button>

> Exercise is completed in `Python` only 
> 
> [![N|Solid](https://user-images.githubusercontent.com/104903815/178705703-b8842343-cded-4e49-be09-933d13e4e618.png)


# importing csv module

```python
import csv
```
# Display the 1st people csv file 

```python
 def read_people_csv():
    with open("people(1).csv",'r') as obj:
        fobj = csv.reader(obj)
        for item in fobj:
            print (item)
```            
            
            
            
