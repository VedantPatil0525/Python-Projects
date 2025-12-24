from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
  data = request.json
  x = data.get('x')
  y = data.get('y')
  op = data.get('operation')

  if None in (x, y, op):
    return jsonify({'error': 'Missing Inputs'}), 400
  
  try:
    x, y = float(x), float(y)
  except:
    return jsonify({'error': 'Invalid numbers'}), 400
  
  if op == 'add':
    result = x + y
  elif op == 'substract':
    result = x - y
  elif op == 'multiply':
    result = x * y
  elif op == 'divide':
    if y == 0:
      return jsonify({'error': 'Divison by zero'}), 400
    result = x / y
  else:
    return jsonify({'error': 'Invalid operation'}), 400
  
  return jsonify({'result': result})

if __name__ == '__main__':
  app.run(debug=True)