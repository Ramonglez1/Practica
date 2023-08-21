# Commented out IPython magic to ensure Python compatibility.
# %pprint
import streamlit as st
from PIL import Image
import pandas as pd #importa la paquetería PAnel DAta (llamada pandas)
#pip install matplotlib_venn
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted # importa paqueteria para graficar diagramas de venn
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt #importa pyplot para hacer gáficas
from matplotlib import numpy as np #importar numpy
import seaborn as sn
import altair as alt
#pip install altair_catplot
import altair_catplot as altcat
#pip install xlsxwriter
import xlsxwriter
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
#from sklearn.tree import export_graphviz



st.set_page_config(
    page_title="Introducción",
    page_icon="	:open_book:",
    layout="wide"

)

st.header("Sarcopenia en el adulto mayor")


"""
Un cambio grave asociado al envejecimiento humano consiste en la reducción progresiva de la masa muscular esquelética, una espiral descendente que puede provocar una disminución de la fuerza y la funcionalidad. En 1989, Irwin Rosenberg propuso el término ‘sarcopenia’ (del griego ‘sarx’ o carne +‘penia’ o pérdida) para describir este descenso de la masa muscular relacionado con la edad. Desde entonces, la sarcopenia se ha definido como la disminución de la masamuscular esquelética y la fuerza que se produce con el envejecimiento.

La sarcopenia es un término médico utilizado para describir la pérdida gradual y progresiva de masa muscular y fuerza que ocurre con el envejecimiento. Es un fenómeno común en las personas mayores, y puede tener efectos significativos en la salud y la calidad de vida. La sarcopenia puede afectar la capacidad funcional, la independencia y la movilidad de las personas mayores, aumentando el riesgo de caídas, fracturas y otras complicaciones.

La pérdida de masa muscular asociada con la sarcopenia se debe a una combinación de factores, incluyendo cambios hormonales, disminución de la actividad física, disminución de la ingesta de proteínas y otros factores metabólicos. La sarcopenia no solo afecta a los músculos esqueléticos, sino también a otros tejidos musculares, como el corazón.

Es importante destacar que la sarcopenia no es simplemente una parte inevitable del envejecimiento, y se pueden tomar medidas para prevenirla o retrasar su progresión. Estas medidas incluyen mantener un estilo de vida activo y saludable, realizar ejercicios de resistencia para mantener y aumentar la masa muscular, y asegurarse de tener una ingesta adecuada de proteínas y nutrientes esenciales.

La evaluación y el diagnóstico de la sarcopenia pueden involucrar medidas como la medición de la masa muscular, la fuerza muscular y la función física. Los profesionales de la salud pueden utilizar diferentes criterios y pruebas para determinar si una persona tiene sarcopenia y si es necesario intervenir con cambios en el estilo de vida o tratamientos específicos."""

st.header("Categorías de sarcopenia según la causa")
st.markdown(
        """
        Sarcopenia primaria Sarcopenia relacionada con la edad: Ninguna otra causa evidente salvo el envejecimiento
        """
)



col1, col2, = st.columns(2)
with col1:
        st.write(" ")
        image1 = "Tipos-de-sarcopenia.jpg"
        st.image(image1, width = 400)
        st.caption(' :blue[Imagen 1: Tipos de Sarcopenia]')
with col2:
        st.write(' ')
        image2 = "Mecanismodesarcopenia.jpg"
        st.image(image2,   width = 450)
        width = 800
        st.caption(' :blue[Imagen 2: Mecanismos asociados a la sarcopenia]')


tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Fuerza de brazo", "Circunferencia de Pantorrilla", "Velocidad de Marcha","Perimetro de Brazo","Porcentaje de grasa","Masa musculo-esquelética","Circunferencia de cintura"])

with tab1:
    st.header("Fuerza de brazo")
    st.markdown(
            """
Las mediciones se realizan con un dinamómetro hidráulico manual, el cual se utiliza para medir la fuerza de agarre. Es utilizado como herramienta diagnóstica y evolución de un paciente, en este caso como criterio para el diagnóstico de sarcopenia.

La medición de la fuerza de agarre máxima (MGS) es un elemento esencial para evaluar a la fuerza durante el crecimiento, envejecimiento, en las secuelas de lesiones traumáticas y en la rehabilitación. El dinamómetro es considerado un instrumento adecuado y confiable para la evaluación de la fuerza de prensión manual del paciente, aunque la fiabilidad de la evaluación puede verse afectada por género, peso y la postura corporal.

**Fuerza de agarre y sarcopenia**: Las manos son una herramienta de gran utilidad para el hombre, quien las utiliza para realizar funciones mecánicas, sensitivas, de protección e incluso de comunicación, la fuerza de agarre es un parámetro simple para determinar la capacidad funcional de un paciente, es necesaria  para realizar las actividades de la vida diaria, tales como subir las escaleras, cargar alimentos, y realizar compras diversas.

**Fuerza de agarre normal**: 
El punto de corte para ser criterio de sarcopenia es:
"""
    )

    import pandas as pd
    import streamlit as st
    
    data = {
        'Genero': ['Hombre', 'Mujer'],
        'Fuerza de agarre': ['<27kg', '<16kg']
    }
    
    df = pd.DataFrame(data)
    
    st.dataframe(df)
    
    
    with st.expander("**Técnica**"):
            st.write(
"""
    1. Se le indica al paciente que se siente con los codos flexionados a 90 grados y los antebrazos en posición neutra. 
    2. Los brazos no deben apoyarse en un apoyabrazos ni ningún otro sitio durante la prueba.
    3. Luego el paciente ejerce presión en la manija del dinamómetro durante algunos segundos. El dinamómetro expresa el resultado en kilogramos.
    4. Dejar descansar al paciente durante 1 minuto y repetir la prueba.
    5. Realizar la prueba en ambas extremidades

    """
    )
    st.markdown(
                """
    **NOTA**
    Diferencias de fuerza en la mano dominante, ¿cuál tomar en cuenta?
    La mayor fuerza en la mano dominante está en 5-40% y puede estar o no relacionada con la actividad laboral. Se toma en cuenta el resultado de la mano con menor fuerza.
    
                """
        )    
    col1, col2, col3 = st.columns(3)
    with col1:
            st.write(" ")
    with col2:
            st.write(" ")
    with col3:
            st.write(' ')



with tab2:
    st.header("Circunferencia de Pantorrilla")
    st.markdown(
    """
    La prueba de circunferencia de pantorrilla es una medida clínica utilizada para evaluar la masa muscular periférica en adultos mayores. Esta prueba es una evaluación simple y no invasiva de la masa muscular que se puede realizar en un entorno clínico o en el hogar. La circunferencia de la pantorrilla es un indicador útil de la masa muscular periférica debido a la alta correlación entre la circunferencia de la pantorrilla y la masa muscular total. La disminución de la masa muscular periférica es un indicador común de la disminución de la fuerza y ​​la función muscular en adultos mayores, lo que se asocia con una mayor discapacidad, caídas y mortalidad. Para realizar la prueba de circunferencia de pantorrilla, se mide la circunferencia de la pantorrilla desnuda en la pierna dominante, en un punto específico, generalmente en la parte más ancha de la pantorrilla.
    """
    )
    with st.expander("**Técnica**"):
            st.write(
"""
Técnica de realización.
– Como pauta general se realizan los siguientes pasos:
• El sujeto puede estar sentado con la pierna izquierda descubierta colgando libremente o de pie erguido con los pies separados en unos 20 cm y con el peso distribuido uniformemente sobre ambos pies.
• Se coloca la cinta métrica en forma horizontal alrededor de la pantorrilla y se mueve hacia arriba y abajo para ubicar el perímetro máximo en un plano perpendicular al eje longitudinal de la pantorrilla.
• La cinta métrica debe estar en contacto con la piel en toda la circunferencia pero no debe producir presión.
• Se registrará la medición redondeando al milímetro más cercano.

– En los pacientes encamados:
• Colocar al paciente en posición supina, con la rodilla de la pierna a medir flexionada en un ángulo de 90 º.
• Colocar la cinta métrica en la pantorrilla en el diámetro mayor.
• Ajustar la cinta sin comprimir y realizar la lectura. Mediciones repetidas no deberían ocasionar diferencias mayores de 0,5 cm.
Interpretación de resultados. La medición de la circunferencia de la pantorrilla interviene en la evaluación del estado nutricional de la persona anciana a través del test Mini Nutritional Assessment (MNA).
    """
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        st.write(" ")
    with col3:
        st.write(' ')





with tab3:
    st.header("Velocidad de Marcha")
    st.markdown(
    """ 
    La prueba de velocidad de marcha, también conocida como prueba de la marcha de 4 metros, es una evaluación simple y rápida que se utiliza comúnmente en adultos mayores para medir su velocidad de marcha y su capacidad funcional. La prueba implica cronometrar el tiempo que tarda una persona en caminar cuatro metros a su ritmo habitual. La velocidad de marcha se considera un predictor importante de la capacidad funcional de los adultos mayores, lo que significa que puede ser un indicador de su capacidad para realizar actividades diarias y su calidad de vida en general. 
    
En particular, se ha demostrado que la velocidad de marcha se correlaciona con la capacidad para realizar actividades básicas de la vida diaria, como levantarse de una silla, caminar y subir escaleras, así como con la capacidad para realizar actividades instrumentales de la vida diaria, como hacer compras, cocinar y manejar el dinero. Además de ser una herramienta útil para la evaluación de la capacidad funcional, la prueba de velocidad de marcha también se ha utilizado como predictor de la mortalidad en adultos mayores. 
    
Se ha demostrado que una velocidad de marcha lenta se asocia con un mayor riesgo de mortalidad en esta población. En resumen, la prueba de velocidad de marcha es una herramienta importante para la evaluación de la capacidad funcional y la salud en adultos mayores. Permite a los profesionales de la salud identificar a las personas que pueden estar en mayor riesgo de limitaciones funcionales y desarrollar planes de tratamiento y prevención para mejorar su calidad de vida y reducir su riesgo de mortalidad.
    """
    )
  
          
    with st.expander("**Técnica**"):
            st.write(
"""
Es necesario  espacio suficiente para realizar las dos marcas en el suelo separadas por 4 metros. Lo ideal es tener un espacio fijo, ya marcado, en el que administrar la prueba. Realiza las marcas de inicio y de llegada con cinta adhesiva o píntalas con rotulador indeleble.
•Se le indica al paciente recorrer la distancia establecida de 4 metros.
•Se tomará con un cronómetro el tiempo el paciente necesito para recorrer los 4 metros.

Se considera con alta probabilidad de sarcopenia a aquellas personas con VM <0,8 m/s, es decir, aquellas que tardan más de 5 segundos en recorrer los 4 metros. 
"""
            )

    link_url = "https://www.sciencedirect.com/science/article/pii/S0212656711002459?via%3Dihub"
    link_text = "Mas infromación"
    # Crear un enlace que redirecciona al hacer clic
    st.markdown(f"[{link_text}]({link_url})")


    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        st.write(" ")
    with col3:
        st.write(' ')



with tab4:
    st.header("Circunferencia de brazo")
    st.markdown(
    """ 
    El perímetro del brazo se mide como la circunferencia alrededor del brazo, generalmente en la mitad superior del brazo. Para medir el perímetro del brazo, se utiliza una cinta métrica flexible y no elástica. El individuo debe estar de pie o sentado con el brazo relajado y extendido a lo largo del cuerpo. La cinta métrica se coloca alrededor del brazo en el punto medio entre el hombro y el codo, asegurándose de que esté nivelada y ajustada sin apretar demasiado la piel. La medición se toma en centímetros o pulgadas, y se registra como la circunferencia del brazo.

    La relación entre el perímetro del brazo y la sarcopenia se basa en la idea de que el perímetro del brazo puede ser un indicador indirecto de la masa muscular en esa región del cuerpo. Un brazo más delgado podría estar relacionado con una disminución de la masa muscular, lo que podría ser un signo de sarcopenia. Sin embargo, es importante tener en cuenta que el perímetro del brazo por sí solo no proporciona una imagen completa de la salud muscular y no es un diagnóstico definitivo de sarcopenia.

    El perímetro del brazo a menudo se utiliza en combinación con otras medidas, como la medición de la masa muscular y la fuerza, para evaluar el estado de la sarcopenia. Los profesionales de la salud pueden utilizar herramientas de evaluación más completas, como la medición de la masa muscular esquelética mediante DEXA, análisis de impedancia bioeléctrica y pruebas de función muscular, para obtener una imagen más precisa de la salud muscular y diagnosticar la sarcopenia.

    En resumen, el perímetro del brazo puede ser una medida simple y rápida para evaluar posibles signos de pérdida de masa muscular, pero se utiliza mejor en conjunto con otras medidas y pruebas más completas para evaluar y diagnosticar la sarcopenia de manera precisa. Si tienes preocupaciones sobre la sarcopenia, es importante hablar con un profesional de la salud para una evaluación completa y adecuada.
    """
    )
 
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
       st.write(" ")
    with col3:
        st.write(' ')



with tab5:
    
    st.header("Porcentaje de Grasa")
    st.write(
    """ 
    El porcentaje de grasa corporal se mide utilizando una variedad de métodos, que van desde técnicas más simples hasta métodos más avanzados y precisos. Algunas de las formas comunes de medir el porcentaje de grasa corporal incluyen:

    - Caliper de Pliegue Cutáneo: Este método implica medir el grosor de los pliegues cutáneos en diferentes áreas del cuerpo con un calibrador. Estas mediciones se utilizan para estimar el grosor total de la grasa subcutánea y calcular el porcentaje de grasa corporal.

    - Bioimpedancia: Al igual que para medir la masa muscular esquelética, la bioimpedancia se puede utilizar para medir el porcentaje de grasa corporal. Este método mide la resistencia eléctrica del cuerpo al paso de una corriente eléctrica de bajo nivel y utiliza esta información para estimar la cantidad de tejido graso.

    - Densitometría de Doble Energía de Rayos X (DXA o DEXA): Además de medir la masa muscular esquelética, la DXA también puede proporcionar información sobre la grasa corporal. Esta técnica utiliza rayos X de dos energías diferentes para medir la densidad de los tejidos y calcular el porcentaje de grasa corporal.

    - Tomografía Computarizada (TC) y Resonancia Magnética (RM): Al igual que para medir la masa muscular esquelética, la TC y la RM también se pueden utilizar para obtener imágenes detalladas de los tejidos grasos y calcular el porcentaje de grasa corporal.

    - Métodos de Impedancia de Aire: Estos métodos utilizan mediciones de la masa y el volumen corporal junto con la densidad del cuerpo para estimar la grasa corporal.

    La relación entre el porcentaje de grasa corporal y la sarcopenia es importante debido a su interacción en la composición corporal general. La sarcopenia se caracteriza por la pérdida de masa muscular esquelética, mientras que el aumento del porcentaje de grasa corporal puede llevar a un exceso de peso y obesidad. La sarcopenia y la obesidad a menudo se denominan "obesidad sarcopénica" cuando ocurren juntas.

    La obesidad sarcopénica es una combinación de estas dos condiciones, donde una persona tiene un alto porcentaje de grasa corporal junto con una disminución de la masa muscular. Esto puede ser especialmente perjudicial, ya que la pérdida de masa muscular contribuye a una disminución de la fuerza y la funcionalidad, lo que puede aumentar el riesgo de discapacidad y otros problemas de salud. Además, la obesidad sarcopénica también se ha asociado con un mayor riesgo de enfermedades crónicas como la diabetes tipo 2, enfermedades cardíacas y problemas metabólicos.

    Es importante tener en cuenta que la relación entre el porcentaje de grasa corporal y la sarcopenia puede ser compleja y variar según la situación individual. Una evaluación completa de la composición corporal y la función muscular es crucial para comprender cómo estas dos condiciones pueden interactuar y afectar la salud general de una persona.

    **¿Cómo medir su grasa corporal con calibradores de pliegues cutáneos?**

    Esta será una prueba habrá 7 ubicaciones que querrá medir utilizando la formula Jackson y Pollock 7. En cada ubicación, querrá tomar 3 medidas para promediar y, en última instancia, conectarlas al cálculo del porcentaje de grasa corporal. Antes de tomar las 3 medidas, debe marcar la ubicación con una “t”, pellizcando la cruz con el calibrador para obtener una lectura consistente cada vez.

    **Porcentaje de grasa corporal normal**
"""
    )

    import pandas as pd
    import streamlit as st
    
    data2 = {
        'Clasificación': ['Delgado', 'Óptimo', 'Ligero sobrepeso', 'Sobrepeso'],
        'grasa corporal hombreen %': ['<8%', '8.1 a 15.9%', '16,0 a 20,9%', '21,0 a 24,9%'],
        'grasa corporal mujer en %': ['<15%', '15,1 a 20,9%', '21,0 a 25,9%', '26,0 a 31,9%']
    }
    df2 = pd.DataFrame(data2)
    
    st.dataframe(df2)



    st.write(
        """ 
        **Técnica**
        1. Pecho
        Para medir el pecho, pellizca en diagonal un pliegue que quede a medio camino entre la axila y el pezón. Para las mujeres, querrá pellizcar 1/3 de la distancia entre la axila y el pezón. Esto le permitirá pellizcar lo suficientemente lejos del tejido mamario para obtener una lectura precisa.
        
        2. abdominales
        La medida abdominal debe tomarse utilizando un pliegue vertical de 2 cm a la derecha de su ombligo.
        
        3. Suprailíaca
        La medida suprailíaca debe tomarse utilizando un pliegue diagonal en la cresta del hueso de la cadera directamente debajo de la parte delantera de la axila. Se encuentra justo encima del hueso de la cadera.
        
        4. Medioaxilar
        La medida medioaxilar debe tomarse con un pliegue vertical directamente debajo de la mitad de la axila al mismo nivel que el esternón. Para medir fácilmente esta ubicación, levante el brazo por encima de la cabeza mientras un compañero mide el área debajo de la axila.
        
        5. Tríceps
        La medida del tríceps se encuentra en el punto medio de la parte posterior de la parte superior del brazo, a medio camino entre el hombro y el codo. Debe tomarse con un pliegue vertical.
        
        6. Subescapular
        La medida subescapular debe tomarse con un pliegue en diagonal. Se encuentra en la región de la escápula en la parte posterior de su cuerpo. Para una lectura más precisa, el pliegue debe tomarse justo debajo del omóplato al costado de la columna.
        
        7. Muslo
        La séptima y última medida es en el muslo. Para medir esta ubicación, tome un pliegue vertical a mitad de camino entre el hueso de la cadera y la rótula.

        Una vez calculados los 7 pliegues, (recordad, la suma de las siete medias procedente de la triple medición de cada pliegue) aplicaremos la siguiente fórmula dependiendo de si somos hombre o mujer para obtener el % de grasa corporal.
        
        % Grasa HOMBRES= 495/(1.112-(0.00043499*pliegues))+(0.00000055*pliegues*pliegues)-(0.00028826*Edad))-450
        
        % Grasa MUJERES= 495/(1.097-(0.00046971*pliegues)+(0.00000056*pliegues*pliegues)-(0.00012828*Edad))-450
        
        pliegues = sustituir por la suma de los 7 pliegues.
        
        Edad = Sustituir por nuestra edad.

        """
        )

with tab6:

    st.header("Masa musculo-esquelética")
    st.write(
    """
El porcentaje de masa muscular esquelética se mide utilizando técnicas de imagenología y mediciones antropométricas. Algunos de los métodos más comunes para medir la masa muscular esquelética incluyen:

- **Densitometría de Doble Energía de Rayos X (DXA o DEXA)**: Esta técnica se utiliza comúnmente para medir la densidad mineral ósea, pero también puede proporcionar información sobre la masa muscular magra. DXA utiliza rayos X de dos energías diferentes para medir la cantidad de tejido magro en el cuerpo.

- **Tomografía Computarizada (TC)**: La TC puede utilizarse para obtener imágenes detalladas de los músculos y medir su volumen y densidad. A partir de esta información, se puede calcular el porcentaje de masa muscular esquelética.

- **Resonancia Magnética (RM)**: Al igual que la TC, la RM puede proporcionar imágenes detalladas de los tejidos musculares, lo que permite calcular el volumen y la masa muscular magra.

- **Bioimpedancia**: Este método mide la resistencia eléctrica del cuerpo al paso de una corriente eléctrica de bajo nivel. La resistencia está relacionada con la cantidad de tejido magro, incluida la masa muscular.

- **Mediciones antropométricas**: Estas incluyen la medición de circunferencias de brazos, piernas y otros segmentos del cuerpo, así como la medición de pliegues cutáneos. Si bien estas medidas pueden proporcionar una estimación del contenido de grasa y masa muscular, son menos precisas que las técnicas de imagen avanzadas.
"""
    )
    st.header("Cálculo de la masa magra")
    st.write(
    """
Una vez que se conoce el porcentaje de grasa corporal, es posible calcular el porcentaje de masa magra restando el porcentaje de grasa del 100%. Luego, este porcentaje se aplica al peso corporal total para obtener la masa magra estimada.

La relación entre el porcentaje de masa muscular esquelética y la sarcopenia es directa. La sarcopenia se caracteriza por una disminución significativa de la masa muscular esquelética, lo que conduce a la pérdida de fuerza muscular y funcionalidad. A medida que disminuye la masa muscular, las personas pueden experimentar una disminución en su capacidad para realizar actividades diarias, lo que a su vez puede aumentar el riesgo de caídas, fracturas y discapacidad.

La medición del porcentaje de masa muscular esquelética es importante en la evaluación y diagnóstico de la sarcopenia. La disminución de la masa muscular es un marcador clave de la enfermedad y se utiliza para identificar a las personas en riesgo de desarrollar sarcopenia. Los profesionales de la salud pueden utilizar estas mediciones junto con otras evaluaciones clínicas y funcionales para determinar si una persona tiene sarcopenia y desarrollar un plan de tratamiento adecuado, que puede incluir ejercicio, cambios en la dieta y otras intervenciones.

    """
    )

with tab7:
    st.header("Circunferencia de cintura")
    st.write(
        """
       Esta medida en adultos es de gran ayuda para estimar el riesgo cardiovascular de las personas,es una medición de fácil acceso, rápida, económica, que no requiere gran entrenamiento del evaluador y es considerada imprescindible para realizar el diagnóstico nutricional del paciente.

Sabemos que la distribución de la masa grasa en el cuerpo es distinta en cada persona por lo que estos valores, no necesariamente van estimar la grasa real del cuerpo, especialmente en adultos mayores, ya que fisiológicamente estos tienen un aumento de esta.

La grasa acumulada alrededor de algunos de los principales órganos del cuerpo, denominada grasa visceral, promueve alteraciones del colesterol, aumento de triglicéridos, incremento del riesgo de padecer diabetes, subida de la tensión arterial y riesgo de trombosis; todos estos factores favorecen el desarrollo de enfermedad cardiovascular. Esta acumulación de grasa es consecuencia de factores genéticos, hormonales y de seguir unos hábitos de vida poco saludables como son la mala alimentación, el consumo de tabaco, el sedentarismo o el estrés.

**Circunferencia de cintura y sarcopenia**
En los adultos mayores hay un aumento de la masa grasa, especialmente la grasa abdominal. En  edad avanzada se pierde masa corporal magra al tiempo que puede conservarse e incluso aumentar la masa grasa. Esta situación se denomina obesidad sarcopénica, de modo que la relación entre la reducción relacionada con la edad de la masa y la fuerza muscular suele ser independiente de la masa corporal.

**Puntos de corte**
La Organización Mundial de la Salud (OMS) establece el valor máximo saludable del perímetro abdominal en 88 centímetros en la mujer, mientras que en el hombre el valor es de 102 centímetros.


**Técnica**
El perímetro abdominal se puede medir fácilmente con una cinta métrica , así, la persona debe estar de pie, con los pies juntos, los brazos a los lados y el abdomen relajado para, a continuación, rodear su abdomen con la cinta métrica a la altura del ombligo y sin presionar hacer una inspiración profunda y al momento sacar el aire.

        """
        )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.write(' ')
    with col3:
        st.write(' ')

st.header("Bibliografia")
st.write(
    """
Cruz-Jentoft AJ, Baeyens JP, Bauer JM, Boirie Y, Cederholm T, Landi F, Martin FC, Michel JP, Rolland Y, Schneider SM, Topinková E, Vandewoude M, Zamboni M; European Working Group on Sarcopenia in Older People. Sarcopenia: European consensus on definition and diagnosis: Report of the European Working Group on Sarcopenia in Older People. Age Ageing. 2010 Jul;39(4):412-23. doi: 10.1093/ageing/afq034. Epub 2010 Apr 13. PMID: 20392703; PMCID: PMC2886201.

Abizanda Soler, P., López-Torres Hidalgo, J., Romero Rizos, L., Sánchez Jurado, P. M., García Nogueras, I., & Esquinas Requena, J. L. (2012). Valores normativos de instrumentos de valoración funcional en ancianos españoles: estudio FRADEA. Atención primaria, 44(3), 162–171.
"""
)


