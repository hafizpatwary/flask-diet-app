from application import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000) # Port 5000 is taken by Control Center in MacOS
