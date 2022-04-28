class School:
  def __init__(self, name, numberOfStudents, level):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents
  def set_number(self, new_numberOfStudents):
    if isinstance(new_numberOfStudents, int):
      self.numberOfStudents = new_numberOfStudents
    else:
      raise TypeError
  def __repr__(self):
    return "A {level} school named {name} with {numberOfStudents} students".format(level=self.level, name=self.name, numberOfStudents=self.numberOfStudents)

testing = School('aykan', 'middle', 5)
print(testing.name)
print(testing.level)
print(testing.numberOfStudents)
testing.set_number(200)
print(testing.numberOfStudents)


class PrimaryChool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(self, name, numberOfStudents, 'primary')
    self.pickupPolicy = pickupPolicy
  def get_policy(self):
    return self.pickupPolicy

  def __repr__(self):
    #super().__repr__(self, pickupPolicy)
    parentRepr = super().__repr__()
    return parentRepr + "The pickup polity is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

class MiddleSchool(School):
  pass

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, numberOfStudents, 'high')
    for i in sportsTeams:
      self.sportsTeams = sportsTeams
  
  def getsportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The sports teams are {sportsTeams}".format(sportsTeams = self.sportsTeams)


c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.getsportsTeams())
print(c)



