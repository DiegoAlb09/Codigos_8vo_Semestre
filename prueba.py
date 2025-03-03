from experta import *

class Senderismo(Fact):
    """Hechos sobre el usuario y su experiencia en senderismo"""
    pass

class SistemaExpertoSenderismo(KnowledgeEngine):

    # 🔹 Determinar el nivel de experiencia en senderismo
    @Rule(Senderismo(ha_realizado_senderismo=False))
    def nivel_principiante(self):
        self.declare(Senderismo(nivel_experiencia="Principiante"))

    @Rule(Senderismo(ha_realizado_senderismo=True, frecuencia="Ocasionalmente"))
    def nivel_principiante_ocasional(self):
        self.declare(Senderismo(nivel_experiencia="Principiante"))

    @Rule(Senderismo(ha_realizado_senderismo=True, frecuencia="Regularmente"))
    def nivel_intermedio(self):
        self.declare(Senderismo(nivel_experiencia="Intermedio"))

    @Rule(Senderismo(ha_realizado_senderismo=True, frecuencia="Frecuentemente"))
    def nivel_avanzado(self):
        self.declare(Senderismo(nivel_experiencia="Avanzado"))

    # 🔹 Verificación para recomendación de rutas
    @Rule(Senderismo(nivel_experiencia=MATCH.nivel))
    def verificar_ruta(self, nivel):
        self.declare(Senderismo(requiere_ruta=True, nivel_experiencia=nivel))

    # 🔹 Reglas para recomendar rutas
    @Rule(Senderismo(requiere_ruta=True, nivel_experiencia="Principiante"))
    def recomendar_rutas_principiante(self):
        print("Recomendación: Senderos cortos y bien señalizados.")

    @Rule(Senderismo(requiere_ruta=True, nivel_experiencia="Intermedio"))
    def recomendar_rutas_intermedio(self):
        print("Recomendación: Senderos con ascensos y terreno irregular.")

    @Rule(Senderismo(requiere_ruta=True, nivel_experiencia="Avanzado"))
    def recomendar_rutas_avanzado(self):
        print("Recomendación: Rutas de alta montaña y travesías largas.")

    # 🔹 🔥 SOLUCIÓN: Cambiar cómo se activan las reglas del equipo
    @Rule(Senderismo(nivel_experiencia=MATCH.nivel))
    def verificar_equipo(self, nivel):
        self.declare(Senderismo(requiere_equipo=True, nivel_experiencia=nivel))

    @Rule(Senderismo(requiere_equipo=True, nivel_experiencia="Principiante"))
    def recomendar_equipo_basico(self):
        print("Recomendación de equipo: Ropa cómoda, calzado básico, agua y snacks.")

    @Rule(Senderismo(requiere_equipo=True, nivel_experiencia="Intermedio"))
    def recomendar_equipo_intermedio(self):
        print("Recomendación de equipo: Bastones y mochila con suministros.")

    @Rule(Senderismo(requiere_equipo=True, nivel_experiencia="Avanzado"))
    def recomendar_equipo_avanzado(self):
        print("Recomendación de equipo: Equipo técnico, brújula/GPS y planificación avanzada.")

    # 🔹 Variables de seguridad
    @Rule(Senderismo(conoce_seguridad=False))
    def nivel_seguridad_bajo(self):
        self.declare(Senderismo(nivel_seguridad="Bajo"))

    @Rule(Senderismo(conoce_seguridad=True))
    def nivel_seguridad_medio(self):
        self.declare(Senderismo(nivel_seguridad="Medio"))

    @Rule(Senderismo(conoce_seguridad=True, nivel_experiencia="Avanzado"))
    def nivel_seguridad_alto(self):
        self.declare(Senderismo(nivel_seguridad="Alto"))

    @Rule(Senderismo(nivel_seguridad="Bajo"))
    def medidas_seguridad_bajo(self):
        print("⚠️ Medidas de seguridad recomendadas: Tomar un curso básico de primeros auxilios y revisar normas de seguridad.")

    @Rule(Senderismo(nivel_seguridad="Medio"))
    def medidas_seguridad_medio(self):
        print("✅ Medidas de seguridad recomendadas: Llevar botiquín de primeros auxilios y aprender técnicas básicas de rescate.")

    @Rule(Senderismo(nivel_seguridad="Alto"))
    def medidas_seguridad_alto(self):
        print("🏕️ Medidas de seguridad recomendadas: Capacidad para responder a emergencias, planificación avanzada y uso de equipo especializado.")

if __name__ == "__main__":
    # Inicializar el sistema experto
    sistema = SistemaExpertoSenderismo()
    sistema.reset()
    
    print("\n" + "="*60)
    print("🏔️  BIENVENIDO AL SISTEMA EXPERTO DE SENDERISMO  🏔️")
    print("="*60)
    print("Este sistema te proporcionará recomendaciones personalizadas")
    print("para rutas de senderismo, equipo necesario y medidas de seguridad")
    print("basado en tu nivel de experiencia.")
    print("="*60 + "\n")
    
    # Validar entrada para experiencia en senderismo
    while True:
        ha_realizado = input("¿Has realizado senderismo anteriormente? (si/no): ").lower()
        if ha_realizado in ["si", "s", "sí", "yes", "y"]:
            ha_realizado_senderismo = True
            break
        elif ha_realizado in ["no", "n"]:
            ha_realizado_senderismo = False
            frecuencia = None
            break
        else:
            print("⚠️ Por favor, responde 'si' o 'no'.")
    
    # Preguntar frecuencia solo si ha hecho senderismo antes
    frecuencia = None
    if ha_realizado_senderismo:
        while True:
            print("\nIndica con qué frecuencia realizas senderismo:")
            print("1. Ocasionalmente (pocas veces al año)")
            print("2. Regularmente (mensualmente)")
            print("3. Frecuentemente (semanalmente)")
            
            opcion = input("Selecciona una opción (1-3): ")
            
            if opcion == "1":
                frecuencia = "Ocasionalmente"
                break
            elif opcion == "2":
                frecuencia = "Regularmente"
                break
            elif opcion == "3":
                frecuencia = "Frecuentemente"
                break
            else:
                print("⚠️ Por favor, selecciona una opción válida (1-3).")
    
    # Validar conocimiento de seguridad
    while True:
        conoce = input("\n¿Conoces las medidas de seguridad básicas para senderismo? (si/no): ").lower()
        if conoce in ["si", "s", "sí", "yes", "y"]:
            conoce_seguridad = True
            break
        elif conoce in ["no", "n"]:
            conoce_seguridad = False
            break
        else:
            print("⚠️ Por favor, responde 'si' o 'no'.")
    
    print("\n" + "-"*60)
    print("Analizando tu perfil... 🔍")
    print("-"*60 + "\n")
    
    # Declarar los hechos basados en la entrada del usuario
    if ha_realizado_senderismo:
        sistema.declare(Senderismo(
            ha_realizado_senderismo=ha_realizado_senderismo,
            frecuencia=frecuencia,
            conoce_seguridad=conoce_seguridad
        ))
    else:
        sistema.declare(Senderismo(
            ha_realizado_senderismo=ha_realizado_senderismo,
            conoce_seguridad=conoce_seguridad
        ))
    
    # Ejecutar el sistema experto
    sistema.run()
    
    print("\n" + "="*60)
    print("¡Gracias por utilizar nuestro sistema experto de senderismo!")
    print("¡Disfruta de tus aventuras de forma segura! 🌄")
    print("="*60 + "\n")

