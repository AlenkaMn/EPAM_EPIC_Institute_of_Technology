(defn generate-pairs []
  (map-indexed
    (fn [idx [x y]]
      (str "Pair #" (inc idx) ": " [x y]))
    (take 100
      (sort-by (fn [[x1 y1]] [(+ x1 y1) x1])
        (for [y (range 1 101)
              x (range 1 (inc y))]
          [x y])))))

(doseq [pair (generate-pairs)]
  (println pair))
