#!/usr/bin/env python

class Bouncy:
    """Bouncies class"""

    __instance = None

    def __new__(cls):
        """Singleton method"""

        if Bouncy.__instance is None:
            Bouncy.__instance = object.__new__(cls)
        return Bouncy.__instance
        
    def is_bouncy(self, number) -> bool:
        """Let check if a number is bouncy"""

        up = False
        dw = False
    
        last = number % 10
        number = int(number/ 10)
    
        while number > 0:
            next = number % 10
            number = int(number / 10)
            if next < last:
                up = True
            elif next > last:
                dw = True
            last = next
    
            if dw and up:
                return True
    
        return dw and up

    def calculate_by_percent(self, percent) -> int:
        """Find the least number for which the proportion of bouncy numbers is exactly the given percent """

        number = 99
        bouncies = 0

        while 100*bouncies/number < percent:
            number+= 1 
            if self.is_bouncy(number):
                bouncies+= 1
            print (number, 100*bouncies/number, self.is_bouncy(number))
        
        return number



