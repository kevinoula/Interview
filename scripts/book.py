class Book:
    def __init__(self, price, quantity, title, author):
        self.price = price
        self.quantity = quantity
        self.title = title
        self.author = author

    def sell(self, customer_cash, desired_quantity):
        # check inventory for book quantity
        if desired_quantity > self.quantity:
            desired_quantity = self.quantity

        # check that customer has enough money
        amount_required = self.price * desired_quantity

        # customer doesn't have enough money so just purchase as many as they can afford
        if customer_cash < amount_required:
            desired_quantity = math.floor(customer_cash / self.price)
            amount_required = self.price * desired_quantity

        # complete transaction by deducting inventory and customer's cash
        customer_cash -= amount_required
        self.quantity -= desired_quantity
        print("Customer has purchased %d books for $%d." % (desired_quantity, amount_required))
        print("Customer has $%d remaining." % customer_cash)
        print("There are %d books left in stock!" % self.quantity)
        return customer_cash
