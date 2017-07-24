Problem:    assign
Rows:       9
Columns:    16 (16 integer, 16 binary)
Non-zeros:  46
Status:     INTEGER OPTIMAL
Objective:  T = 4 (MINimum)

   No.   Row name        Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 T                           4                             
     2 L1[A1]                      1             1             = 
     3 L1[A2]                      1             1             = 
     4 L1[A3]                      1             1             = 
     5 L1[A4]                      1             1             = 
     6 L2[B1]                      1             1             = 
     7 L2[B2]                      1             1             = 
     8 L2[B3]                      1             1             = 
     9 L2[B4]                      1             1             = 

   No. Column name       Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 X[A1,B1]     *              0             0             1 
     2 X[A1,B2]     *              0             0             1 
     3 X[A1,B3]     *              0             0             1 
     4 X[A1,B4]     *              1             0             1 
     5 X[A2,B1]     *              1             0             1 
     6 X[A2,B2]     *              0             0             1 
     7 X[A2,B3]     *              0             0             1 
     8 X[A2,B4]     *              0             0             1 
     9 X[A3,B1]     *              0             0             1 
    10 X[A3,B2]     *              1             0             1 
    11 X[A3,B3]     *              0             0             1 
    12 X[A3,B4]     *              0             0             1 
    13 X[A4,B1]     *              0             0             1 
    14 X[A4,B2]     *              0             0             1 
    15 X[A4,B3]     *              1             0             1 
    16 X[A4,B4]     *              0             0             1 

Integer feasibility conditions:

KKT.PE: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.PB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

End of output
