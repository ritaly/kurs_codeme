class Person:
    school = 'SecondarySchoolPoznan'

    def __init__(self, name, twitter, facebook, followers):
        self.name = name
        self.twitter = twitter
        self.facebook = facebook
        self.followers = followers

    def instagram(self):
        insta = '@' + self.name + self.school
        insta = insta.lower()
        return insta


marta = Person('Marta', '@martatw', '@martafb', 1000)

# print(Person.instagram(marta))


age = 30
print(type(age))
w = 60.1
print(type(w))

welcome = 'Hello World!'
print(type(welcome))

print(welcome.lower())

print(str.upper(welcome))