class Person:
    def __init__(self,name,age,id):
        
        """
        Constructor for Person class.
        :param name: Name of the person (string)
        :param age: Age of the person (integer)
        :param id: ID of the person (string or integer)
        """
        self.name = name
        self.id = id
        self.age = age
    
    def __str__(self):
        
        """
        Return a string representation of the Person object.
        :return: A string containing person's name, age, and ID"objec
        """

        return f"Name : {self.name}, Age : {self.age}, Student Number : {self.id}"

