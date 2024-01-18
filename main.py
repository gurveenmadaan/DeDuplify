from linkedlist import LinkedList #Imports the LinkedList class from the linkedlist.py module.
from hash import HashSet #Imports the HashSet class from the hash.py module.
from readfile import read_data #Imports the read_data function from the readfile.py module.

def remove_duplicates(data): #takes a list as input
    size = len(data) #calculates the size of the input data list
    unique_set = HashSet(size)  #creates an instance of the HashSet class named unique_set with that size.

    for item in data: #iterates through the input data and adds each item 
        unique_set.add(item)
    
    unique_set.remove_dupes()

    dedupdata = []
    for linkedlist in unique_set.buckets: #calls the remove_duplicates method on the unique_set, which in turn calls the remove_dupes method for each linked list inside the set's buckets.
        if linkedlist:
            current = linkedlist.head
            while current:
                dedupdata.append(current.data) #constructs a new list dedupdata containing the deduplicated data from the linked lists in the unique_set
                current = current.next
    
    return dedupdata

if __name__ == "__main__":
    data1 = "data1.txt"
    data2 = "data2.txt"
    
    data1 = read_data(data1)
    data2 = read_data(data2)
    
    print("Data from", data1, ":", data1)
    print("Data from", data2, ":", data2)
    
    combined_data = data1 + data2
    
    dedupdata = remove_duplicates(combined_data)
    #reads data from two files, combines the data into a single list, removes duplicates, and then prints the original data from both files, the combined data, and the deduplicated data.
    
    print("\nData after removing duplicates:")
    print(dedupdata)
    #deduplicated data is printed, show the data after duplicates have been removed.