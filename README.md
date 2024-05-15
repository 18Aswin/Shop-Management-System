# Shop Management System

The Shop Management System is a Python-based application designed to facilitate inventory management and customer transactions for a shop. It consists of three main files: `Add_to_Database.py`, `update.py`, and `customer.py`.

- `Add_to_Database.py`: Allows the shopkeeper to add products into the inventory table of the SQLite database.
- `update.py`: Enables the shopkeeper to update the stock, price, and other information related to products.
- `customer.py`: Used by customers to make purchases. It adds selected items to a list, calculates the total, handles payment, generates a bill, and records transactions in the SQLite database.

The program utilizes Python and Tkinter for the graphical user interface (GUI) to provide an intuitive and user-friendly experience.

## Features

- **Inventory Management**: Shopkeeper can add and update products in the inventory.
- **Customer Transactions**: Customers can select items, calculate the total, make payments, and generate bills.
- **Database Integration**: Records of transactions are stored in the SQLite database for future reference.
- **Bill Generation**: Generates physical copies of bills in the 'invoice' folder.

## Files

- **Add_to_Database.py**: Add products to the inventory table.
- **Update.py**: Update stock, price, and other product information.
- **Customer.py**: Interface for customer transactions.

## Dependencies

- Python 3.0
- Tkinter (Python GUI library)
- SQLite (Database management system)

## Usage

1. Clone the repository:

```
git clone https://github.com/18Aswin/Shop-Management-System.git
```

2. Run `Add_to_Database.py` to add products to the inventory initially.
3. Use `update.py` to update stock, price, or other information as needed.
4. Customers can make purchases using `customer.py`.
5. Bills will be generated in the 'invoice' folder, and transaction records will be stored in the SQLite database.

## Database Schema

The database schema consists of at least two tables:
1. **Inventory**: Contains information about available products.
2. **Transactions**: Stores records of customer transactions.

## Note

- Ensure all dependencies are installed before running the application.
- Make sure the database connection details are correctly configured in each file.
- Customize the GUI and functionality as per specific shop requirements.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or create a pull request.

## About

The Shop Management System Application is developed and maintained by Aswin A Nair. Feel free to reach out with any questions or feedback.

---

Streamline your shop's operations with the Shop Management System! If you have any questions or encounter any issues, don't hesitate to contact us.
