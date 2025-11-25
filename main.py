import functions_framework

@functions_framework.http
def hello_http(request):
    #return 'Hello Cloud!'
    return '''<!DOCTYPE html>
              <html lang="en">
              <head>
              <title>Eric Ervin</title>
              <style>table,th,td {
                               border: 1px solid black;
                               border-collapse: collapse;
                               padding: 3px;
                               text-align: center
                               }
                             td {text-align: left}</style>
              </head>
              <body>
              <div id="header">
              <h1>Eric Ervin</h1>
              <p>A toy website to release some Python into the world.</p>
              </div>
              </html>
              '''
