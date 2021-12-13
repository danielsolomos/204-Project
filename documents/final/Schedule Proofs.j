CONJECTUREPANEL Quiz
PROOF "((G1→D1)∧(G2→D2))→((G3→¬D3)∨(G0→¬D0)), D1∧D2, G3, G0 ⊢ ¬D0∨¬D3"
INFER ((G1→D1)∧(G2→D2))→((G3→¬D3)∨(G0→¬D0)),
     D1∧D2,
     G3,
     G0 
     ⊢ ¬D0∨¬D3 
FORMULAE
0 ¬D0,
1 ¬D3,
2 G0,
3 G0→¬D0,
4 ¬D0∨¬D3,
5 G3,
6 G3→¬D3,
7 (G3→¬D3)∨(G0→¬D0),
8 (G1→D1)∧(G2→D2),
9 (G1→D1)∧(G2→D2)→(G3→¬D3)∨(G0→¬D0),
10 (G3→¬D3)∨(G0→¬D0),
11 G2→D2,
12 G1→D1,
13 D2,
14 D1∧D2,
15 D1,
16 G2,
17 G1,
18 ((G1→D1)∧(G2→D2))→((G3→¬D3)∨(G0→¬D0))
IS
SEQ (cut[B,C\12,4]) ("→ intro"[A,B\17,15]) (cut[B,C\15,15]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\15,13]) (hyp[A\14])) (hyp[A\15]) (cut[B,C\11,4]) ("→ intro"[A,B\16,13]) (cut[B,C\13,13]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\15,13]) (hyp[A\14])) (hyp[A\13]) (cut[B,C\8,4]) ("∧ intro"[A,B\12,11]) (hyp[A\12]) (hyp[A\11]) (cut[B,C\10,4]) ("→ elim"[A,B\8,10]) (hyp[A\9]) (hyp[A\8]) ("∨ elim"[A,B,C\6,3,4]) (hyp[A\7]) (cut[B,C\1,4]) ("→ elim"[A,B\5,1]) (hyp[A\6]) (hyp[A\5]) (LAYOUT "∨ intro" (0) ("∨ intro(R)"[B,A\0,1]) (hyp[A\1])) (cut[B,C\0,4]) ("→ elim"[A,B\2,0]) (hyp[A\3]) (hyp[A\2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\1,0]) (hyp[A\0]))
END
CONJECTUREPANEL Quiz
PROOF "∀x.D(x), ∃y.G(y), T1, T2 ⊢ ∃z.G(z)→T1∧T2"
INFER ∀x.D(x),
     ∃y.G(y),
     T1,
     T2 
     ⊢ ∃z.G(z)→T1∧T2 
FORMULAE
0 T2,
1 T1,
2 ∃z.G(z),
3 i1,
4 T1∧T2,
5 G(z),
6 z,
7 ∃y.G(y),
8 i,
9 ∃z.G(z)→T1∧T2,
10 G(y),
11 y,
12 actual i1,
13 G(i),
14 G(i1),
15 actual i,
16 ∀x.D(x)
IS
SEQ ("∃ elim"[i,C,P,x\8,9,10,11]) (hyp[A\7]) ("→ intro"[A,B\2,4]) ("∃ elim"[i,C,P,x\3,4,5,6]) (hyp[A\2]) ("∧ intro"[A,B\1,0]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Quiz
PROOF "G→(H∧A), T1, T2 ⊢ G→(((T1→H)∨(T1→A))∧((T2→H)∨(T2→A)))"
INFER G→(H∧A),
     T1,
     T2 
     ⊢ G→(((T1→H)∨(T1→A))∧((T2→H)∨(T2→A)))
FORMULAE
0 (T2→H)∨(T2→A),
1 (T1→H)∨(T1→A),
2 T2→A,
3 T2→H,
4 ((T1→H)∨(T1→A))∧((T2→H)∨(T2→A)),
5 A,
6 H∧A,
7 H,
8 T2,
9 T1→H,
10 T1→A,
11 T1,
12 G,
13 G→H∧A,
14 G→(H∧A)
IS
SEQ ("→ intro"[A,B\12,4]) (cut[B,C\6,4]) ("→ elim"[A,B\12,6]) (hyp[A\13]) (hyp[A\12]) (cut[B,C\9,4]) ("→ intro"[A,B\11,7]) (cut[B,C\7,7]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\7,5]) (hyp[A\6])) (hyp[A\7]) (cut[B,C\1,4]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\10,9]) (hyp[A\9])) (cut[B,C\2,4]) ("→ intro"[A,B\8,5]) (cut[B,C\5,5]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\7,5]) (hyp[A\6])) (hyp[A\5]) (cut[B,C\0,4]) (LAYOUT "∨ intro" (0) ("∨ intro(R)"[B,A\3,2]) (hyp[A\2])) ("∧ intro"[A,B\1,0]) (hyp[A\1]) (hyp[A\0])
END
