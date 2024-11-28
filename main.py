class Person:
    def __init__(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number
    
    def set_details(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number
    
    def get_details(self):
        print("Name: " +self.name+ ", Age: " +str(self.age)+ ", Contact Number: " +str(self.contact_number))
    
class Member(Person):
    def __init__(self, name, age, contact_number, membership_id, sport):
        super().__init__(name, age, contact_number)
        self.membership_id = membership_id
        self.sport = sport
        self.performance_scores = []
        self.average = "Not Calculated"
    
    def set_member_details(self, membership_id, sport):
        self.membership_id = membership_id
        self.sport = sport
    
    def add_performance_score(self, score):
        self.performance_scores.append(score)
    
    def calculate_average_score(self):
        if (len(self.performance_scores) != 0):
            self.average = sum(self.performance_scores)/len(self.performance_scores)
        else:
            self.average = 0
        return self.average

    def get_member_summary(self):
        print("Name: " + self.name+ ", Age: " + str(self.age)+ ", Contact Number: " +str(self.contact_number)+ ", Membership ID: " + str(self.membership_id)+ ", Sport: "+ self.sport+ ", Average Score: " +str(self.average))

class Coach(Person):
    def __init__(self, name, age, contact_number, coach_id, specialisation, salary):
        super().__init__(name, age, contact_number)
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []
        self.mentorship_group = []
    
    def set_coach_details(self, coach_id, specialisation, salary):
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
    
    def assign_mentee(self, member):
        if isinstance(member, Member)==False:
            print("Cannot mentor non-members.")
        else:
            self.mentees.append(member.name)
            print(self.name + " is now mentoring Member " + member.name + " in " + member.sport)
        
    def get_mentees(self):
        print(self.mentees)
    
    def increase_salary(self, percentage):
        self.salary = self.salary * (1+(percentage/100))
    
    def mentor_coach(self, coach):
        if isinstance(coach, Coach):
            self.mentorship_group.append(coach)
            print("Coach " + self.name+ " is now mentoring Coach " + coach.name + " in " + coach.specialisation)
        else:
            print("Cannot mentor non-coaches.")
    
    def get_mentorship_group(self):
        for coach in self.mentorship_group:
            print(coach.name+ " (" + coach.specialisation +")")
    
    def get_coach_summary(self):
        print("Name: " +self.name+ ", Age: " + str(self.age)+ ", Contact Number: " + str(self.contact_number)+ ", Coach ID: " + self.coach_id + ", Specialisation: " + self.specialisation + ", Annual Salary: £" + str("{:.2f}".format(self.salary)))
    
class Staff(Person):
    def __init__(self, name, age, contact_number, staff_id, position, years_of_service):
        super().__init__(name, age, contact_number)
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service
    
    def set_staff_details(self, staff_id, position, years_of_service):
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service
    
    def increment_years_of_service(self):
        self.years_of_service += 1
    
    def assist_member(self, member):
        if isinstance(member, Member)==True:
            print("Staff " +self.name+ " assisted " +member.name+ " in resolving an issue.")
        else:
            print("Cannot help non-members.")
    
    def get_staff_summary(self):
        print("Name: " +self.name+ ", Age: " +str(self.age)+ ", Contact Number: " +str(self.contact_number)+ ", Staff ID: " +str(self.staff_id)+ ", Position: " +self.position+ ", Years of Service: " +str(self.years_of_service))


    
alex = Member("Alex", 20, 12341231, "D1231", "Kickboxing")
katie = Member("Katie", 16, 1235234, "D24985", "Netball")
coach = Coach("Coach", 54, 123123, "C42134", "Football", 1000)
gymTeach = Coach("Jim", 65, 1231231, "C13231", "Basketball", 100)
staff = Staff("Steph", 40, 2131, "S23423", "Teacher", 10)

coach.assign_mentee(alex)
katie.add_performance_score(10)
katie.add_performance_score(20)
katie.add_performance_score(30)
katie.calculate_average_score()

gymTeach.increase_salary(15)
staff.increment_years_of_service()


alex.get_member_summary()
katie.get_member_summary()
coach.get_coach_summary()
gymTeach.get_coach_summary()
staff.get_staff_summary()

coach.mentor_coach(gymTeach)
coach.get_mentorship_group()
coach.get_mentees()