
def main():
    from module import Person, Wizard, HealthPotion
    import numpy as np
    import random
    user_1 = Person("Hero")
    user_2 = Wizard("Wizard")
    #user_1 = Person("Hero")
    #user_2 = Wizard("Wizard")

    while user_1.is_dead() == False and user_2.is_dead() == False:
        rando = random.randrange(0,3,1)
    
        if rando == 1:
            user_1.hit( user_2)
        else:
            user_2.hit( user_1)

        random_health_potion_use = np.random.randint(3)
        
        if random_health_potion_use == 0:
            HealthPotion.was_used_by( user_1)
    
        elif random_health_potion_use == 0:
            HealthPotion.was_used_by( user_1)
        else:
            pass

        if user_1.get_life_points() <= 0:
            #resultat.funcresult( self.user_1.name)
            result= ( user_1.name + " wins")
    #print(result)
        if user_2.get_life_points() <= 0:
            #resultat.funcresult( self.user_2.name)
            result= ( user_2.name + " wins")
    #print(result)
    #print( self.user_2.name + " wins")

    return result
    #print(result)

if __name__ == '__main__':
    print(main())

