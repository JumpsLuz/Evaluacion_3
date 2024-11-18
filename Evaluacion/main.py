from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        try:
            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            promedio = (nota1 + nota2 + nota3) / 3
            estado = 'Aprobado' if promedio >= 40 and asistencia >= 75 else 'Reprobado'
            resultado = f'{promedio:.2f}<br>{estado}'
        except ValueError:
            resultado = 'Por favor ingresa valores válidos.'
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)
        resultado = f'El nombre con mayor cantidad de caracteres es: {nombre_mas_largo}<br>El nombre tiene : {longitud} caracteres.'
    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)