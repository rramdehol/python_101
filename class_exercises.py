class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = [];
        self.greet_counter = 0;
    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
    	self.greet_counter += 1;
    def print_info(self):
    	print "The persons info is" + ' ' +self.name + ' ' +self.email + ' ' +self.phone
    def add_friend(self, friend):
    	self.friends.append(friend);
    def num_friends(self):
    	print len(self.friends);
    def greet_count(self):
    	print str(self.greet_counter);
	def __repr__(self):
    	print '%r %r %r' % (self.name, self.email, self.phone)





Sonny = Person("Sonny", 'sonny@hotmail.com', '483-485-4948');
print vars(Sonny);
Jordan = Person("Jordan", 'jordan@aol.com', '495-586-3456');
print vars(Jordan);
# print Sonny.greet(Jordan);
print Jordan.greet(Sonny);
print Jordan.greet(Sonny);
print Jordan.greet_count();
# print Sonny.email +" "+ Sonny.phone;
# print Jordan.email +" "+ Jordan.phone;
# print Sonny.print_info();
# Jordan.add_friend(Sonny);
# print vars(Jordan);
# print Jordan.num_friends();
# print Jordan.greet_count();


# class Vehicle(object):
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_info(self):
#     	print "The car is" + ' ' +str(self.year) + ' ' +self.make + ' ' +self.model
# Car1 = Vehicle("Nissan","Leaf",2015);
# print vars(Car1);
# print Car1.print_info();
# print 
print Jordan;

