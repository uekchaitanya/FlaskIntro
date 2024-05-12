Docker build command -
docker build -t docker-sample-app

Docker run command -
docker run -p 8080:8080 docker-sample-app


Web URL(post docker run) - 

in hosted use - http://localhost:8080/
to navigate to index.html page where you will have  sample text box to enter message and convert to json on submit.


APIserviceEndpoint:
http://localhost:8080/api/StrJsonConvertor?param=INPUTTEXT

Pass in a message in INPUTTEXT as shown above or call the API through postman to receive the response

sample request : key: param Value: test-Message Hello
endPoint: http://localhost:8080/api/StrJsonConvertor?param=test-Message Hello

Response: 
{
    "message": "Value entered: test-Message Hello"
}
