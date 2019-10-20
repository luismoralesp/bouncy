#!/usr/bin/env python
from numba import jit

@jit(nopython=True, nogil=True)
def is_bouncy(number) -> bool:
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

@jit(nopython=True, nogil=True)
def calculate_by_percent(percent):
    """Find the least number for which the proportion of bouncy numbers is exactly the given percent """
    
    number = 99
    bouncies = 0

    while 100*bouncies/number < percent:
        number+= 1 
        if is_bouncy(number):
            bouncies+= 1
    
    return number




