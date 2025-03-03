# **Δημιουργήστε το δικό σας Visual Studio Code GitHub Copilot Chat με τη σειρά Microsoft Phi-3**

Έχετε χρησιμοποιήσει τον workspace agent στο GitHub Copilot Chat; Θέλετε να δημιουργήσετε τον δικό σας agent για την ομάδα σας; Αυτό το εργαστήριο έχει σκοπό να συνδυάσει το ανοιχτό μοντέλο για τη δημιουργία ενός επιχειρησιακού agent για κώδικα.

## **Βάση**

### **Γιατί να επιλέξετε τη σειρά Microsoft Phi-3**

Η σειρά Phi-3 περιλαμβάνει τα μοντέλα phi-3-mini, phi-3-small και phi-3-medium, τα οποία βασίζονται σε διαφορετικές παραμέτρους εκπαίδευσης για δημιουργία κειμένου, ολοκλήρωση διαλόγου και δημιουργία κώδικα. Υπάρχει επίσης το phi-3-vision που βασίζεται στην Όραση. Είναι ιδανικό για επιχειρήσεις ή διαφορετικές ομάδες που θέλουν να δημιουργήσουν offline λύσεις γεννητικής AI.

Συνιστάται να διαβάσετε αυτόν τον σύνδεσμο: [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Το πρόσθετο GitHub Copilot Chat παρέχει μια διεπαφή συνομιλίας που σας επιτρέπει να αλληλεπιδράτε με το GitHub Copilot και να λαμβάνετε απαντήσεις σε ερωτήσεις που σχετίζονται με τον κώδικα απευθείας μέσα στο VS Code, χωρίς να χρειάζεται να ανατρέχετε σε τεκμηρίωση ή να ψάχνετε σε διαδικτυακά φόρουμ.

Το Copilot Chat μπορεί να χρησιμοποιήσει λειτουργίες όπως επισήμανση σύνταξης, εσοχές και άλλα χαρακτηριστικά μορφοποίησης για να προσθέσει σαφήνεια στις παραγόμενες απαντήσεις. Ανάλογα με τον τύπο της ερώτησης του χρήστη, το αποτέλεσμα μπορεί να περιέχει συνδέσμους με το πλαίσιο που χρησιμοποίησε το Copilot για να δημιουργήσει μια απάντηση, όπως αρχεία πηγαίου κώδικα ή τεκμηρίωση, ή κουμπιά για πρόσβαση σε λειτουργικότητες του VS Code.

- Το Copilot Chat ενσωματώνεται στη ροή εργασίας του προγραμματιστή και παρέχει βοήθεια εκεί που χρειάζεται:

- Ξεκινήστε μια συνομιλία απευθείας από τον επεξεργαστή ή το τερματικό για βοήθεια κατά τη συγγραφή κώδικα

- Χρησιμοποιήστε την προβολή Chat για να έχετε έναν AI βοηθό στο πλάι ανά πάσα στιγμή

- Εκκινήστε το Quick Chat για να κάνετε μια γρήγορη ερώτηση και να επιστρέψετε σε αυτό που κάνετε

Μπορείτε να χρησιμοποιήσετε το GitHub Copilot Chat σε διάφορα σενάρια, όπως:

- Να απαντά σε ερωτήσεις σχετικά με το πώς να λύσετε ένα πρόβλημα

- Να εξηγεί τον κώδικα κάποιου άλλου και να προτείνει βελτιώσεις

- Να προτείνει διορθώσεις κώδικα

- Να δημιουργεί περιπτώσεις δοκιμών μονάδας

- Να παράγει τεκμηρίωση κώδικα

Συνιστάται να διαβάσετε αυτόν τον σύνδεσμο: [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Η αναφορά στο **@workspace** στο Copilot Chat σας επιτρέπει να κάνετε ερωτήσεις σχετικά με ολόκληρη τη βάση κώδικα. Με βάση την ερώτηση, το Copilot ανακτά έξυπνα σχετικά αρχεία και σύμβολα, τα οποία στη συνέχεια αναφέρει στις απαντήσεις του ως συνδέσμους και παραδείγματα κώδικα.

Για να απαντήσει στην ερώτησή σας, το **@workspace** αναζητά στις ίδιες πηγές που θα χρησιμοποιούσε ένας προγραμματιστής κατά την πλοήγηση σε μια βάση κώδικα στο VS Code:

- Όλα τα αρχεία στον workspace, εκτός από αυτά που αγνοούνται από ένα αρχείο .gitignore

- Τη δομή των φακέλων με τους ονομασίες των φακέλων και των αρχείων

- Τον δείκτη αναζήτησης κώδικα του GitHub, εάν ο workspace είναι αποθετήριο του GitHub και έχει καταχωριστεί για αναζήτηση κώδικα

- Τα σύμβολα και τους ορισμούς στον workspace

- Το επιλεγμένο κείμενο ή το ορατό κείμενο στον ενεργό επεξεργαστή

Σημείωση: Το .gitignore παρακάμπτεται εάν έχετε ανοίξει ένα αρχείο ή έχετε επιλέξει κείμενο μέσα σε ένα αρχείο που αγνοείται.

Συνιστάται να διαβάσετε αυτόν τον σύνδεσμο: [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Μάθετε περισσότερα για αυτό το Εργαστήριο**

Το GitHub Copilot έχει βελτιώσει σημαντικά την αποδοτικότητα του προγραμματισμού στις επιχειρήσεις, και κάθε επιχείρηση ελπίζει να προσαρμόσει τις σχετικές λειτουργίες του GitHub Copilot. Πολλές επιχειρήσεις έχουν προσαρμόσει επεκτάσεις παρόμοιες με το GitHub Copilot βασισμένες στα δικά τους επιχειρηματικά σενάρια και στα ανοιχτά μοντέλα. Για τις επιχειρήσεις, οι προσαρμοσμένες επεκτάσεις είναι πιο εύκολες στη διαχείριση, αλλά αυτό επηρεάζει και την εμπειρία χρήστη. Εξάλλου, το GitHub Copilot είναι πιο ισχυρό στην αντιμετώπιση γενικών και επαγγελματικών σεναρίων. Εάν η εμπειρία μπορεί να παραμείνει συνεπής, θα ήταν καλύτερο να προσαρμοστεί η επέκταση της επιχείρησης. Το GitHub Copilot Chat παρέχει σχετικές APIs για τις επιχειρήσεις ώστε να επεκταθούν στην εμπειρία Chat. Η διατήρηση μιας συνεπούς εμπειρίας και η προσθήκη προσαρμοσμένων λειτουργιών προσφέρει μια καλύτερη εμπειρία χρήστη.

Αυτό το εργαστήριο χρησιμοποιεί κυρίως το μοντέλο Phi-3 σε συνδυασμό με τοπικό NPU και Azure hybrid για να δημιουργήσει έναν προσαρμοσμένο Agent στο GitHub Copilot Chat ***@PHI3*** που βοηθά τους εταιρικούς προγραμματιστές να ολοκληρώσουν τη δημιουργία κώδικα ***(@PHI3 /gen)*** και τη δημιουργία κώδικα από εικόνες ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.410a18b85555fad4ca8bfb8f0b1776a96ae7f8eae1132b8f0c09d4b92b8e3365.el.png)

### ***Σημείωση:*** 

Αυτό το εργαστήριο υλοποιείται επί του παρόντος στο AIPC του Intel CPU και του Apple Silicon. Θα συνεχίσουμε να ενημερώνουμε την έκδοση Qualcomm του NPU.


## **Εργαστήριο**


| Όνομα | Περιγραφή | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Εγκαταστάσεις(✅) | Διαμόρφωση και εγκατάσταση σχετικών περιβαλλόντων και εργαλείων | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Εκτέλεση Prompt flow με Phi-3-mini (✅) | Σε συνδυασμό με AIPC / Apple Silicon, χρήση τοπικού NPU για δημιουργία κώδικα μέσω του Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Ανάπτυξη Phi-3-vision στο Azure Machine Learning Service(✅) | Δημιουργία κώδικα μέσω της ανάπτυξης του Azure Machine Learning Service's Model Catalog - Phi-3-vision image | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Δημιουργία ενός agent @phi-3 στο GitHub Copilot Chat(✅)  | Δημιουργία ενός προσαρμοσμένου agent Phi-3 στο GitHub Copilot Chat για ολοκλήρωση δημιουργίας κώδικα, δημιουργία κώδικα από γραφήματα, RAG κ.λπ. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Παράδειγμα Κώδικα (✅)  | Λήψη παραδείγματος κώδικα | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Πόροι**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Μάθετε περισσότερα για το GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Μάθετε περισσότερα για το GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Μάθετε περισσότερα για το API του GitHub Copilot Chat [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Μάθετε περισσότερα για το Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Μάθετε περισσότερα για το Model Catalog του Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μετάφρασης με βάση την τεχνητή νοημοσύνη. Ενώ καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.