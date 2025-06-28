

class rectangulo {
    constructor(ancho, altura) {
        this.ancho = ancho;
        this.altura = altura;
    }
    areaRectangulo() {
            console.log(`El área del rectangulo es de: ${this.ancho * this.altura}`);
        }
    perimetroRectangulo() {
            console.log(`El perímetro del rectangulo es de: ${2 * (this.ancho + this.altura)}`);
    }
};

let newRectangulo = new rectangulo(5, 10);
newRectangulo.areaRectangulo();
newRectangulo.perimetroRectangulo();