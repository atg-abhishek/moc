import simplify
import simplejson as json

with open('simplify_keys.json') as infile: 
	keys = json.load(infile)

public_key =  keys['public_key']
private_key =  keys['private_key']
simplify.public_key = public_key
simplify.private_key = private_key

def token_generate():
	

def payment_create(token, amount=100, desc="test", curr="USD"):

	payment = simplify.Payment.create({
	        "token" : token,
	        "amount" : amount,
	        "description" : desc,
	        "currency" : curr
	})
	if payment.paymentStatus == 'APPROVED':
	    print "Payment approved"
