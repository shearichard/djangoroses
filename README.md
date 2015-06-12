# Middleware[1] #
Enables us, developers, to plug into the request / response cycle and make global alterations to the input or output.

Django comes with a set of prebuild middleware and developers may use some or all of those, they can also write their own for whatever needs they might have.

The ```MIDDLEWARE_CLASSES``` element of the setup file defines those middlewares in use within a project.

## Request Phase ##
Middleware may make use of two hooks during the request phase: ```process_request``` and ```process_view```.
### process_request ###
The ```process_request``` hook is activated as soon as the HTTP Request as soon as the incoming HTTP request, eg ```/species/update/1/``` is received and results in the creation of a HTTPRequest object.

Processing here is capable of fundamentally changing the nature of the request.

### process_view ###
The ```process_view``` hook is activated just before the relevant view method is executed.

## Response Phase ##
Middleware may make use of three hooks during the response phase: ```process_exception``` , ```process_template_response``` and ```process_response```.
### process_response ###
The ```process_response``` hook is activated just after the relevant view method execution is complete but before any attempt has been made to return data to the requesting agent. For this reason there's scope here to applying : caching; compression to the body. In addition there's scope here to apply updates to the headers and/or body of the returned data.
### process_exception ###
The ```process_exception``` hook is activated when something goes wrong in handling a request (including within middleware). An argument passed to the hook is the exception that corresponds to the problem. As such the processing tied to the `process_exception` may, for instance, provide specialised logging.
### process_template_response ###
The ```process_template_response``` is activated immediately after the view function has finished executing if the response instance has a `render()` method. The value returned from the code on the end of the hook must be a response object with a `render()` method. Hook code can alter the template name, context contents or produce an entirely new response.

# Signals #
Inbuilt signals can look a little like database triggers.

Paypal OSS project sends signals in ordder that other apps in the same project can "hear" that a payment has been made successfully (quite a good example but a pain to hook up).

https://docs.djangoproject.com/en/1.8/topics/signals/ has some good comments as does 2 scoops . 

# Authentication #
# Caching #
# Internationalization #
# Serialization #
# Other possible topics #



----
[1]:https://docs.djangoproject.com/en/1.8/topics/http/middleware/
