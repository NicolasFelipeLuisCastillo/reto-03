# Taller de Programación Orientada a Objetos en Python  

Este repositorio contiene ejercicios prácticos de POO en Python, documentados y explicados.  

---

## 🔹 Ejercicio de Clase (`ejercicio_clase.py`)  

En este ejercicio trabajamos con las clases:  

- **Point**: Representa un punto en el plano.  
- **Line**: Representa una línea definida por dos puntos, con métodos para calcular:  
  - Longitud (`compute_length`)  
  - Pendiente (`compute_slope`)  
  - Cruce vertical (`compute_vertical_crossing`)  
  - Cruce horizontal (`compute_horizontal_crossing`)  
- **Rectangle**: Ahora tiene **4 métodos de inicialización**:  
  1. Punto inferior izquierdo + ancho + alto.  
  2. Centro + ancho + alto.  
  3. Dos esquinas opuestas.  
  4. **Cuatro líneas** (composición → un rectángulo se compone de 4 lados).  
- **Square**: Hereda de `Rectangle` y asegura que el ancho y el alto sean iguales.  

## 🔹 Ejercicio de Clase (`ejercicio_clase.py`)

Aquí está el código completo del ejercicio:

```python
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class Line(Point):
    def __init__(self, start: Point, end: Point ) -> None:
        super().__init__(start.x, start.y)
        self.start = start
        self.end = end

    def compute_length(self) -> float:
        length = ((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2) ** 0.5
        return length


---

## 🔹 Reto 03 (`Reto_03.py`)  

### 📖 Enunciado

**Restaurant scenario:**  
You want to design a program to calculate the bill for a customer's order in a restaurant.  

- `MenuItem`: Clase base con atributos `name`, `price` y un método para calcular el precio total.  
- Subclases de `MenuItem`: `Beverage`, `Appetizer`, `MainCourse`.  
- `Order`: Clase que mantiene una lista de `MenuItem` y puede:  
  - Agregar ítems.  
  - Calcular la cuenta total.  
  - Aplicar descuentos especiales.  

### 📊 Diagrama de clases  

El diagrama de clases se encuentra en el archivo [`class_diagram_restaurant.mmd`](./class_diagram_restaurant.mmd).  
Si tu editor soporta Mermaid, lo puedes visualizar directamente.  

### 📌 Código  

El código completo está en [`Reto_03.py`](./Reto_03.py).  

Ejemplo de uso incluido en el archivo:  

```python
order = Order()
order.add_item(Beverage("Cola", 2.0, "large"))
order.add_item(Appetizer("Nachos", 5.0, 2))
order.add_item(MainCourse("Burger", 10.0, "regular"))

print("Total bill:", order.calculate_total())
