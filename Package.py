

class Package:
    _registry = []

    def __init__(self, id, address, city, state, zip, deliveryTime, weight):
        self._registry.append(self)
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryTime = deliveryTime
        self.weight = weight
        self.status = 'At The Hub'
        self.deliveredTime = None
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
    def setZip(self, zip):
        self.zip = zip

    def getDeliveryTime(self):
        return self.deliveryTime

    def getWeight(self):
        return self.weight

    def getStatus(self):
        return self.status

    def setEnRoute(self):
        self.status = 'En Route'
    def setDelivered(self):
        self.status = 'Delivered'

    def setDeliveredTime(self, time):
        self.deliveredTime = time
    def getDeliveredTime(self):
        return self.deliveredTime
