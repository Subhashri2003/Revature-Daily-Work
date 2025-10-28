#this is s module

def simple_interest(pri,ny,roi):   # this is a function
    """
    :param pri: principle amount
    :param ny: no of years
    :param roi: rate of interest
    :return: si,amount
    """
    si=pri*ny*roi/100
    amt=pri + si
    return si,amt


def compound_interest(pri,ny,roi):    #this is a function
    """
    :param pri: principle
    :param ny: no of years
    :param roi: rate of interest
    :return: amount
    """
    amount=pri*(1+(roi/100)**(1*t))
    return amount