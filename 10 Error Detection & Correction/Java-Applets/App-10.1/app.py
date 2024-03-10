from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/check_parity', methods=['POST'])
def check_parity():
    binary_data= request.form['binary_data']
    
    if not binary_data.isdigit() or set(binary_data) - {'0', '1'}:
        return "Invalid binary input! Please enter a valid binary sequence (0s and 1s only)."
    
    count_ones = binary_data.count('1')
    parity = "even" if count_ones % 2 == 0 else "odd"
    
    return f"Parity: {parity} ({count_ones} ones)"

if __name__ =="__main__":
    app.run(debug=True)
