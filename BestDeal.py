from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
# from flask.ext.mysql import MySQL
import mysql.connector

config = {
  'user':'root', 
  'password':'admin', 
  'host':'localhost', 
  'database':'bi_data',
  'raise_on_warnings': True,
}
	 
app = Flask(__name__)
api = Api(app)

# mysql.init_app(app)

class BestDeal(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('param1', type=int, help='Hotel Id to search for')
            parser.add_argument('param2', type=str, help='Check In Date to search for')
            parser.add_argument('param3', type=str, help='Check Out Date to search for')
            args = parser.parse_args()

            # Connect to mysql
            cnx = mysql.connector.connect(**config)
            crsr = cnx.cursor()

            # Execute Query
            crsr.execute("SELECT offer_id, hotel_id, cast(checkin_date as char) as checkin_date, cast(checkout_date as char) as checkout_date, round(min(price_usd),2) as sellingprice FROM bi_data.valid_offers WHERE hotel_id = %s AND checkin_date = %s AND checkout_date= %s", (args['param1'],args['param2'],args['param3'],))
            resultset = crsr.fetchall()	

            # Retrieve Resultset
            for row in resultset:
                offer_id=row[0]
                hotel_id=row[1]
                checkin_date=row[2]
                checkout_date=row[3]
                sellingprice=str(row[4])
            crsr.close()
            cnx.close()

            # If no deal found return StatuCode 1000
            if offer_id is None:
              return {'StatusCode':'1000','Message': 'no Deal found'}
            else:
              return {"offerId":offer_id,'hotelId':hotel_id,'checkinDate':checkin_date,'checkoutDate':checkout_date,'sellingPrice':sellingprice,'currencyCode':'USD'} 
        except Exception as e:
            return {'error': str(e)}
			
api.add_resource(BestDeal, '/offer/best-deal')			
			
if __name__ == '__main__':
    app.run(debug=True)			