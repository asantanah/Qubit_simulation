
import pylab
from qutip import *
from numpy import *

def negativity(sigma):
    """ Function to compute the negativity 
    of a two qubit system
    """
    #Partial transpose of sigma
    sigmapt = partial_transpose(sigma,(0,1))
    #Eigenvalues of Sigmapt
    evals = sigmapt.eigenenergies()
    #Sum of negative eigenvalues
    s = 0
    l = sigma.shape[0]
    for i in range(0,l):
        s = s + abs((evals[i] - abs(evals[i])))
    return s

# definitions

# print simulation parameters
def parameters():
    print("## Simulation parameters ##")
    print("# Frequecies:")
    print("wa = ", wa)
    print("wb = ", wb)
    print("wr = ", wr)
    print("ga = ", ga)
    print("gb = ", gb)
    print("# Displacements:")
    print("chi_a = ", chi_a)
    print("chi_b = ", chi_b)
    print("chi_ab = ", chi_ab)
    print("chi_ba = ", chi_ba)
    print("# External fields:")
    if E_a > 0:
        print("Cavity A drive:")
        print("E_a = ", E_a)
    if E_b > 0:
        print("Cavity B drive:")
        print("E_b = ", E_b)
    else:
        if E_a == 0:
            print("NONE")
    print("# States:")
    print("dim_Fock = ", N)
    if isFockQ_a:
        print("Cavity A is initially in a Fock state: na = %d\n" % na)
    if isCoherentQ_a:
        print("Cavity A is initially in a Coherent state: ")
        print("alpha_a = %.2f, na_avg = %.2f\n" % (alpha_a, na_avg))
    if isSuperposQ_a: 
        print("Cavity A is initially in a superposition (|%d> + |%d>)\n" % (na[0],na[1]))
    if isCatEvenQ_a:
        print("Cavity A is initially in an EVEN Cat state: ")
        print("alpha_a = %.2f" % alpha_a)
    if isCatOddQ_a:
        print("Cavity A is initially in an ODD Cat state: ")
        print("alpha_a = %.2f" % alpha_a)
        
    if isFockQ_b:
        print("Cavity B is initially in a Fock state: nb = %d\n" % nb)
    if isCoherentQ_b:
        print("Cavity B is initially in a Coherent state: ")
        print("alpha_b = %.2f, nb_avg = %.2f\n" % (alpha_b, nb_avg))
    if isSuperposQ_b: 
        print("Cavity B is initially in a superposition (|%d> + |%d>)\n" % (nb[0],nb[1]))
    if isCatEvenQ_b:
        print("Cavity B is initially in an EVEN Cat state: ")
        print("alpha_b = %.2f" % alpha_b)
    if isCatOddQ_b:
        print("Cavity B is initially in an ODD Cat state: ")
        print("alpha_b = %.2f" % alpha_b)
    if isEntangledQ:
        print("Cavity A and B are initially entangled.")
    if nr >= 0:
        print("MR is initially in a Fock state: nr = %d\n" % nr)
    print("# Dissipation parameters:")
    print("kappa_a = ", kappa_a)
    print("kappa_b = ", kappa_b)
    print("gamma = ", gamma)
    print("n_th_a = ", n_th_a)
    print("n_th_b = ", n_th_b)
    print("n_th_r = ", n_th_r)
    print("# timelist in M.E. simulation:")
    print("t0 = ", t0,", tf = ", tf,", nt = ", nt)
    print("# timelist in Spectrum simulation:")
    print("t0_2 = ", t0_2,", tf_2 = ", tf_2,", nt_2 = ", nt_2)
    return 

# save simulation parameters
def save_parameters():
    filename = "_" + name + "-" + "parameters" + "-" + time_index + ".txt"
    file = open(save_path + filename,"w")
    file.write("Simulation:" + name + "\n")
    file.write("Author:" + author + "\n\n")
    file.write("## Simulation parameters ##\n")
    file.write("# Frequecies:\n")
    file.write("wa = %.2f\n" % wa)
    file.write("wb = %.2f\n" % wb)
    file.write("wr = %.2f\n" % wr)
    file.write("ga = %.3f\n" % ga)
    file.write("gb = %.3f\n" % gb)
    file.write("# Displacements:\n")
    file.write("chi_a = %.5f\n" % chi_a)
    file.write("chi_b = %.5f\n" % chi_b)
    file.write("chi_ab = %.5f\n" % chi_ab)
    file.write("chi_ba = %.5f\n" % chi_ba)
    file.write("# External fields:\n")
    if E_a > 0:
        file.write("Cavity A drive:\n")
        file.write("E_a = %.4f, we_a = %.2f\n" % (E_a,we_a))
    if E_b > 0:
        file.write("Cavity B drive:\n")
        file.write("E_b = %.4f, we_b = %.2f\n" % (E_b,we_b))
    else:
        if E_a == 0:
            file.write("NONE\n")
    file.write("# States:\n")
    file.write("dim_Fock = %d\n" % N)
    if isFockQ_a:
        file.write("Cavity A is initially in a Fock state: na = %d\n" % na)
    if isCoherentQ_a:
        file.write("Cavity A is initially in a Coherent state: ")
        file.write("alpha_a = %.2f, na_avg = %.2f\n" % (alpha_a, na_avg))
    if isSuperposQ_a: 
        file.write("Cavity A is initially in a superposition (|%d> + |%d>)\n" % (na[0],na[1]))
    if isCatEvenQ_a:
        file.write("Cavity A is initially in an EVEN Cat state: ")
        file.write("alpha_a = %.2f" % alpha_a)
    if isCatOddQ_a:
        file.write("Cavity A is initially in an ODD Cat state: ")
        file.write("alpha_a = %.2f" % alpha_a)
        
    if isFockQ_b:
        file.write("Cavity B is initially in a Fock state: nb = %d\n" % nb)
    if isCoherentQ_b:
        file.write("Cavity B is initially in a Coherent state: ")
        file.write("alpha_b = %.2f, nb_avg = %.2f\n" % (alpha_b, nb_avg))
    if isSuperposQ_b: 
        file.write("Cavity B is initially in a superposition (|%d> + |%d>)\n" % (nb[0],nb[1]))
    if isCatEvenQ_b:
        file.write("Cavity B is initially in an EVEN Cat state: ")
        file.write("alpha_b = %.2f" % alpha_b)
    if isCatOddQ_b:
        file.write("Cavity B is initially in an ODD Cat state: ")
        file.write("alpha_b = %.2f" % alpha_b)
    if isEntangledQ:
        file.write("Cavity A and B are initially entangled.")
    if nr >= 0:
        file.write("MR is initially in a Fock state: nr = %d\n" % nr)
    file.write("# Dissipation parameters:\n")
    file.write("kappa_a = %.4f\n" % kappa_a)
    file.write("kappa_b = %.4f\n" % kappa_b)
    file.write("gamma = %.4f\n" % gamma)
    file.write("T = %.3f K\n" % T)
    file.write("n_th_a = %.3f\n" % n_th_a)
    file.write("n_th_b = %.3f\n" % n_th_b)
    file.write("n_th_r = %.3f\n" % n_th_r)
    file.write("# timelist for qutip.mesolve():\n")
    file.write("t0 = %.1f, tf = %.1f, nt = %d\n" % (t0,tf,nt))
    file.write("# timelist for qutip.correlation_2op_2t() simulation:\n")
    file.write("t0_2 = %.1f, tf_2 = %.1f, nt_2 = %d\n" % (t0_2,tf_2,nt_2))
    file.write("# wlist for qutip.spectrum() simulation:\n")
    file.write("w0 = %.1f, wf = %.1f, nw = %d" % (w0,wf,nw))
    file.close()
    return 
