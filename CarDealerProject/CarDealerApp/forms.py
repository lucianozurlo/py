from django import forms

# Listas desplegables
flotaMarcaModelo = [
    ('VW Vento', 'VW Vento'), 
    ('VW Bora', 'VW Bora'), 
    ('VW Amarok', 'VW Amarok'), 
    ('Ford Fiesta', 'Ford Fiesta'), 
    ('Ford Mondeo', 'Ford Mondeo'), 
    ('Toyota Corola', 'Toyota Corola'), 
    ('Toyota Hilux', 'Toyota Hilux'), 
    ('Renault Clio', 'Renault Clio'), 
    ('Renault Kangoo', 'Renault Kangoo'), 
    ('Peugeot Partner', 'Peugeot Partner')]

flotaTransmision = [
    ('Automático', 'Automático'),
    ('Manual', 'Manual')]

flotaCombustible = [
    ('Nafta', 'Nafta'),
    ('Diesel', 'Diesel'),
    ('Eléctrico', 'Eléctrico'),
    ('Hibrido', 'Hibrido')]

flotaFoto = [
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
    ('06', '06'),
    ('07', '07'),
    ('08', '08'),
    ('09', '09'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17')]

choferFoto = [
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04')]

puntosProvincia = [
    ('Buenos Aires', 'Buenos Aires'),
    ('CABA', 'CABA'),
    ('Catamarca', 'Catamarca'),
    ('Chaco', 'Chaco'),
    ('Chubut', 'Chubut'),
    ('Córdoba', 'Córdoba'),
    ('Corrientes', 'Corrientes'),
    ('Entre Ríos', 'Entre Ríos'),
    ('Formosa', 'Formosa'),
    ('Jujuy', 'Jujuy'),
    ('La Pampa', 'La Pampa'),
    ('La Rioja', 'La Rioja'),
    ('Mendoza', 'Mendoza'),
    ('Misiones', 'Misiones'),
    ('Neuquén', 'Neuquén'),
    ('Río Negro', 'Río Negro'),
    ('Salta', 'Salta'),
    ('San Juan', 'San Juan'),
    ('San Luis', 'San Luis'),
    ('Santa Cruz', 'Santa Cruz'),
    ('Santa Fe', 'Santa Fe'),
    ('Santiago del Estero', 'Santiago del Estero'),
    ('Tierra del Fuego', 'Tierra del Fuego'),
    ('Tucumán', 'Tucumán')]

# Formularios de carga
class FormCargarFlota(forms.Form):
    marcaModelo = forms.ChoiceField(choices=flotaMarcaModelo, label="Marca - Modelo")
    anio = forms.IntegerField(label="Año")
    km = forms.IntegerField()
    transmision = forms.ChoiceField(choices=flotaTransmision)
    combustible = forms.ChoiceField(choices=flotaCombustible)
    costo = forms.IntegerField()
    foto = forms.ChoiceField(choices=flotaFoto)

class FormCargarChofer(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    puesto = forms.CharField()
    foto = forms.ChoiceField(choices=choferFoto)

class FormPuntoDeRetiro(forms.Form):
    provincia = forms.ChoiceField(choices=puntosProvincia)
    localidad = forms.CharField()
    direccion = forms.CharField()
    telefono = forms.CharField()
    email = forms.EmailField()

# Formularios del buscador
class FormBuscarFlota(forms.Form):
    marcaModelo = forms.CharField()
