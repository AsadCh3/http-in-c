from flask import Flask, jsonify

app = Flask(__name__)

orders = [
	{
		"order_id": 1,
		"product_name": "Fruitamin Orange",
		"customer_name": "John Flask"
	},
	{
		"order_id": 1,
		"product_name": "Fruitamin Orange",
		"customer_name": "John Flask"
	},
	{
		"order_id": 1,
		"product_name": "Fruitamin Orange",
		"customer_name": "John Flask"
	},
	{
		"order_id": 1,
		"product_name": "Fruitamin Orange",
		"customer_name": "John Flask"
	},
	{
		"order_id": 1,
		"product_name": "Fruitamin Orange",
		"customer_name": "John Flask"
	}
]


@app.route('/getOrders', methods=['GET'])
def get_orders():
	return jsonify(orders)


if __name__ == "__main__":
	app.run(debug=True)
