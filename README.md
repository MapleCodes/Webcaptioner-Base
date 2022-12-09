# Flask-WebCaptioner
This is a simple Flask app that uses the Flask web framework to create a web app. It then grabs the Webhook from WebCaptioner and prints the data to the console.
From there, feel free to do anything to your hearts content with WebCaptioner.

### How to use
 1. Install the required dependencies
 2. Run the `app.py` file
 3. Go to the **WebCaptioner** website and create a new project, be aware of the `CHUNKING`!
 4. Add the webhook to the project based on the `ROUTE` and `PORT` variables:

> Example: http://localhost:52842/listener

ROUTE = `"listener"` 
PORT =    `52842`

 5. Start the project
 2. Edit to your heart's content
 3. Profit!
 
 ### Example Setup from WebCaptioner

![image](https://user-images.githubusercontent.com/96672739/206719934-ddde8e69-90d3-481b-8888-6e208fd8b992.png)
