class GrandParents:
    def __init__(self, name="GrandParents"):
        self.name = name

    def land_property(self):
        print(f"{self.name} passed down land property.")


class Parents(GrandParents):
    def __init__(self, name="Parents"):
        super().__init__(name="GrandParents")
        self.name = name

    def house_property(self):
        print(f"{self.name} owns the house inherited from {super().name}.")


class Childs(Parents):
    def __init__(self, name="Child"):
        super().__init__(name="Parents")
        self.name = name

    def vehicle_property(self):
        print(f"{self.name} bought a vehicle.")

    def land_property(self):
        print(f"{self.name} converted the land property into a commercial building.")


# Example usage
akash = Childs(name="Akash")
akash.land_property()
akash.house_property()
akash.vehicle_property()