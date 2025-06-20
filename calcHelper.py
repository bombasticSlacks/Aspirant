basicCost = 3
artisanCost = 5
exoticCost = 10
serviceCost = 5
MWCost = 10

def getQuality(quality: str):
    if(quality.lower() is "basic"): return basicCost
    elif(quality.lower() is "artisan"): return artisanCost
    elif(quality.lower() is "exotic"): return exoticCost
    else: return -1


def calcWeapon(size: int, quality: str, mw=False):
    qualityCost = getQuality(quality)
    
    baseCost = (size + 1) * qualityCost + 5
    if(mw): baseCost += MWCost

    return baseCost

def calcArmour(quality: str, mw=False):
    qualityCost = getQuality(quality)
    
    baseCost = 5 * qualityCost + 5
    if(mw): baseCost += MWCost

    return baseCost
    

def calcStorage(quality: str, mw=False):
    qualityCost = getQuality(quality)
    
    baseCost = 6 * qualityCost + 5
    if(mw): baseCost += MWCost

    return baseCost