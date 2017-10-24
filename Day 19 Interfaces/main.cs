using System;

namespace ConsoleApplication.Day_1_Data_Types
{
    // Locked code start.
    public interface AdvancedArithmetic{
        int divisorSum(int n);
    }
    // Locked code end.
    
    class Calculator : AdvancedArithmetic
    {
        public int divisorSum(int integer)
        {
            var sum = 0;
            foreach (var divisor in getDivisors(integer))
            {
                sum = sum + divisor;
            }
            return sum;
        }
    
        private System.Collections.Generic.List<int> getDivisors(int integer)
        {
            var result = new System.Collections.Generic.List<int>(){};
            for (int i = 1; i < integer + 1; i++)
            {
                if (integer % i == 0)
                {
                    result.Add(i);
                }
            }
            return result;
        }
    }
    
    // Locked code start.
    class Solution{
        static void Main(string[] args){
            int n = Int32.Parse(Console.ReadLine());
            AdvancedArithmetic myCalculator = new Calculator();
            int sum = myCalculator.divisorSum(n);
            Console.WriteLine("I implemented: AdvancedArithmetic\n" + sum); 
        }
    }
    // Locked code end.
}