# Αξιολόγηση του Fine-tuned Μοντέλου Phi-3 / Phi-3.5 στο Azure AI Foundry με Εστίαση στις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft

Αυτό το ολοκληρωμένο δείγμα βασίζεται στον οδηγό "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" από την κοινότητα Microsoft Tech.

## Επισκόπηση

### Πώς μπορείτε να αξιολογήσετε την ασφάλεια και την απόδοση ενός fine-tuned μοντέλου Phi-3 / Phi-3.5 στο Azure AI Foundry;

Η προσαρμογή ενός μοντέλου μπορεί μερικές φορές να οδηγήσει σε ανεπιθύμητες ή απρόβλεπτες απαντήσεις. Για να διασφαλιστεί ότι το μοντέλο παραμένει ασφαλές και αποτελεσματικό, είναι σημαντικό να αξιολογηθεί η δυνατότητα του μοντέλου να παράγει επιβλαβές περιεχόμενο καθώς και η ικανότητά του να παρέχει ακριβείς, σχετικές και συνεκτικές απαντήσεις. Σε αυτό το σεμινάριο, θα μάθετε πώς να αξιολογείτε την ασφάλεια και την απόδοση ενός fine-tuned μοντέλου Phi-3 / Phi-3.5 ενσωματωμένου με το Prompt flow στο Azure AI Foundry.

Ακολουθεί η διαδικασία αξιολόγησης του Azure AI Foundry.

![Αρχιτεκτονική του σεμιναρίου.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.el.png)

*Πηγή εικόνας: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Για περισσότερες λεπτομέρειες και πρόσθετους πόρους σχετικά με το Phi-3 / Phi-3.5, επισκεφθείτε το [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Προαπαιτούμενα

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned μοντέλο Phi-3 / Phi-3.5

### Πίνακας Περιεχομένων

1. [**Σενάριο 1: Εισαγωγή στην αξιολόγηση Prompt flow του Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Εισαγωγή στην αξιολόγηση ασφάλειας](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Εισαγωγή στην αξιολόγηση απόδοσης](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Σενάριο 2: Αξιολόγηση του μοντέλου Phi-3 / Phi-3.5 στο Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Πριν ξεκινήσετε](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ανάπτυξη του Azure OpenAI για την αξιολόγηση του μοντέλου Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Αξιολόγηση του fine-tuned μοντέλου Phi-3 / Phi-3.5 χρησιμοποιώντας την αξιολόγηση Prompt flow του Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Συγχαρητήρια!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Σενάριο 1: Εισαγωγή στην αξιολόγηση Prompt flow του Azure AI Foundry**

### Εισαγωγή στην αξιολόγηση ασφάλειας

Για να διασφαλιστεί ότι το AI μοντέλο σας είναι ηθικό και ασφαλές, είναι κρίσιμο να αξιολογηθεί σύμφωνα με τις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft. Στο Azure AI Foundry, οι αξιολογήσεις ασφάλειας σας επιτρέπουν να εξετάσετε την ευπάθεια του μοντέλου σε jailbreak επιθέσεις και τη δυνατότητά του να παράγει επιβλαβές περιεχόμενο, κάτι που ευθυγραμμίζεται άμεσα με αυτές τις αρχές.

![Αξιολόγηση ασφάλειας.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.el.png)

*Πηγή εικόνας: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft

Πριν ξεκινήσετε τα τεχνικά βήματα, είναι σημαντικό να κατανοήσετε τις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft, ένα ηθικό πλαίσιο που έχει σχεδιαστεί για να καθοδηγεί την υπεύθυνη ανάπτυξη, υλοποίηση και λειτουργία συστημάτων τεχνητής νοημοσύνης. Αυτές οι αρχές διασφαλίζουν ότι οι τεχνολογίες AI σχεδιάζονται με τρόπο δίκαιο, διαφανή και χωρίς αποκλεισμούς. Αποτελούν τη βάση για την αξιολόγηση της ασφάλειας των AI μοντέλων.

Οι Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft περιλαμβάνουν:

- **Δικαιοσύνη και Συμπερίληψη**: Τα συστήματα AI πρέπει να αντιμετωπίζουν όλους δίκαια και να αποφεύγουν διακρίσεις μεταξύ παρόμοιων ομάδων ανθρώπων. Για παράδειγμα, όταν τα συστήματα AI παρέχουν καθοδήγηση για ιατρική θεραπεία, αιτήσεις δανείων ή απασχόληση, πρέπει να κάνουν τις ίδιες προτάσεις σε όλους με παρόμοια συμπτώματα, οικονομικές συνθήκες ή επαγγελματικά προσόντα.

- **Αξιοπιστία και Ασφάλεια**: Για να χτιστεί εμπιστοσύνη, είναι κρίσιμο τα συστήματα AI να λειτουργούν αξιόπιστα, με ασφάλεια και συνέπεια. Πρέπει να ανταποκρίνονται με ασφάλεια σε απρόβλεπτες συνθήκες και να αντιστέκονται σε κακόβουλους χειρισμούς.

- **Διαφάνεια**: Όταν τα συστήματα AI επηρεάζουν αποφάσεις που έχουν σημαντικές επιπτώσεις στις ζωές των ανθρώπων, είναι κρίσιμο να κατανοούν οι άνθρωποι πώς ελήφθησαν αυτές οι αποφάσεις.

- **Ιδιωτικότητα και Ασφάλεια**: Η προστασία της ιδιωτικότητας και η ασφάλεια των δεδομένων είναι ζωτικής σημασίας καθώς το AI γίνεται πιο διαδεδομένο.

- **Λογοδοσία**: Οι άνθρωποι που σχεδιάζουν και υλοποιούν συστήματα AI πρέπει να είναι υπεύθυνοι για τον τρόπο λειτουργίας τους.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.el.png)

*Πηγή εικόνας: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Για να μάθετε περισσότερα σχετικά με τις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft, επισκεφθείτε το [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Δείκτες Ασφάλειας

Σε αυτό το σεμινάριο, θα αξιολογήσετε την ασφάλεια του fine-tuned μοντέλου Phi-3 χρησιμοποιώντας τους δείκτες ασφάλειας του Azure AI Foundry. Αυτοί οι δείκτες σας βοηθούν να αξιολογήσετε τη δυνατότητα του μοντέλου να παράγει επιβλαβές περιεχόμενο και την ευπάθειά του σε jailbreak επιθέσεις. Οι δείκτες ασφάλειας περιλαμβάνουν:

- **Περιεχόμενο σχετικό με αυτοτραυματισμό**: Αξιολογεί αν το μοντέλο έχει την τάση να παράγει περιεχόμενο σχετικό με αυτοτραυματισμό.
- **Μισαλλόδοξο και άδικο περιεχόμενο**: Αξιολογεί αν το μοντέλο έχει την τάση να παράγει μισαλλόδοξο ή άδικο περιεχόμενο.
- **Βίαιο περιεχόμενο**: Αξιολογεί αν το μοντέλο έχει την τάση να παράγει βίαιο περιεχόμενο.
- **Σεξουαλικό περιεχόμενο**: Αξιολογεί αν το μοντέλο έχει την τάση να παράγει ακατάλληλο σεξουαλικό περιεχόμενο.

Η αξιολόγηση αυτών των πτυχών διασφαλίζει ότι το AI μοντέλο δεν παράγει επιβλαβές ή προσβλητικό περιεχόμενο, ευθυγραμμισμένο με κοινωνικές αξίες και κανονιστικά πρότυπα.

![Αξιολόγηση με βάση την ασφάλεια.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.el.png)

### Εισαγωγή στην αξιολόγηση απόδοσης

Για να διασφαλιστεί ότι το AI μοντέλο σας αποδίδει όπως αναμένεται, είναι σημαντικό να αξιολογηθεί με βάση δείκτες απόδοσης. Στο Azure AI Foundry, οι αξιολογήσεις απόδοσης σας επιτρέπουν να εξετάσετε την αποτελεσματικότητα του μοντέλου στη δημιουργία ακριβών, σχετικών και συνεκτικών απαντήσεων.

![Αξιολόγηση ασφάλειας.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.el.png)

*Πηγή εικόνας: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Δείκτες Απόδοσης

Σε αυτό το σεμινάριο, θα αξιολογήσετε την απόδοση του fine-tuned μοντέλου Phi-3 / Phi-3.5 χρησιμοποιώντας τους δείκτες απόδοσης του Azure AI Foundry. Αυτοί οι δείκτες σας βοηθούν να αξιολογήσετε την αποτελεσματικότητα του μοντέλου στη δημιουργία ακριβών, σχετικών και συνεκτικών απαντήσεων. Οι δείκτες απόδοσης περιλαμβάνουν:

- **Ευθυγράμμιση**: Αξιολογεί πόσο καλά ευθυγραμμίζονται οι παραγόμενες απαντήσεις με τις πληροφορίες της εισόδου.
- **Σχετικότητα**: Αξιολογεί τη συνάφεια των παραγόμενων απαντήσεων με τις δεδομένες ερωτήσεις.
- **Συνοχή**: Αξιολογεί πόσο ομαλά ρέει το παραγόμενο κείμενο και αν μοιάζει με ανθρώπινη γλώσσα.
- **Ευφράδεια**: Αξιολογεί την γλωσσική ικανότητα του παραγόμενου κειμένου.
- **Ομοιότητα με GPT**: Συγκρίνει την παραγόμενη απάντηση με την πραγματική για ομοιότητα.
- **F1 Score**: Υπολογίζει τον λόγο κοινών λέξεων μεταξύ της παραγόμενης απάντησης και των δεδομένων πηγής.

Αυτοί οι δείκτες σας βοηθούν να αξιολογήσετε την αποτελεσματικότητα του μοντέλου στη δημιουργία ακριβών, σχετικών και συνεκτικών απαντήσεων.

![Αξιολόγηση με βάση την απόδοση.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.el.png)
![Συμπληρώστε το hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.el.png)

1. Επιλέξτε **Επόμενο**.

#### Δημιουργία Έργου Azure AI Foundry

1. Στο Hub που δημιουργήσατε, επιλέξτε **Όλα τα έργα** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **+ Νέο έργο** από το μενού πλοήγησης.

    ![Επιλέξτε νέο έργο.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.el.png)

1. Εισάγετε **Όνομα έργου**. Πρέπει να είναι μοναδικό.

    ![Δημιουργία έργου.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.el.png)

1. Επιλέξτε **Δημιουργία έργου**.

#### Προσθήκη προσαρμοσμένης σύνδεσης για το fine-tuned μοντέλο Phi-3 / Phi-3.5

Για να ενσωματώσετε το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5 με το Prompt flow, πρέπει να αποθηκεύσετε το endpoint και το κλειδί του μοντέλου σε μια προσαρμοσμένη σύνδεση. Αυτή η ρύθμιση διασφαλίζει την πρόσβαση στο προσαρμοσμένο μοντέλο σας μέσω του Prompt flow.

#### Ορισμός api key και endpoint uri του fine-tuned μοντέλου Phi-3 / Phi-3.5

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Μεταβείτε στον χώρο εργασίας Azure Machine Learning που δημιουργήσατε.

1. Επιλέξτε **Endpoints** από την καρτέλα στην αριστερή πλευρά.

    ![Επιλέξτε endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.el.png)

1. Επιλέξτε το endpoint που δημιουργήσατε.

    ![Επιλέξτε endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.el.png)

1. Επιλέξτε **Κατανάλωση** από το μενού πλοήγησης.

1. Αντιγράψτε το **REST endpoint** και το **Primary key**.

    ![Αντιγραφή api key και endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.el.png)

#### Προσθήκη Προσαρμοσμένης Σύνδεσης

1. Επισκεφθείτε το [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Μεταβείτε στο έργο Azure AI Foundry που δημιουργήσατε.

1. Στο έργο που δημιουργήσατε, επιλέξτε **Ρυθμίσεις** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **+ Νέα σύνδεση**.

    ![Επιλέξτε νέα σύνδεση.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.el.png)

1. Επιλέξτε **Προσαρμοσμένα κλειδιά** από το μενού πλοήγησης.

    ![Επιλέξτε προσαρμοσμένα κλειδιά.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε **+ Προσθήκη ζευγών κλειδιού-τιμής**.
    - Για το όνομα κλειδιού, εισάγετε **endpoint** και επικολλήστε το endpoint που αντιγράψατε από το Azure ML Studio στο πεδίο τιμής.
    - Επιλέξτε **+ Προσθήκη ζευγών κλειδιού-τιμής** ξανά.
    - Για το όνομα κλειδιού, εισάγετε **key** και επικολλήστε το κλειδί που αντιγράψατε από το Azure ML Studio στο πεδίο τιμής.
    - Μετά την προσθήκη των κλειδιών, επιλέξτε **είναι μυστικό** για να αποτρέψετε την έκθεση του κλειδιού.

    ![Προσθήκη σύνδεσης.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.el.png)

1. Επιλέξτε **Προσθήκη σύνδεσης**.

#### Δημιουργία Prompt flow

Προσθέσατε μια προσαρμοσμένη σύνδεση στο Azure AI Foundry. Τώρα, ας δημιουργήσουμε ένα Prompt flow χρησιμοποιώντας τα παρακάτω βήματα. Στη συνέχεια, θα συνδέσετε αυτό το Prompt flow με την προσαρμοσμένη σύνδεση για να χρησιμοποιήσετε το fine-tuned μοντέλο μέσα στο Prompt flow.

1. Μεταβείτε στο έργο Azure AI Foundry που δημιουργήσατε.

1. Επιλέξτε **Prompt flow** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **+ Δημιουργία** από το μενού πλοήγησης.

    ![Επιλέξτε Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.el.png)

1. Επιλέξτε **Chat flow** από το μενού πλοήγησης.

    ![Επιλέξτε chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.el.png)

1. Εισάγετε **Όνομα φακέλου** για χρήση.

    ![Επιλέξτε chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.el.png)

1. Επιλέξτε **Δημιουργία**.

#### Ρύθμιση του Prompt flow για συνομιλία με το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5

Πρέπει να ενσωματώσετε το fine-tuned μοντέλο Phi-3 / Phi-3.5 σε ένα Prompt flow. Ωστόσο, το υπάρχον Prompt flow δεν είναι σχεδιασμένο για αυτόν τον σκοπό. Επομένως, πρέπει να επανασχεδιάσετε το Prompt flow για να επιτρέψετε την ενσωμάτωση του προσαρμοσμένου μοντέλου.

1. Στο Prompt flow, εκτελέστε τις παρακάτω ενέργειες για να αναδομήσετε την υπάρχουσα ροή:

    - Επιλέξτε **Λειτουργία ακατέργαστου αρχείου**.
    - Διαγράψτε όλο τον υπάρχοντα κώδικα στο αρχείο *flow.dag.yml*.
    - Προσθέστε τον παρακάτω κώδικα στο *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Επιλέξτε **Αποθήκευση**.

    ![Επιλέξτε λειτουργία ακατέργαστου αρχείου.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.el.png)

1. Προσθέστε τον παρακάτω κώδικα στο *integrate_with_promptflow.py* για να χρησιμοποιήσετε το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5 στο Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Επικολλήστε τον κώδικα του prompt flow.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.el.png)

> [!NOTE]
> Για περισσότερες λεπτομέρειες σχετικά με τη χρήση του Prompt flow στο Azure AI Foundry, μπορείτε να ανατρέξετε στο [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Επιλέξτε **Είσοδος συνομιλίας**, **Έξοδος συνομιλίας** για να ενεργοποιήσετε τη συνομιλία με το μοντέλο σας.

    ![Επιλέξτε Είσοδος Έξοδος.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.el.png)

1. Τώρα είστε έτοιμοι να συνομιλήσετε με το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5. Στην επόμενη άσκηση, θα μάθετε πώς να ξεκινήσετε το Prompt flow και να το χρησιμοποιήσετε για να συνομιλήσετε με το fine-tuned μοντέλο Phi-3 / Phi-3.5.

> [!NOTE]
>
> Η αναδομημένη ροή πρέπει να μοιάζει με την παρακάτω εικόνα:
>
> ![Παράδειγμα ροής](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.el.png)
>

#### Έναρξη του Prompt flow

1. Επιλέξτε **Έναρξη συνεδριών υπολογισμού** για να ξεκινήσετε το Prompt flow.

    ![Έναρξη συνεδρίας υπολογισμού.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.el.png)

1. Επιλέξτε **Επικύρωση και ανάλυση εισόδου** για να ανανεώσετε τις παραμέτρους.

    ![Επικύρωση εισόδου.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.el.png)

1. Επιλέξτε την **Τιμή** της **σύνδεσης** στην προσαρμοσμένη σύνδεση που δημιουργήσατε. Για παράδειγμα, *σύνδεση*.

    ![Σύνδεση.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.el.png)

#### Συνομιλία με το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5

1. Επιλέξτε **Συνομιλία**.

    ![Επιλέξτε συνομιλία.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.el.png)

1. Ακολουθεί ένα παράδειγμα αποτελεσμάτων: Τώρα μπορείτε να συνομιλήσετε με το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5. Συνιστάται να κάνετε ερωτήσεις με βάση τα δεδομένα που χρησιμοποιήθηκαν για fine-tuning.

    ![Συνομιλία με prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.el.png)

### Ανάπτυξη Azure OpenAI για την αξιολόγηση του μοντέλου Phi-3 / Phi-3.5

Για να αξιολογήσετε το μοντέλο Phi-3 / Phi-3.5 στο Azure AI Foundry, πρέπει να αναπτύξετε ένα μοντέλο Azure OpenAI. Αυτό το μοντέλο θα χρησιμοποιηθεί για την αξιολόγηση της απόδοσης του μοντέλου Phi-3 / Phi-3.5.

#### Ανάπτυξη Azure OpenAI

1. Συνδεθείτε στο [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Μεταβείτε στο έργο Azure AI Foundry που δημιουργήσατε.

    ![Επιλέξτε Έργο.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.el.png)

1. Στο έργο που δημιουργήσατε, επιλέξτε **Αναπτύξεις** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **+ Ανάπτυξη μοντέλου** από το μενού πλοήγησης.

1. Επιλέξτε **Ανάπτυξη βασικού μοντέλου**.

    ![Επιλέξτε Αναπτύξεις.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.el.png)

1. Επιλέξτε το μοντέλο Azure OpenAI που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, **gpt-4o**.

    ![Επιλέξτε το μοντέλο Azure OpenAI που θέλετε να χρησιμοποιήσετε.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.el.png)

1. Επιλέξτε **Επιβεβαίωση**.

### Αξιολόγηση του fine-tuned μοντέλου Phi-3 / Phi-3.5 χρησιμοποιώντας το Prompt flow αξιολόγησης του Azure AI Foundry

### Έναρξη νέας αξιολόγησης

1. Επισκεφθείτε το [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Μεταβείτε στο έργο Azure AI Foundry που δημιουργήσατε.

    ![Επιλέξτε Έργο.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.el.png)

1. Στο έργο που δημιουργήσατε, επιλέξτε **Αξιολόγηση** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **+ Νέα αξιολόγηση** από το μενού πλοήγησης.
![Επιλέξτε αξιολόγηση.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.el.png)

1. Επιλέξτε **Prompt flow** αξιολόγηση.

    ![Επιλέξτε Prompt flow αξιολόγηση.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Εισαγάγετε το όνομα της αξιολόγησης. Πρέπει να είναι μοναδικό.
    - Επιλέξτε **Ερώτηση και απάντηση χωρίς πλαίσιο** ως τύπο εργασίας. Αυτό συμβαίνει επειδή το σύνολο δεδομένων **UlTRACHAT_200k** που χρησιμοποιείται σε αυτό το σεμινάριο δεν περιέχει πλαίσιο.
    - Επιλέξτε το prompt flow που θέλετε να αξιολογήσετε.

    ![Prompt flow αξιολόγηση.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.el.png)

1. Επιλέξτε **Επόμενο**.

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε **Προσθέστε το σύνολο δεδομένων σας** για να ανεβάσετε το σύνολο δεδομένων. Για παράδειγμα, μπορείτε να ανεβάσετε το αρχείο δοκιμαστικού συνόλου δεδομένων, όπως το *test_data.json1*, το οποίο περιλαμβάνεται όταν κατεβάσετε το σύνολο δεδομένων **ULTRACHAT_200k**.
    - Επιλέξτε τη σωστή **Στήλη συνόλου δεδομένων** που ταιριάζει με το σύνολο δεδομένων σας. Για παράδειγμα, εάν χρησιμοποιείτε το σύνολο δεδομένων **ULTRACHAT_200k**, επιλέξτε **${data.prompt}** ως τη στήλη συνόλου δεδομένων.

    ![Prompt flow αξιολόγηση.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.el.png)

1. Επιλέξτε **Επόμενο**.

1. Εκτελέστε τις παρακάτω ενέργειες για να ρυθμίσετε τις μετρήσεις απόδοσης και ποιότητας:

    - Επιλέξτε τις μετρήσεις απόδοσης και ποιότητας που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε το Azure OpenAI μοντέλο που δημιουργήσατε για αξιολόγηση. Για παράδειγμα, επιλέξτε **gpt-4o**.

    ![Prompt flow αξιολόγηση.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες για να ρυθμίσετε τις μετρήσεις κινδύνου και ασφάλειας:

    - Επιλέξτε τις μετρήσεις κινδύνου και ασφάλειας που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε το όριο που θέλετε να χρησιμοποιήσετε για τον υπολογισμό του ποσοστού ελαττωμάτων. Για παράδειγμα, επιλέξτε **Μεσαίο**.
    - Για **ερώτηση**, επιλέξτε **Πηγή δεδομένων** σε **{$data.prompt}**.
    - Για **απάντηση**, επιλέξτε **Πηγή δεδομένων** σε **{$run.outputs.answer}**.
    - Για **ground_truth**, επιλέξτε **Πηγή δεδομένων** σε **{$data.message}**.

    ![Prompt flow αξιολόγηση.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.el.png)

1. Επιλέξτε **Επόμενο**.

1. Επιλέξτε **Υποβολή** για να ξεκινήσετε την αξιολόγηση.

1. Η αξιολόγηση θα χρειαστεί κάποιο χρόνο για να ολοκληρωθεί. Μπορείτε να παρακολουθήσετε την πρόοδο στην καρτέλα **Αξιολόγηση**.

### Ανασκόπηση των Αποτελεσμάτων Αξιολόγησης

> [!NOTE]
> Τα αποτελέσματα που παρουσιάζονται παρακάτω έχουν σκοπό να δείξουν τη διαδικασία αξιολόγησης. Σε αυτό το σεμινάριο, χρησιμοποιήσαμε ένα μοντέλο που έχει προσαρμοστεί σε ένα σχετικά μικρό σύνολο δεδομένων, κάτι που μπορεί να οδηγήσει σε υποβέλτιστα αποτελέσματα. Τα πραγματικά αποτελέσματα μπορεί να διαφέρουν σημαντικά ανάλογα με το μέγεθος, την ποιότητα και την ποικιλία του συνόλου δεδομένων που χρησιμοποιείται, καθώς και τη συγκεκριμένη διαμόρφωση του μοντέλου.

Μόλις ολοκληρωθεί η αξιολόγηση, μπορείτε να ανασκοπήσετε τα αποτελέσματα για τις μετρήσεις απόδοσης και ασφάλειας.

1. Μετρήσεις απόδοσης και ποιότητας:

    - Αξιολογήστε την αποτελεσματικότητα του μοντέλου στη δημιουργία συνεκτικών, ευφραδών και σχετικών απαντήσεων.

    ![Αποτέλεσμα αξιολόγησης.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.el.png)

1. Μετρήσεις κινδύνου και ασφάλειας:

    - Βεβαιωθείτε ότι οι έξοδοι του μοντέλου είναι ασφαλείς και ευθυγραμμίζονται με τις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης, αποφεύγοντας οποιοδήποτε επιβλαβές ή προσβλητικό περιεχόμενο.

    ![Αποτέλεσμα αξιολόγησης.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.el.png)

1. Μπορείτε να μετακινηθείτε προς τα κάτω για να δείτε **Αναλυτικά αποτελέσματα μετρήσεων**.

    ![Αποτέλεσμα αξιολόγησης.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.el.png)

1. Με την αξιολόγηση του προσαρμοσμένου μοντέλου Phi-3 / Phi-3.5 βάσει μετρήσεων απόδοσης και ασφάλειας, μπορείτε να επιβεβαιώσετε ότι το μοντέλο είναι όχι μόνο αποτελεσματικό, αλλά και συμμορφώνεται με τις υπεύθυνες πρακτικές τεχνητής νοημοσύνης, καθιστώντας το έτοιμο για ανάπτυξη στον πραγματικό κόσμο.

## Συγχαρητήρια!

### Ολοκληρώσατε αυτό το σεμινάριο

Έχετε αξιολογήσει με επιτυχία το προσαρμοσμένο μοντέλο Phi-3 που ενσωματώνεται με το Prompt flow στο Azure AI Foundry. Αυτό είναι ένα σημαντικό βήμα για να διασφαλίσετε ότι τα μοντέλα τεχνητής νοημοσύνης σας όχι μόνο αποδίδουν καλά, αλλά συμμορφώνονται και με τις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft, βοηθώντας σας να δημιουργήσετε αξιόπιστες και ασφαλείς εφαρμογές τεχνητής νοημοσύνης.

![Αρχιτεκτονική.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.el.png)

## Καθαρισμός Πόρων Azure

Καθαρίστε τους πόρους Azure σας για να αποφύγετε επιπλέον χρεώσεις στον λογαριασμό σας. Μεταβείτε στην πύλη Azure και διαγράψτε τους παρακάτω πόρους:

- Τον πόρο Azure Machine Learning.
- Το endpoint του μοντέλου Azure Machine Learning.
- Τον πόρο Project του Azure AI Foundry.
- Τον πόρο Prompt flow του Azure AI Foundry.

### Επόμενα Βήματα

#### Τεκμηρίωση

- [Αξιολόγηση συστημάτων AI χρησιμοποιώντας τον πίνακα εργαλείων Υπεύθυνης Τεχνητής Νοημοσύνης](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Μετρήσεις αξιολόγησης και παρακολούθησης για γενετική AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Τεκμηρίωση Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Τεκμηρίωση Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Εκπαιδευτικό Υλικό

- [Εισαγωγή στην Προσέγγιση Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Εισαγωγή στο Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Αναφορά

- [Τι είναι η Υπεύθυνη Τεχνητή Νοημοσύνη;](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Ανακοίνωση νέων εργαλείων στο Azure AI για τη δημιουργία ασφαλέστερων και αξιόπιστων γενετικών εφαρμογών AI](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Αξιολόγηση γενετικών εφαρμογών AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μετάφρασης βασισμένες σε τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή παρερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.