
#Class is defined as Dolphin that has two functions associated with it, one for swimming and one for being awesome.
class Dolphin:
    def swim(self):
        print("The Dolphin is swimming.")
        
    def be_awesome(self):
        print("The Dolphin is being awesome.")

        
def main():
    #We'll make a Dolphin object called nebula
    nebula = Dolphin()
    #Calls the swim function
    nebula.swim()
    #Calls the awesome function
    nebula.be_awesome()
 
 #The object nebula calls the two methods in the main function of the program, causing those methods to run.   
if __name__ == "__main__":
    main()