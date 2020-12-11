using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;

namespace AdventOfCode2020
{
    public class Day7
    {
        private readonly List<Bag> bagContainer = new List<Bag>();

        #region Init

        public void ReadData()
        {
            var counter = 0;
            string line;

            // Read the file and display it line by line.  
            var file = new StreamReader(@"D:\\Projekte\\AdventOfCode2020\\input\\day7.txt");
            while ((line = file.ReadLine()) != null)
            {
                var bag = CreateOrReturn(line.Split("contain")[0].Replace("bags", "").Trim());

                PackMyBag(bag, line.Split("contain")[1]);
                counter++;
            }

            file.Close();
            Console.WriteLine("There were {0} lines.", counter);
            Console.WriteLine("There were {0} bags.", bagContainer.Count);

            foreach (var bag in bagContainer)
            {
                Console.WriteLine("{0} contains {1} bags:", bag.color, bag.sumOfBags);
            
                for (var index = 0; index < bag.containingBags.Count; index++)
                {
                    Console.WriteLine("- {1} {0}", bag.containingBags[index].color, bag.amountOfBags[index]);
                }
            }
            
            FindAmountOfGoldBags();
            
            PartTwo();
        }


        private Bag CreateOrReturn(string color)
        {
            var newBag = bagContainer.Find(containingBag => containingBag.color.Equals(color));

            if (newBag == null)
            {
                newBag = new Bag(color);
                bagContainer.Add(newBag);
            }

            return newBag;
        }

        #endregion

        #region Part One

        private void FindAmountOfGoldBags()
        {
            Console.WriteLine("{0} bags contains at least one shiny gold bag!",
                bagContainer.Count(bag => ContainsGoldBag(bag.containingBags)));
        }

        private static bool ContainsGoldBag(IReadOnlyCollection<Bag> bagList)
        {
            if (bagList.Count == 0) return false;
            foreach (var bag in bagList)
            {
                if (bag.IsShinyGold()) return true;

                if (bag.ContainsShinyGold()) return true;

                if (ContainsGoldBag(bag.containingBags)) return true;
            }

            return false;
        }

        private void PackMyBag(Bag mainBag, string bagStrings)
        {
            var bagString = bagStrings.Split(",");
            foreach (var bs in bagString)
            {
                var listOfString = bs.Trim().Split(" ");
                var count = listOfString[0];

                if (count == "no")
                    continue;

                var bag = CreateOrReturn(listOfString[1] + " " + listOfString[2]);

                mainBag.containingBags.Add(bag);
                mainBag.amountOfBags.Add(int.Parse(count));
                mainBag.sumOfBags += int.Parse(count);
            }
        }

        #endregion

        #region Part Two

        private void PartTwo()
        {
            Console.WriteLine("GoldBag Sums: {0}", CountBags(bagContainer.Find(bag => bag.color == "shiny gold")));
        }

        private static int CountBags(Bag parent)
        {
            return parent.containingBags.Select((t, i) => parent.amountOfBags[i] + parent.amountOfBags[i] * CountBags(t)).Sum();
        }

        #endregion
    }
}