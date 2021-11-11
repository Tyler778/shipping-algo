class Package:
    def __init__(self, id, address, city, state, zip, deliveryTime, weight):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryTime = deliveryTime
        self.weight = weight
        self.status = 'Loaded'
    def getId(self):
        return self.id

    def getAddress(self):
        return self.address
    def setAddress(self, address):
        self.address = address

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getZip(self):
        return self.zip

    def getDeliveryTime(self):
        return self.deliveryTime

    def getWeight(self):
        return self.weight

    def getStatus(self):
        return self.status

    def setStatus(self, stat):
        self.status = stat