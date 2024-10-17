(def cities [{:name "Tokyo"
              :country "Japan"
              :population 39105000
              :area 8231}
             {:name "Delhi"
              :country "India"
              :population 31870000
              :area 2233}
             {:name "Shanghai"
              :country "China"
              :population 22118000
              :area 4069}
             {:name "Sao Paulo"
              :country "Brazil"
              :population 22495000
              :area 1521}
             {:name "Mexico City"
              :country "Mexico"
              :population 21505000
              :area 2385}
             {:name "Cairo"
              :country "Egypt"
              :population 19787000
              :area 2010}
             {:name "Mumbai"
              :country "India"
              :population 22186000
              :area 1008}
             {:name "Beijing"
              :country "China"
              :population 19437000
              :area 4172}
             {:name "Dhaka"
              :country "Bangladesh"
              :population 16839000
              :area 456}
             {:name "Osaka"
              :country "Japan"
              :population 15490000
              :area 3020}
             {:name "New York"
              :country "United States"
              :population 23582649
              :area 34493}
             {:name "Karachi"
              :country "Pakistan"
              :population 15292000
              :area 1044}
             {:name "Buenos Aires"
              :country "Argentina"
              :population 16216000
              :area 3222}
             {:name "Chongqing"
              :country "China"
              :population 8261000
              :area 1356}
             {:name "Istanbul"
              :country "Turkiye"
              :population 15311000
              :area 1375}
             {:name "Kolkata"
              :country "India"
              :population 18698000
              :area 1352}
             {:name "Manila"
              :country "Philippines"
              :population 23971000
              :area 1873}
             {:name "Lagos"
              :country "Nigeria"
              :population 15487000
              :area 1966}
             {:name "Rio de Janeiro"
              :country "Brazil"
              :population 12486000
              :area 2020}
             {:name "Tianjin"
              :country "China"
              :population 10932000
              :area 2813}])

(def countries [{:name "Pakistan"
                 :continent "Asia"}
                {:name "Argentina"
                 :continent "South America"}
                {:name "Turkiye"
                 :continent "Asia"}
                {:name "Brazil"
                 :continent "South America"}
                {:name "United States"
                 :continent "North America"}
                {:name "Bangladesh"
                 :continent "Asia"}
                {:name "Mexico"
                 :continent "North America"}
                {:name "Egypt"
                 :continent "Africa"}
                {:name "Japan"
                 :continent "Asia"}
                {:name "Nigeria"
                 :continent "Africa"}
                {:name "Philippines"
                 :continent "Asia"}
                {:name "China"
                 :continent "Asia"}
                {:name "India"
                 :continent "Asia"}
                {:name "DR Congo"
                 :continent "Africa"}
                {:name "Russia"
                 :continent "Europe"}
                {:name "France"
                 :continent "Europe"}])

;1 вопрос
;defn-функция
(println "The 1 question: Print the number of unique countries in the cities database")
(defn get-all-countries [cities-data]
  (->> cities-data
        ;созд список
       (map :country)
       (distinct)))
;на всякий случай выведу названия всех уникальных стран, чтобы проверить всё ли корректно
(println (get-all-countries cities))
(println (count (get-all-countries cities)))
(println)
;2 вопрос
(println "The 2 question: Print the total area of the cities located in China")
(defn S_C [cities-data]
  (->> cities-data

       (filter #(= (:country %) "China"))
       (map :area)
       (apply +)))

(println (S_C cities))
(println)
; 3 вопрос
(println "The 3 question: Print the names of the cities located in India")
(defn cities-in-india [cities-data]
  (->> cities-data
       (filter #(= (:country %) "India"))
       (map :name)))

(println (cities-in-india cities))
(println)

; 4 вопрос
(println "The 4 question: Print the names of top five cities with the largest area")
(defn top-five-cities-by-area [cities-data]
  (->> cities-data
    ;сортировка по площади
       (sort-by :area >)
    ;берём первые 5
       (take 5)
       (map :name)))

(println "Top five cities by area:")
(println (top-five-cities-by-area cities))
(println)

; 5 вопрос
(println "The 5 question: Print the names of top five cities with the largest population density")

(defn top-five-cities-by-density [cities-data]
  (->> cities-data
       (sort-by #(-> % :population (/ (:area %))) >)
       (take 5)
       (map :name)))

(doseq [city-name (top-five-cities-by-density cities)]
  (println city-name))

(println)

; 6 вопрос
(println "The 6 question:Print the number of cities located in Asia
")
(defn count_asian_cities [cities countries]
  (let [asian_countries (->> countries
                             (filter #(= (:continent %) "Asia"))
                             (map :name)
                             (set))]
    (->> cities
         (filter #(contains? asian_countries (:country %)))
         (count))))

(println (count_asian_cities cities countries))
(println)
;7 вопрос
(println "The 7 question: Print the names of top five cities with the smaller area, alongside with their continent.")

(defn smaller-area-cities [n]
  (->> (sort-by :area cities)
       (take n)))

(defn continent [city]
  (let [country-info (first (filter #(= (:name %) (:country city)) countries))]
    {:name (:name city)
     :continent (:continent country-info)}))

(defn five []
  (let [top-five (smaller-area-cities 5)
        cities-with-continent (map continent top-five)]
    (doseq [city cities-with-continent]
      (println "City:" (:name city) "| Continent:" (:continent city)))))

;; To print the top five cities with smaller areas and their continents
(five)
(println)
;8 вопрос
(println "The 8 question: Print the total area of the cities located in South America")

(defn total-area-south-america []
  ;страны Южной Америки
  (let [south-american-countries #{"Argentina" "Brazil"}
        ; Фильтрация городов по странам Южной Америки
        south-american-cities (filter #(contains? south-american-countries (:country %)) cities)
        ; Получение площадей городов ЮА
        south-american-areas (map :area south-american-cities)
        total-area (apply + south-american-areas)]
    (println "Total area of cities in South America:" total-area)))

(total-area-south-america)

(println)

;9 вопрос
(println "The 9 question: Print the total population of the cities for each country.")
(defn total-population-per-country [cities countries]
  (let [cities-by-country (group-by :country cities)
        populations (reduce
                     (fn [acc [country city-list]]
                       (let [total-population (->> city-list
                                                   (map :population)
                                                   (apply +))]
                         (conj acc {:country country
                                    :total-population total-population})))
                     []
                     cities-by-country)
        countries-map (zipmap (map :name countries) countries)]
    (map (fn [{:keys [country total-population]}]
           (if-let [country-data (get countries-map country)]
             (assoc country-data :total-population total-population)))
         populations)))

(def result (total-population-per-country cities countries))

(doseq [country-data result]
  (println (str "Country: " (:name country-data) ", Total Population: " (:total-population country-data))))

(println)

(println "The 10 question: Print the largest city by population for each country.")

(defn largest-city-by-population [city-data]
  (->> city-data
       (group-by :country)
       (map (fn [[country cities]]
              (->> cities
                   (sort-by :population)
                   (reverse)
                   (first))))
       (doall)))

(def largest-cities (largest-city-by-population cities))

(doseq [country countries]
  (let [country-name (:name country)
        city (->> largest-cities
                  (filter #(= country-name (:country %)))
                  first)]
    (when city
      (println (str "Largest city in " country-name " is " (:name city) " with population " (:population city))))))
(println)

(println "The 11 question: Print the total population of the cities for each continent")
;немного переделаю функцию из 9 вопроса
(defn total-population-per-country [cities countries]
  (let [cities-by-country (group-by :country cities)
        countries-map (zipmap (map :name countries) countries)
        countries-with-populations (reduce
                                    (fn [acc [country city-list]]
                                      (let [continent (->> country
                                                           (get countries-map)
                                                           :continent)
                                            total-population (->> city-list
                                                                  (map :population)
                                                                  (apply +))]
                                        (update acc
                                                continent
                                                #(conj % {:country country
                                                          :total-population total-population}))))
                                    {}
                                    cities-by-country)]
    countries-with-populations))

(def result (total-population-per-country cities countries))

(doseq [[continent country-data] result]
  (println (str "Continent: " continent))
  (doseq [{:keys [country total-population]} country-data]
    (println (str "  Country: " country ", Total Population: " total-population))))

(println)

(println "The 12 question: Print the names of the cities whose area is larger than the average area of a city in Asia.
         ;     The cities to be printed can be from any continent.")

;ищем среднюю S в Азии
(defn avg-asia-area []
  (let [asia-countries (filter #(= (:continent %) "Asia") countries)
        asia-cities (filter #(some #{(:country %)} (map :name asia-countries)) cities)
        asia-city-areas (map :area asia-cities)
        avg-asia-area (if (seq asia-city-areas)
                        (/ (apply + asia-city-areas) (count asia-city-areas))
                        0)]
    avg-asia-area))

(defn print-cities-larger-than-avg-asia []
  (let [average-asia-area (avg-asia-area)
        cities-larger-than-avg (filter #(> (:area %) average-asia-area) cities)
        city-names (map :name cities-larger-than-avg)]
    (doseq [name city-names]
      (println name))))

(print-cities-larger-than-avg-asia)

; You are given the database about cities and countries (see above).
;
; You need to answer some queries using Clojure. It is highly recommended to
; use the functions such as map, filter, reduce and sort-by. You can also use
; list comprehensions.
;
; The only data you can use is the data from the databases above.

; 1. Print the number of unique countries in the cities database

; 2. Print the total area of the cities located in China

; 3. Print the names of the cities located in India

; 4. Print the names of top five cities with the largest area

; 5. Print the names of top five cities with the largest population density

; 6. Print the number of cities located in Asia

; 7. Print the names of top five cities with the smaller area, alongside with their continent.

; 8. Print the total area of the cities located in South America

; 9. Print the total population of the cities for each country. Hint: use group-by

; 10. Print the largest city by population for each country

; 11. Print the total population of the cities for each continent

; 12. Print the names of the cities whose area is larger than the average area of a city in Asia.
;     The cities to be printed can be from any continent.
