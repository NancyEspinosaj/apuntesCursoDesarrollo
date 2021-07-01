class TeamMember(object):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid


# Parent class 2
class Worker(object):
    def __init__(self, pay, jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle


class COSO(object):
    def __init__(self, coso2, coso3):
        self.pay = coso2
        self.jobtitle = coso3


# Deriving a child class from the two parent classes
class TeamLeader(TeamMember, Worker, COSO):
    def __init__(self, name, uid, pay, jobtitle, exp, coso2, coso3):
        self.exp = exp
        TeamMember.__init__(self, name, uid)
        Worker.__init__(self, pay, jobtitle)
        COSO.__init__(self, coso2, coso3)
        print("Name: {}, Pay: {}, Exp: {}".format(self.name, self.pay, self.exp))
