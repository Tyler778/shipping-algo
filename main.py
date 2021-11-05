from hash import HashMap



if __name__ == '__main__':
    h = HashMap()
    h.add('Bob', '567-888')
    h.add('Ming', '293-6753')
    h.add('Mike', '567-2188')
    h.print()
    h.delete('Bob')
    h.print()




