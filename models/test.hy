(defn crear_globales []
    (global mivar )
    (global PP AP DP)
    (global PC AC EC)
    (global PR AR ER)
    "sobre percepcion"
    (setv PP "poca_percepcion")
    (setv AP "adecuada_percepcion")
    (setv DP "demasiada_percepcion")
    "sobre la comprension de emociones"
    (setv PC "poca_comprension")
    (setv AC "adecuada_comprension")
    (setv EC "excelente_comprension")
    "sobre la regulacion"
    (setv PR "poca_regulacion")
    (setv AR "adecuada_regulacion")
    (setv ER "excelente_regulacion")
)
"Resultados de la percepcion de emociones de un hombre"
(defn percepcion [CANTIDAD]
    (cond   [(< CANTIDAD 22) PP]
            [(< CANTIDAD 34) AP]
            [(> CANTIDAD 33) DP]
    )
)
"resultados sobre la comprension de emociones de hombre"
(defn comprension [CANTIDAD]
    (cond   [(< CANTIDAD 26) PC]
            [(< CANTIDAD 37) AC]
            [(> CANTIDAD 36) EC]
    )
)
"resultados sobre la regulaciones de emociones de hombre"
(defn regulacion [CANTIDAD]
    (cond   [(< CANTIDAD 24) PR]
            [(< CANTIDAD 37) AR]
            [(> CANTIDAD 36) ER]
    )
)
"FUNCIONES PARA VERIFICAR RESULTADO DE POSIBLE TRANSTORNO EMOCIONAL"
(defn verifica_impulsivo [X Y Z]
    (if
        (and
            (= X DP)
            (= Y EC)
            (= Z AR)
        )
        "estable_compulsivo" "por_defecto"
    )
)

(defn verifica_toc [X Y Z]
    (if
        (and
            (= X DP)
            (= Y EC)
            (= Z PR)
        )
        "estable_compulsivo" (verifica_impulsivo X Y Z)
    )
)

(defn verifica_sociopata [X Y Z]
    (if
        (and
            (= X PP)
            (= Y PC)
            (= Z ER)
        )
        "sociopata_positivo" (verifica_toc X Y Z)
    )
)

(defn verifica_calculador [X Y Z]
    (if
        (and
            (= X PP)
            (= Y EC)
            (= Z ER)
        )
        "estable_calculador" (verifica_sociopata X Y Z)
    )
)

(defn verifica_retraido [X Y Z]
    (if
        (and
            (= X PP)
            (= Y AC)
            (= Z ER)
        )
        "estable_retraido" (verifica_calculador X Y Z)
    )
)

(defn verifica_individual [X Y Z]
    (if
        (and
            (= X PP)
            (= Y AC)
            (= Z AR)
        )
        "estable_individualista" (verifica_retraido X Y Z)
    )
)

(defn verifica_pas [X Y Z]
    (if
        (and
            (= X DP)
            (= Y EC)
            (= Z ER)
        )
        "pas_positivo" (verifica_individual X Y Z)
    )
)

(defn verifica_estable [X Y Z]
    (if
        (and
            (= X AP)
            (= Y AC)
            (= Z AR)
        )
        "estable_positivo" (verifica_pas X Y Z)
    )
)

(defn verifica_primero [X Y Z]
    (if
        (and
            (= X PP)
            (= Y PC)
            (= Z PR)
        )
        "ezquizoide_positivo" (verifica_estable X Y Z)
    )
)