from controllers.fraction_controller import FractionController
from models.fraction_model import FractionModel
from views.main_view import MainView


def main() -> None:
    """Función principal que inicializa el modelo, la vista y el controlador, y ejecuta la app."""
    model = FractionModel()          
    view = MainView()               
    FractionController(model, view)  
    view.mainloop()                 


if __name__ == "__main__":
    main()  