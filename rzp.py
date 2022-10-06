import razorpay
import string
import random

from flask import Flask, render_template
client = razorpay.Client(auth=("rzp_test_jmo9zQ3obMeuLP", "gjjiadWIaAX1izDhPwRT3AEA"))

app = Flask(__name__)

@app.route("/payment")
def welcome():
    res = 'stockify_'+''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=10))
    receipt = str(res)
    data = { "amount": 999*100, "currency": "INR", "receipt": str(res) }
    payment = client.order.create(data=data)
    id = str(payment["id"])
    print(id)
    return render_template("payment.html", id=id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8012)

