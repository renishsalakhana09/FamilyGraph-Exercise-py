#importing csv (common separated values)
import csv
 
#1.display 1st people csv file:
 
def read_people_csv():
    with open("people(1).csv",'r') as obj:
        fobj = csv.reader(obj)
        for item in fobj:
            print (item)
			

#2.display 2nd relationships csv file:
def read_relationship_csv():
    with open("relationships.csv",'r') as obj:
        fobj = csv.reader(obj)
        for item in fobj:
            print (item)

#3.display the total relationship with each other

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
        
        
#4.display the family relations of the member

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
        
        		
		
