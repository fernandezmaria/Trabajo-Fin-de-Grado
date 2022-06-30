### Import Packages ########################################
import dash
from dash import Dash, dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import numpy as np
import pickle

### Setup ###################################################
app = dash.Dash(__name__)
app.title = 'Machine Learning Model Deployment'
server = app.server
### cargar modelo ML #########################################
with open('modelo.pickle', 'rb') as f:
    clf = pickle.load(f)

app = Dash(__name__)

### App Layout ###############################################
app.layout = html.Div([
    dbc.Row([html.H3(children='Dónde tendrá éxito tu negocio')]),
    dbc.Row([
        dbc.Col(html.Label(children='Escoge una localización concreta'), width={"order": "first"}),
        dbc.Col([dcc.Dropdown(
                id='distrito', #asi se va a llamar lo escogido
                placeholder="Selecciona un distrito",
                options=[
                    {'label': 'Centro', 'value': 'desc_distrito_local_centro'},
                    {'label': 'Chamberí', 'value': 'desc_distrito_local_chamberi'},
                    {'label': 'Puente de Vallecas', 'value': 'desc_distrito_local_puente_de_vallecas'},
                    {'label': 'Salamanca', 'value': 'desc_distrito_local_salamanca'},
                    {'label': 'Otro', 'value': 'Otro'}
                ],
                #value='desc_distrito_local_centro',
                style={
                    'margin-bottom': '1.0rem',
                    'margin-top': '1.0rem'
                }
            )]),
        dbc.Col([dcc.Dropdown(
                id='barrio', #asi se va a llamar lo escogido
                placeholder="Selecciona un barrio",
                options=[
                    {'label': 'Justicia', 'value': 'desc_barrio_local_justicia'},
                    {'label': 'Recoletos', 'value': 'desc_barrio_local_recoletos'},
                    {'label': 'Otro', 'value': 'Otro'}
                ],
                #value='desc_barrio_local_justicia',
                style={
                    'margin-bottom': '1.0rem',
                    'margin-top': '1.0rem'
                }
            )]),
        dbc.Col(html.Label(children='Escoge un tipo de negocio concreto'), width={"order": "first"}),
        dbc.Col([dcc.Dropdown(
                id='seccion', #asi se va a llamar lo escogido
                placeholder="Selecciona una sección CNAE",
                options=[
                    {'label': 'Actividades Financieras y de Seguros', 'value': 'desc_seccion_actividades_financieras_y_de_seguros'},
                    {'label': 'Actividades Sanitarias y de Servicios Sociales', 'value': 'desc_seccion_actividades_sanitarias_y_de_servicios_sociales'},
                    {'label': 'Comercio al por mayor y al por menor; reparación de vehículos de motor y motocicletas', 'value': 'desc_seccion_comercio_al_por_mayor_y_al_por_menor_reparación_de_vehículos_de_motor_y_motocicletas'},
                    {'label': 'Educación', 'value': 'desc_seccion_educación'},
                    {'label': 'Hostelería', 'value': 'desc_seccion_hostelería'},
                    {'label': 'Otros servicios', 'value': 'desc_seccion_otros_servicios'}
                ],
                #value='desc_seccion_hostelería',
                style={
                    'margin-bottom': '1.0rem',
                    'margin-top': '1.0rem'
                }
            )]),
        dbc.Col([dcc.Dropdown(
                id='division', #asi se va a llamar lo escogido
                placeholder="Selecciona una división CNAE",
                options=[
                    {'label': 'Actividades Sanitarias', 'value': 'desc_division_actividades_sanitarias'},
                    {'label': 'Comercio al por menor, excepto de vehículos de motor y motocicletas', 'value': 'desc_division_comercio_al_por_menor_excepto_de_vehículos_de_motor_y_motocicletas'},
                    {'label': 'Educación', 'value': 'desc_division_educación'},
                    {'label': 'Otros servicios personales', 'value': 'desc_division_otros_servicios_personales'},
                    {'label': 'Servicios de comidas y bebidas', 'value': 'desc_division_servicios_de_comidas_y_bebidas'},
                    {'label': 'Servicios financieros, excepto seguros y fondos de pensiones', 'value': 'desc_division_servicios_financieros_excepto_seguros_y_fondos_de_pensiones'},
                    {'label': 'Venta y reparación de vehículos de motor y motocicletas', 'value': 'desc_division_venta_y_reparación_de_vehículos_de_motor_y_motocicletas'}
                ],
                #value='desc_division_servicios_de_comidas_y_bebidas',
                style={
                    'margin-bottom': '1.0rem',
                    'margin-top': '1.0rem'
                }
            )]),
        dbc.Col([dcc.Dropdown(
                id='epigrafe', #asi se va a llamar lo escogido
                placeholder="Selecciona un epígrafe CNAE",
                options=[
                    {'label': 'Comercio al por menor de ferretería, pintura y vidrio en establecimientos especializados', 'value': 'desc_epigrafe_bueno_comercio_al_por_menor_de_ferretería_pintura_y_vidrio_en_establecimientos_especializados'},
                    {'label': 'Comercio al por menor de prendas de vestir en establecimientos especializados', 'value': 'desc_epigrafe_bueno_comercio_al_por_menor_de_prendas_de_vestir_en_establecimientos_especializados'},
                    {'label': 'Comercio al por menor de productos farmacéuticos en establecimientos especializados', 'value': 'desc_epigrafe_bueno_comercio_al_por_menor_de_productos_farmacéuticos_en_establecimientos_especializados'},
                    {'label': 'Establecimientos de bebidas', 'value': 'desc_epigrafe_bueno_establecimientos_de_bebidas'},
                    {'label': 'Mantenimiento y reparación de vehículos de motor', 'value': 'desc_epigrafe_bueno_mantenimiento_y_reparación_de_vehículos_de_motor'},
                    {'label': 'Otro comercio al por menor de artículos nuevos en establecimientos especializados', 'value': 'desc_epigrafe_bueno_otro_comercio_al_por_menor_de_artículos_nuevos_en_establecimientos_especializados'},
                    {'label': 'Otro comercio al por menor de productos alimenticios en establecimientos especializados', 'value': 'desc_epigrafe_bueno_otro_comercio_al_por_menor_de_productos_alimenticios_en_establecimientos_especializados'},
                    {'label': 'Peluquería y otros tratamientos de belleza', 'value': 'desc_epigrafe_bueno_peluquería_y_otros_tratamientos_de_belleza'},
                    {'label': 'Restaurantes y puestos de comidas', 'value': 'desc_epigrafe_bueno_restaurantes_y_puestos_de_comidas'},
                    {'label': 'Intermediación monetaria: bancos, cajas de ahorro', 'value': 'desc_epigrafe_bueno_intermediacion_monetaria_bancos_cajas_de_ahorro'}
                ],
                #value='desc_epigrafe_bueno_establecimientos_de_bebidas',
                style={
                    'margin-bottom': '1.0rem',
                    'margin-top': '1.0rem'
                }
            )])
    ]),
    dbc.Row([dbc.Button('Enviar', id='submit-val', n_clicks=0, color="primary")]),
    html.Br(),
    dbc.Row([html.Div(id='prediction output')])

], style={'padding': '0px 0px 0px 150px', 'width': '50%'})

@app.callback(
    Output('prediction output', 'children'),
    Input('submit-val', 'n_clicks'),
    State('distrito', 'value'),
    State('barrio', 'value'),
    State('seccion', 'value'),
    State('division', 'value'),
    State('epigrafe', 'value')
)


def update_output(n_clicks,distrito,barrio,seccion,division,epigrafe):

    desc_distrito_local_centro = 0
    desc_distrito_local_chamberi = 0
    desc_distrito_local_puente_de_vallecas = 0
    desc_distrito_local_salamanca = 0
    desc_barrio_local_justicia = 0
    desc_barrio_local_recoletos = 0
    desc_seccion_99999 = 0
    desc_seccion_actividades_financieras_y_de_seguros = 0
    desc_seccion_actividades_sanitarias_y_de_servicios_sociales = 0
    desc_seccion_comercio_al_por_mayor_y_al_por_menor_reparación_de_vehículos_de_motor_y_motocicletas = 0
    desc_seccion_educación = 0
    desc_seccion_hostelería = 0
    desc_seccion_otros_servicios = 0
    desc_seccion_sin_actividad=0
    desc_division_99999=0
    desc_division_actividades_sanitarias=0
    desc_division_comercio_al_por_menor_excepto_de_vehículos_de_motor_y_motocicletas=0
    desc_division_educación=0
    desc_division_otros_servicios_personales=0
    desc_division_sin_actividad=0
    desc_division_servicios_de_comidas_y_bebidas=0
    desc_division_servicios_financieros_excepto_seguros_y_fondos_de_pensiones=0
    desc_division_venta_y_reparación_de_vehículos_de_motor_y_motocicletas=0
    desc_epigrafe_bueno_99999=0
    desc_epigrafe_bueno_comercio_al_por_menor_de_ferretería_pintura_y_vidrio_en_establecimientos_especializados=0
    desc_epigrafe_bueno_comercio_al_por_menor_de_prendas_de_vestir_en_establecimientos_especializados=0
    desc_epigrafe_bueno_comercio_al_por_menor_de_productos_farmacéuticos_en_establecimientos_especializados=0
    desc_epigrafe_bueno_establecimientos_de_bebidas=0
    desc_epigrafe_bueno_mantenimiento_y_reparación_de_vehículos_de_motor=0
    desc_epigrafe_bueno_otro_comercio_al_por_menor_de_artículos_nuevos_en_establecimientos_especializados=0
    desc_epigrafe_bueno_otro_comercio_al_por_menor_de_productos_alimenticios_en_establecimientos_especializados=0
    desc_epigrafe_bueno_peluquería_y_otros_tratamientos_de_belleza=0
    desc_epigrafe_bueno_restaurantes_y_puestos_de_comidas=0
    desc_epigrafe_bueno_intermediacion_monetaria_bancos_cajas_de_ahorro=0
    desc_epigrafe_bueno_local_sin_actividad=0

    if (distrito == 'desc_distrito_local_chamberi'):
        desc_distrito_local_chamberi = 1
    elif (distrito == 'desc_distrito_local_centro'):
        desc_distrito_local_centro = 1
    elif (distrito == 'desc_distrito_local_puente_de_vallecas'):
        desc_distrito_local_puente_de_vallecas = 1
    elif (distrito == 'desc_distrito_local_salamanca'):
        desc_distrito_local_salamanca = 1

    if (barrio == 'desc_barrio_local_justicia'):
        desc_barrio_local_justicia = 1
    elif (barrio == 'desc_barrio_local_recoletos'):
        desc_barrio_local_justicia = 1

    if(seccion == 'desc_seccion_actividades_financieras_y_de_seguros'):
        desc_seccion_actividades_financieras_y_de_seguros = 1
    elif(seccion == 'desc_seccion_actividades_sanitarias_y_de_servicios_sociales'):
        desc_seccion_actividades_sanitarias_y_de_servicios_sociales = 1
    elif(seccion == 'desc_seccion_comercio_al_por_mayor_y_al_por_menor_reparación_de_vehículos_de_motor_y_motocicletas'):
        desc_seccion_comercio_al_por_mayor_y_al_por_menor_reparación_de_vehículos_de_motor_y_motocicletas = 1
    elif(seccion=='desc_seccion_educación'):
        desc_seccion_educación=1
    elif(seccion=='desc_seccion_hostelería'):
        desc_seccion_hostelería=1
    elif(seccion=='desc_seccion_otros_servicios'):
        desc_seccion_otros_servicios=1

    if(division=='desc_division_actividades_sanitarias'):
        desc_division_actividades_sanitarias=1
    elif(division=='desc_division_comercio_al_por_menor_excepto_de_vehículos_de_motor_y_motocicletas'):
        desc_division_comercio_al_por_menor_excepto_de_vehículos_de_motor_y_motocicletas=1
    elif(division=='desc_division_educación'):
        desc_division_educación=1
    elif(division=='desc_division_otros_servicios_personales'):
        desc_division_otros_servicios_personales=1
    elif(division=='desc_division_servicios_de_comidas_y_bebidas'):
        desc_division_servicios_de_comidas_y_bebidas=1
    elif(division=='desc_division_servicios_financieros_excepto_seguros_y_fondos_de_pensiones'):
        desc_division_servicios_financieros_excepto_seguros_y_fondos_de_pensiones=1
    elif(division=='desc_division_venta_y_reparación_de_vehículos_de_motor_y_motocicletas'):
        desc_division_venta_y_reparación_de_vehículos_de_motor_y_motocicletas=1

    if(epigrafe=='desc_epigrafe_bueno_comercio_al_por_menor_de_ferretería_pintura_y_vidrio_en_establecimientos_especializados'):
        desc_epigrafe_bueno_comercio_al_por_menor_de_ferretería_pintura_y_vidrio_en_establecimientos_especializados=1
    elif(epigrafe=='desc_epigrafe_bueno_comercio_al_por_menor_de_prendas_de_vestir_en_establecimientos_especializados'):
        desc_epigrafe_bueno_comercio_al_por_menor_de_prendas_de_vestir_en_establecimientos_especializados=1
    elif(epigrafe=='desc_epigrafe_bueno_comercio_al_por_menor_de_productos_farmacéuticos_en_establecimientos_especializados'):
        desc_epigrafe_bueno_comercio_al_por_menor_de_productos_farmacéuticos_en_establecimientos_especializados=1
    elif(epigrafe=='desc_epigrafe_bueno_establecimientos_de_bebidas'):
        desc_epigrafe_bueno_establecimientos_de_bebidas=1
    elif(epigrafe=='desc_epigrafe_bueno_mantenimiento_y_reparación_de_vehículos_de_motor'):
        desc_epigrafe_bueno_mantenimiento_y_reparación_de_vehículos_de_motor=1
    elif(epigrafe=='desc_epigrafe_bueno_otro_comercio_al_por_menor_de_artículos_nuevos_en_establecimientos_especializados'):
        desc_epigrafe_bueno_otro_comercio_al_por_menor_de_artículos_nuevos_en_establecimientos_especializados=1
    elif(epigrafe=='desc_epigrafe_bueno_otro_comercio_al_por_menor_de_productos_alimenticios_en_establecimientos_especializados'):
        desc_epigrafe_bueno_otro_comercio_al_por_menor_de_productos_alimenticios_en_establecimientos_especializados=1
    elif(epigrafe=='desc_epigrafe_bueno_peluquería_y_otros_tratamientos_de_belleza'):
        desc_epigrafe_bueno_peluquería_y_otros_tratamientos_de_belleza=1
    elif(epigrafe=='desc_epigrafe_bueno_restaurantes_y_puestos_de_comidas'):
        desc_epigrafe_bueno_restaurantes_y_puestos_de_comidas=1
    elif(epigrafe=='desc_epigrafe_bueno_intermediacion_monetaria_bancos_cajas_de_ahorro'):
        desc_epigrafe_bueno_intermediacion_monetaria_bancos_cajas_de_ahorro=1

        #return f'You have selected {distrito} and You have selected {barrio} and {seccion} and {division} and {epigrafe}'

    x = np.array([[float(desc_distrito_local_centro), float(desc_distrito_local_chamberi), desc_distrito_local_puente_de_vallecas, float(desc_distrito_local_salamanca), desc_barrio_local_justicia, desc_barrio_local_recoletos, desc_seccion_99999, int(desc_seccion_actividades_financieras_y_de_seguros),
                   int(desc_seccion_actividades_sanitarias_y_de_servicios_sociales), int(desc_seccion_comercio_al_por_mayor_y_al_por_menor_reparación_de_vehículos_de_motor_y_motocicletas), desc_seccion_educación, int(desc_seccion_hostelería), int(desc_seccion_otros_servicios), desc_seccion_sin_actividad,
                   desc_division_99999, int(desc_division_actividades_sanitarias), int(desc_division_comercio_al_por_menor_excepto_de_vehículos_de_motor_y_motocicletas), desc_division_educación, int(desc_division_otros_servicios_personales), desc_division_sin_actividad, int(desc_division_servicios_de_comidas_y_bebidas),
                   int(desc_division_servicios_financieros_excepto_seguros_y_fondos_de_pensiones), int(desc_division_venta_y_reparación_de_vehículos_de_motor_y_motocicletas), desc_epigrafe_bueno_99999, desc_epigrafe_bueno_comercio_al_por_menor_de_ferretería_pintura_y_vidrio_en_establecimientos_especializados,
                   int(desc_epigrafe_bueno_comercio_al_por_menor_de_prendas_de_vestir_en_establecimientos_especializados), int(desc_epigrafe_bueno_comercio_al_por_menor_de_productos_farmacéuticos_en_establecimientos_especializados), int(desc_epigrafe_bueno_establecimientos_de_bebidas), int(desc_epigrafe_bueno_mantenimiento_y_reparación_de_vehículos_de_motor),
                   desc_epigrafe_bueno_otro_comercio_al_por_menor_de_artículos_nuevos_en_establecimientos_especializados, int(desc_epigrafe_bueno_otro_comercio_al_por_menor_de_productos_alimenticios_en_establecimientos_especializados), int(desc_epigrafe_bueno_peluquería_y_otros_tratamientos_de_belleza),
                   int(desc_epigrafe_bueno_restaurantes_y_puestos_de_comidas), int(desc_epigrafe_bueno_intermediacion_monetaria_bancos_cajas_de_ahorro), desc_epigrafe_bueno_local_sin_actividad]])

    prediction = clf.predict(x)[0]
    pred=clf.predict_proba(x)[:, 1][0]

    if not n_clicks:
        return f'Completa los campos'
    else:
        if prediction == 0:
            output = 'No tienes muchas posibilidades de durar varios años.'
        elif prediction == 1:
            output = 'Tienes posibilidades de durar varios años.'
        else:
            output = 'WTF'
        return f'{output}  \n                                                  ' \
               f'La probabilidad de éxito estimada es de un {pred*100:.2f}% \n ' \
               f'¡Mucho ánimo!'

### Run the App ###############################################
if __name__ == '__main__':
    app.run_server(debug=True)