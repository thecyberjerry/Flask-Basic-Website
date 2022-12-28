import requests
import base64
import json
import uuid
# email = input("enter email: ")
def write_json(data):
    with open('../static/emails.json', 'w') as file:
        json.dump(data, file, indent=4)
        pass
# var = input('enter:')
var2 = str(uuid.uuid1())
with open('../static/emails.json') as json_file:
        data = json.load(json_file)
        temp = data["emails"]
        user = {"UID: ":"{}".format(var2),
            "email": "{}".format(em)}
        temp.append(user)
write_json(data)


# regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
#
#     def isValid(email):
#         if re.fullmatch(regex, email):
#             print("Valid email")
#         else:
#             print("Invalid email")

# var = requests.get('https://api.github.com/repos/thecyberjerry/Dirfu/contents/dirfu.py')
# data = var.json()
# file_content = data['content']
# file_content_encoding = data.get('encoding')
# if file_content_encoding == 'base64':
#         file_content = base64.b64decode(file_content).decode()
# print(file_content)
# """
#  if request.form.get('op') == '+':
#             number1 = int(request.form.get('numberOne'))
#             number2 = int(request.form.get('numberTwo'))
#             result = number1+number2
#             var = (f'Result is {result}')
#         elif request.form.get('op') == '-':
#             number1 = int(request.form.get('numberOne'))
#             number2 = int(request.form.get('numberTwo'))
#             result = number1-number2
#             var = (f'Result is {result}')
#         elif request.form.get('op') == '*':
#             number1 = int(request.form.get('numberOne'))
#             number2 = int(request.form.get('numberTwo'))
#             result = number1 * number2
#             var = (f'Result is {result}')
#         elif request.form.get('op') == '/':
#             number1 = int(request.form.get('numberOne'))
#             number2 = int(request.form.get('numberTwo'))
#             result = number1 / number2
#             var = (f'Result is {result}')
#         else:
#             var = 'Please Enter Valid Operator: ' \
#                   'Possible Operations supported: +,-,*,/'"""

