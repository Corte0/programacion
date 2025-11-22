import math
from astropy.constants import GM_earth
from astropy.constants import R_earth
from astropy import units as u
import numpy as np

def calcular_velocidades(ha_km: float, phi_deg:float, hb_km:float):
    '''
    '''
    ha = (ha_km * u.km).to(u.m) + R_earth
    hb = (hb_km * u.km).to(u.m) + R_earth
    phi = phi_deg * u.deg
    vaf = (2 * GM_earth * (ha**(-1) - hb**(-1)) * (1 - (ha / (hb * np.sin(phi)))**2)**(-1))**(1/2)
    vbf = ha / (hb * np.sin(phi)) * vaf
    return vaf.value, vbf.value

if __name__ == '__main__':
    print(calcular_velocidades(362.1,60,67.37))

