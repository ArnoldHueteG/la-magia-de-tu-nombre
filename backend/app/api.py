from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from unidecode import unidecode
from datetime import datetime
app = FastAPI()

origins = [
    "*"
    # "http://localhost:3000",
    # "localhost:3000",
    # "http://localhost:5173",
    # "localhost:5173",
    # "https://la-magia-de-tu-nombre-gl3rxvbmka-ue.a.run.app:80"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

meanings = {
    7: "Te interesará mucho todo lo místico, misterioso y existe una tendencia fuerte a ser algo intolerante con los demás cuando consideras que carecen de capacidad para comprenderte.",
    8: "Vida material desahogada, puedes nacer en un hogar con comodidades o ser heredero, pero al ser 8 debes luchar por mantener el equilibrio entre lo material y espiritual para no perder las perspectivas y caer en la superficialidad y malos caminos de vida.",
    9: "Tienes capacidad innata para hacer buenos contactos con el público, porque tendrás una fuerte capacidad persuasiva. Sin embargo, deberás poner especial atención a los cambios de ánimo por altibajos en tu vida que te costará controlar si te dejas dominar por la depresión y los temores. ",
    10: "Tienes capacidad de embarcarte en la organización y dirección de grandes proyectos, pero sentirás a menudo que los demás no logran ayudarte como lo esperas y te costará delegar. Debes evitar atarte a las cargas y problemas de otros, postergando tus mayores sueños. Posees una necesidad de mandar, ordenar y llegar al poder en el ámbito que te encuentres y para ello te vales de una gran elocuencia. ",
    11: "Posees un innato talento artístico, pero debes luchar por sacarlo a flote sin temores porque cuando lo haces puedes llegar lejos. Tiendes a dudar de tus talentos y dejarte vencer por la inseguridad e indecisión. Es muy importante que busques elevar tu autoestima de apariencia y evites compararte con los demás, olvidando que eres especial y hermoso como todos, porque tiendes a ser dependiente en amores y caer en depresiones. Un ejemplo de 11 letras en el nombre es la cantante Mariah Carey que desde pequeña se inclinó al canto. Se conoce que cuando ha tenido sonados romancen con artistas como Luis Miguel, al culminar su relación cayó en un fuerte estado depresivo que la tuvo algo inestable por unos meses. ",
    12: "Tu capacidad de escuchar y manejar problemas en tu vida privada y en el entorno será notable. Tiendes a ser muy diplomático y llamado a solucionar conflictos como mediador nato. Debes evitar dejar las cosas a medias y también a dejar atrás el pasado para avanzar. ",
    13: "Debes cuidar mucho de no meterte en líos, chismes y problemas, porque suelen a veces involucrarte sin que tú lo esperes. Tu carácter es variante, oscila entre la calma y los ataques de euforia que a veces pueden costarte caro, así como caprichos. Serás luchador nato y de escalar poco a poco hasta llegar donde te haga feliz. Tu mayor reto será hallar el amor adecuado para comunicarse bien contigo. Un ejemplo de esta cantidad de letras es nuestro jugador de fútbol Paolo Guerrero. Su nombre de pila como jugador y personaje público es ese y como recordaremos, pese a su juventud, estuvo metido en chismes y problemas con los medios de comunicación. Tiene cambios de ánimo al jugar y a veces le salen unos berrinches de niño, pero cuando se repone su actuación es alabada y reconocida por todos. De amores aún no lo vemos asentado, porque tal vez es algo que llegará cuando sea necesario y esté más preparado. Otro ejemplo de un personaje con 13 letras en el nombre se da con la cantante Britney Spears, que como conocemos siempre pasa por imprevistos y está en el ojo de la tormenta. Ha tenido etapas en las que brilla por su trabajo y ha logrado mantener unidos a sus seguidores. ",
    14: "Nombre marcado por la imperiosa necesidad de que el amor sea el centro de su vida, hecho que debe aprender a controlar para no caer en dependencia afectiva. Además, debe luchar por evitar complejos y baja autoestima por miedo a no sentirse atractivo, porque lo hará vivir a la defensiva con los demás y pasar etapas depresivas. ",
    15: "Es posible que alcance beneficios, pero llevado no siempre por la honestidad sino la comodidad; busca mejoras en su vida gracias a lo que otras personas pueden hacer por él. Puede tender al capricho o la manipulación. También a ser muy sensible, pero ingresar en estados egoístas cuando no se siente escuchado o no consigue lo que desea pronto. ",
    16: "Esta persona debe aprender a observar, a ser concentrado y ordenado porque de no hacerlo atrae un sinfín de contratiempos en su existencia, que pasan a veces de la nada. Pero la razón real es que necesita centrarse, tener humildad para aprender y decidir mejoras de vida. Deberá luchas por elevar la autoestima y ser más agradecido con sus afectos. ",
    17: "Esta cantidad de letras atrae renombre y cercanía al éxito económico si las personas luchan con empeño por demostrar sus talentos. Además, existe la posibilidad de ser un muy buen empresario y siempre debe recordar de no perder el juicio y evitar la superficialidad para no caer en pérdidas repentinas. Por otro lado, cabe la posibilidad de tener problemas con la autoestima y fuertes cambios de humor, que si no controla o aprende a manejar pueden hacer que pierda muchas oportunidades y que sea rechazado por muchas personas al perder capacidad de diálogo. Un ejemplo de este número es el jugador de fútbol argentino Lionel Andrés Messi, cuyo nombre tiene 17 letras y posee reconocimiento mundial por su labor. ",
    18: "Esta cantidad de letras comunica la necesidad de búsqueda espiritual porque si se dan cuenta 1 + 8 suma 9, y esta es la vibración de los líderes espirituales. Sin embargo, en muchos casos, cuando no ha existido una debida guía, personas con estas letras caen en infancias o etapas de la adolescencia en extremo rebeldes y con tintes de agresividad a todo lo que les rodea. Si logra ese balance emocional puede destacar con renombre en todos los niveles de su vida. ",
    19: "Esta vibración atrae luego de pasar momentos complicados en infancia y adolescencia, felicidad, triunfo, dinero y protección. Puede toparse con excelentes socios, con una gran pareja que lo ayudará a salir adelante con amor sincero. Si pone esfuerzo, sus talentos se convertirán en obras y proyectos muy exitosos que pueden traspasar las fronteras. Un ejemplo de esta vibración es el empresario y destacado filántropo Warren Edward Buffet, quien destaca por estar en la lista de empresarios más exitosos y millonarios del mundo, pero además por su profunda calidad humana y lealtad con sus afectos y colaboradores. ",
    20: "Atrae la fama, abrir puertas, cambios, vida llena de sorpresas y excelentes oportunidades. Pero si la persona se deja arrastrar por las dudas, ego y malos consejos, pasará etapas polémicas en su vida. Sin embargo, su nombre siempre será reconocido para bien o para mal, dará que hablar en varias generaciones. Un ejemplo de ello es el jugador Diego Armando Maradona, que usa solo el primer apellido como jugador y posee 20 letras. No solo es famoso, sino que ha pasado por etapas de vida donde al caer y levantarse siempre han dado que hablar. ",
    21: "Estas personas anhelan sueños y poder, pero pasarán por luchas, contratiempos y una serie de impases para lograrlo. La edad madura será aquella donde alcancen el éxito, que se mantendrá firme dependiendo de su forma de obrar. Deben controlar la impulsividad al expresarse porque la carencia de tino y diplomacia puede meterlo en grandes líos. Un gran reto será aprender a amarse y a ser constante en la vida académica. Necesita de estímulos emocionales (buena comunicación y atención de personas capaces para extraer lo mejor de sus talentos). Un ejemplo de este número es el expresidente de Venezuela, Hugo Rafael Chávez Frías = 21 letras. Si solo lo analizamos como Hugo Chávez, tenemos 10 letras. Y si observan líneas más arriba lo que se dice sobre los nombres con esta cantidad de letras, verán cómo calza perfectamente para describir aspectos del exmandatario. ",
    22: "Esta persona necesita aprender a escuchar, a recibir consejos y a controlar los impulsos para no cometer errores garrafales, los cuales le pueden costar muchos problemas durante su juventud. Por otro lado, busca el orden y necesita a veces llamar la atención. Tiene capacidad de liderazgo, así como excelente sentido del humor y le cuesta ser estable con la pareja. Un ejemplo es Alan Gabriel García Pérez = 22. ",
    23: "Persona que puede llegar a conseguir fortuna porque sabe moverse en el mundo de las influencias y dar giros a su vida cuando lo amerita. Se arriesga y no tiene problemas para incluso mudarse de país si con ello alcanzará sus metas más preciadas. Ama su libertad en extremo y tiene poca tolerancia con la gente mediocre o que no va a su ritmo. ",
    24: "Persona que es el amigo de las mil amigas, es decir, tiende a tener más amigas si es varón y más amigos si es mujer. Si se trata de un varón, es posible que sus superiores, protectores y gente vital en su vida sean mujeres, las mismas que harán fuerza para librarlo de problemas o apoyarlo en proyectos importantes. Si se trata de una mujer, es al revés, serán los varones sus grandes aliados y amigos. Le cuesta embarcarse en una relación formal con alguien porque debe luchar por vencer temores, fantasmas del pasado y sobre todo aprender a escoger a una persona porque la admira en todo sentido, de lo contrario irá de tumbo en tumbo y con tendencia a ser un ermitaño. ",
    25: "Personas de temperamento fuerte, que por su capacidad de resolver problemas y juicio puede ser visto como fuente de apoyo de toda una familia (si deja a relucir su parte emotiva) y es posible que ello le traiga obstáculos para llegar a sus sueños si no controla su deseo de manejarlo todo sin delegar. Es además perfeccionista en muchas cosas, terco y constante. Debe controlar la forma dura en que dice las cosas cuando cae en estados de ira o frustración. En algunos casos, atrae problemas emocionales fuertes que necesitan largo tratamiento y también falta de tino para controlar los gastos por caer en alienaciones, complejos y superficialidad. ",
    26: "Las personas con 26 letras en el nombre pueden llegar a importantes logros si establecen buenos contactos y a menudo pueden ocupar cargos, alcanzar un puesto, ser exitosos en algún proyecto, etc. Cuando han ido de la mano con alguien o alguien les echa una mano, deben aprender a mantener el equilibrio entre lo material y espiritual, así como a evitar tendencias ególatras, ataques de ira que suelen ser silenciosos, pero lo llevan a decidir cosas de las que suele arrepentirse ya sin solución. Por otro lado, es posible que en edad madura desarrolle mejor sus talentos y profesión, al ser más consciente de las pérdidas y luchas en las que estuvo involucrado. ",
    27: "Persona de elevada percepción. Algunos investigadores indican que esta cantidad de letras la poseen psíquicos, místicos, así como líderes religiosos. Desde muy pequeño vivirá rodeado de personas de poder y autoridad a todo nivel. Tiende a ser estimado y protegido donde sea que pise, porque posee fuerte magnetismo. Suele ser de decisiones firmes y profunda sensibilidad, y de enojos profundos cuando ha observado injusticias o ha descubierto una mentira. No tiene problemas para dejar el pasado o personas atrás si es necesario, a quienes considera negativos, por lo que será criticado y tachado de intolerante o arrogante. Gustan mucho del arte en general, algunos van por el canto, pintura, escritura. En él existen personas también inclinada a los estudios de temas emocionales. Atrae enemigos fuertes, envidias, pero suele llegar al éxito porque la constancia difícilmente lo abandona. ",
    28: "Persona que pasará por fuertes cambios de vida como mudanzas o cambios de país para vivir. Sin embargo, todo ello será para bien. Muchas personas que caen en la vida diplomática poseen esta cantidad de letras en su nombre. Tendrá buenos amigos, casi en todas partes, y es posible que ocupe cargos importantes y tiende a estudiar varias disciplinas para salir adelante. Debe evitar caer en el derroche o malos hábitos. Cuando no encamina bien sus talentos, suele pasar a estados de vida rebeldes y críticos, donde puede sentirse juzgado todo el tiempo por su propia irresponsabilidad y soberbia. Necesita de fe y de buenos consejeros para mantener el equilibrio. ",
    29: "Persona algo tímida, insegura, que duda de sus capacidades y puede cambiar de trabajo más de una vez porque a veces se siente atacado. Pero en el fondo su alta susceptibilidad le impide a veces dialogar de modo correcto sin tomarse las cosas a pecho. También esto puede afectar su vida sentimental porque puede dejarse manipular por la pareja o mantenerse al lado de una que no lo hace dichoso por miedo y por falta de decisión. Aprender a decidir y comunicarse mejor será su mayor prueba de fe. De lograrlo será exitoso, líder y gran consejero. ",
    30: "Persona algo hiperactiva, le gustan muchas disciplinas, pero sabe lo que más quiere y lucha por ello. Tiene buen pronóstico de vida y suele tener excelente sentido del humor, así como despertar magnetismo de otras personas por su carisma y amabilidad. Suele ser terco y osado, toma riesgos en pos de sus sueños. Gran orador si aprende a ser ordenado en sus ideas y también perceptivo y bondadoso, así como algo hipocondriaco. Puede destacar en puestos de finanzas, o como director de proyectos. Su capacidad de mandar es nata si sabe aprovecharla y ser constante en su preparación. ",
    31: "Las personas le tiene confianza por su velocidad al pensar y decidir. Si bien podrá tener una infancia algo solitaria o con reveses por influencias de sus progenitores, su fortaleza, constancia y capacidad de lucha lo llevarán lejos. Es muy trabajador y competitivo, es ambicioso, pero básicamente busca logros y paz para su familia, así como orden. Es algo nervioso, tenso y con posible tendencia a problemas circulatorios. Odia las peleas y la gente conflictiva porque su carácter suele ser muy pacífico y conciliador, pero cuando se enoja toma decisiones tajantes y no da marcha atrás. ",
    32: "Son personas que poseen elevada necesidad de mantener su libertad. También poseen magnetismo y capacidad para dirigir y mandar; por ello, prefieren un negocio propio. Tiene facilidad para hacer amigos, abrir puertas pronto, pero a menudo tomar responsabilidades desde muy joven y ocuparse de otros lo puede agobiar. Deberá aprender a manejar el ego e intolerancia para evitar problemas legales por imprudencia. Sentirá que nunca es suficiente lo que hace ni lo que aprende, por lo que decidirá recorrer el mundo tanto como pueda. Debe evitar involucrarse con una pareja que termine siendo alguien que le robe energía porque le tocará ser apoyo y empuje siempre. Vías respiratorias y alergias de piel cada cierto tiempo serán parte de aquello que debe vigilar con sana alimentación y liberándose del estrés.",
  }

vocal_meanings = {
    'a': {
        1 : "esto indica seguridad en sus actos.",
        2 : "predomina la inteligencia, seguridad y la capacidad de dirigir.",
        3 : "la persona tiende a ser firme e intuitivo, así como a saber salir de situaciones complejas con aplomo y desapego. Le cuesta dar su confianza si le ha descubierto algo que no le parece justo.",
        4 : "habla de una independencia extrema, ser algo intolerante y decir las cosas de manera algo ruda, así como detestar la rutina."
    },
    'e': {
        1: "predominan los nervios y el temperamento emotivo.",
        2: "existe peligro de padecer ciertas fobias y anuncia la posibilidad de una vida plagada de sorpresas desde los treinta y cuatro años, así como peligros de padecer de insomnios si no controlan las emociones.",
        3: "prevalecen el movimiento, la dualidad de personalidad y la falta de compromiso con las cosas o las personas si se siente que lo aturden. Así como también existe una tendencia a ser agresivo verbalmente y obsesivo.",
        4: "hay que tener cuidado de no cometer excesos que perjudiquen a los demás, peligro de caer en derroches de dinero, así como una vida algo ligera."
    },
    'i': {
        1: "la sensibilidad no es vista con facilidad y mucha gente los cree inflexibles",
        2: "la persona puede ser muy nerviosa, especialmente de pequeño, con ciertos temores e incapacidad para demostrar los talentos, hecho que pasa a mejorar a partir de los ocho años. También estas personas parecen ser depresivas o algo introspectivas y desconfiadas. Dependiendo de las otras vocales, también hay tendencia a ser irritable y terco.",
        3: "la persona puede sumirse en una timidez extrema que le impide expresarse como se debe o tiende a aislarse, así como tendencia a padecer de ansiedad por no parar de pensar.",
        4: "la persona necesitaría ayuda para adaptarse al mundo en el que vive. Tendrá cierta tendencia a la paranoia, fobias y terquedad extrema."
    },
    'o': {
        1: "busca el orden en su vida y no le gustan los imprevistos, planifica todo con tiempo y le incomoda mucho pedir favores.",
        2: "hay tendencia a buscar el orden en su vida, pero también en la de los demás siendo algo intolerante y severo en los juicios.",
        3: "implica terquedad extrema, la misma que se refleja en la falta de acuerdos y entendimiento, incapacidad para comunicarse sin ser hiriente.",
        4: "hay tendencia a tener conducta tiránica, dominante y algo ególatra."
    },
    'u': {
        1: "esto habla de sabiduría, curiosidad, buen sentido del humor y osadía, así como algo de terquedad.",
        2: "se posee una visión muy amplia de la realidad universal, capacidad de manejar momentos tensos en masa.",
        3: "peligro de desapego completo en el campo sentimental, así como comprensión clara del mundo espiritual y material.",
        4: "tendencia al materialismo y superficialidad."
    }
}

pitagoric_dict_reversed = {
    1: ["A","J","S"],
    2: ["B","K","T"],
    3: ["C","L","U"],
    4: ["D","M","V"],
    5: ["E","N","Ñ","W"],
    6: ["F","O","X"],
    7: ["G","P","Y"],
    8: ["H","Q","Z"],
    9: ["I","R"]
}
pitagoric_dict = {}
for k,v in pitagoric_dict_reversed.items():
    for letter in v:
        pitagoric_dict[letter] = k

first_letter_meanings = {
    1: "Este número al comienzo del nombre aporta una sensación de esfuerzo personal, de soledad en el sentido de hacer las cosas solo para llegar lejos, de abrir nuevos horizontes; y será una constante en su vida. La A es la letra de los líderes, pero también de las personas que sienten que los demás dependen mucho de él o ella y poseen además una fuerte resistencia al dolor emocional.",
    2: "Revela la predisposición a un comportamiento dual con el que tendrá que luchar para aprender a tomar decisiones a tiempo, porque el miedo lo pueden arrastrar a ser ansioso, mas si lo controla dará paso a la percepción e intuición de que lo acompañará cuando se serena.",
    3: "Es la necesidad de abrirse a la comunicación, tanto en el entorno cercano como en grupos grandes. Las letras, música, medios de comunicación serán importantes en su vida, pero debe aprender a concretar los sueños y no vivir imaginando las cosas.",
    4: "Este número habla de una niñez difícil, marcada por situaciones de displacer o que no pueden olvidarse, quizá porque la familia no respondió a la sensibilidad y necesidades emocionales del portador del nombre. Ello lo lleva a trabajar mucho para crear su propio mundo según su alma lo pide. Debe evitar ser intolerante e impositivo por lo vivido en el ayer y por temor a fracasar.",
    5: "Este número habla de la tendencia a seducir y gustar. Esto puede lograrse aún a costa de las propias necesidades. También deberá luchar con los excesos y que su espíritu aventurero no lo embarque en situaciones de riesgo. Es creativo, incansable y siempre con posibilidades e impulso de viajar y conocer nuevos sitios.",
    6: "Significa amor al hogar, la familia, necesidad de servir desde el alma a otros y búsqueda de armonía. Son personas tercas y obstinadas cuando quieren lograr algo porque creen en ello. Debe prestarle atención a lo físico porque está predispuesto a enfermedades y dolencias, tanto reales como imaginarias.",
    7: "Son personas con tendencia a problemas emocionales que pueden afectar sus estudios, pero no por falta de talento. Les encanta aprender, investigar y son curiosos, pero deben luchar con la tendencia a la depresión, hipersensibilidad que les puede generar todo tipo de enfermedades y problemas con los afectos. De controlarlos pueden llegar lejos laboralmente.",
    8: "Este número aporta una energía potente que genera fuertes acontecimientos en la vida con los que se debe luchar para no ser agresivo. También vibra la necesidad de incursionar en los misterios que se esconden detrás de lo esotérico. Navegar sobre lo desconocido es un desafío que debe aprender a usar con prudencia.",
    9: "Implica el desafío permanente de superar pruebas que aceleran el proceso evolutivo, aprendiendo a recibir también premios, según el éxito de la empresa. El objetivo más fuerte apunta al engrandecimiento de la fe y a entender los caminos de alta espiritualidad."
}

lastname_meanings = {
    1: "Tiene como regente al Sol. Es un número fuerte, que marca independencia, tendencia dominante. Concede inteligencia rápida, eficaz y abierta que capta pronto dónde nace un problema. Muy trabajador, abre las puertas a nuevas oportunidades. Destinado a ser cabeza por su don de mando. Es sensible y generoso, pero trata de no darlo a notar para protegerse. Debe luchar por no caer en el egocentrismo, la ambición desmedida, celos, egoísmo y cierta tendencia a la soledad. Debe reflexionar antes de actuar y se destaca en cualquier carrera, pero se inclinará por las que tengan contenido científico que generen un desafío.",
    2: "Su regente es la Luna. Tienen tendencia a ser dominadas por sus emociones, sensibilidad y tendrán complicaciones para manejar sus reacciones. Es amable, generoso, muy intuitivo y perceptivo. Suele ser desidioso para actuar (voy, no voy, lo hago, no lo hago) y debe luchar con esa dualidad para no caer en altibajos y luchar por correr riesgos. Tendrá tendencia hacia carreras de ayuda social como diplomacia, trabajo social, secretariado, artes. Debe luchar porque su miedo e indecisión no lo conviertan en su sometido.",
    3: "Los rige el planeta Mercurio y desde pequeños los marcará su deseo por estudiar y curiosidad por conocer de todo. De mente perceptiva y con capacidad para ocultar lo más profundos de sus sentimientos. Tienen habilidad para comunicar con la palabra hablada y escrita, pero además poseen tendencia a ser envidiados donde vayan porque son carismáticos y magnéticos y de gran sentido del humor si están de buenas. Pero también caen en silencios largos que nadie puede comprender porque es entonces que están tomando decisiones tajantes de las que no dan marcha atrás. Debe ponerse objetivos pequeños para poder cumplirlos diariamente. Tienden a destacarse como locutores, terapeutas, actores, escritores, músicos, políticos y todo aquello que tenga que ver con el contacto humano y servicio.",
    4: "El regente es el planeta Urano, lo cual lo hace a llevar orden y disciplina. No es innovador, es un organizador.Tiende a estudiar todo lo que hará antes de embarcarse en un proyecto. Adora la discreción y crea lazos afectivos y fieles porque pone mucho empeño y ama con profundidad. Cuando forma una pareja, lo hace muy seguro de la decisión tomada y de sus sentimientos. Puede ser exitoso en carreras que tienen que ver con leyes, fórmulas matemáticas, fórmulas químicas y puede desempeñarse en una empresa e ir escalando.",
    5: "Tiene como regente a Mercurio, son inteligentes y talentosos. Su necesidad básica es la del movimiento y la acción. Ama profundamente la libertad, sintiendo que solo desde ella puede crear. Sabe tomar inmediatas decisiones debido a su capacidad de rápida adaptación por los cambios que se producen. Posee una intuición aguda y percepción afinada. Es capaz de sacrificar todo para volar en pos de un sueño. Los viajes largos serán de su máximo interés para rodearse de otras culturas y dejar el estrés atrás. Vive cada día de su vida como si fuese el último. Su personalidad, talento y energía hacen que no pase inadvertido en ningún lugar y, aunque parezca impulsivo, sabe analizar las cosas con gran velocidad y certeza. Debe cuidarse de no cometer excesos cuando está ansioso como comer, beber, drogas, sexo. Entendiendo por exceso el consumo como el no consumo (anorexia, obesidad, anemia). Buscará liberarse pronto si siente que lo quieren encerrar. Le espera una vida de viajes que acrecentaran su conocimiento y su vida siempre estará rodeada de riesgos y sorpresas.",
    6: "Lo rige Venus y busca lo bello, bueno y verdadero, pero si no trabaja en su interior fácilmente cae en la superficialidad y adopta posturas de moda o de otros por ser centro de atención. Necesita del amor y la armonía. Tiende a crear un mundo privado donde se cobijen la familia y los amigos, o sea, sus verdaderos afectos. Es hipersensible y noble cuando lo decide, notablemente creativo. Estará marcado por una infancia plagada de exigencias y de frialdad emocional por parte de sus progenitores, siendo ello el detonante de los problemas de comunicación y ausencia de seguridad que en muchas ocasiones lo acompañan. Es muy inteligente y desarrollará actividades que tienen que ver con lo social y la humanidad. Despierta simpatía y confianza en quienes lo rodean, la misma que cuando no es auténtico puede usar para manipular y llegar al poder que aspira. Debe luchar por no ser caprichoso y querer imponer sus ideas porque necesita que acepten sus pautas para lograr la armonía a su modo, lo cual puede volverlo tiránico. Puede, además, mostrarse terco y obstinado. Debido a su hipersensibilidad, también se muestra inestable en su comportamiento. El temor a que sus emociones lo debiliten le hará ocultar sus sentimientos bajo una apariencia cínica, desenfadada y fría, cuando en realidad lo aterre sentirse rechazado. Tiene tendencia a la dependencia afectiva y suelen tener un primer fracaso en el matrimonio o una relación por conveniencia para cubrir apariencias, hasta que deciden salir de esta o vivir doble vida en muchos casos. Puede trabajar en puestos donde despliegue su creatividad y capacidad de organización (desde administración, publicidad, periodismo, docencia, ciencias médicas).",
    7: "Lo rige Neptuno. Posee capacidad para ser disciplinado y genera siempre un inicio que crece, alcanza la cumbre y luego vuelve a la nada. Es intuitivo y puede atraerle el mundo de la filosofía y metafísica. Es analítico, busca independencia y con gran curiosidad por todos los campos. Es algo introvertido y busca investigar en soledad. Necesita aislarse para ser el mismo, meditar y buscará un espacio para lograrlo. Hace pocos amigos, pero le duran toda la vida y en especial aquellos que comparten su necesidad de búsqueda espiritual y de lo místico. Su tendencia al aislamiento debe ponerlo alerta para evitar cuadros depresivos que en muchos casos pueden ser de severa atención médica. Es importante que aprenda a mostrar sus sentimientos. Debe controlar el perfeccionismo para no pensar que nadie puede hacer mejor las cosas que él. Tiene talento para ser artesano, escultor, buen maestro, científico y sobre todo la búsqueda de crear una especie de claustro; muchos optan por ser religiosos.",
    8: "Tiene como regente a Saturno. Toma como desafío el equilibrar el mundo material y el mundo espiritual, dándole al dinero su verdadero valor y colaborando con aquel que lo necesite. Posee gran fuerza espiritual y mental. Es activo, magnético y con la fuerza para llegar a sus objetivos cualquiera sea el tiempo que le demande. Es sensual y sexual. Sabe concretar su energía y ejercer el autocontrol. No tolera la mediocridad ni lo mezquino. No se detiene ante los obstáculos y usa siempre su percepción. No se siente ofendido con facilidad, pero cuando lo hieren o ve mellada su dignidad, borra de su vida esa relación, como si nunca hubiese existido. Luego de albergar mucho conocimiento, tiende a ser líder espiritual. Debe luchar por cultivar la tolerancia para no caer en la agresividad y en lo irreflexivo, lo que puede llevarlo a ser obstinado y enfermarse al punto de generar operaciones. También puede caer en la búsqueda de lo material olvidando lo espiritual. Por su autodisciplina puede desempeñarse en cualquier lugar profesional y tiene tendencia a ser líder porque sabe mandar y hacerse obedecer. También le atrae todo lo científico y lo relacionado con el espionaje.",
    9: "Tiene como regente a Marte, es el número del líder espiritual. Tiene ideas que buscan la paz y armonía en el mundo y le choca cuando se entera de noticias que hablan de destrucción. Es afectuoso, emotivo y algo vergonzoso cuando se siente observado y solo se muestra en público cuando lo mueve una causa. Es fiel a su pareja y puede descuidarla porque se suele meter en metas humanitarias. Ha nacido para ser espiritual y cuando siente que no puede o no sabe cómo orientarse, puede perder la claridad y perderse en situaciones autodestructivas como fanatismos, drogas, vicios y hasta presentar característica psicopáticas, así como todo tipo de conductas anormales. Tiene tendencia a pasar pruebas de fe para demostrar que puede mantener su espiritualidad. Esas pruebas indican pérdidas, sacrificios, dolores y renuncias, experiencias que debe tomar como aprendizaje y no como castigo. Así como un 9 puede buscar la alta espiritualidad, también encontramos al líder espiritual de la sombra y el mal. Podrá estudiar vocaciones de servicio como medicina, sacerdocio, veterinaria, derecho."
}

birthdate_meanings = {
    1: """Si naciste un día 1 o la reducción a un solo dígito del día de tu nacimiento da valor 1, “fuerza en tu corazón” porque el uno es el número de los líderes. Por tanto, posees un importante potencial para salir adelante solo, ser independiente y realizar actividades con esmero y voluntad. Sin embargo, es posible que siempre sientas que los demás no van a tu ritmo, que te sacrificas demasiado y todos los problemas recaen sobre tu espalda. A ti nadie te regala nada, todo te lo ganas. 
Si pese a nacer con este excelente dígito notas que eres apático, postergas cosas y esa fuerza tuya parece ausente o dormida, es altamente posible que el apellido paterno no te favorezca energéticamente porque posee una vibración numérica que te resta luz. Por ello los numerólogos profesionales realizamos el estudio completo del nombre y fecha de nacimiento, y preparamos lo que denominamos “nombre de realización”, con la finalidad de elegir las mejores cargas vibracionales para usar en tarjetas de presentación. Es increíble como una sola letra bien usada cambia la historia y es una fuente mágica de energía divina para quien lo necesita. 
Un tip que les doy es mandarse a preparar una medalla con el número uno si sientes que no vibras como este excelente número. Si no eres del 1, coloca uno de bronce en tu dormitorio, junto a tu escritorio o debajo de tu cama; de este modo jalas energía de este número. Algunas personas lo llevan en pulseritas, etc. 
Si te sientes identificado con el número 1 en tu personalidad, solo debes controlar el temperamento, nada de ser impositivo y recoge siempre humildad para servir. Te toca moverlo todo en tu vida y en la de otros, pero con amor, bondad y respeto. Los números 1 son algo intolerantes, tercos, impacientes, pero también de excelente humor. Pueden trabajar como hormigas sin quejarse, aunque deben cuidar mucho la columna y rodillas, zonas vulnerables porque comandan estos chakras o centros energéticos.""",
    2: """Si naciste en esta fecha o por ejemplo un 20 y al reducirlo nos da 2, o naciste un 11 y al reducirlo también nos da 2, eres una persona altamente susceptible. Si no aprendes a controlarlo, sentirás que todos te hacen daño, caerás en depresión, ansiedad y postergarás metas. Solo buscarás culpables o retrocederás en lo que te has trazado. 
Eres caritativo y amable, pero la apatía te puede visitar muy a menudo y tus pensamientos van entre un “¿lo hago o no lo hago?”. A veces puedes dejarte guiar por inseguridad, o por tus padres o amigos. Eres altamente influenciable, pero a la vez intuitivo, de modo que debes entrenar el temperamento, elevar la autoconfianza para vencer esa vibración baja natural. Eres paciente, respetuoso y a menudo caes en ira por resentido o nervios, pero no de furia innata. 
Si naciste un día 11, posees una energía superior extra, una misión y regalo de la Divinidad llamada “número maestro” que implicará que en la vida ayudes a miles de personas (labor social, dictar clases, mejorarles el ánimo). El número 11 posee la necesidad de hacer cosas variadas, pero cuando decaes vibras como un 2 y te paralizan los temores e inseguridades. Así que lucha por vibrar siempre como un 11 porque te hará incluso lograr cosas que no imaginas a nivel emocional. 
Mucha gente con vibración 2 elige trabajos donde casi no sea visto, o rutinarios. Si por suerte tienen un buen apellido paterno, esa vibración extra los hace duales, a veces osados y decididos; otra suelen paralizarse como autos descompuestos. Como son propensos a la ansiedad, deben practicar deportes cardios, comer sano y siembre beber mucha agua. Ojo con problemas como urticaria y temores a expresarse en público casi fóbicos. 
Sugiero que siempre tengan un cuarzo amatista en la cabecera de la cama (que deben lavar semanal con un puñado de sal y cargarlo de noche cuando salga la luna con la ventana abierta). Este cuarzo equilibra el temor interno, lo disminuye, los serena. Y para sus miedos, usar un cuarzo lapislázuli de medalla o usarlo cinco minutos, tres veces al día sobre las manos para cargarte con su energía que atrae paz interior y pensamientos sanadores.""",
    3: """Puede venir de una fecha 3, de reducir el día 30 a un dígito o de reducir un 21 a un solo dígito. Son personas con temperamento curioso por naturaleza, algo inquieto de chicos y también muy nerviosos. Les cuesta esperar, soportar un “no”, pero su sonrisa, bromas y sentido de la creatividad los hace saber qué decir, cómo y en qué momento. Su principal reto es aprender a ordenarse, ser disciplinados porque les gustan muchas cosas a la vez y se estresan, aburren y no las terminan. 
Deben evitar el engreírse con todos y por todo. Y les queda sacar provecho de su habilidad persuasiva: pueden ser buenos vendedores, jefes de marketing, moverse, ir de aquí para allá les encanta. Son algo hipocondriacos y nerviosos porque todo debe ser “ya”. Pueden equilibrarse comiendo sano, tomando mucho aire. Necesitan energía yin para calmar esa euforia, y la consiguen en el campo, comiendo cosas frescas y muchas verduras. 
Cuidado con la presión alta y mareos, porque como son tan inquietos mentalmente, esto afecta la circulación. Deben cargar siempre un cuarzo de agua marina para poder relajarse y pensar mejor para romper los impulsos. Si el apellido paterno es de buena vibración, la combinación con un 3 lo hará estupendo profesional y revolucionará donde pise para bien.""",
    4: """4: Si naciste un 4, reduces un 13 a un dígito o naciste un 22 y al reducirlo también obtienes 4. En esta vibración hallamos personas con tendencia a la rigidez de pensamiento, con esquemas de vida bien definidos; por tanto les cuesta ceder, negociar y a veces prefieren no arriesgarse. Necesitan aprender a ver la vida con mayor osadía, fuerza y capacidad creativa, porque muchos 4 llegan a viejos quejándose de lo que no hicieron por agentes externos.
Son pudorosos, observadores y escuchan mucho, captan de todos lados. Pero deben evitar escuchar para asustarse; se escucha para aprender. 
Sin embargo, prestar atención a esto: si el número 4 viene de una fecha de nacimiento 13, este día es lo que denominamos en numerología “número kármico”. Es un reto de fe, algo que traes en esta vida para pulir y aprender; en este caso se trata de vencer la frustración, tendencia a la irritabilidad y cuando algo no te guste, no te enojes ni lo eches por la borda. Si conoces a alguien nacido un 13 y es renegón, ya sabes el motivo. ¿Qué hacer?: aprender a pensar, pulir el alma, orar, hacer ejercicio cardio, comer sano, orar mucho y cargar siempre un cuarzo amatista para ese enojo. 
Y si, por ejemplo, el 4 vino de una fecha de nacimiento 22, este día es muy especial, porque se le conoce en numerología como “número maestro”. Significa que a la divinidad se le ocurrió colocarte una energía especial para servir al mundo en tu país, pero especialmente en otras fronteras, a nivel internacional. Muchos 22 son gente que va y viene por el mundo: diplomáticos, políticos, cantantes, escritores, etc. 
Y si solo eres un 4 tal cual, debes captar todo lo que indiqué en los primeros párrafos.""",
    5: """Si naciste un 5 o lo consigues reduciendo una fecha de nacimiento 14, posees un número especial. Son osados por naturaleza, apasionados con todo lo que les gusta, curioso y creativo. Un 5 no se queda callado si lo ofenden jamás: se puede enojar mucho y decir cosas fuertes, o decir poco, y lanzar igual una “bomba atómica con sus palabras”. 
Son viajeros natos, saben hablar, dirigir, tienen un sentido del humor impredecible (son gente que arranca lágrimas, pero de risa). Nerviosos, apurados, quisquillosos, eticosos para comer y amantes de la música, porque son súper románticos y algo de lágrima fácil. 
También son excelentes jefes de personal, vendedores, dirigen, miden y siempre se les ocurren soluciones veloces. Sus zonas delicadas son las articulaciones, músculos y con tendencia a las alergias de piel. Pueden ser muy perceptivos. 
Ocurre, por ejemplo, que si no naciste bajo este número, pero si sumas tu día de nacimiento, más el mes y el año, y reduces todo a un solo dígito, te da 5… Lo que te espera en la vida, porque de ser así, existe tendencia a tener habilidades paranormales.""",
    6: """Si naciste un 6 o al reducir un 24 da 6, eres una persona dulce, romántica, pero cuando notas que lo que te rodea te estresa o es agresivo, tiendes a irritarte, te apartas, te sumes en tu cueva y pasas como introvertido. 
Son veloces para decidir, pero altamente impulsivos y por ello dicen y hacen cosas que luego les pesa. Algo obsesivo con sus metas, así como su resentimiento porque suelen echar en cara el daño que les han hecho. Muchos 6 son rebeldes, contestones e incluso irreverentes con sus padres por capricho, actitud que deben entrenar para evitar ser injustos y dañar.
Aman la música, cantar a solas y la euforia de los grupos de amigos que elige por la simpatía y lealtad. Deben evitar la tendencia a caer en dependencia afectiva y cuidarse de migrañas. Muchas personas con este número han sido grandes revolucionarios porque tienden a reclamar sus derechos con vehemencia. 
Deberían cargar siempre un cuarzo blanco para poder controlar la impulsividad y prevenir las migrañas y evitar alergias.""",
    7: """Si naciste un 7, o al reducir el 16 a un solo dígito da 7, eres una persona de temperamento analítico, desconfiado y de idea fijas sobre lo que deseas en la vida. 
Sin embargo poseen elevada susceptibilidad, tendencia a vivir a la defensiva y problemas para comunicarse de manera pertinente. Suelen esperar que los demás comprendan sus actitudes y den por entendido lo que quieren. La frustración por postergar decisiones con tendencia al temor, por presión al pensar o agentes externos (entorno, familia, amigos, etc.) pueden llevarlos a estados de apatía y ansiedad. 
De humor sarcástico, diplomáticos, les incomoda el conflicto, pero curiosamente viven en él o lo tienen cerca porque les cuesta desprenderse de aquello que ven como autoridad (figura paterna, jefes, etc.). Suelen ser buenos abogados o dados a laborar en un solo rubro o profesión, porque mantienen rutinas laborales para no sentirse angustiados. Son generosos y terminan por adaptarse a diversos grupos de modo educado, aunque no por mucho tiempo (al menos pueden disimular un poco). 
Les cuesta reconocer errores y prefieren hacer obsequios o gastar bromas para comunicar su culpabilidad. Sus zonas de salud de cuidado son estómago, aspectos circulatorios y tobillos. Podrían usar la piedra lapislázuli para bajar sus niveles de temor y mejorar sus formas de comunicación. 
Si naciste el día 7, existe tendencia a la habilidad manual (carpintería, electricidad, mecánica, etc.). Pueden organizarse en negocios vinculados al rubro con éxito, pero necesitan aprender en ventas, marketing y socialización para darlo a conocer. 
Si naciste un 16 y al sumarlo da 7, el día 16 es también un número kármico. Esto significa que tienes un reto de fe que pulir en esta vida. Y es que nacer bajo un número kármico significa tendencia a no controlar la frustración, renegar cuando algo no sale pronto o como esperas, y a cometer impulsos absurdos por rabia, ira o descontrol. Por otro lado, los nacidos el 16 poseen tendencia a ser mal pensados, celosos y además cargar con elevado ego o altanería, que en realidad viene de su temor fuerte al rechazo y abandono.
    """,
    8: """Si naciste un 8, o un 17 reducido a un dígito da 8, eres una persona marcada por la diversidad laboral. Dependiendo el apellido paterno y año de nacimiento, los 8 son personas que por ejemplo tendrán diversos oficios desde temprana edad porque son curiosos, creativos y necesitan disfrutar aquello a lo que se dediquen. 
El 8 es el número de la lucha del bien contra el mal, de la elevada espiritualidad o del capricho, conflicto y terquedad. Y es que un 8 con buen apellido paterno y excelente año de nacimiento puede llegar a ser líder, capaz de comunicarse con todo grupo humano y con tendencia al liderazgo nato. 
Muchos 8 son grandes empresarios, artistas (música, escritura). De temperamento fuerte y directo, no se van con medias tintas y si algo les molesta no buscan ocultarlo. Sin embargo, cuando llegan a la espiritualidad que por destino poseen y necesitan siempre, logran vivir de manera muy estable, sin apegos y, sobre todo, de manera comprometida con sus planes de vida. Se caracterizan por ser caritativos, risueños y prácticos. 
Si por el contrario vibras como un 8 que se hunde en el lado superficial, son personas a las que jamás les alcanza el dinero, no se organizan bien, todo lo postergan y buscan hacer pleitos donde pisan. Entonces descuidan su arreglo personal, se les ve envejecidos pronto y no escuchan consejos. 
Para saber a qué tipo de 8 te inclinas más, debes sumar tu día, mes y año de nacimiento para evaluar así tu número de karma que es el más importante en un estudio numerológico. Por ejemplo, si naciste un 17 de enero de 1970, tu número de karma es 1 + 7 + 1 + 1 + 9 + 7 + 0 = 26, que reducido a un dígito da 8. 
Entonces tenemos que por número de destino esta persona es un 8 con karma 8. Le interesará crecer como empresario independiente, será una máquina de generar ideas, proyectos y debe luchar por no alejarse del campo espiritual y aprender a expresar sus emociones con mayor claridad, sin ego y sin miedo al rechazo.""",
    9: """Si naciste un 9 o el 18, que reducido a un dígito nos da 9, eres una persona que debe luchar mucho por aprender a mantener el equilibrio. El nueve es el número de gente de elevado sentido espiritual o autodestructiva. 
Un nueve es una persona con tendencia a vivir en un hogar complejo, donde el consejo paterno y materno no ha sido el mejor. Suelen ser ansiosos, depresivos y su reto de fe es luchar contra la corriente, creer y esforzarse al máximo por pensar de modo maduro. Muchos 9 pasan tragedias familiares de infancia (lutos, mudanzas repentinas, abandono total familiar, etc.), hechos que al marcarlos los pueden sumir en malos hábitos de vida. 
Sin embargo, si logran aprender del dolor y abrir los ojos (ayuda cuando existe un excelente apellido paterno o un buen número de karma con los números completos de nacimiento), existe tendencia a salir airoso, mejorar la personalidad y vibrar no solo con fe sino con un empuje digno de santos. Por ello, no es extraño que muchos sacerdotes y religiosas hayan nacido un 9, pero también cantantes y gente famosa que acabó por ejemplo en mala vida o muerte por autodestrucción. 
Pueden ser introvertidos, lentos y distraídos, con grandes complejos; pero también carismáticos, divertidos y dulces para comunicarse. Por ello cargar siempre en el pecho la piedra cuarzo amatista los calmaría mucho. 
Sus zonas de salud compleja son los riñones y tienen tendencia a problemas de asma y alergias notorias, porque viven al susto o pensando que lo malo llega a ellos siempre.""",
    13: """Deben luchar para evitar caer en dispersión, pereza, irritabilidad. Necesitan ser objetivos y vencer el engreimiento.""",
    14: "Los nacidos esta fecha deben luchar por no ser tajantes, porque por ejemplo suelen desarrollar aversión a situaciones o personas y pueden cerrarse de tal modo que jamás le darían la oportunidad de demostrar que no son malas personas. También deben luchar por no ser hipocondriacos, les da terror enfermarse y se estresan por ello más de la cuenta.",
    16: "Deben hacer un fuerte trabajo para vencer el orgullo excesivo y el ego, así como caer en superficialidades, estereotipos y ansiedades que los llevan a cometer actos impulsivos de los que luego se pueden arrepentir toda la vida.",
    19: "Deben aprender a entrenar la compasión. Suelen ser dominantes, autoritarios y hasta tiranos; no toleran un “no” por respuesta y no saben pedir perdón. Cuando el ego los desborda, su egoísmo no posee límites, creando conflicto donde pisan."
}
@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}

# create fastapi function to receive firstName , middleName, lastName, secondLastName  and return a value from dict depend on the total number of letters in the name
@app.get("/get-meaning-from-length", tags=["name"])
async def get_meaning_from_length(firstName: str, middleName: str, lastName: str, secondLastName: str):
    total_length = len(firstName.strip()) + len(middleName.strip()) + len(lastName.strip()) + len(secondLastName.strip())
    return {"message": meanings[total_length],
            "totalLength" : total_length
            }
    
# create function to count appearances of each vocal using firstname
@app.get("/get-vocals-meaning", tags=["name"])
async def get_vocals_meaning(firstName: str,middleName: str):
    vocals = ['a', 'e', 'i', 'o', 'u']
    vocals_count = {}
    for vocal in vocals:
        vocals_count[vocal] = firstName.lower().count(vocal) + middleName.lower().count(vocal)
    vocals_message = {}
    for v,c in vocals_count.items():
        c = 4 if c > 4 else c
        if c>0:
            vocals_message[v] = { 
                                "count":c,
                                "message": vocal_meanings[v][c] if c > 0 else ""
                            }
    return vocals_message

@app.get("/get-first-letter-meaning", tags=["name"])
async def get_first_letter_meaning(firstName: str):
    first_letter = firstName[0].upper()
    return { "letter": first_letter , "message" : first_letter_meanings[pitagoric_dict[ unidecode( first_letter )]] }

@app.get("/get-lastname-meaning", tags=["name"])
async def get_lastname_meaning(lastName: str):
    lastName=lastName.strip().upper()
    first_sum_operation = " + ".join([f"{pitagoric_dict[letter]}({letter})" for letter in lastName])
    sum_letters = sum([pitagoric_dict[letter] for letter in lastName])
    first_sum_operation = first_sum_operation + f" = {sum_letters}"
    second_sum_operation = " + ".join([digit for digit in str(sum_letters)])
    sum_letters = sum([int(digit) for digit in str(sum_letters)])
    second_sum_operation = second_sum_operation + f" = {sum_letters}"
    if sum_letters > 9:
        third_sum_operation = " + ".join([digit for digit in str(sum_letters)])
        sum_letters = sum([int(digit) for digit in str(sum_letters)])
        third_sum_operation = third_sum_operation + f" = {sum_letters}"
        second_sum_operation = second_sum_operation + " -> " + third_sum_operation
    return { "first_sum_operation": first_sum_operation,
            "second_sum_operation": second_sum_operation,
            "result": sum_letters,
            "message" : lastname_meanings[sum_letters] }
    
@app.get("/get-birthdate-meaning", tags=["birthdate"])
async def get_birthdate_meaning(birthdate: str):
    birthdate = datetime.strptime(birthdate, '%d/%m/%Y')
    day = birthdate.day
    if len(str(day)) > 1:
        sum_digits = sum([int(digit) for digit in str(day)])
        if day > 9:
            sum_digits = sum([int(digit) for digit in str(sum_digits)])
    else:
        sum_digits = day
    message = birthdate_meanings[sum_digits]
    if day in [13,14,16,19]:
        message = message + "\n" + birthdate_meanings[day]
    return { "day": day,
            "message" : message }
    
@app.get("/print")
async def print():
    import os
    return {"message": os.getenv("POSTGRES_DATABASE", "default message")}