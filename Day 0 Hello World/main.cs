using System;

namespace ConsoleApplication.Day_0_Hello_World
{
    class Solution
    {
        public static void _Main(String[] args)
        {
            // Declare a variable named 'inputString' to hold our input.
            String inputString;
            var result = new System.Collections.Generic.List<int>(){1, 2, 3};
            
            int integer = 12;
            for (int i = 1; i < integer + 1; i++)
            {
                if (integer % 5 == 1)
                {
                    Console.WriteLine(true);
                }
            }
            
            // Read a full line of input from stdin (cin) and save it to our variable, input_string.
            inputString = Console.ReadLine();

            // Print a string literal saying "Hello, World." to stdout using cout.
            Console.WriteLine("Hello, World.");

            // TODO: Write a line of code here that prints the contents of input_string to stdout.
            Console.WriteLine(inputString);
        }
    }
}