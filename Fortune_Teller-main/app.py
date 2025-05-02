from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    if request.method == 'POST':
        user = request.form['user']
        color = request.form['color']
        number = request.form['number']
        
        # fortune logic
        fortunes = {
            ('red', '1'): "You will find a lucky penny!",
            ('red', '2'): "An adventure awaits you soon",
            ('yellow', '1'): "You’ll reconnect with an old friend",
            ('yellow', '2'): "You will encounter geat fortunes",
            ('blue', '3'): "A calm mind brings inner strength",
            ('green', '4'): "You will ace your next test",
        }
        fortune = fortunes.get((color, number), "Something unexpected is coming!")
        return render_template('result.html', user=user, fortune=fortune)
    
    return render_template('form.html')
