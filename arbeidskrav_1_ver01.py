# -*- coding: utf-8 -*-
"""
Arbeidskrav 1 for emnet PY1010-1

Created on Thu Oct 17 11:10:34 2024

@author: håvard mallaug
"""

#%% Kjoerelengde

kjorelengde = 10000   # [km per aar]


#%% forsikring per aar


forsikring_E = 5000   # [kroner per aar]
forsikring_B = 7500   # [kroner per aar]


#%% trafikkforsikringsavgift

trafikkforsikringsavgift_per_aar = 8.38 * 365   # [Forsikringen per dag er kroner 8.38 for begge drivstofftyper]


#%% drivstoffforbruk per km og for hele aaret

drivstofforbruk_E = 0.2   # [kWh/km]
drivstoffpris_E = 2   # [kr/kWh]

drivstoffkostnad_km_E = drivstofforbruk_E * drivstoffpris_E   # [kostnad per kilometer]
drivstoffkostnad_km_B = 1.0   # [kr/km]

drivstoffkostnad_aar_E = kjorelengde * drivstoffkostnad_km_E   # [kostnad per aar]
drivstoffkostnad_aar_B = kjorelengde * drivstoffkostnad_km_B   # [kostnad per aar]
    

#%% bomavgift

bomavgift_E = 0.1   # [kostnad per kilometer for elbil]
bomavgift_B = 0.3   # [kostnad per kilometer for bensinbil]

bomavgift_aar_E = bomavgift_E * kjorelengde   # [kostnad per aar for elbil]
bomavgift_aar_B = bomavgift_B * kjorelengde   # [kostnad per aar for bensinbil]


#%% aarlig kostnad

totalkost_aar_E = forsikring_E + trafikkforsikringsavgift_per_aar + drivstoffkostnad_aar_E + bomavgift_aar_E

totalkost_aar_B = forsikring_B + trafikkforsikringsavgift_per_aar + drivstoffkostnad_aar_B + bomavgift_aar_B

diff_aar_E_B = totalkost_aar_B - totalkost_aar_E


#%% differanse elbil og bensinbil

print ('Aarlig kostnad for elbil er kr.', totalkost_aar_E)
print ('Aarlig kostnad for bensinbil er kr.', totalkost_aar_B)
print ('Differanse i pris er kr.', diff_aar_E_B)