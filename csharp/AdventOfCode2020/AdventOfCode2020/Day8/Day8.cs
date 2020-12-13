using System;
using System.Collections.Generic;
using System.IO;

public class Day8
{
    private readonly List<Instruction> instructions = new();
    
    private int accumulator = 0;
 
    public void ReadData()
    {
        var counter = 0;
        string line;

        // Read the file and display it line by line.  
        var file = new StreamReader(@"D:\\Projekte\\AdventOfCode2020\\input\\day8.txt");
        while ((line = file.ReadLine()) != null)
        {
            var lineArray = line.Split(" ");
            instructions.Add(new Instruction(lineArray[0], int.Parse(lineArray[1])));
            counter++;
        }

        file.Close();
        Console.WriteLine("There were {0} lines.", counter);

        // foreach (var instruction in readInstructions)
        // {
        //     Console.WriteLine("{0} {1} {2}", instruction.type, instruction.value, instruction.used);
        // }

        FindLoop(instructions[0], 0);
        
        Console.WriteLine("Part one: {0}", accumulator);
    }

    private void FindLoop(Instruction instruction, int pos)
    {
        while (true) 
        {
            if (instruction.used || pos == instructions.Count-1) break;
            instruction.used = true;

            switch (instruction.type)
            {
                case "acc":
                    accumulator += instruction.value; 
                    pos += 1;
                    break;
                case "nop": 
                    pos += 1;
                    break;
                case "jmp":
                    pos += instruction.value;
                    break;
            }
            
            instruction = instructions[pos];
        }
    }
}