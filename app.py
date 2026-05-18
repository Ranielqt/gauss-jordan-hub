from flask import Flask, render_template, request, jsonify
from gauss_jordan import gauss_jordan_solve

app = Flask(__name__)

# Expose the app object for Vercel
app = app

@app.route('/')
def index():
    # Render the main page with mathematical discussion and examples
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    matrix = data.get('matrix')
    
    if not matrix:
        return jsonify({"error": "No matrix provided"}), 400
        
    try:
        success, final_matrix, steps, solution = gauss_jordan_solve(matrix)
        return jsonify({
            "success": success,
            "steps": steps,
            "solution": solution
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
