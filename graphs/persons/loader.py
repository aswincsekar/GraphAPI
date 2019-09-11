from persons.models import Person
import tqdm

def load_rel(path):
    with open(path,'r+') as f:
        lines = f.readlines()
        p1 = None
        for f in tqdm.tqdm(lines):
            if "#" not in f:
                # print(f.replace("\n","").split("\t"))
                persons = f.replace("\n","").split("\t")
                if int(persons[0])<1000000 and int(persons[1])<1000000:
                    if not p1 or (p1 and persons[0] != p1.name):
                        p1 = Person.nodes.get(name=persons[0])
                    if p1:
                        p2 = Person.nodes.get(name=persons[1])
                        p1.friends.connect(p2)
                        p1.save()