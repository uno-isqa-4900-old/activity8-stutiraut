#Python program to create Customer Viewer application
import csv

#prints the title
print("Customer Viewer")
print()
choice = "y"
while choice.lower() == "y":

    #Created Customer class
    class Customer:

            #Defined the constructor with the given attributes
            def __init__(self, cust_id, first_name, last_name, company_name, address, city, state, zip):
                self.cust_id = cust_id
                self.first_name = first_name
                self.last_name = last_name
                self.company_name = company_name
                self.address = address
                self.city = city
                self.state = state
                self.zip = zip

            #Created a method that returns the full address
            def get_address(self):
                #address is used as a variable
                #prints first and last name
                address = self.first_name + " " + self.last_name + "\n"
                #if condition where the address prints three lines if there is no company
                # and four lines if there is company name
                if self.company_name != "":
                    address = address + self.company_name + "\n"
                address = address + self.address + "\n" + self.city + ", " + self.state + " " + self.zip
                return address

            #Defined find_customer function
            def find_customer(self, id):
                customers = []
                with open('customers.csv', newline='') as csv_file:
                    #reads the customer data from a CSV file
                    reader = csv.reader(csv_file)
                    for row in reader:
                        #created customer object
                        customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                        customers.append(customer)

                #check whether the specified ID matches the ID stored in the Customer object.

                for customer in customers:
                    if customer.cust_id == id:
                        #if id matches, it prints the address
                        print(customer.get_address())
                        print()
                        return
                #or else prints the given statement
                print("No customer with that id")
                print()

    if __name__ == "__main__":
        #customer object with blank attributes
        customer = Customer ("","","","","","","","")
        #user inputs the id
        id = str(input("Enter customer ID: "))
        print()
        ##call to customer function
        customer.find_customer(id)
        # Ask user if they want to continue
        choice = input("Continue(Y/N)?:")
        print()

print("BYE")




