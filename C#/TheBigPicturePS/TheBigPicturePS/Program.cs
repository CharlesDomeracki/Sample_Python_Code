using System;

namespace TheBigPicturePS
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please select Fahrenheight or Celsius.");
            string userSelection = Console.ReadLine();

            if (userSelection.ToUpper() == "F" || userSelection.ToUpper() == "FAHRENHEIGHT")
            {
                Console.WriteLine("Please enter a temperature in Fahrenheight");
                string userInputTemp = Console.ReadLine();
                var results = TemperatureConverisons.FahrenheightToCelsius(Convert.ToDouble(userInputTemp));
                Console.WriteLine($"{userInputTemp} is {results} degrees in Celsius");
            }

            if (userSelection.ToUpper() == "C" || userSelection.ToUpper() == "Celsius")
            {
                Console.WriteLine("Please enter a temperature in Celsius");
                string userInputTemp = Console.ReadLine();
                var results = TemperatureConverisons.CelsiusToFahrehight(Convert.ToDouble(userInputTemp));
                Console.WriteLine($"{userInputTemp} is {results} degrees in Fahrenheight");
            }
           


        }


    }
}
