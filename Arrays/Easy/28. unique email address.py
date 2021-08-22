# Problem disc: https://leetcode.com/problems/unique-email-addresses/

def solve(emails):
    unique = set()
    for eID in emails:
        name, domain = eID.split('@')
        username = name.split('+')[0].replace('.', '')
        newEmail = username + '@' + domain
        
        if newEmail not in unique:
            unique.add(newEmail)
    return len(unique)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",
"testemail+david@lee.tcode.com"]
print(solve(emails))

