#######################################################
#     Spyros Daskalakis                               #
#     last Revision: 29/03/2022                       #
#     Python Version:  3.9                            #
#######################################################

# Inputs
############################################
# End of Charge overvoltage/battery voltage
VEOC = 5
# Undervoltage protection voltage
VUVP = 2.3
############################################

# Operation
############################################
# The pass transistor is closed once the (rising) voltage on the STORE pin triggers the overvoltage threshold
# VSTORE(EOC) (corresponding to VEOC > VBG). An internal hysteresis (EOCHYS) sets the restart voltage level for
# DC-DC converter. The IC also offers the undervoltage protection threshold: the pass transistor is opened once the
# (falling) voltage on the STORE pin decreases down to the undervoltage threshold VSTORE(UVP) (corresponding to
# VUVP < VBG).
############################################
# IC internal voltage reference
VBG = 1.23

# Resistor Calculation
############################################
# ROUT_TOT = R4 + R5 + R6
ROUT_TOT = 20e6
# To 10 MΩ ≤ ROUT(TOT) ≤ 20 MΩ
R6 = (VBG / VEOC) * ROUT_TOT
R5 = (VBG / VUVP) * ROUT_TOT - R6
R4 = ROUT_TOT - R6 - R5

print('Results R4-R6:')
print('R4 (MOhm):', R4 / 1e6)
print('R5 (MOhm):', R5 / 1e6)
print('R6 (MOhm):', R6 / 1e6)

# VOC(MAX), intended as VOC at max operating condition of the source
# MPPTRATIO , intended as VMP/VOC at typical operating conditions of the source
# 0.1 μA ≤ ILEAKAGE ≤ 1 μA fits for most of the applications
# SPV1050 constraints:
# 150 mV ≤ VMPP(MAX) ≤ 2.1 V
# VMPP(MAX) < VOC(MAX)

# Harvesting source is a PV panel with VMP(TYP) = 1.5 V and VOC(TYP) = 2.0 V
VMP_TYP = 1.5
VOC_TYP = 2.0
MPPT_RATIO = (VMP_TYP / VOC_TYP)
print('MPPTRATIO (%):', MPPT_RATIO)
# Inputs
############################################
VOC_MAX = 2.2  # Volts
VMPP_MAX = 0.5  # Volts
I_LEAKAGE = 0.1 * 1e-6  # Amperes

RIN_TOT = (VOC_MAX / I_LEAKAGE) * MPPT_RATIO
# print('RIN_TOT (MOhm):', RIN_TOT / 1e6)
R1 = RIN_TOT * (1 - (VMPP_MAX / VOC_MAX))
R2 = RIN_TOT * (VMPP_MAX / VOC_MAX) * (1 - MPPT_RATIO)
R3 = RIN_TOT * (VMPP_MAX / VOC_MAX) * MPPT_RATIO
print('Results R1-R3:')
print('R1 (MOhm):', R1 / 1e6)
print('R2 (MOhm):', R2 / 1e6)
print('R3 (MOhm):', R3 / 1e6)
