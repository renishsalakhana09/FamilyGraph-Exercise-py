# FamilyGraph-Exercise-py
- Building a graph of people, and their relationships with each other 
- For Detail Explanation of Problem please refer pdf attached <button>
    <a href="README.pdf"> Go to </a>
</button>

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
            
            
            
