(defn is-pythagorean-triple? [x y z]
  (= (+ (* x x) (* y y)) (* z z)))

(defn generate-pythagorean-triples []
  (let [triples (for [z (range 1 200)
                      y (range 1 (inc z))
                      x (range 1 (inc y))
                      :when (and (is-pythagorean-triple? x y z)
                                 (<= x y z))]
                  [x y z])]
    (doseq [[idx [x y z]] (map-indexed vector (take 100 (sort-by (fn [[x y z]] [(+ x y z) x]) triples)))]
      (println (str (inc idx) ": ") x y z))))

(generate-pythagorean-triples)
