# Opracowanie planu eksperymentów

## Przygotowanie zbioru

Na początku jest planowana procedura przygotowania zbioru do pracy z nim. Czyli takie operacje jak:

- Usuwanie kolumn nieprzydatnych.
- Traktowanie danych brakujących.
- Usuwanie cech stałych oraz quasi-stałych
- Transformacja danych

## EDA

Po tym jak zbiór zostanie przetworzony można przeprowadzić proces eksploracji danych. Na początku chciałbym zbadać dane pod względem problemu klasyfikacji pozycji. Najważniejszymi punktami tutaj jest zbadanie rozkładu cech, korelacji pomiędzy cechami a zmiennej docelowej oraz wizualizacja.

## Selekcjonowanie cech

Na tym etapie chciałbym przetestować oraz porównać różne metody wyboru cech, które są dostępne w pakiecie sklearn.

Przykładowe Metody:

- Test ANOVA
- Rekurencyjna Eliminacja
- Wybór na podstawie stabilności i regularyzacji L1

Dodatkowe Eksperymenty:

- Stworzenie nowej cechy, łącząc skorelowane cechy za pomocą PCA

Celem eksperymentów jest odnalezienie najlepszego podzbioru cech. Porównanie wyników  odbędą się za pomocą bezpośrednią ewaluacją modelu uczącego (MAE, trafność, czułość, macierz konfuzji).

## Eksperyment

lista estymatorów  :

- KNeighborsClassifier (sklearn)
- DecisionTreeClassifier (sklearn)
- RandomForestClassifier (sklearn)
- MLPClassifier (sklearn)
- GradientBoostingClassifier (sklearn)
- AdaBoostClassifier (sklearn)
- XGBoost (xgboost lib)

Jeden eksperyment to przeprowadzenia ewaluacji modelu dla każdego estymatora z listy oraz dla różnych paramerów dotyczących konkretny estymator.
