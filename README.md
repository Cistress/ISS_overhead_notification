A small follow along project where I will get an email notification if ISS is overhead and the sky is dark for me to spot it by utilizing libraries such as requests and smtplib. 

By storing daytime and current ISS position in a JSON format using requests, I was able to manipulate current informations of both to iterate through the condtions mentioned in line 1. 

The conditions will be tested every minute and if both conditions are matched, then a email will be sent to notify the user. 

Note that the password in my script is just a random combination and not the actual App Password that is required to gain access to my gmail. Modify as needed :). 


