Demo hii inaonyesha jinsi ya kutumia modeli iliyofunzwa awali kuunda msimbo wa Python kulingana na picha na ombi la maandishi.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Hapa kuna maelezo ya hatua kwa hatua:

1. **Uingizaji na Mpangilio**:
   - Maktaba na moduli zinazohitajika zinaingizwa, zikiwemo `requests`, `PIL` kwa usindikaji wa picha, na `transformers` kwa kushughulikia modeli na usindikaji.

2. **Kupakia na Kuonyesha Picha**:
   - Faili ya picha (`demo.png`) inafunguliwa kwa kutumia maktaba ya `PIL` na inaonyeshwa.

3. **Kufafanua Ombi**:
   - Ujumbe unaundwa unaojumuisha picha na ombi la kuunda msimbo wa Python wa kusindika picha na kuihifadhi kwa kutumia `plt` (matplotlib).

4. **Kupakia Kisindikaji**:
   - `AutoProcessor` inapakuliwa kutoka kwa modeli iliyofunzwa awali iliyobainishwa na saraka ya `out_dir`. Kisindikaji hiki kitashughulikia pembejeo za maandishi na picha.

5. **Kuunda Ombi**:
   - Njia ya `apply_chat_template` inatumika kuunda ujumbe kuwa ombi linalofaa kwa modeli.

6. **Kusindika Pembejeo**:
   - Ombi na picha vinasindikwa kuwa tensors ambazo modeli inaweza kuelewa.

7. **Kuweka Hoja za Uzalishaji**:
   - Hoja za mchakato wa uzalishaji wa modeli zinafafanuliwa, ikiwa ni pamoja na idadi ya juu ya tokeni mpya za kuzalisha na kama pato litachaguliwa kwa sampuli.

8. **Kuzalisha Msimbo**:
   - Modeli inazalisha msimbo wa Python kulingana na pembejeo na hoja za uzalishaji. `TextStreamer` inatumika kushughulikia pato, ikiruka ombi na tokeni maalum.

9. **Pato**:
   - Msimbo uliotengenezwa unachapishwa, ambao unapaswa kujumuisha msimbo wa Python wa kusindika picha na kuihifadhi kama ilivyobainishwa kwenye ombi.

Demo hii inaonyesha jinsi ya kutumia modeli iliyofunzwa awali kwa kutumia OpenVino kuunda msimbo kwa njia ya kiotomatiki kulingana na pembejeo za mtumiaji na picha.

**Kanusho:**  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kuwa chanzo cha mamlaka. Kwa maelezo muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.