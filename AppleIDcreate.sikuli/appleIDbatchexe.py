import os
import sys
import csv
idIndex = 1
csvRead = []
csvReader = csv.reader(open('/Users/318admin/Desktop/ids.csv'))
for row in csvReader:
    csvRead.append(row)
while idIndex < len(csvRead):
    appleid = str(csvRead[idIndex][0])
    password = str(csvRead[idIndex][1])
    birthMonth = str(csvRead[idIndex][2])
    birthDay = str(csvRead[idIndex][3])
    birthYear = str(csvRead[idIndex][4])
    firstName = str(csvRead[idIndex][5])
    lastName = str(csvRead[idIndex][6])
    streetAddress = str(csvRead[idIndex][7])
    city = str(csvRead[idIndex][8])
    stateCode = str(csvRead[idIndex][9])
    zipCode = str(csvRead[idIndex][10])
    areaCode = str(csvRead[idIndex][11]) 
    phoneNum = str(csvRead[idIndex][12])
    openApp("iTunes")
    click("Screen Shot 2013-01-08 at 9.36.17 AM.png")
    type("iBooks"+Key.ENTER)
    # clear search field, just 'cause
    click("1357656258285.png")
    onAppear("iPadAppsEBoo.png", click("LiBooksBooks.png"))
    # appleID login should appear
    wait("SignIntodown.png")
    click("CreateAppleI.png")
    wait("IDclickcanon.png", 12)
    click("IDclickcanon.png")
    wait("innrirnnrntn.png", 12)
    click("innrirnnrntn.png")
    # accept terms checkbox
    click("1357656934662.png")
    # big details form
    wait("EmailemaiIex.png", 12)
    type("EmailemaiIex.png", appleid + Key.TAB + password + Key.TAB + password + 
            Key.TAB + Key.DOWN + Key.DOWN + Key.ENTER + Key.TAB + "Newton" +
            Key.TAB + Key.DOWN + Key.DOWN + Key.ENTER + Key.TAB + "Apple" +
            Key.TAB + Key.DOWN + Key.DOWN + Key.DOWN + Key.ENTER + Key.TAB + "Steve" +
            Key.TAB + Key.TAB + birthMonth + Key.ENTER + Key.TAB +
            birthDay + Key.ENTER + Key.TAB + birthYear)
    click("WouldNeldMn.png")
    click("NlNi.png")
    type(Key.PAGE_DOWN)
    click("1357659787705.png")
    wait("sclickhereal.png", 12)
    click("BillingAddre.png")
    click("Screen Shot 2013-01-08 at 12.52.37 PM.png")
    type("BillingAddre-1.png", firstName + Key.TAB + lastName + Key.TAB + streetAddress +
             Key.TAB + Key.TAB + city + Key.TAB + stateCode + Key.TAB + zipCode +
             Key.TAB + areaCode + Key.TAB + phoneNum)
    
    click("CreateAppleI-1.png")
    wait("1357672144168.png", 12)
    idIndex += 1