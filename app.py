import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitorCounterTable')
def lambda_handler(event, context):
    response = table.get_item(Key={
        'visitor_id':'VisitorCount'
    })
    item = response["Item"]
    views = response['Item']['visitor_counter']
    views = views + 1
    print(views)
    response = table.put_item(Item={
        'visitor_id':'VisitorCount',
        'visitor_counter':views
    })
    
    return{
            "statusCode": 200,
            "headers": {
                "body":"This is working as expected from AWS Lambda integration with GitHub Actions",
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
          "body": json.dumps({"Visit_Count": str(item["visitor_counter"] + 1)})
    }