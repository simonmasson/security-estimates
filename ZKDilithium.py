from MSIS_security import MSIS_summarize_attacks, MSISParameterSet
from MLWE_security import MLWE_summarize_attacks, MLWEParameterSet
from math import sqrt


class UniformDilithiumParameterSet(object):
    def __init__(self, n, k, l, gamma1, gamma2, tau, q, eta, pkdrop=0):
        self.n = n
        self.k = k
        self.l = l
        self.gamma1 = gamma1
        self.gamma2 = gamma2
        self.q = q
        self.eta = eta
        # SIS l_oo bound for unforgeability
        self.zeta = max(gamma1, 2*gamma2 + 1 + 2**(pkdrop-1) *
                        tau)                # Define in section 6.2
        # SIS l_oo bound for strong unforgeability
        # Define in section 6.2
        self.zeta_prime = max(2*gamma1, 4*gamma2 + 1)
        self.pkdrop = pkdrop


# class GaussianDilithiumParameterSet(object):
#     def __init__(self, n, k, l, sigma, q, eta, pkdrop=0):
#         self.n = n
#         self.k = k
#         self.l = l
#         self.sigma = sigma
#         self.q = q
#         self.eta = eta
#         self.pkdrop = pkdrop
#         self.B = 2*equation5(self)


# def equation5(dps):
#     B2 = ((1.05 * dps.sigma * sqrt((dps.k + dps.l)*dps.n))**2
#           +(2**(dps.pkdrop-1) * sqrt(60*dps.n*dps.k))**2)
#     return sqrt(B2)

n = 256
q = 8380417
q_BB = 2**31 - 2**27 + 1  # babybear
q_M31 = 2**31 - 1  # Mersenne31

Dilithium = UniformDilithiumParameterSet(
    n, 4, 4, 2**17, (q-1)/88, 39, q, 2, pkdrop=13)
DilithiumBB_1 = UniformDilithiumParameterSet(
    n, 4, 4, 2**17, (q-1)/88, 39, q_BB, 2, pkdrop=13)
DilithiumBB_2 = UniformDilithiumParameterSet(
    n, 4, 4, 2**17, (q-1)/88, 39, q_BB, 10, pkdrop=13)
DilithiumBB_3 = UniformDilithiumParameterSet(
    n, 4, 5, 2**17, (q-1)/88, 39, q_BB, 2, pkdrop=13)
DilithiumBB_4 = UniformDilithiumParameterSet(
    n, 4, 5, 2**17, (q-1)/88, 39, q_BB, 4, pkdrop=13)
DilithiumBB_5 = UniformDilithiumParameterSet(
    n, 4, 5, 2**17, (q_BB-1)/2**10, 39, q_BB, 4, pkdrop=13)
DilithiumBB_6 = UniformDilithiumParameterSet(
    n, 4, 5, 2**17, (q_BB-1)/2**11, 39, q_BB, 4, pkdrop=13)
DilithiumBB_7 = UniformDilithiumParameterSet(
    n, 4, 5, 2**18, (q_BB-1)/2**11, 39, q_BB, 4, pkdrop=13)

DilithiumM31_1 = UniformDilithiumParameterSet(
    n, 4, 4, 2**17, (q-1)/88, 39, q_M31, 2, pkdrop=13)
DilithiumM31_2 = UniformDilithiumParameterSet(
    n, 4, 4, 2**17, (q-1)/88, 39, q_M31, 10, pkdrop=13)
DilithiumM31_3 = UniformDilithiumParameterSet(
    n, 4, 5, 2**17, (q-1)/88, 39, q_M31, 2, pkdrop=13)
DilithiumM31_4 = UniformDilithiumParameterSet(
    n, 4, 5, 2**17, (q-1)/88, 39, q_M31, 4, pkdrop=13)
DilithiumM31_5 = UniformDilithiumParameterSet(
    n, 4, 5, 2**17, (q_M31-1)/(3*7), 39, q_M31, 4, pkdrop=13)
DilithiumM31_6 = UniformDilithiumParameterSet(
    n, 4, 5, 2**17, (q_M31-1)/(3*7*151), 39, q_M31, 4, pkdrop=13)
DilithiumM31_7 = UniformDilithiumParameterSet(
    n, 4, 5, 2**18, (q_M31-1)/(3*7*151), 39, q_M31, 4, pkdrop=13)


all_params_unif = [
    ("Dilithium", Dilithium),
    # ("DilithiumBB_1", DilithiumBB_1),
    # ("DilithiumBB_2", DilithiumBB_2),
    # ("DilithiumBB_3", DilithiumBB_3),
    # ("DilithiumBB_4", DilithiumBB_4),
    # ("DilithiumBB_5", DilithiumBB_5),
    # ("DilithiumBB_6", DilithiumBB_6),
    ("DilithiumBB_7", DilithiumBB_7),
    # ("DilithiumM31_1", DilithiumM31_1),
    # ("DilithiumM31_2", DilithiumM31_2),
    # ("DilithiumM31_3", DilithiumM31_3),
    # ("DilithiumM31_4", DilithiumM31_4),
    # ("DilithiumM31_5", DilithiumM31_5),
    # ("DilithiumM31_6", DilithiumM31_6),
    ("DilithiumM31_7", DilithiumM31_7),

]

all_params = all_params_unif


def Dilithium_to_MSIS(dps, strong_uf=False):
    if strong_uf:
        return MSISParameterSet(dps.n, dps.k + dps.l + 1, dps.k, dps.zeta_prime, dps.q, norm="linf")
    else:
        return MSISParameterSet(dps.n, dps.k + dps.l + 1, dps.k, dps.zeta, dps.q, norm="linf")


def Dilithium_to_MLWE(dps):
    return MLWEParameterSet(dps.n, dps.l, dps.k, dps.eta, dps.q, distr="uniform")


text_SIS = ["BKZ block-size $b$ to break SIS", "Best Known Classical bit-cost",
            "Best Known Quantum bit-cost", "Best Plausible bit-cost"]
text_LWE = ["BKZ block-size $b$ to break LWE", "Best Known Classical bit-cost",
            "Best Known Quantum bit-cost", "Best Plausible bit-cost"]


table_SIS = [4*[0] for i in range(4)]
table_LWE = [4*[0] for i in range(4)]
j = 0

for (scheme, param) in all_params_unif:
    print("\n"+scheme)
    print(param.__dict__)
    print("")
    print("=== WEAK UF")
    v = MSIS_summarize_attacks(Dilithium_to_MSIS(param))
    print("=== STRONG UF")
    v = MSIS_summarize_attacks(Dilithium_to_MSIS(param, strong_uf=True))
    for i in range(4):
        table_SIS[i][j] = v[i]
    print("=== SECRET KEY RECOVERY")
    v = MLWE_summarize_attacks(Dilithium_to_MLWE(param))
    for i in range(4):
        table_LWE[i][j] = v[i]
    j += 1

print("UNIFORM DILITHIUM TABLE")
print("========================")

print("\\hline")
for j in range(4):
    print(text_SIS[j]+" & "),
    for i in range(4):
        print(table_SIS[j][i]),
        if i < 3:
            print(" & "),
    print("\\\\")
print("\\hline")
for j in range(4):
    print(text_LWE[j]+" & "),
    for i in range(4):
        print(table_LWE[j][i]),
        if i < 3:
            print(" & "),
    print("\\\\")
print("\\hline")

print("========================")

table_SIS = [4*[0] for i in range(4)]
table_LWE = [4*[0] for i in range(4)]
j = 0
