import numpy as np
import matplotlib.pyplot as plt
from warnings import warn
from sklearn.datasets import make_spd_matrix

def LinearCG(AA, bb, xxZero, tol):
    xx = xxZero
    rr = np.dot(AA, xx) - bb
    pp = -rr

    rrNorm = np.linalg.norm(rr)

    numIterations = 0

    print("--------------------------------------------------------")
    print("iteration: " + str(numIterations) + '\n')
    print("residual norm: " + str(rrNorm) + '\n')
    print("xx solution vector: ")
    print(xx)
    print('\n')
    print("rr residual vector: ")
    print(rr)
    print('\n')
    print("pp direction vector: ")
    print(pp)
    print("--------------------------------------------------------")

    # Create an array to store the histoy of the solution vector during
    # the convergence process
    curveXX = [xx]

    while (rrNorm > tol):
        numIterations += 1
        print("iteration: " + str(numIterations) + '\n')

        # Compute the alpha (scalar) coefficient
        alpha = np.dot(rr,rr) / np.dot(pp, np.dot(AA,pp))
        print("alpha: " + str(alpha) + '\n')

        # Update solution vector
        xxNew = xx + alpha * pp
        print("xx solution vector: ")
        print(xxNew)
        print('\n')
        curveXX.append(xxNew)

        # Update residual vector
        rrNew = rr + alpha * np.dot(AA, pp)
        print("rr residual vector: ")
        print(rrNew)
        print('\n')

        # Compute the current residual norm
        rrNorm = np.linalg.norm(rrNew)
        print("rrNorm: " + str(rrNorm) + '\n')

        # Compute the beta (scalar) coefficient
        beta = np.dot(rrNew,rrNew) / np.dot(rr,rr)
        print("beta: " + str(beta) + '\n')

        # Update the direction vector
        ppNew = -rrNew + beta * pp
        print("pp direction vector: ")
        print(ppNew)

        # Update vectors for next iterations
        xx = xxNew
        rr = rrNew
        pp = ppNew
        print("--------------------------------------------------------")

    return np.array(curveXX)


np.random.seed(0)

AA = make_spd_matrix(2,random_state = 0)
bb = np.random.random(2)

print("A\n", AA, '\n')
print("b\n", bb, '\n')

xxZero  = np.array([-3,-4])
xxFinal = LinearCG(AA, bb, xxZero, 1e-5)
