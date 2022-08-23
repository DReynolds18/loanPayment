# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:56:45 2022

@author: dreynolds18
name = Dylan Reynolds
22 August 2022
"""

def payment(pv, rAPR, nMonths):
    """
    

    Parameters
    ----------
    pv : TYPE floating point number
        DESCRIPTION. how much $$ I borrow
    rAPR : TYPE. float
        DESCRIPTION. annual percentage rate
    nMonths : TYPE integer
        DESCRIPTION. term - length of loan

    Returns
    -------
    Pmt: TYPE float
        DESCRIPTION. monthly payment

    
    """
    Pmt =  rAPR/1200*pv/(1-(1+(rAPR/1200))**(-nMonths))
    
    return Pmt
'''
write a loop!
input pv, n, rAPR
print out the input variables
print out the payment
and loop back to get a new case

if pv is put a '0', exit the loop
'''


while(1):
    pv = input('input pv ')
    if float(pv) != 0: 
        print(pv)
        rAPR = input('input rAPR ')
        print(rAPR)
        n = input('input n ')
        print(n)
        paymentDollars = payment(float(pv), float(rAPR), float(n))
        print('my payment is ${:.2f}'.format(paymentDollars))
    if float(pv) == 0:
        break
print('out of the loop')