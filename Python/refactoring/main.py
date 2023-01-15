__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


class Homeowner:
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs


class Specialist:
    def __init__(self, name):
        self.name = name


class Electrician(Specialist):
    pass


class Painter(Specialist):
    pass


class Plumber(Specialist):
    pass


alice = Electrician("Alice Aliceville")
bob = Painter("Bob Bobsville")
craig = Plumber("Craig Craigsville")


def alfred_contracts():
    alfred = Homeowner("Alfred Alfredson", "Alfredslane 123", [Painter, Plumber])
    alfred_contracts = []
    for need in alfred.needs:
        if need == alice.__class__:
            alfred_contracts.append(alice.name)
        elif need == bob.__class__:
            alfred_contracts.append(bob.name)
        elif need == craig.__class__:
            alfred_contracts.append(craig.name)
    print("Alfred's contracts:", alfred_contracts)


def bert_contracts():
    bert = Homeowner("Bert Berston", "Bertslane 231", [Plumber])
    bert_contracts = []
    for need in bert.needs:
        if need == alice.__class__:
            bert_contracts.append(alice.name)
        elif need == bob.__class__:
            bert_contracts.append(bob.name)
        elif need == craig.__class__:
            bert_contracts.append(craig.name)
    print("Bert's contracts:", bert_contracts)


def candice_contracts():
    candice = Homeowner(
        "Candice Candicedottir", "Candicelane 321", [Electrician, Painter]
    )
    candice_contracts = []
    for need in candice.needs:
        if need == alice.__class__:
            candice_contracts.append(alice.name)
        elif need == bob.__class__:
            candice_contracts.append(bob.name)
        elif need == craig.__class__:
            candice_contracts.append(craig.name)
    print("Candice's contracts:", candice_contracts)


if __name__ == "__main__":
    alfred_contracts()
    bert_contracts()
    candice_contracts()
