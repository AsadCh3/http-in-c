from flask import Flask, jsonify

app = Flask(__name__)

orders = [
	{
		"order_id": 1,
		"product_name": "Fruitamin Orange",
		"customer_name": "John Flask"
	},
	{
		"order_id": 2,
		"product_name": "Nestle Milkpack",
		"customer_name": "Rais M"
	},
	{
		"order_id": 3,
		"product_name": "Nestle Milo",
		"customer_name": "Joseph W"
	},
	{
		"order_id": 4,
		"product_name": "RedBull Drink",
		"customer_name": "Albert C"
	},
	{
		"order_id": 2,
		"product_name": "Fruitamin Mango",
		"customer_name": "Martin D"
	}
]


@app.route('/getOrders', methods=['GET'])
def get_orders():
	return jsonify(orders)


if __name__ == "__main__":
	app.run(debug=True)
