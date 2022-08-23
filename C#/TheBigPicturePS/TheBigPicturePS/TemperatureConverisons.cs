using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TheBigPicturePS
{
    public class TemperatureConverisons
    {
        public static double FahrenheightToCelsius(double temp)
        {
            return Math.Round((temp - 32) / 1.8);
        }

        public static double CelsiusToFahrehight(double temp)
        {
            return (1.8 * temp) + 32;
        }
    }
}
