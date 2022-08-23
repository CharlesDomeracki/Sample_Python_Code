using System;

namespace OODemo
{
    public class RentalCar
    {
        public int RetalId { get; set; }
        public string CurrentRenter { get; set; }
        public decimal PricePerDay { get; set; }
        public int NumberOfPassengers { get; set; }
        public CarType Style { get; set; }


        public void StartEngine()
        {
            Console.WriteLine("Turn key to ignition setting");
            Console.WriteLine("Turn key to on");
        }
        
        public void StopEngine()
        {
            Console.WriteLine("Turn key to off");
        }
    }
}
