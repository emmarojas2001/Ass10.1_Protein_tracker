#Assignment 10.1
#Emmanuel Rojas
#CSE-20 MWF
#Professor Hari
#Dec 3, 2021

"""The purpose of this program is to create a class that models an real-world object. 
I have chosen a protein bag, since I use that daily."""

# This is the class that will represent my real-world object, the protein bag(s).
class ProteinBag:
    # This is a class variable that will be accessed by every object in the class.
    protein_g=24
    # This function will initialize the Class ProteinBag, it will take in an argument. The argument is a dictionary,
    # the name of the protein bag will be the key and the amount of scoops in the protein bag will be the value.
    def __init__(self, protein_dict=None):
        if protein_dict is None:
            # create a dictionary
            self.protein_bags = {}
        # The code will create a dictionary which will contain the protein bag as the key and the amount of scoops in the protein bag as the value.
        else: 
            self.protein_bags = {}
            # For the two elements in the original dictionary, protein_dict, the code will get the keys and values and store them inside a new 
            # dictionary, "self.protein_bags"
            for bag_name, servings in protein_dict.items():
                self.protein_bags[bag_name.lower()] = servings
        # the code will then set the number of scoops in each protein bag
        self.set_scoops()
    # This function will set the number of scoops in each protein bag
    def set_scoops(self):
        # This empty dictionary will hold the brand names and the number of scoops as keys and values, respectively.
        self.setscoops={}
        for name, count in zip(self.protein_bags.keys(), self.protein_bags.values()):
            self.setscoops[name] = count
        
    # This function will return the dictionary that holds the brand names and the number of scoops
    def get_scoops(self):
        return (f"{self.setscoops}")

    # This function will sum and return the total number of scoops in all of the protein bags together
    def get_totalscoops_left(self):
        # this variable will hold the sum of all the values inside the self.protein_bags dictionary
        string=sum(list(self.protein_bags.values()))
        return (f"{string}")
    
    # This function will take in two arguments and will subtract a number of scoops from a certain protein bag
    def take_scoop(self, bag, scoops):
        # this variable will be available to all other functions, it is the number of scoops subtracted
        self.scoops = scoops
        # this variable is only available to this specific function
        x=bag.lower()
        # if the bag name is in dictionary then the number of scoops will be subtracted from the value of the bag
        if x in self.protein_bags.keys():
            self.protein_bags[x] -= self.scoops
            if self.protein_bags[x]<=0:
                del self.protein_bags[x]
            self.set_scoops()
            print(self.get_protein_grams())
        # If the bag name is not in dictionary then this error message will print
        else:
            print("You cannot take scoops from a bag that doesn't exist silly goose.")
    
    # This function will take in two arguments and will add a number of scoops to a certain protein bag
    def add_scoop(self, bag, scoops):
        # This data variable will only be used in this function and is private
        self.__x=bag.lower()
        # If the bag exists in dictionary then the scoop will be added to the protein bag, else, the protein bag will be created 
        if self.__x in self.protein_bags.keys():
            self.protein_bags[self.__x] += scoops
        else:   
            self.protein_bags[self.__x]=scoops
        self.set_scoops()
    # This function will find the protein inside the scoops being taken and will store that value inside a private data variable
    def get_protein_grams(self):
        # This data variable will only be used in this function and will be used to hold the grams of protein inside of desired scoops
        self.__protein_in_scoops=self.scoops*self.protein_g
        return(f"{self.__protein_in_scoops}g of Protein in {self.scoops} scoops")
# This is the main function that will create the shell
def main():
    # Welcome greet and an empty dictionary that will hold the protein bag inventory
    print(f"Welcome to Protein Tracker. Possible commands are 'add list', 'add', 'take', 'total left', 'total of each', 'help', and 'exit'. ")
    # Pass the empty dictionary through Class ProteinBag
    dictionary={}
    # Create object Protein with argument "dictionary"
    protein=ProteinBag(dictionary)
    # Create a loop to create the shell
    while True:
        print("Protein Tracker...")
        # Ask the user for an input
        command=input("<<<")
        # If input is equal to one of these commands then execute the certain process
        if command == "add list":
            print("Possible commands are 'add' and 'done'. Enter 'add' if you would like to continue to add the list. Enter 'done' if you are done adding to the list.")
            while True:
                print("Protein Adder...")
                second_command=input("<<<<")
                if second_command == "add":
                    protein_add=str(input("Protein Name: "))
                    protein_amount_add=int(input("Amount of Scoops: "))
                    # Add the user's protein brands and scoops into the dictionary
                    dictionary[protein_add]= protein_amount_add
                    
                elif second_command == "done":
                    protein.__init__(dictionary)
                    print("Going back...")
                    break
                else:
                    print("Invalid Command. Try again.")

        elif command == "add":
            user_protein_add=str(input("Which protein do you want to add to: "))
            user_amount_add=int(input("How much are you adding to this protein: "))
            # Pass user inputs through the "add_scoop" method
            protein.add_scoop(user_protein_add, user_amount_add)
        elif command == "take":
            user_protein=str(input("Which protein do you want to take from: "))
            user_amount=int(input("How much are you taking from this protein: "))
            # Pass user inputs through the "take_scoop" method
            protein.take_scoop(user_protein, user_amount) 
        elif command == "total left":
            # Call the "get_totalscoops_left" method and return the total scoops left in all the bags
            print(f"{protein.get_totalscoops_left()} scoops left")
        elif command == "total of each":
            # Call the "get_scoops" method and return the dictionary of the protein bags and the scoops
            print(protein.get_scoops())
        elif command == "help":
            print("Possible commands are: 'add list', 'add', 'take', 'total left', 'total of each', 'help', and 'exit'.\n Enter 'add list' to add to the protein bags available, enter 'add' to add to a specific protein bag, enter 'take' to take fromo a specific protein bag, enter 'total left' to see how many total scoops are left, enter 'total of each' to see how many scoops each protein there are left, and enter 'exit' to close Protein Tracker.")
        elif command == "exit":
            print("Closing Protein Tracker, goodbye!")
            # Break the while loop, closing the shell, and ending the program
            break
        else:
            print("Invalid Command. Try again.")

# Run the main code and run the program
if __name__=="__main__":
    main()