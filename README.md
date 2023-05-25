pdf-utils
Dokumentace
·	Funkce
o	pdfMerge
§	Rozšíří pdf_1 o stránky dokumentu pdf_2
§	pdfMerge(pdf_1_location, pdf_2_location) 
§	Postup funkce:
1.	Otevření pdf_1
2.	Otevření pdf_2
3.	Rozšíření pdf_1 o pdf_2 pomocí metody .extend
4.	Uložení upraveného pdf
o	pdfReturn
§	-
o	pdfDelete
§	Odstraní z pdf požadované strany ze seznamu page_numbers
§	pdfDelete(pdf_location, page_numbers)
§	Postup funkce:
1.	Otevření pdf
2.	Vymazání redundantních stránek
3.	Projití seznamu požadovaných stránek a vymazání jich z pdf
4.	Uložení upraveného pdf
o	pdfMetadata
§	Uloží ve formátu .json – název PDF, verzi, datum vytvoření a popis
§	pdfMetadata(pdf_location)
§	Postup funkce:
1.	Otevření pdf
2.	Načtení metadat
3.	Slovník požadovaných metadat
4.	Vytvoření .json souboru
5.	Převedění metadat na string a uložení do souboru
6.	Zavření souboru
o	pdfWatermark
§	Přidá na všechny strany pdf požadovaný vodoznak
§	pdfWatermark(pdf_location, watermark_location)
§	Vodoznak musí být uložený ve formátu PDF na první straně 
§	Postup funkce
1.	Otevření pdf
2.	Otevření PDF dokumentu ve kterém je vodoznak
3.	Načtení první strany na které se má nacházet vodoznak
4.	Projití všech stran v pdf
5.	Na každou jednotlivou stranu se nanese vodoznak pomocí metody .add_overlay
6.	Pozice se dá měnit v argumentech objektu Rectangle
7.	Uložení upraveného pdf
o	pdfEncrypt
§	Zahesluje pdf požadovanými hesly
§	pdfEncrypt(pdf_location, password, owner_password)
§	Postup funkce:
1.	Otevření pdf
2.	Uložení enkryptovaného pdf s hesly 
·	Argumenty funkcí
o	pdf_location – místo kde je uložený požadovaný PDF dokument
o	page_numbers – seznam stránek PDF dokumentu
o	watermark_location – místo kde je uložený požadovaný vodoznak v PDF formátu
o	password – heslo uživatele PDF dokument
o	owner_password – heslo vlastníka PDF dokumentu  

