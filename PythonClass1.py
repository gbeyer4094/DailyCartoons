class BranchOffice:
    company = "CheeseMeat Associates"
    sector = "food science"

    @classmethod
    def showClassInfo(self):
        ci = self.company + ", a "
        ci = ci + self.sector + " trendsetter"
        return ci

    def __init__(self, city, street, state, zip, manager):
        self.city = city
        self.street = street
        self.state = state
        self.zip = zip
        self.manager = manager

    def getInfo(self):
        br = (
            f"{self.city} Office\n\n"
            f"Manager: {self.manager}\n\n"
            f"{self.street}\n"
            f"{self.city}, {self.state} {self.zip}"
        )
        return br

    @staticmethod
    def cm2cf(m3):
        return str(round(m3 * 35.3, 1)) + " cubic feet"


a = BranchOffice("Aurora", "442 Front", "CA", "95221-1111", "Aurora Smith")

b = BranchOffice("Blythe", "6 Lincoln", "CA", "92225-1234", "Art Kimura")

print(a.getInfo())
print(BranchOffice.showClassInfo())
print(BranchOffice.cm2cf(float(input("Enter the number of cubic meters: "))))
