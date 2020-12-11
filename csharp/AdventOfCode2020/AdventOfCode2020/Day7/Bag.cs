using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode2020
{
    public class Bag
    {
        public string color;
        public List<Bag> containingBags = new List<Bag>();
        public List<int> amountOfBags = new List<int>();

        public Bag(string color)
        {
            this.color = color;
        }

        private bool ContainsColor(string color)
        {
            return containingBags.Any(bag =>bag.color.Equals(color));
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