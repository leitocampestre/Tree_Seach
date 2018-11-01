""" Busqueda en arbol"""


class Food():
    def __init__(self, n, v, w):
        self._name = n
        self._value = v
        self._calories = w
        
    @property
    def name(self):
        return self._name
    @property
    def value(self):
        return self._value
    @property
    def calories(self):
        return self._calories    
    def density(self):
        return self.value()/self.calories()
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    menu=[]
    for i in range(len(values)):
        menu.append(Food(names[i],values[i],calories[i]))
    return menu
    
def maxVal(toConsider, avail):
    if toConsider == [] or avail==0:
        result = (0,())
    elif toConsider[0].calories > avail: # explora derecha
        result = maxVal(toConsider[1:], avail)
    else: # explora izquierda
        Considered = toConsider[0]  
    
        withVal, withToTake = maxVal(toConsider[1:], avail - toConsider[0].calories)#explora izquierda
        
        withVal += Considered.value
        
        withOutVal, withOutToTake = maxVal(toConsider[1:], avail) 
        if withVal > withOutVal:
            result = (withVal, withToTake + (Considered,))
        else:
            result = (withOutVal, withOutToTake)
    return result
    
def main ():
    names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
    values = [89,90,95,100,90,79,50,10]
    calories = [123,154,258,354,365,150,95,195]
    foods = buildMenu(names, values, calories)
    a=Food('wine', 76, 82)
    for food in foods:    
        print(food)
    val,taken=maxVal(foods, 750)
    print('Total value of items taken =', val)
    for item in taken:
            print('   ', item)
              
if __name__ == "__main__":

    main()        