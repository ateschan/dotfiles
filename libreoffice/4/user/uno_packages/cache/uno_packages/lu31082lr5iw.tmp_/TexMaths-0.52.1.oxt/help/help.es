
1. Modos TexMaths

A partir de la versión 0.51, TexMaths tiene dos modos de ecuación, dependiendo de la posición del cursor en un documento Writer, Impress o Draw. Cuando el cursor se encuentra dentro de un cuadro de texto (en Impress es donde se escribe el texto, en Draw se puede entrar en un cuadro de texto haciendo doble clic en un formulario, y en Writer es cuando se inserta un cuadro de texto en la página), TexMaths cambia automáticamente al modo Texto. En cualquier otro lugar, TexMaths utiliza el modo LaTeX.

En el modo LaTeX, obtendrá como siempre su ecuación como una imagen gráfica en formato PNG o SVG. En el modo Texto, la ecuación se inserta como un conjunto de caracteres utilizando fuentes TexMaths (estas fuentes son específicas de TexMaths y se instalan automáticamente cuando se necesitan). Esto se debe a que, debido a una limitación de LibreOffice, no es posible insertar gráficos dentro de un cuadro de texto, por lo que TexMaths tiene que insertar las ecuaciones como texto.

El modo Texto tiene algunas características y limitaciones que se explican más adelante, en el apartado 6.
 


2. La barra de herramientas TexMaths

Una vez instalada la extensión TexMaths en LibreOffice, debería ver una nueva barra de herramientas en Writer, Impress y Draw. Se trata de la barra de herramientas TexMaths. En Writer, esta barra de herramientas consta de cuatro iconos, mientras que en Impress y Draw sólo hay tres.

En Writer, haciendo clic en el icono situado más a la izquierda (el que tiene el símbolo Pi azul) se inicia la macro Ecuaciones TexMaths. El segundo icono se utiliza para TexMaths Numbered Equations. El tercer icono está vinculado a la macro TexMaths Recompilar ecuaciones. Por último, haciendo clic en el icono situado más a la derecha se abre el cuadro de diálogo Configuración del sistema TexMaths. Observe que en Impress y Draw, el segundo icono no está presente. También hay un submenú Herramientas/TexMaths, situado justo encima del submenú Herramientas/Macros. 



3. Introducción a TexMaths Equations

Si LaTeX ya está instalado en su sistema, todo lo que tiene que hacer para empezar con TexMaths es hacer clic en el icono Ecuaciones de TexMaths de la barra de herramientas de TexMaths. TexMaths intentará encontrar los programas externos que utiliza para generar ecuaciones LaTeX. A continuación, escriba algún código LaTeX en el campo de texto del editor de ecuaciones TexMaths y haga clic en el botón LaTeX para generar la imagen de la ecuación.

Ej: x(t) = \mu ^2 (t) debería producir la ecuación x(t)=(t)

A partir de TexMaths 0.46, el editor de ecuaciones dispone de paletas de símbolos para introducir el código LaTeX de más de 300 símbolos. Basta con hacer clic en el símbolo seleccionado y el código LaTeX correspondiente se insertará en la posición del cursor en el editor de ecuaciones. Los iconos de símbolos pueden ocultarse en la pestaña Interfaz del cuadro de diálogo Configuración del sistema TexMaths. Allí también puede definirse el color de los símbolos (blanco o negro).

Si el cursor del documento se sitúa dentro de un cuadro de texto, TexMaths cambia automáticamente al modo Texto e instala fuentes TexMaths para el usuario local. En este caso, las ecuaciones no se insertan como imágenes gráficas PNG o SVG, sino como caracteres normales que utilizan fuentes TexMaths. 



4. Generar ecuaciones LaTeX

Una vez escrita una ecuación, puede generarla haciendo clic en el botón LaTeX del cuadro de diálogo Ecuaciones de TexMaths. En modo LaTeX, esto genera una imagen de tu ecuación en el formato, tipo y tamaño que hayas seleccionado. Puede elegir entre los compiladores LaTeX, XeLaTeX y LuaLaTeX en el cuadro de diálogo Configuración del sistema. En el modo Texto, se inserta un conjunto de caracteres utilizando fuentes TexMaths que representa la ecuación. El tamaño de la fuente es igual al tamaño de la fuente de texto. 



5. Modo LaTeX

  5.1. Selección del formato de imagen

TexMaths puede generar e insertar dos tipos de imágenes en un documento LibreOffice (cuando el cursor no está dentro de un cuadro de texto). Para seleccionar el formato de imagen, utilice el selector situado dentro del marco Formato de imagen.

El formato de imagen por defecto es el formato vectorial SVG. Permite redimensionar las ecuaciones LaTeX sin pérdida de precisión y no necesita instalar ninguna fuente matemática especial en LibreOffice, porque los símbolos matemáticos se dibujan simplemente usando curvas. Es el formato preferido (y predeterminado), pero puede haber algunos problemas al exportar documentos de LibreOffice a MS Office (véase el apartado 11).

El otro formato de imagen soportado es PNG y es un formato de imagen rasterizada. Por lo tanto, tiene que seleccionar una resolución para utilizarlo. Aunque la resolución predeterminada es de 600 ppp, puede elegir entre varios valores predefinidos. No debería haber problemas de compatibilidad al utilizar el formato PNG para la exportación de documentos de MS Office.

Tenga en cuenta que cada formato sólo está disponible si el programa externo correspondiente (dvisvgm para SVG y dvipng para PNG) está instalado en su sistema con su ruta establecida mediante el cuadro de diálogo Configuración del sistema de TexMaths (normalmente se adivina en la primera ejecución). Al menos uno de estos dos programas es necesario para ejecutar TexMaths.


  5.2. Tamaño de letra

TexMaths puede manejar diferentes tamaños de letra para sus ecuaciones. Para cambiar el tamaño de la fuente, utilice el selector situado dentro del marco de tamaño de fuente. Puede elegir entre los tamaños de fuente predefinidos o escribir el que prefiera si no aparece en la lista.


  5.3. Transparencia

Puede activar la transparencia de la imagen de la ecuación marcando la casilla Transparencia en el cuadro de diálogo Ecuaciones de TexMaths. Esto puede ser útil cuando el fondo del documento no es blanco. La transparencia puede utilizarse con los formatos de imagen SVG y PNG.


  5.4. Tipo de ecuación

En modo LaTeX, TexMaths puede generar tres tipos de ecuaciones LaTeX:
- ecuaciones de visualización
- ecuaciones de visualización en línea
- Ecuaciones LaTeX

Para seleccionar un tipo de ecuación, sólo tiene que utilizar el botón de opción situado dentro del marco Tipo de ecuación. 

Para generar ecuaciones de visualización o ecuaciones de visualización en línea, todo lo que tiene que hacer es seleccionar el tipo de ecuación apropiado y, a continuación, escribir el código de la ecuación en el campo de texto del cuadro de diálogo Ecuaciones de TexMaths.

Ejemplo: Para generar el símbolo alfa griego, basta con escribir \alpha

Las ecuaciones de visualización en línea se obtienen del mismo modo, pero la diferencia es el estilo de la ecuación generada, que se integra mejor dentro de un texto en Writer. Por ejemplo, el índice de suma y el exponente se muestran junto al signo de suma y no debajo o encima.

Ambos tipos de ecuaciones son ideales para ecuaciones simples de una línea y la alineación vertical dentro del texto es correcta, pero no pueden manejar ecuaciones multilínea o entornos LaTeX más generales. Para ese tipo de ecuaciones, seleccione el tipo de ecuación LaTeX y escriba su ecuación dentro de las instrucciones \begin{} y \end{}. Puede utilizar cualquier instrucción del entorno LaTeX.

Ej: Escriba las siguientes líneas para mostrar una ecuación de tres líneas, alineadas en el signo igual.
\Comienza.
x &= 1 \\
y &= 2x+1\\\
&= 3\\
\fin


  5.5. Nombre de la ecuación

En el cuadro de diálogo Ecuaciones de TexMaths, puede introducir una etiqueta en el campo de texto Nombre. Esto se puede utilizar para recuperar una ecuación por su nombre y podría ayudar cuando se trata de animaciones en Impress.


  5.6. Preferencias

TexMaths viene con algunos ajustes por defecto. Si estos ajustes no se adaptan a sus necesidades, puede cambiarlos utilizando el diálogo Preferencias de TexMaths que se obtiene haciendo clic en el botón Preferencias. Este diálogo permite cambiar el formato de imagen, tamaño de fuente, tipo de ecuación, etc., para cada tipo de documento LibreOffice. A continuación, puede guardar la nueva configuración, restaurar la configuración predeterminada o cargar la configuración ya guardada.


  5.7. Preámbulo LaTeX

Haciendo clic en el botón Preámbulo se muestra el diálogo Preámbulo de TexMaths que permite ajustar su preámbulo LaTeX. Por ejemplo, para generar ecuaciones coloreadas, descomente las tres líneas siguientes del preámbulo por defecto, cambie el valor del color RGB como prefiera y guarde el preámbulo.

%\definecolor{fgcolor}{RGB}{0,0,255}
%\definecolor{bgcolor}{RGB}{255,0,0}
%\pagecolor{bgcolor}\color{fgcolor}

Ahora, todas las ecuaciones nuevas tendrán el esquema de colores que haya definido en el preámbulo. Tenga en cuenta que las ecuaciones con un color de fondo ya no son transparentes, incluso si la opción de transparencia estaba marcada. Por lo tanto, debe eliminar el fondo de color si desea transparencia.

El preámbulo se almacena en las propiedades del documento. De esta manera cada documento puede tener su propio preámbulo. Tenga en cuenta que el preámbulo por defecto es global y no se puede cambiar. Tenga en cuenta que LaTeX, XeLaTeX y LuaLaTeX tienen un preámbulo por defecto diferente.


  5.8. Comandos \input, \include y \usepackage

A partir de TexMaths 0.41, los comandos \input y \include LaTeX pueden utilizarse para insertar el contenido de un archivo de texto LaTeX (.tex). Se supone que los archivos .tex insertados se encuentran en el mismo directorio que el documento.

Ej: En el documento mi_doc.odt, el comando LaTeX:

\{include{my_equations}

puede utilizarse para insertar el contenido del archivo LaTeX mis_ecuaciones.tex siempre que este archivo se encuentre en el mismo directorio que mi_doc.odt. 

También existe la posibilidad de utilizar archivos .sty personalizados mediante el uso de comandos \usepackage. Estos comandos deben insertarse en el preámbulo y luego (si se desea) almacenarse en el documento actual. Los archivos .sty deben estar en el mismo directorio que el documento.

Ej: En el documento mi_doc.odt, se puede utilizar el estilo del documento mi_estilo.sty añadiendo al preámbulo de LaTeX el comando:

\usepackage{my_style}

El archivo mi_estilo.sty debe encontrarse en el mismo directorio que mi_doc.odt, de lo contrario no funcionará.


  5.9. Texto a LaTeX en Writer

Escriba algún código LaTeX directamente dentro de un documento Writer (es decir, sin abrir el cuadro de diálogo TexMaths), seleccione el texto y haga clic en el icono Ecuaciones TexMaths (o utilice un atajo de teclado si ha definido uno). El texto seleccionado se convierte silenciosamente en una imagen de ecuación LaTeX. El formato de imagen aplicado, el tamaño de la ecuación y el tipo de ecuación son los definidos por defecto en las Preferencias de TexMaths. Tenga en cuenta que esto no funcionará en Writer cuando el cursor se encuentre dentro de un cuadro de texto.


  5.10. Editar ecuaciones

Dentro de un documento LibreOffice, seleccione una imagen de ecuación (ya generada utilizando TexMaths) y haga clic en el icono Ecuaciones TexMaths de la barra de herramientas TexMaths (o utilice un atajo de teclado si ha definido uno). Aparecerá el cuadro de diálogo Ecuaciones TexMaths con el texto de la ecuación seleccionado. Edite el texto y haga clic en el botón LaTeX para generar la ecuación modificada.

Por supuesto, puedes cerrar un documento, abrirlo de nuevo y editar las ecuaciones guardadas.


  5.11. Recompilación de ecuaciones TexMaths

Cuando un documento (en Writer, Impress o Draw) contiene muchas ecuaciones, puede ser útil cambiar su tamaño de fuente, transparencia, formato de imagen, etc., de una sola vez. Este es el propósito de la macro TexMaths Recompilar Ecuaciones.

Al hacer clic en el icono de la barra de herramientas correspondiente (el que tiene el engranaje), se abre un cuadro de diálogo en el que puede cambiar varios parámetros de la ecuación y el preámbulo. Si no desea cambiar un parámetro de una lista, active el botón Dejar como está.

En cualquiera de los tres tipos de documento, puede recompilar todas las ecuaciones del documento seleccionando la opción Recompilar todas las ecuaciones.

En los documentos Writer, al seleccionar la opción Recompilar ecuaciones seleccionadas, puede elegir recompilar sólo las ecuaciones que se encuentran dentro del área de texto seleccionada. Tenga en cuenta que, debido a algunas limitaciones con las selecciones en LibreOffice, esta macro no recompila las ecuaciones situadas en tablas, marcos de texto, encabezados y pies de página. Si es necesario, puede recompilar esas ecuaciones una a una, editándolas de la forma habitual. 

En los documentos de Impress y Draw, seleccionando la opción Recompilar ecuaciones de la diapositiva, puede recompilar sólo las ecuaciones que se encuentren dentro de la diapositiva actual.

Una vez configurados todos los parámetros y opciones, haga clic en el botón Ejecutar y todas las ecuaciones o las seleccionadas se actualizarán con los nuevos valores de los parámetros. Cuando se trata de cientos de ecuaciones, esto puede tomar un tiempo, así que por favor sea paciente.


  5.12. Numeración de ecuaciones en Writer

Numerar ecuaciones es tan sencillo como hacer clic en el icono Ecuaciones numeradas de TexMaths (o introducir un atajo de teclado si has definido uno), introducir tu ecuación y hacer clic en el botón LaTeX. Una ecuación centrada y numerada (con numeración a la izquierda o a la derecha) se inserta automáticamente en su documento Writer.

También puede seleccionar el espaciado que desee y el título de la ecuación en la pestaña Opciones del cuadro de diálogo Configuración del sistema TexMaths.

Las ecuaciones numeradas no pueden insertarse en Writer cuando el cursor está dentro de un cuadro de texto. 


  5.13. Compatibilidad con ooolatex

A partir de la versión 0.34, TexMaths es compatible con ooolatex. Esto significa que si tienes un documento que contiene ecuaciones ooolatex, puedes editar esas ecuaciones seleccionándolas (una a una) y llamando a la macro TexMaths Equation. A continuación, puede modificar el código LaTeX y regenerar la ecuación en formato SVG o PNG, según prefiera.



6. Modo texto

  6.1. Ecuaciones

El modo Texto es seleccionado automáticamente por TexMaths cuando el cursor está dentro de un cuadro de texto. En Impress, ésta es la única manera de introducir una ecuación en línea que se mueve con el texto cuando se modifica. En modo Texto, TexMaths intenta convertir el código LaTeX en un conjunto de caracteres utilizando fuentes TexMaths. 

En el modo Texto, sólo es posible generar ecuaciones simples con un máximo de un nivel de subíndice y superíndice. Cualquier otra cosa no es posible. Tenga en cuenta que en Impress todavía es posible generar ecuaciones complejas en modo LaTeX colocando el cursor fuera de los cuadros de texto y haciendo clic en el icono Ecuación de TexMaths.


  6.2. Entornos

En el modo Texto, las llaves se utilizan para obtener entornos con diferentes posiciones y propiedades, como en la siguiente ecuación:
y_n = \suma_{n=1}^{N-1} x_n

Se pueden introducir todos los símbolos que no estén atenuados en la paleta de símbolos.

También es posible utilizar algunos entornos sencillos para dar formato a su ecuación:
- \text{}, \textrm{}, \textbf{}, \textit{} para el formato de texto
- negrita{}, cursiva{}, subrayado{} para el peso de la fuente
- \mathbb{}, \mathcal{}, \mathscr{}, \mathfrak{} para fuentes matemáticas especiales.
- \huge{}, \Huge{}, \large{}, \Large{}, \small{}, \tiny{} para el tamaño de letra

También puede anidar entornos, como en el siguiente ejemplo:
w \textrm{\large{text} x


  6.3. Compartir documentos con ecuaciones de texto
  
Si desea compartir un documento que contiene ecuaciones TexMaths Text, no es necesario enviar las fuentes TexMaths a su destinatario. En su lugar, puede incrustar las fuentes TexMaths en su documento utilizando el menú Archivo / Propiedades / Fuentes / Incrustación de fuentes y activando la opción Incrustar fuentes en el documento. Esto funciona igual para los documentos Writer / Impress y Draw.


7. Historia

A partir de la versión 0.51, un mecanismo de historial permite recuperar códigos de ecuaciones anteriores dentro del editor de ecuaciones. Los dos botones << y >> permiten navegar por el historial y el botón <> sirve para borrarlo.
 


8. Configuración del sistema

Haciendo clic en el tercer icono se abre el cuadro de diálogo Configuración del sistema TexMaths. En la primera pestaña de este diálogo, puede cambiar las rutas de los archivos de los programas externos. Desde TexMaths 0.46, se debe proporcionar la ruta de archivo completa.

La segunda pestaña permite seleccionar el compilador LaTeX (LaTeX, XeLaTeX o LuaLaTeX, si estos últimos están instalados y son compatibles con la versión de dvisvgm que utilice. Tenga en cuenta que XeLaTeX no puede utilizarse para producir imágenes de ecuaciones PNG). También se ofrecen opciones para la numeración de ecuaciones y la compatibilidad con MS Word. En la tercera pestaña es posible seleccionar el tipo de letra utilizado en el editor de ecuaciones y configurar diversas opciones relacionadas con los iconos de símbolos. La cuarta pestaña del cuadro de diálogo Configuración del sistema permite definir algunos atajos de teclado para lanzar las macros de TexMaths.



9. Exportación de documentos a MS Office

Si piensa exportar sus documentos a MS Office (Word y Powerpoint, cualquiera que sea su versión), puede guardar sus documentos de LibreOffice en los formatos .docx y .pptx.

También se recomienda establecer la opción de compatibilidad con la alineación vertical de Word (en el cuadro de diálogo Configuración del sistema TexMaths) si sus documentos Writer tienen que exportarse a Word. Esto mejorará en gran medida en Word la alineación vertical de las ecuaciones en texto. Tenga en cuenta que puede ser necesario ajustar manualmente la alineación vertical de las ecuaciones en Word.



10. Atajos de teclado

Para configurar los accesos directos para lanzar las ecuaciones TexMaths con o sin numeración, haga clic en el botón Configuración del sistema TexMaths de la barra de herramientas TexMaths y defina sus accesos directos. Para las ecuaciones sin numeración, puede tener un único acceso directo para todas las aplicaciones o uno diferente para cada una. Como las ecuaciones numeradas sólo pueden utilizarse en Writer, sólo hay un atajo para ellas.

Dentro del cuadro de diálogo Ecuaciones de TexMaths, puede utilizar los siguientes atajos:
- Esc para cerrar el diálogo sin generar una ecuación
- Alt-L o Ctrl-L para generar una ecuación
- Alt-P o Ctrl-P para mostrar el cuadro de diálogo Preferencias
- Alt-B o Ctrl-B para mostrar el diálogo Preámbulo


11. Problemas conocidos

- Aunque desarrollado para LibreOffice, TexMaths también puede utilizarse en Apache Openoffice 4.x.

- Las ecuaciones que incluyen comandos PSTricks no se pueden renderizar correctamente como imágenes PNG debido a dvipng. En su lugar, puede utilizar con seguridad el formato SVG.

- Al exportar documentos de Impress con ecuaciones de texto a formato MS PowerPoint, aunque la opción de incrustar fuentes esté activada en Impress, existe un error que hace que las fuentes incrustadas no estén disponibles en PowerPoint. Afortunadamente, aquí hay una solución: en Windows, teniendo las fuentes TexMaths instaladas, abra el .pptx con PowerPoint e incruste las fuentes allí (utilice Archivo / Opciones / Guardar, luego Incrustar fuentes en el archivo y seleccione la opción de incrustación deseada). Ahora tu documento .pptx tiene fuentes incrustadas y puede ser compartido con otras personas. 
