def de_identify(A):
    B = A.replace("-", "")

    B = B.replace(B[6]+B[7]+B[8]+B[9]+B[10]+B[11]+B[12], "*******")
    return B

print(de_identify("9701031234567"))