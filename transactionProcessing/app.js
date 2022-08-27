console.log("Loading function")

exports.lambda_handler = async(event) => {
    // console.log("receive:", JSON.stringify(event,null,2))
    for (const { messageId, body} of event.Records){
        console.log("SQS message is %s:", messageId, body);
    }
    return `Successfully processed ${event.Records.length} messages.`
}