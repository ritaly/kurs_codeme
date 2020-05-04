class Queue:
    def __init__(self, queue_list):
        self.queue_list = queue_list

    # metoda czy_pusta (is_empty) -> zwróć prawda / fałsz
    def is_empty(self):
        return len(self.queue_list) == 0

    # metoda dodaj (put) -> dodaje element na ostatniej pozycji
    def put(self, elem):
        self.queue_list.append(elem)
        print(f"{elem} is added to queue")

    # metoda zdejmij (get) -> zdejmuje element z pierwszej pozycji
    def get(self):
        if self.is_empty():
            return 'no more elements'
        else:
            return self.queue_list.pop(0)

    def show(self):
        print(self.queue_list)



lista_elementow = ['1', '2', 'trzy', 4.0]
kolejka = Queue(lista_elementow)

kolejka.show()
print(kolejka.is_empty())
kolejka.put('aaa')
kolejka.show()
print(kolejka.get())
kolejka.show()
print(kolejka.get())
print(kolejka.get())
print(kolejka.get())
print(kolejka.get())
kolejka.show()
print(kolejka.is_empty())
print(kolejka.get())
