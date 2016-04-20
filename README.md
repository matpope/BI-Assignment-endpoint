BI-Assignment-endpoint" 
=============

For this task I used Python and Flask-RESTful. Pre-isntallation requirements:

1. Python
2. PIP install
3. Flask-RESTful

Details about Flask can be found here:
http://codehandbook.org/creating-restful-api-using-python-flask-mysql/

For testing I used:
Postman chrome extension

Testing, for e.g. hotel_id=25, checkin 2015-11-12 and CheckOut 2015-11-13:

http://localhost:5000/offer/best-deal?param1=25&param2=2015-11-12&param3=2015-11-13

{  

  "offerId": 136986160,
  
  "hotelId": 25,
  
  "checkinDate": "2015-11-12",
  
  "checkoutDate": "2015-11-13",
  
  "currencyCode": "USD",
  
  "sellingPrice": "72.85"
  
}

Test with an invalid hotel_id(-1)
http://localhost:5000/offer/best-deal?param1=-1&param2=2015-11-12&param3=2015-11-13

Result:

{
  "Message": "no Deal found",
  
  "StatusCode": "1000"
  
}

####Limitations
I have not implementation and safeguards against sql injection and other types of attacks.
