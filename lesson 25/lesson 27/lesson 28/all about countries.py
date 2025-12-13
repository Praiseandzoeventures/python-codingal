class India():

    def capital(self):
        print("New delhi is capital of india")    
    def language(self):

        print("hindi is the most widely spoken language")

    def type(self):

        print("India is a developinf country")

class USA():

    def capital(self):

        print("Washington DC is capital of USA")

    def language(self):

        print("english is the most widely spoken language")

    def type(self):

        print("USA is a developed country")


obji = India()

obju = USA()

for country in (obji , obju):

    country.capital()

    country.language()

    country.type()