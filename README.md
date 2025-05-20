# security-estimates

## How to use:
```
python ZKDilithium.py
```
This takes few minutes to compute the security estimation (disabling the dual SIS attack reduces the computational time if you are in a hurry). It should output:
* For Dilithium (NIST II):
    ```
    Dilithium
    {'n': 256, 'k': 4, 'l': 4, 'gamma1': 131072, 'gamma2': 95232.0, 'q': 8380417, 'eta': 2, 'zeta': 350209.0, 'zeta_prime': 380929.0, 'pkdrop': 13}

    === WEAK UF
    Attack uses block-size 423 and 2304 dimensions, with 0 q-vectors
    log2(epsilon) = -84.52, log2 nvector per run 87.78
    shortest vector used has length l=7242509.01, q=8380417, `l<q'= 1
    SIS & 2304 & 423 & 123 & 112 & 87
    === STRONG UF
    Attack uses block-size 417 and 2304 dimensions, with 0 q-vectors
    log2(epsilon) = -82.72, log2 nvector per run 86.54
    shortest vector used has length l=7835854.32, q=8380417, `l<q'= 1
    SIS & 2304 & 417 & 121 & 110 & 86
    === SECRET KEY RECOVERY
    Primal attacks uses block-size 424 and 977 samples; dim d=2002
    Primal & 977 & 424 & 124 & 112 & 87
    Dual attacks uses block-size 422 and 1014 samples; dim d=2038
    shortest vector used has length l=7347307.38, q=8380417, `l<q'= 1
    log2(epsilon) = -43.78, log2 nvector per run 87.57
    Dual & 1014 & 422 & 123 & 111 & 87 
    ```
* For our ZK-Dilithium:
    ```
    DilithiumZK6
    {'n': 256, 'k': 4, 'l': 5, 'gamma1': 131072, 'gamma2': 983040.0, 'q': 2013265921, 'eta': 4, 'zeta': 2125825.0, 'zeta_prime': 3932161.0, 'pkdrop': 13}

    === WEAK UF
    Attack uses block-size 468 and 2560 dimensions, with 0 q-vectors
    log2(epsilon) = -92.21, log2 nvector per run 97.12
    shortest vector used has length l=47388212.06, q=2013265921, `l<q'= 1
    SIS & 2560 & 468 & 136 & 124 & 97
    === STRONG UF
    Attack uses block-size 426 and 2560 dimensions, with 0 q-vectors
    log2(epsilon) = -86.18, log2 nvector per run 88.40
    shortest vector used has length l=85708324.96, q=2013265921, `l<q'= 1
    SIS & 2560 & 426 & 124 & 112 & 88
    === SECRET KEY RECOVERY
    Primal attacks uses block-size 426 and 1017 samples; dim d=2298
    Primal & 1017 & 426 & 124 & 112 & 88
    Dual attacks uses block-size 424 and 1024 samples; dim d=2304
    shortest vector used has length l=968498746.70, q=2013265921, `l<q'= 1
    log2(epsilon) = -43.93, log2 nvector per run 87.99
    Dual & 1024 & 424 & 124 & 112 & 87 
    ```

## Summary
|Security| Dilithium | ZK-Dilithium |
|-|-|-|
| Quantum| 121  bits|124 bits|
|Classical| 110 bits|112 bits|
|Plausible | 86 bits|87  bits|