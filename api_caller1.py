import requests 
import simplejson as json
import xml.etree.ElementTree as ET
import re

def contlength(inp):
	return len(inp.encode('utf-8'))
# url1 = 'https://sandbox.api.mastercard.com/moneysend/v2/mapping/card?Format=XML'
# url2 = 'https://api.mastercard.com/moneysend/v2/mapping/card?Format=XML'
def create_mapping_id(filename, accType, alias='x', subsID='13147449993', subsType='SOCIAL_NETWORK', ica='009674', accno='5184680430000006', expdate='201801',fname='John', mname='Q', lname='Public', address={'l1':'123 Main Street', 'l2': '#5A', 'city' : 'Somewhere', 'state' : 'MO', 'PostalCode' : '69999', 'Country' : 'USA'}, dob='19460102'):
	url3 = 'http://dmartin.org:8026/moneysend/v2/mapping/card?Format=JSON'
	payload = """<CreateMappingRequest>
		<SubscriberId>"""+subsID+"""</SubscriberId>
		<SubscriberType>"""+subsType+"""</SubscriberType>
		<AccountUsage>"""+accType+"""</AccountUsage>
		<DefaultIndicator>T</DefaultIndicator>
		<Alias>"""+alias+"""</Alias>
	 	<ICA>"""+ica+"""</ICA>
		<AccountNumber>"""+accno+"""</AccountNumber>
	 		<ExpiryDate>"""+expdate+"""</ExpiryDate>
		<CardholderFullName>
	 		<CardholderFirstName>"""+fname+"""</CardholderFirstName>
			<CardholderMiddleName>"""+mname+"""</CardholderMiddleName>
			<CardholderLastName>"""+lname+"""</CardholderLastName>
	 		</CardholderFullName>
		<Address>
				<Line1>"""+address['l1']+"""</Line1>
	 			<Line2>"""+address['l2']+"""</Line2>
	 			<City>"""+address['city']+"""</City>
				<CountrySubdivision>"""+address['state']+"""</CountrySubdivision>
	 			<PostalCode>"""+address['PostalCode']+"""</PostalCode>
				<Country>"""+address['Country']+"""</Country>
	 	</Address>
	 	<DateOfBirth>"""+dob+"""</DateOfBirth>
	</CreateMappingRequest>"""
	length = contlength(payload)
	headers = {'content-type' : 'application/xml', 'content-length' : length}

	r = requests.post(url3, data=payload, headers=headers)
	res = r.json()
	mapid = res['CreateMapping']['Mapping']['MappingId']
	with open('./datafiles/'+filename+'.json', 'w') as outfile:
		json.dump({'name' : fname + " " + lname, 'mapid' : mapid, 'susbid' : subsID}, outfile)

def create_send_user(filename, fname, lname, provID):
	create_mapping_id(filename, 'SENDING', subsID= provID,fname=fname, lname=lname)

def create_receive_user(filename, fname, lname, provID):
	create_mapping_id(filename, 'RECEIVING', subsID= provID,fname=fname, lname=lname)

# create_receive_user('Middleman_recv','Assassins', 'Creed', 'a129xmaskar3')

def transfer():
	url10 = 'http://dmartin.org:8026/moneysend/v2/transfer?Format=XML'
	payload = """
<TransferRequest>
    <LocalDate>0612</LocalDate>
    <LocalTime>161222</LocalTime>
    <TransactionReference>4100768010101010220</TransactionReference>
    <FundingMapped>
        <SubscriberId>13145551234</SubscriberId >
        <SubscriberType>PHONE_NUMBER</SubscriberType >
        <SubscriberAlias>My Debit Card2</SubscriberAlias>
    </FundingMapped>
 
    <ReceivingMapped>
        <SubscriberId>13145551212</SubscriberId >
        <SubscriberType>PHONE_NUMBER</SubscriberType >
        <SubscriberAlias>My Debit Card2</SubscriberAlias>
    </ReceivingMapped>

    <FundingAmount>
        <Value>15000</Value>
        <Currency>840</Currency>
    </FundingAmount>
    
    <ReceiverPhone>1800639426</ReceiverPhone>
    <ReceivingAmount>
        <Value>182206</Value>
        <Currency>484</Currency>
    </ReceivingAmount>
    <Channel>W</Channel>
    <UCAFSupport>true</UCAFSupport>
    <ICA>009674</ICA>
    <ProcessorId>9000000442</ProcessorId>
    <RoutingAndTransitNumber>990442082</RoutingAndTransitNumber>
    <CardAcceptor>
        <Name>My Local Bank</Name>
        <City>Saint Louis</City>
        <State>MO</State>
        <PostalCode>63101</PostalCode>
        <Country>USA</Country>
    </CardAcceptor>
    <TransactionDesc>P2P</TransactionDesc>
    <MerchantId>123456</MerchantId>
</TransferRequest>"""
	headers = {'content-type' : 'application/xml', 'content-length' : contlength(payload)}
	r = requests.post(url10, data=payload, headers=headers)
	print (r.text)

def inquire(subid):
	url5 = 'http://dmartin.org:8026/moneysend/v2/mapping/card?Format=XML'
	payload = """<InquireMappingRequest>
        <SubscriberId>"""+subid+"""</SubscriberId>
        <SubscriberType>SOCIAL_NETWORK</SubscriberType>
</InquireMappingRequest>"""
	headers = {'content-type' : 'application/xml', 'content-length' : contlength(payload)}
	r = requests.put(url5, data=payload, headers=headers)

	print (r.text)
# inquire('21100')


transfer()