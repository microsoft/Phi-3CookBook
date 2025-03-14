# **Ποσοτικοποίηση του Phi-3.5 με το Apple MLX Framework**

Το MLX είναι ένα πλαίσιο υπολογιστικών πινάκων για έρευνα στη μηχανική μάθηση που έχει αναπτυχθεί από την Apple για τις συσκευές με Apple Silicon.

Το MLX σχεδιάστηκε από ερευνητές μηχανικής μάθησης για ερευνητές μηχανικής μάθησης. Το πλαίσιο είναι φιλικό προς τον χρήστη, αλλά ταυτόχρονα παραμένει αποδοτικό για την εκπαίδευση και την ανάπτυξη μοντέλων. Η ίδια η σχεδίαση του πλαισίου είναι επίσης απλή σε επίπεδο εννοιών, με στόχο να διευκολύνει τους ερευνητές να επεκτείνουν και να βελτιώσουν το MLX, επιτρέποντας την ταχεία εξερεύνηση νέων ιδεών.

Τα LLMs μπορούν να επιταχυνθούν σε συσκευές Apple Silicon μέσω του MLX, και τα μοντέλα μπορούν να εκτελούνται τοπικά με μεγάλη ευκολία.

Τώρα το Apple MLX Framework υποστηρίζει τη μετατροπή ποσοτικοποίησης του Phi-3.5-Instruct(**υποστήριξη από το Apple MLX Framework**), του Phi-3.5-Vision(**υποστήριξη από το MLX-VLM Framework**), και του Phi-3.5-MoE(**υποστήριξη από το Apple MLX Framework**). Ας το δοκιμάσουμε παρακάτω:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Δείγματα για το Phi-3.5 με το Apple MLX**

| Εργαστήρια    | Περιγραφή | Σύνδεσμος |
| -------- | ------- |  ------- |
| 🚀 Εργαστήριο-Εισαγωγή στο Phi-3.5 Instruct  | Μάθετε πώς να χρησιμοποιείτε το Phi-3.5 Instruct με το πλαίσιο Apple MLX   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Εργαστήριο-Εισαγωγή στο Phi-3.5 Vision (εικόνα) | Μάθετε πώς να χρησιμοποιείτε το Phi-3.5 Vision για ανάλυση εικόνων με το πλαίσιο Apple MLX     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Εργαστήριο-Εισαγωγή στο Phi-3.5 Vision (moE)   | Μάθετε πώς να χρησιμοποιείτε το Phi-3.5 MoE με το πλαίσιο Apple MLX  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Πόροι**

1. Μάθετε για το Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες αυτόματης μετάφρασης με τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή παρερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.