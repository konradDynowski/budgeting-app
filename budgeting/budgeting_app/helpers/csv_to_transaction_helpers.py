class Csv_To_Transaction_Helper:
    
    def __init__(self):
        self.csv_transactions = []


    def proces_mbank_payload(self, csv_file):
        found_transactions = False
        lines = csv_file.splitlines()

        for line in lines:
            if not found_transactions:
                found_transactions = "#Data operacji;" in line
                continue 
                # if not found_transactions:
                    # continue

            if ";" in line:
                self.process_transaction(line)

        return self.csv_transactions


    def process_transaction(self, transaction_csv_row):
        if not ";" in transaction_csv_row:
            return None
        
        transaction_columns = transaction_csv_row.split(";")
        self.csv_transactions.append(
                self.Csv_Transaction(
                    transaction_columns[0],
                    transaction_columns[1],
                    transaction_columns[4],
                    )
                )

    class Csv_Transaction:
        def __init__(self, date, description, amount):
            self.date = date
            self.description = description
            self.amount = float(amount.replace(",", ".").replace("PLN", "").replace(" ", "").strip()) 

        

        def __str__(self):
            return "DATE:{}\tDESC:{}\tAMOUNT:{}\n".format(self.date, self.description, self.amount)
