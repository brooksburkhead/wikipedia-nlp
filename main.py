from modules.search import search_name
from modules.knn_similar_persons import find_similar_people

def main() -> None:
    print("Welcome to my interactive NLP tool!\n")
    print("You can use this tool to search for people in the dbpedia dataset, and find the 10 most similar people!")
    
    while True:       
        print("\nWhat would you like to do?")
        print("1. Search for a person")
        print("2. Find similar people to a person")
        print("3. Exit")
        
        choice = input("\nEnter the number of your choice: ")
      
        if choice == '1':
            name = input("\nEnter the name to search for: ")
            results = search_name(name)
            print(results)
            
        elif choice == '2':
            index = int(input("\nEnter the index of the person: "))
#            print(f"\nFinding similar people to {dbpedia_data.iloc[index]['name']}... \n")
            find_similar_people(index)
            
        elif choice == '3':
            print("\nGoodbye!\n")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
    return None


if __name__ == "__main__":
    main()
