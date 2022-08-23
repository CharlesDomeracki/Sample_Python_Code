using Microsoft.VisualStudio.TestTools.UnitTesting;
using ACM.BL;
using System;

namespace ACM.BLTest
{
    [TestClass]
    public class ProductTest
    {
        [TestMethod]
        public void ProductNameTestValid()
        {
            //-- Arrange
            Product product = new Product();
            product.ProductName = "Test Product";

            string expected = "Test Product";
            //-- Act
            string actual = product.ProductName;
            //-- Assert
            Assert.AreEqual(expected, actual);
        }       
    }
}
