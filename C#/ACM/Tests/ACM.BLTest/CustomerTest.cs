using Microsoft.VisualStudio.TestTools.UnitTesting;
using ACM.BL;
using System;

namespace ACM.BLTest
{
    [TestClass]
    public class CustomerTest
    {
        [TestMethod]
        public void FullNameTestValid()
        {
            //-- Arrange
            Customer customer = new Customer();
            customer.FirstName = "Mark";
            customer.LastName = "Domeracki";

            string expected = "Domeracki, Mark";

            //-- Act
            string actual = customer.FullName;

            //-- Assert
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void FullNameFirstNameEmpty()
        {
            //-- Arrange
            Customer customer = new Customer
            {
                FirstName = "Mark"
            };
            string expected = "Mark";
            //-- Act
            string actual = customer.FullName;
            //-- Assert
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void FullNameLastNameEmpty()
        {
            //-- Arrange
            Customer customer = new Customer
            {
                LastName = "Domeracki"
            };
            string expected = "Domeracki";
            //-- Act 
            string actual = customer.FullName;
            //-- Assert
            Assert.AreEqual(expected, actual);

        }
        
        [TestMethod]
        public void StaticTest()
        {
            //-- Arrange
            var c1 = new Customer();
            c1.FirstName = "Mark";
            Customer.InstanceCount += 1;

            var c2 = new Customer();
            c2.FirstName = "Abbie";
            Customer.InstanceCount += 1;

            var c3 = new Customer();
            c3.FirstName = "Mandy";
            Customer.InstanceCount += 1;
            //-- Act
            //-- Assert
            Assert.AreEqual(3, Customer.InstanceCount);
        }
        

        [TestMethod]
        public void ValidateValid()
        {
            //- Arrange 
            var customer = new Customer
            {
                LastName = "Domeracki",
                EmailAddress = "domerackimark@gmail.com"
            };

            var expected = true;

            //-- Act 
            var actual = customer.Validate();

            //-- Assert
            Assert.AreEqual(expected, actual);
        }


        [TestMethod]
        public void ValidateMissingLastName()
        {
            //-- Arragne
            var customer = new Customer
            {
                EmailAddress = "domerackimark@gmail.com"
            };
            var expected = false;
            //-- Act
            var actual = customer.Validate();
            //-- Assert
            Assert.AreEqual(expected, actual);

        }
    }
}
