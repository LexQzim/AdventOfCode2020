using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode2020
{
    public class Bag
    {
        public readonly string color;
        public readonly List<Bag> containingBags = new List<Bag>();
        public List<int> amountOfBags = new List<int>();
        public int sumOfBags = 0;

        public Bag(string color)
        {
            this.color = color;
        }

        private bool ContainsColor(string bagColor)
        {
            return containingBags.Any(bag =>bag.color.Equals(bagColor));
        }
        
        public bool ContainsShinyGold()
        {
            return ContainsColor("shiny gold");
        }

        public bool IsShinyGold()
        {
            return color.Equals("shiny gold");
        }
    }
}