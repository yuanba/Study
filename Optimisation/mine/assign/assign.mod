#Assign problem

#集合
set problem;
set person;

#参数
param C{person,problem}>=0;

#变量
var X{person,problem} binary;

#目标
minimize T : sum{ i in person , j in problem} X[i,j]*C[i,j];

#约束
s.t. L1{i in person} : sum{j in problem} X[i,j] = 1;
s.t. L2{i in problem} : sum{j in person} X[j,i] = 1;

end;
