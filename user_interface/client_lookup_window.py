import copy
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QVBoxLayout
from user_interface.manage_data import load_data, update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    ClientLookupWindow is a class that manages the UI for looking up clients and their associated bank accounts.
    It provides functionality to search for clients by their client number, view their associated accounts,
    apply filters to the account data, and view detailed account information.

    Attributes:
        client_listing (dict): A dictionary of clients with client numbers as keys.
        accounts (dict): A dictionary of accounts with account numbers as keys.
        lookup_button (QPushButton): A button to trigger the client lookup action.
        account_table (QTableWidget): A table widget to display account details.
        filter_button (QPushButton): A button to apply or reset filters on the account data.
        filter_combo_box (QComboBox): A combo box to select which account attribute to filter.
        filter_edit (QLineEdit): A text input to enter the filter value.
        filter_label (QLabel): A label to display the filter status.
    """

    def __init__(self):
        """
        Initializes the ClientLookupWindow, loads client and account data, 
        and sets up UI event handlers for lookup, account selection, and filtering.

        It also ensures that the filtering UI elements are configured, 
        and data is loaded properly before user interaction.
        """
        super().__init__()

        # Load client and account data
        self.client_listing, self.accounts = load_data()

        # Debugging: Check if data is loaded correctly
        print("Loaded Clients:", self.client_listing)
        print("Loaded Accounts:", self.accounts)

        # Connect UI elements to their handlers
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.account_table.cellClicked.connect(self.on_select_account)

        # Connect filter_button's clicked event to on_filter_clicked
        self.filter_button.clicked.connect(self.on_filter_clicked)

    def on_lookup_client(self):
        """
        Handles the action of looking up a client based on the client number entered in the input field.
        Retrieves the client details and their associated accounts, then updates the UI to display this data.
        
        If the client number is invalid or not found, an error message is displayed.
        """
        try:
            client_number = int(self.client_number_edit.text())  # Ensure client number is an integer
        except ValueError:
            QMessageBox.warning(self, "Non-Numeric Client", "Please enter a valid numeric client number.")
            self.reset_display()
            return

        if client_number not in self.client_listing:
            QMessageBox.warning(self, "Client Not Found", f"Client {client_number} not found.")
            self.reset_display()
            return

        # Retrieve client details and update UI
        client = self.client_listing[client_number]
        print("Client found:", client)
        self.client_info_label.setText(f"Client: {client.first_name} {client.last_name}")

        # Clear the previous account table data
        self.account_table.setRowCount(0)

        # Populate the account table with the client’s accounts
        for account in self.accounts.values():
            if account.client_number == client_number:
                print(f"Adding account: {account.account_number} for client {client_number}")
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)

                # Add account details to the table
                self.account_table.setItem(row_position, 0, QTableWidgetItem(str(account.account_number)))
                self.account_table.setItem(row_position, 1, QTableWidgetItem(f"${account.balance:,.2f}"))
                self.account_table.setItem(row_position, 2, QTableWidgetItem(account.date_created.strftime('%Y-%m-%d')))
                self.account_table.setItem(row_position, 3, QTableWidgetItem(account.__class__.__name__))

        self.account_table.resizeColumnsToContents()

        # Reset filtering state after loading new client data
        self.toggle_filter(False)

        # Enable the filter button once the client data is loaded
        self.filter_button.setEnabled(True)

    def toggle_filter(self, filter_on: bool):
        """
        Toggles the state of the filter UI elements and applies/removes the filter based on the `filter_on` flag.

        If `filter_on` is True, filter the account data based on the filter criteria. If False, reset the filter
        and show all rows.

        Args:
            filter_on (bool): A flag indicating whether the filter should be applied (True) or reset (False).
        """
        if filter_on:
            # Apply the filter
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_label.setText("Data is Currently Filtered")
            self.filter_button.setEnabled(True)

            # Hide rows that don't match the filter criteria
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

        else:
            # Reset the filter
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.clear()
            self.filter_combo_box.setCurrentIndex(0)
            self.filter_label.setText("Data is Not Currently Filtered")

            # Show all rows
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

    def on_filter_clicked(self):
        """
        Handles the action of clicking the filter button. If the filter is applied, it updates the account table
        to show only the rows that match the filter criteria. If the filter is reset, it shows all rows.

        It works by reading the user-defined filter value and the selected column to filter by, 
        then filtering the accounts displayed in the table.
        """
        if self.filter_button.text() == "Apply Filter":
            filter_value = self.filter_edit.text().strip()  # User-defined filter value
            filter_column = self.filter_combo_box.currentIndex()  # Selected column index

            # Clear the table before applying the filter
            self.account_table.setRowCount(0)

            for account in self.accounts.values():
                account_column_value = None

                if filter_column == 0:
                    account_column_value = str(account.account_number)
                elif filter_column == 1:
                    account_column_value = f"${account.balance:,.2f}"
                elif filter_column == 2:
                    account_column_value = account.date_created.strftime('%Y-%m-%d')
                elif filter_column == 3:
                    account_column_value = account.__class__.__name__

                if account_column_value and filter_value.lower() in account_column_value.lower():
                    row_position = self.account_table.rowCount()
                    self.account_table.insertRow(row_position)

                    # Add account details to the row
                    self.account_table.setItem(row_position, 0, QTableWidgetItem(str(account.account_number)))
                    self.account_table.setItem(row_position, 1, QTableWidgetItem(f"${account.balance:,.2f}"))
                    self.account_table.setItem(row_position, 2, QTableWidgetItem(account.date_created.strftime('%Y-%m-%d')))
                    self.account_table.setItem(row_position, 3, QTableWidgetItem(account.__class__.__name__))

            self.account_table.resizeColumnsToContents()

            self.toggle_filter(True)

        elif self.filter_button.text() == "Reset":
            self.reset_display()
            self.toggle_filter(False)

    def on_select_account(self, row, column):
        """
        Handles the selection of an account from the account table. When an account is selected, it opens the 
        AccountDetailsWindow to show more details about the selected account.

        Args:
            row (int): The row index of the selected account.
            column (int): The column index of the selected account.
        """
        account_number_item = self.account_table.item(row, 0)
        if account_number_item:
            account_number = int(account_number_item.text())
        else:
            QMessageBox.warning(self, "Invalid Selection", "Please select a valid account.")
            return

        if account_number in self.accounts:
            account = self.accounts[account_number]
            account_details_window = AccountDetailsWindow(account)
            account_details_window.balance_updated.connect(self.update_data)
            account_details_window.exec_()
        else:
            QMessageBox.warning(self, "Invalid Selection", "Account not found. Please select a valid account.")

    def update_data(self, account: BankAccount):
        """
        Updates the account details in the table after a transaction or modification is made in the AccountDetailsWindow.

        Args:
            account (BankAccount): The updated account object that contains the new account information.
        """
        for row in range(self.account_table.rowCount()):
            account_number_item = self.account_table.item(row, 0)
            if account_number_item and account_number_item.text() == str(account.account_number):
                self.account_table.item(row, 1).setText(f"${account.balance:,.2f}")
                self.accounts[account.account_number] = account
                update_data(account)
                break
