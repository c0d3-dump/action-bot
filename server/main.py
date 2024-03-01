from flask import Flask, request
from gorilla import get_gorilla_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def execute_function_from_string(function_string):
    # Assuming the string follows a specific format
    if function_string.startswith('todo(') and function_string.endswith(')'):
        # Extracting the content within the parentheses
        function_arguments = function_string[len('todo('):-1]
        
        # Splitting the arguments by commas
        arguments_list = [arg.strip() for arg in function_arguments.split(',')]

        # Creating a dictionary to pass as keyword arguments to the function
        kwargs = {}
        for arg in arguments_list:
            key, value = arg.split('=')
            kwargs[key.strip()] = value.strip()[1:-1]

        return kwargs
    else:
        print("Invalid function format")


@app.route("/todo", methods=['POST'])
def todos():
    query = request.form['query']
    print(query)
    functions = [
        {
          "name": "todo",
          "api_name": "todo",
          "description": "todo list function which will allow to add, delete or complete list",
          "parameters": [
              {
                  "name": "type",
                  "enum": ["add", "delete", "complete"],
                  "description": """
                    types of todo for processing content. 
                    add - adding todo to list, 
                    delete - delete todo from list
                    complete - mark todo as complete
                  """
              },
              {
                  "name": "content",
                  "description": "content of todo to do any action based on type"
              }
          ]
        }
    ]
    
    if query :
      func = get_gorilla_response(query, functions=functions)
      print("func: ", func)
      res = execute_function_from_string(func)
      return res
    return ""

if __name__ == "__main__":
    
    app.run(debug=True, host="0.0.0.0")
