class Queue:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavors, scoops):
        if flavors not in self.flavors: 
        print(" Flavor not avaible ")
        elif scoops < 1 or scoops > 3:
            print("Number of scoops not avaible")
        else:
            print("Order Created")
            order = {"Customer": customer,"Flavor":flavors, "Scoops": scoops}
            self.order.enquene(order)


    def show_all_orders():
        print("Next Order")
        for order in self.order.items:
            print(order)
    

    def next_order():
        print(self.order.dequeue())


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()