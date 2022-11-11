from data_structures.stack_and_queue.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.shelter = Queue()

    def enqueue(self, animal):
        self.shelter.enqueue(animal)

    def dequeue(self, pref):
        if pref == "dog" or pref == "cat":
            animal_type = pref.capitalize()
            current = self.shelter.front
            if current.value.__class__.__name__ == animal_type:
                matching_animal = current.value
                self.shelter.front = current.next_node
                return matching_animal
            else:
                while current.next_node is not None:
                    if current.next_node.value.__class__.__name__ == animal_type:
                        matching_animal = current.next_node.value
                        current.next_node = current.next_node.next_node
                        return matching_animal
                    else:
                        current = current.next_node


class Dog:
    pass


class Cat:
    pass
