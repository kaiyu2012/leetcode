
from typing import List
import datetime

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        newList = []
        for i in range(len(emails)):
            email = emails[i].split('@')
            emailName = email[0].split('+')
            userNameSplit = emailName[0].split('.')
            userNameSplit.append("@")
            userNameSplit.append(email[1])
            emailAddress = ""
            emailAddress =  emailAddress.join(userNameSplit)
            if emailAddress not in newList:
                newList.append(emailAddress)

        return len(newList)
            
    
        



def main():
    start_time = datetime.datetime.now().replace(microsecond=0)

    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    email = emails[0].split('@')
    emailName = email[0].split('+')
    emailTitle = emailName[0].split('.')
    userName = ""

    userName = userName.join(emailTitle)
    x = [userName, "@", email[1]]
    y = ""
    y = y.join(x)

    
    
    
    print(email)
    print(emailName)
    print(emailTitle)
    print(userName)
    print(y)

    stop_time = datetime.datetime.now().replace(microsecond=0)

    print(f'Total time used: {stop_time - start_time}')


if __name__ == "__main__":
    main()