"""
Satisfiability
Instance: CNF formula F on a set V of Boolean variables
Question: Is F satifiable, i.e., does there exist a truth 
assignment f: V->{FALSE, TRUE} which satisfy F?
"""

import cnf

def sat(cnf):
    """
    Solve SAT by loop through
    """
    v = [False] * cnf.n_literal
    return _sat(cnf, v, 0)

ss = 0

def _sat(cnf, v, n_assign):
    global ss
    if n_assign == len(v):
        ret = cnf.satisfy(v)
        ss += 1
        if ss % 10 == 0:
            print(ss)
        if(ret):
            print("Satisfy with v:")
            print(v)
        return ret

    v_t = v.copy()
    v_t[n_assign] = True

    v_f = v.copy()
    v_f[n_assign] = False

    n_assign += 1

    return _sat(cnf, v_t, n_assign) or _sat(cnf,
               v_f, n_assign)

if __name__ == "__main__":
    print("Satisfiability")

    fname = "aim-100-1_6-no-1.cnf"
    fname = "simple_v3_c2.cnf"
    fname = "aim-50-1_6-yes1-4.cnf"
    fname = "quinn.cnf"

    f = open(fname)
    cnf = cnf.load_cnf_file(f)
    f.close()

    v = [False] * cnf.n_literal

    print(cnf.satisfy(v))

    v2 = [True] * cnf.n_literal
    print(cnf.satisfy(v2))

    #v3 = [True, True, True, False, True, True, True, True, True, True, False, True, True, False, False, True]
    #print(cnf.satisfy(v3))

    print(sat(cnf))

