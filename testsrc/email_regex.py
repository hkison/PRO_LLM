#Extrahieren Sie alle E-Mail-Adressen aus dem folgenden Text

text = "E-Mail-Liste: max.mustermann@gmail.com, anna.schmidt@yahoo.de, info@firma.org"


#write your code here
def extract_emails(text):
    return

#this is the test cases
try:
    assert extract_emails(text) == ['max.mustermann@gmail.com', 'anna.schmidt@yahoo.de', 'info@firma.org']
    print("Test passed!")
except AssertionError:
    print("Test failed!")