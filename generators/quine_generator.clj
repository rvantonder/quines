(def src "(use '[clojure.string :only (join)])\n((fn [x] (print (str (join \"\" (map #(str (char %)) x)) x \")\\n\")))'") ; define the 'source' code, which converts ints to characters and concatenates into a string, then prince the source in characters
(defn stringtochars [x] (map #(int %) (seq x))) ; convert the string into ints
(print (str src (seq (stringtochars src)) ")\n")) ; print the src code followed by the encoded src code
