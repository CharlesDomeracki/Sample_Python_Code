using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ACM.BL
{
    public class CustomerRepository
    {
        public Customer Retrive(int customerId)
        {
            Customer customer = new Customer(customerId);

            if (customerId == 1)
            {
                customer.EmailAddress = "domerackimark@gmail.com";
                customer.FirstName = "Mark";
                customer.LastName = "Domeracki";
            }

            return customer;
        }

        public bool Save(Customer customer)
        {
            return true;
        }
    }
}
