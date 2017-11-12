"""
problem 1.1: Satisfying truth assignment
Instance: CNF formula F on a set of V of Boolean variables, truth assignment
 on V, f:V->{TRUE, FALSE}.
Question: Does f satisfy F?
"""

class CNF():
    def __init__(self, n_literal=0):
        self.n_literal = abs(int(n_literal))
        self.assign = [False] * (self.n_literal)
        self.formula  = []

    def set_assign(self, ass):
        assert(len(ass) == self.n_literal)
        self.assign = ass

    def satisfy(self, assign=None):
        if(assign):
            ass = assign
        else:
            ass = self.assign

        assert(len(ass)==self.n_literal)

        for clause in self.formula:
            cv = False
            for l in clause:
                if(l > 0):
                    cv = cv or ass[l-1]
                else:
                    cv = cv or (not ass[-l-1])
                if cv: break
            if not cv: return False

        return True


    def append_clause(self, clause):
        c = [int(i) for i in clause]
        for i in c:
            assert(abs(i) <= self.n_literal)
        self.formula.append(c)
        return

    def __repr__(self):
        ret = "cnf d %d %d\n" % (self.n_literal, len(self.formula))
        for i in self.formula:
            i.append(0)
            si = [str(ss) for ss in i]
            ret += " ".join(si)
            ret += "\n"

        return ret

def load_cnf_file(f):
    cnf = None
    n_literal = 0
    n_clause = 0
    n_c = 0
    for l in f:
        if l.startswith('c'): continue

        if l.startswith('p cnf'):
            ss = l.split()
            n_literal = int(ss[2])
            n_clause = int(ss[3])
            cnf = CNF(n_literal)
            continue

        ss = [int(i) for i in l.split()]
        assert(ss[-1] == 0)
        ss.pop()
        cnf.append_clause(ss)
        n_c += 1   

    assert(n_clause == n_c)
    return cnf


if __name__ == "__main__":
    print("CNF satisfying assignment")

    cnf = CNF(3)

    cnf.append_clause([1,2])
    cnf.append_clause([2,-3])
    cnf.append_clause([2,-3])
    
    cnf.set_assign([1,0,1])
    print(cnf.satisfy())

    cnf.set_assign([0,0,1])
    print(cnf.satisfy())

    cnf.set_assign([0,1,0])
    print(cnf.satisfy())

    cnf.set_assign([1,0,1])
    print(cnf.satisfy())

    #cnf.set_assign([1,0])
    #print(cnf.satisfy())

    fname = "aim-100-1_6-no-1.cnf"
    f = open(fname)
    cnf2 = load_cnf_file(f)
    f.close()

    print(cnf2)
    print(cnf2.n_literal)
    print(len(cnf2.formula))
