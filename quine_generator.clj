(def src "(use '[clojure.string :only (join)])\n((fn [x] (print (str (join \"\" (map #(str (char %)) x)) x \")\\n\")))'")
(defn stringtochars [x] (map #(int %) (seq x))) 
(print (str src (seq (stringtochars src)) ")\n"))
