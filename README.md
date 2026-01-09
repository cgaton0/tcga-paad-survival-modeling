# TFM-TCGA-PAAD
TFM del máster de ciencia de datos de la UOC basado en los datos del TCGA-PAAD.

## Descripción del contenido

- data: Contiene los datos sin procesar en la carpeta raw y los datos procesados, una vez ejecutado el notebook correspondiente, en la carpeta processed.
- html: Contiene las versiones html de los notebook para facilitar su visualización.
- images: Directorio preferente para el guardado de las imágenes generadas en los notebook.
- model: Contiene los archivos relacionados con el modelo de regresión de supervivencia implementado. Se encuentra el escalador serializado y los parámetros del modelo para facilitar su posterior reutilización.
- tables: Contiene las diferentes tablas generadas durante la ejecución del notebook.
- Archivo utils.py contiene funciones auxiliares utilizadas en los diferentes notebook.

## Orden de ejecución

En primer lugar, es necesario ejecutar el notebook llamado "1_Preprocessing". Este notebook realiza todos los procesos de carga y preprocesamiento de los datos y guarda la información resultante en la carpeta processed dentro de data.

Los otros notebook se pueden ejecutar de manera independiente, debido a que estos no modifican ninguno de los datos procesados. Es recomendable seguir el flujo de ejecución establecido para poder comprender mejor los diferentes resultados que se van obteniendo.

El notebook llamado "2_EDA" realiza todas las tareas relacionadas con el análisis exploratorio de los datos y genera la mayoría de tablas y imágenes. El notebook llamado "3_Survival_analysis" realiza todas las tareas de análisis de supervivencia mediante curvas de supervivencia de Kapplan-Meier y regresiones de Cox. El notebook llamado "4_Model_prediction" genera y entrena el modelo de regresión de supervivencia y muestra la bondad del modelo mediante el índice de concordancia (C-Index) y el método SHAP. 
