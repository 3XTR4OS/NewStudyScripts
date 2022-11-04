using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Intrinsics.Arm;

Solver ex1 = new Solver();
ex1.solve_my_exam(1,2);
ex1.solve_my_exam(10,21);
ex1.solve_my_exam(51,101);

public class Solver
{
    public void solve_my_exam(int t, int l)
    {
        // R = 3*t^2 + 3*l^5 + 4.9
        Console.WriteLine((3 * (t * t)) + (3 * (l * l * l * l * l)) + 4.9); 
    }
}
