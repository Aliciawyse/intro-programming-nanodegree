#Let python know we're creating a class. 
#Pet indicates the name of the class. 
#Object is the class that pet is inheriting from.
class Pet(object):
    
    #Create a new pet & specify its name and species. 
    #Accomplish this using the init function which is called 
    #when an instance of a class is first created. 
    
    #self VARIABLE is the instance of the class. 
    #Values in an instance vary, instance to instance; therefore, 
    #we want to specify that our instance has different values in it 
    #than some other instance -- hence self.name = name NOT pet.name = name.
    
    #every function inside a class has to take self as its first parameter
    
    def __init__(self, name, species):
        self.name = name 
        self.species = species 
    
    #
    def getName(self):
        return self.name
        
    def getSpecies(self):
        return self.species
    
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

#Call the method by passing in two values. No self parameter needed. 
#Why? When you call a method of an instance, python figures out
#what self should be and passes it to the function.
polly = Pet("Polly", "Parrot")

print polly