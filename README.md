# Discount Calculator

## Overview
This Python script calculates the final price of an item after applying a discount. The discount is applied only if the discount percentage is 20% or higher. If the discount is less than 20%, the original price is returned without any discount.

## Features
- Takes user input for the original price and discount percentage.
- Applies discount based on the specified condition (20% or higher).
- Prints the final price formatted to two decimal places.

## How to Use
1. Run the script.
2. Enter the price of the item when prompted.
3. Enter the discount percentage when prompted.
4. The script will calculate and display the final price after applying the discount.

## Code Explanation

### Apply discount if discount_percent is 20 or greater
if discount_percent >= 20:
    finalPrice = price - discount
else:
    finalPrice = price
    
return finalPrice


#### Notes
- Make sure to enter valid numeric values for price and discount percentage.
- The output price is shown in Kenyan Shillings (Ksh).
- Discounts below 20% will not be applied as per the program logic.

## License
This project is provided as-is for educational purposes.

