import csv
import random
import string
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_date():
    return datetime.strftime(datetime.today(), '%Y-%m-%d')

def generate_random_paragraphs():
    return '\n'.join(fake.paragraphs())

# Nombre de lignes à générer dans le fichier CSV
nombre_de_lignes = 10

# Nom du fichier CSV à créer
fichier_csv = 'DATA2.csv'

# Ouvrir le fichier CSV en mode écriture
with open(fichier_csv, mode='w', newline='', encoding='utf-8') as csv_file:
    # Définir le séparateur comme point virgule
    csv_writer = csv.writer(csv_file, delimiter=';')

    # Écrire l'en-tête du fichier CSV
    csv_writer.writerow([
        'rowid', 'nom', 'name_alias', 'entity', 'ref_ext', 'statut', 'parent',
        'status', 'code_client', 'code_fournisseur', 'code_compta',
        'code_compta_fournisseur', 'address', 'zip', 'town', 'fk_departement',
        'fk_pays', 'fk_account', 'phone', 'fax', 'url', 'email',
        'socialnetworks', 'fk_effectif', 'fk_typent', 'fk_forme_juridique',
        'fk_currency', 'siren', 'siret', 'ape', 'idprof4', 'idprof5', 'idprof6',
        'tva_intra', 'capital', 'fk_stcomm', 'note_private', 'note_public',
        'model_pdf', 'last_main_doc', 'prefix_comm', 'client', 'fournisseur',
        'supplier_account', 'fk_prospectlevel', 'fk_incoterms',
        'location_incoterms', 'customer_bad', 'customer_rate', 'supplier_rate',
        'remise_client', 'remise_supplier', 'mode_reglement', 'cond_reglement',
        'deposit_percent', 'transport_mode', 'mode_reglement_supplier',
        'cond_reglement_supplier', 'transport_mode_supplier',
        'fk_shipping_method', 'tva_assuj', 'vat_reverse_charge',
        'localtax1_assuj', 'localtax1_value', 'localtax2_assuj',
        'localtax2_value', 'barcode', 'fk_barcode_type', 'price_level',
        'outstanding_limit', 'order_min_amount', 'supplier_order_min_amount',
        'default_lang', 'logo', 'logo_squarred', 'canvas', 'fk_warehouse',
        'webservices_url', 'webservices_key', 'accountancy_code_sell',
        'accountancy_code_buy', 'tms', 'datec', 'fk_user_creat', 'fk_user_modif',
        'fk_multicurrency', 'multicurrency_code', 'import_key'
    ])

    for _ in range(nombre_de_lignes):
        rowid = random.randint(100, 10000)
        nom = fake.company()
        name_alias = f"{fake.first_name()} {fake.last_name()}"
        entity = '1'
        ref_ext = f"{fake.first_name().lower()}-{fake.last_name().lower()}"
        statut = '1'
        parent = '0'
        code_client = 'NULL'
        code_fournisseur = 'NULL'
        code_compta = 'NULL'
        code_compta_fournisseur = 'NULL'
        address = fake.street_address()
        zip_code = fake.zipcode()
        town = fake.city()
        fk_departement = 'NULL'
        fk_pays = 'NULL'
        fk_account = 'NULL'
        phone = fake.phone_number()
        fax = fake.phone_number()
        url = fake.url()
        email = f"{fake.first_name().lower()}.{fake.last_name().lower()}@{fake.domain_name()}"
        socialnetworks = generate_random_paragraphs()
        fk_effectif = 'NULL'
        fk_typent = 'NULL'
        fk_forme_juridique = 'NULL'
        fk_currency = 'NULL'
        siren = 'NULL'
        siret = 'NULL'
        ape = 'NULL'
        idprof4 = 'NULL'
        idprof5 = 'NULL'
        idprof6 = 'NULL'
        tva_intra = 'NULL'
        capital = 'NULL'
        fk_stcomm = 'NULL'
        note_private = generate_random_paragraphs()
        note_public = generate_random_paragraphs()
        model_pdf = 'NULL'
        last_main_doc = 'NULL'
        prefix_comm = 'NULL'
        client = 'NULL'
        fournisseur = 'NULL'
        supplier_account = 'NULL'
        fk_prospectlevel = 'NULL'
        fk_incoterms = 'NULL'
        location_incoterms = 'NULL'
        customer_bad = 'NULL'
        customer_rate = 'NULL'
        supplier_rate = 'NULL'
        remise_client = 'NULL'
        remise_supplier = 'NULL'
        mode_reglement = 'NULL'
        cond_reglement = 'NULL'
        deposit_percent = 'NULL'
        transport_mode = 'NULL'
        mode_reglement_supplier = 'NULL'
        cond_reglement_supplier = 'NULL'
        transport_mode_supplier = 'NULL'
        fk_shipping_method = 'NULL'
        tva_assuj = 'NULL'
        vat_reverse_charge = 'NULL'
        localtax1_assuj = 'NULL'
        localtax1_value = 'NULL'
        localtax2_assuj = 'NULL'
        localtax2_value = 'NULL'
        barcode = generate_random_string(14)
        fk_barcode_type = '0'
        price_level = 'NULL'
        outstanding_limit = 'NULL'
        order_min_amount = 'NULL'
        supplier_order_min_amount = 'NULL'
        default_lang = 'NULL'
        logo = 'NULL'
        logo_squarred = 'NULL'
        canvas = 'NULL'
        fk_warehouse = 'NULL'
        webservices_url = 'NULL'
        webservices_key = 'NULL'
        accountancy_code_sell = generate_random_string(32)
        accountancy_code_buy = generate_random_string(32)
        tms = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        datec = 'NULL'
        fk_user_creat = 'NULL'
        fk_user_modif = 'NULL'
        fk_multicurrency = 'NULL'
        multicurrency_code = 'NULL'
        import_key = generate_random_string(14)

        csv_writer.writerow([
            rowid, nom, name_alias, entity, ref_ext, statut, parent, 'NULL',
            code_client, code_fournisseur, code_compta, code_compta_fournisseur,
            address, zip_code, town, fk_departement, fk_pays, fk_account, phone,
            fax, url, email, socialnetworks, fk_effectif, fk_typent,
            fk_forme_juridique, fk_currency, siren, siret, ape, idprof4, idprof5,
            idprof6, tva_intra, capital, fk_stcomm, note_private, note_public,
            model_pdf, last_main_doc, prefix_comm, client, fournisseur,
            supplier_account, fk_prospectlevel, fk_incoterms, location_incoterms,
            customer_bad, customer_rate, supplier_rate, remise_client,
            remise_supplier, mode_reglement, cond_reglement, deposit_percent,
            transport_mode, mode_reglement_supplier, cond_reglement_supplier,
            transport_mode_supplier, fk_shipping_method, tva_assuj,
            vat_reverse_charge, localtax1_assuj, localtax1_value,
            localtax2_assuj, localtax2_value, barcode, fk_barcode_type,
            price_level, outstanding_limit, order_min_amount,
            supplier_order_min_amount, default_lang, logo, logo_squarred,
            canvas, fk_warehouse, webservices_url, webservices_key,
            accountancy_code_sell, accountancy_code_buy, tms, datec,
            'NULL', 'NULL', 'NULL', 'NULL', import_key
        ])

print(f"Fichier CSV '{fichier_csv}' généré avec succès.")

