# Expense and Income Tracker

This is a Python-based application to track expenses and incomes, manage financial records, and generate reports. The application uses **Tkinter** for the user interface and **Pandas** for data manipulation and storage.

---

## Features

### 1. Add Financial Records
- Record details such as:
  - **Date**: Specify the date of the transaction in `YYYY-MM-DD` format.
  - **Category**: Enter the category (e.g., Food, Salary, Bills).
  - **Type**: Select whether it is an "Income" or an "Expense".
  - **Amount**: Enter the transaction amount.
  - **Description**: Optionally, add a brief description of the transaction.

### 2. Generate Reports
- View a detailed financial summary:
  - Total Income
  - Total Expense
  - Net Balance

### 3. Persistent Storage
- All records are saved in a `financial_data.csv` file for future reference and retrieval.

### 4. Clear All Data
- Delete all financial records after confirmation.

### 5. Responsive Table
- View all financial records in a scrollable table interface.

---

## Installation

### Prerequisites
- Python 3.x installed on your system.
- Required Python libraries:
  - `pandas`
  - `tkinter` (default with Python)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/lakshjain898/ExpenseTrackerApp.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ExpenseTrackerApp
   ```

3. Install required dependencies:
   ```bash
   pip install pandas
   ```

4. Run the application:
   ```bash
   python expense_tracker.py
   ```

---

## Usage

### Adding an Entry
1. Enter the date in the `YYYY-MM-DD` format.
2. Provide a category (e.g., "Food", "Rent").
3. Select the type (Income/Expense).
4. Enter the amount as a numeric value.
5. Add an optional description.
6. Click the **Add Entry** button to save the record.

### Generating Reports
- Click the **Generate Report** button to view:
  - Total Income
  - Total Expense
  - Net Balance

### Clearing All Data
- Click the **Clear All Data** button to delete all financial records. Confirm the action when prompted.

---

## File Structure
```
ExpenseTrackerApp/
├── financial_data.csv       # Stores all financial records
├── expense_tracker.py       # Main application file
├── README.md                # Documentation file
```

---

## Future Improvements
- Add category-specific reports.
- Include graphical visualizations for financial trends.
- Add the ability to edit and delete individual records.
- Implement user authentication for secure access.

---

## Contributing
Feel free to fork this repository, create new branches, and submit pull requests for any improvements or bug fixes.

---
