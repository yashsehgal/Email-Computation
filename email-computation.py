import pandas as pandas
import matplotlib.pyplot as plt
from csv import DictWriter
import requests as rqst     # for calling APIs from various web-services

class EmailClassification:

  def __init__(self, activity):
    self.activity = activity
  
  def interface(self):
    # interface model
    self.menuChoice = ""
    while(self.menuChoice != "exit"):
      print("EMAIL CLASSIFICATION PROGRAM") 
      print("Type \"add\" to add an email address")
      print("Type \"show\" to show the email address records")
      print("Type \"data\" to show the statistics")
      print("Type \"exit\" to close the program")

      self.menuChoice = input("Enter your choice> ")

      if self.menuChoice == "add":
        # add function
        # class method interface
        # name: addNewRecord()
        self.addNewRecord()
      elif self.menuChoice == "show":
        # show function
        # class method interface
        # name: showRecord()
        self.showRecord()
      elif self.menuChoice == "data":
        # data function
        # class method interface
        # name: showUsageGraph()
        self.showUsageGraph()
      elif self.menuChoice == "exit":
        print("THANKS FOR USING!")
      else:
        print("Select a valid option...")

  def addNewRecord(self):
    self.emailAddress = input("enter email address> ")
    # username for email address
    self.username = ""
    self.companyName = ""
    self.domainName = ""

    # fetching username from the email address
    for value in range(len(self.emailAddress)):
      if (self.emailAddress[value] != '@'):
        # self.username.append(self.emailAddress[value])
        self.username += self.emailAddress[value]
      else:
        break

    # fetching companyName from the email address
    for value in range(len(self.emailAddress)):
      if (self.emailAddress[value] != '.'):
        # self.companyName.append(self.emailAddress[value])
        self.username += self.emailAddress[value]
      else:
        break

    # fetching domain name from the email address
    for value in range(len(self.emailAddress)):
      if (self.emailAddress[value] != '\0'):
        # self.domainName.append(self.emailAddress[value])
        self.domainName += self.emailAddress[value]
      else:
        break
    # saving data in the csv file
    # appending username in a specific username file named: username_list.csv
    # username_list = pandas.read_csv("username_list.csv", delimiter=",", self.username)
    username_set = []
    with open('username_list.csv', 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames='emails')     # object constructing statement
        # Add dictionary as work in the csv
        username_set.append(dict_writer)
        dict_writer.writerow(username_set)
    # appending source/company name in a specific file named: company_name_list.csv
    with open('company_name_list.csv', 'a+', newline='') as write_obj:
      # Create a writer object from csv module
      dict_writer = DictWriter(write_obj)
      # Add dictionary as work in the csv
      dict_writer.writerow(self.companyName)
    # appending domain_name in a specific file named: domain_list.csv
    with open('domain_list.csv', 'a+', newline='') as write_obj:
      # Create a writer object from csv module
      dict_writer = DictWriter(write_obj)
      # Add dictionary as work in the csv
      dict_writer.writerow(self.domainName)   
    # appending the complete email address as a string in a specific file named: email_address_list.csv
    with open('email_address_list.csv', 'a+', newline='') as write_obj:
      # Create a writer object from csv module
      dict_writer = DictWriter(write_obj)
      # Add dictionary as work in the csv
      dict_writer.writerow(self.emailAddress)

  def showRecord(self):
    self.showMenuChoice = ""
    while self.showMenuChoice != "exit":
      print("EMAIL RECORDS")
      print("Type \"email\" to see the email address")
      print("Type \"username\" to see the usernames")
      print("Type \"source\" to see the source names")
      print("Type \"domain\" to see the domains")
      print("Type \"exit\" to exit this menu")
      self.showMenuChoice = input("Select an option> ")

      # conditional functionality
      if self.showMenuChoice == "email":
        # show full email list
        with open('email_address_list.csv', 'a+', newline='') as write_obj:
          # Create a writer object from csv module
          dict_writer_for_email_address = DictWriter(write_obj)
          print(dict_writer_for_email_address)
      elif self.showMenuChoice == "username":
        # show all username list
        with open('username_list.csv', 'a+', newline='') as write_obj:
          # Create a writer object from csv module
          dict_writer_username = DictWriter(write_obj)
          print(dict_writer_username)
      elif self.showMenuChoice == "source":
        # show usernames list
        with open('company_name_list.csv', 'a+', newline='') as write_obj:
          # Create a writer object from csv module
          dict_writer_for_company = DictWriter(write_obj)
          print(dict_writer_for_company)
      elif self.showMenuChoice == "domain":
        # show domain name list
        with open('domain_list.csv', 'a+', newline='') as write_obj:
          # Create a writer object from csv module
          dict_writer_for_domain = DictWriter(write_obj)
          print(dict_writer_for_domain) 
      elif self.showMenuChoice == "exit":
        print("EXITING...")
      else:
        print("PLEASE SELECT A VALID OPTION")

  def showUsageGraph(self):
    # graphs, hell yeah
    self.stat_choice = ""
    while self.stat_choice != "exit":
      print("GRAPHS AND STATISTICS")
      print("Type \"username\" to see the username statistics")
      print("Type \"source\" to see the source/company statistics")
      print("Type \"domain\" to see the domain statistics")
      print("Type \"exit\" to exit this menu")

      self.stat_choice = input("Select an option> ")

      if self.stat_choice == "username":
        # username stats
        self.getUsernameStatistics()
      elif self.stat_choice == "source":
        # source stats
        self.getSourceStatistics()
      elif self.stat_choice == "domain":
        # domain stats
        self.getDomainStatistics()
      elif self.stat_choice == "exit":
        print("EXITING MENU...")
      else:
        print("PLEASE SELECT A VALID OPTION")
  
  def getUsernameStatistics(self):
    self.username_set = []
    with open('username_list.csv', 'a+', newline='') as write_obj:
      dict_writer = DictWriter(write_obj)
      username_set.append(len(dict_writer))

    # generating graphs
    plt.plot(username_set)
    plt.title("Username Statistics")
    plt.xlabel("Username Lengths")
    plt.ylabel("Amount")
    plt.show()

  def getSourceStatistics(self):
    source_set = []
    gmail_accounts = 0
    yahoo_accounts = 0
    hotmail_accounts = 0
    orchid_accounts = 0
    apple_accounts = 0
    rediffmail_accounts = 0
    microsoft_accounts = 0
    bing_accounts = 0
    other_accounts = 0

    with open('company_name_list.csv', 'a+', newline='') as write_obj:
      dict_writer = DictWriter(write_obj)
      source_set.append(dict_writer)

      # fetching source names at different conditions
      if dict_writer == "gmail":
        gmail_accounts += 1
      elif dict_writer == "yahoo":
        yahoo_accounts += 1
      elif dict_writer == "hotmail":
        hotmail_accounts += 1
      elif dict_writer == "orchid":
        orchid_accounts += 1
      elif dict_writer == "apple":
        apple_accounts += 1
      elif dict_writer == "rediffmail":
        rediffmail_accounts += 1
      elif dict_writer == "microsoft":
        microsoft_accounts += 1
      elif dict_writer == "bing":
        bing_accounts += 1
      else:
        other_accounts += 1

    # generating graphs
    plt.plot(gmail_accounts)
    plt.plot(yahoo_accounts)
    plt.plot(hotmail_accounts)
    plt.plot(orchid_accounts)
    plt.plot(apple_accounts)
    plt.plot(rediffmail_accounts)
    plt.plot(microsoft_accounts)
    plt.plot(bing_accounts)
    plt.plot(other_accounts)
    plt.title("Source Provider Statistics")
    plt.xlabel("Source Names")
    plt.ylabel("Amount")
    plt.legend(["Gmail", "Yahoo", "Hotmail", "Orchid", "Apple", "Rediffmail", "Microsoft", "Bing", "Others"])
    plt.show()

  def getDomainStatistics(self):
    domain_set = []
    _com = 0
    _org = 0
    _io = 0
    _co = 0
    _in = 0
    _ca = 0
    _uk = 0
    _us = 0
    other = 0

    with open('domain_list.csv', 'a+', newline='') as write_obj:
      dict_writer = DictWriter(write_obj)
      domain_set.append(dict_writer)

      # fetching domain names from the list at different conditions
      if dict_writer == "com":
        _com += 1
      elif dict_writer == "org":
        _org += 1
      elif dict_writer == "io":
        _io += 1
      elif dict_writer == "co":
        _co += 1
      elif dict_writer == "in":
        _in += 1
      elif dict_writer == "ca":
        _ca += 1
      elif dict_writer == "uk":
        _uk += 1
      elif dict_writer == "us":
        _us += 1
      else:
        other += 1
      

      # plotting data-values in the graph
      plt.plot(_com)
      plt.plot(_org)
      plt.plot(_io)
      plt.plot(_co)
      plt.plot(_in)
      plt.plot(_ca)
      plt.plot(_uk)
      plt.plot(_us)
      plt.plot(other)
      plt.title("Domain Usage Statistics")
      plt.xlabel("Domain Names")
      plt.ylabel("Amount")
      plt.legend(["COM", "ORG", "IO", "CO", "IN", "CA", "UK", "US", "Others"])
      plt.show()

def connector():
  # activating the connection for the EmailClassification Class Method
  emailConnector = EmailClassification(True)
  emailConnector.interface()

if __name__ == "__main__":
    connector()
