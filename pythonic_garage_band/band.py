from abc import abstractclassmethod

class Musician:


    arrayOfNum = []



    def __init__(self, n) :


          self.name = n
        

          Musician.arrayOfNum.append(self)


    @abstractclassmethod


    def __str__(self) :



             pass

    @abstractclassmethod


    def __repr__(self):

             pass


    @abstractclassmethod


    def get_instrument(self):

           pass

    @abstractclassmethod


    def play_solo(self):

        pass

class Band:

    def __init__(self,n,mem,i=''):

          self.name=n

          self.members=mem

    def play_solo(self) :

        return self.i

class Guitarist(Band) :

    def __init__(self,n,val='') :

        self.name=n

    def __str__(self):


        return f"My name is {self.name} and I play guitar"

    def __repr__(self) :


        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self) :


        return "guitar"

class Drummer(Band) :


    def __init__(self,n,val='rattle boom crash'):

           self.name=n

    def __str__(self):


           return f"My name is {self.name} and I play drums"

    def __repr__(self):
 
           return f"Drummer instance. Name = {self.name}"


    def get_instrument(self):


        return "drums"



class Bassist(Band):

    def __init__(self,n,i='bom bom buh bom'):

        self.name=n

    def __str__(self):

       return f"My name is {self.name} and I play bass"

    def __repr__(self):

        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):

        return "bass"