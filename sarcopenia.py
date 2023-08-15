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

st.write("Sobre envejecimiento y la sarcopenia")


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

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Fuerza de brazo", "Circunferencia de Pantorrilla", "Velocidad de Marcha","Perimetro de Brazo","Porcentaje de grasa","Masa musculo-esquelética","grasa"])

with tab1:
    st.header("Fuerza de brazo")
    st.markdown(
            """
       eeeeeee
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
    La prueba de circunferencia de pantorrilla es una medida clínica utilizada para evaluar la masa muscular periférica en adultos mayores. Esta prueba es una evaluación simple y no invasiva de la masa muscular que se puede realizar en un entorno clínico o en el hogar. La circunferencia de la pantorrilla es un indicador útil de la masa muscular periférica debido a la alta correlación entre la circunferencia de la pantorrilla y la masa muscular total. La disminución de la masa muscular periférica es un indicador común de la disminución de la fuerza y ​​la función muscular en adultos mayores, lo que se asocia con una mayor discapacidad, caídas y mortalidad. Para realizar la prueba de circunferencia de pantorrilla, se mide la circunferencia de la pantorrilla desnuda en la pierna dominante, en un punto específico, generalmente en la parte más ancha de la pantorrilla. La medida se toma utilizando una cinta métrica flexible y se registra en centímetros. Los valores normales de la circunferencia de la pantorrilla pueden variar según la edad, el sexo y la etnia, pero generalmente se considera normal una medida superior a 31 cm en mujeres y 34 cm en hombres. La prueba de circunferencia de pantorrilla es una herramienta útil para la evaluación de la masa muscular periférica en adultos mayores, pero debe usarse junto con otras medidas clínicas y pruebas de función muscular para una evaluación más completa del estado de la masa muscular y la fuerza en los adultos mayores. 
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
    La prueba de velocidad de marcha, también conocida como prueba de la marcha de 4 metros, es una evaluación simple y rápida que se utiliza comúnmente en adultos mayores para medir su velocidad de marcha y su capacidad funcional. La prueba implica cronometrar el tiempo que tarda una persona en caminar cuatro metros a su ritmo habitual. La velocidad de marcha se considera un predictor importante de la capacidad funcional de los adultos mayores, lo que significa que puede ser un indicador de su capacidad para realizar actividades diarias y su calidad de vida en general. En particular, se ha demostrado que la velocidad de marcha se correlaciona con la capacidad para realizar actividades básicas de la vida diaria, como levantarse de una silla, caminar y subir escaleras, así como con la capacidad para realizar actividades instrumentales de la vida diaria, como hacer compras, cocinar y manejar el dinero. Además de ser una herramienta útil para la evaluación de la capacidad funcional, la prueba de velocidad de marcha también se ha utilizado como predictor de la mortalidad en adultos mayores. Se ha demostrado que una velocidad de marcha lenta se asocia con un mayor riesgo de mortalidad en esta población. En resumen, la prueba de velocidad de marcha es una herramienta importante para la evaluación de la capacidad funcional y la salud en adultos mayores. Permite a los profesionales de la salud identificar a las personas que pueden estar en mayor riesgo de limitaciones funcionales y desarrollar planes de tratamiento y prevención para mejorar su calidad de vida y reducir su riesgo de mortalidad.
    """
    )

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
    st.markdown(
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
    """
    )

with tab6:

    st.header("Masa musculo-esquelética")
    st.markdown(
    """
    El porcentaje de masa muscular esquelética se mide utilizando técnicas de imagenología y mediciones antropométricas. Algunos de los métodos más comunes para medir la masa muscular esquelética incluyen:

    - Densitometría de Doble Energía de Rayos X (DXA o DEXA): Esta técnica se utiliza comúnmente para medir la densidad mineral ósea, pero también puede proporcionar información sobre la masa muscular magra. DXA utiliza rayos X de dos energías diferentes para medir la cantidad de tejido magro en el cuerpo.

    - Tomografía Computarizada (TC): La TC puede utilizarse para obtener imágenes detalladas de los músculos y medir su volumen y densidad. A partir de esta información, se puede calcular el porcentaje de masa muscular esquelética.

    - Resonancia Magnética (RM): Al igual que la TC, la RM puede proporcionar imágenes detalladas de los tejidos musculares, lo que permite calcular el volumen y la masa muscular magra.

    - Bioimpedancia: Este método mide la resistencia eléctrica del cuerpo al paso de una corriente eléctrica de bajo nivel. La resistencia está relacionada con la cantidad de tejido magro, incluida la masa muscular.

    - Mediciones antropométricas: Estas incluyen la medición de circunferencias de brazos, piernas y otros segmentos del cuerpo, así como la medición de pliegues cutáneos. Si bien estas medidas pueden proporcionar una estimación del contenido de grasa y masa muscular, son menos precisas que las técnicas de imagen avanzadas.

    La relación entre el porcentaje de masa muscular esquelética y la sarcopenia es directa. La sarcopenia se caracteriza por una disminución significativa de la masa muscular esquelética, lo que conduce a la pérdida de fuerza muscular y funcionalidad. A medida que disminuye la masa muscular, las personas pueden experimentar una disminución en su capacidad para realizar actividades diarias, lo que a su vez puede aumentar el riesgo de caídas, fracturas y discapacidad.

    La medición del porcentaje de masa muscular esquelética es importante en la evaluación y diagnóstico de la sarcopenia. La disminución de la masa muscular es un marcador clave de la enfermedad y se utiliza para identificar a las personas en riesgo de desarrollar sarcopenia. Los profesionales de la salud pueden utilizar estas mediciones junto con otras evaluaciones clínicas y funcionales para determinar si una persona tiene sarcopenia y desarrollar un plan de tratamiento adecuado, que puede incluir ejercicio, cambios en la dieta y otras intervenciones.
    """
    )

with tab7:
    st.header("otro nombre")
    st.markdown("oihfdiouhgodfhiosfhsiodfhsiofhiosf")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.write(' ')
    with col3:
        st.write(' ')

if selected_tab == "Configuración":
    st.title("Bienvenido a la Pestaña de Configuración")
    st.write("Este es el contenido de la pestaña de Configuración.")



