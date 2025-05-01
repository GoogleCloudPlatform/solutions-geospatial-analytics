PROMPT = """
    The user will provide two tables from the state keys "source_schema" and "target_schema". 
    These are referred to below as Tables B and A, repectively.

    Your goal is to produce a SQL query that merges Table B into Table A.

    Tables A and B are both GIS-related tables containing information about county tax assessor parcels from a CAMA (Computer Assisted Mass Appraisal) system.

    You evaluate the schemas and sample records from the two tables to determine how to merge these two tables together.
    Columns should map one-to-one if possible.

    Explain what each column in Tables A and B represents in detail, and their datatypes.
    Explain what the data records in Tables A and B represent in detail, and their datatypes.

    Explain how to map the columns in Table B to the columns in Table A.

    Adhere to the following guidelines:
    1. The columns are unordered. Do not consider the column ordering in your mapping decision.
    2. Ensure that the two columns in the mapping have a similar data type.
    3. Ignore columns representing longitude/latitude coordinates or parcel geometry.
    4. Ensure the mapping for each column is consistent with your explanations.
    5. If there is not a good match, map the Table B column to null.
    6. Ensure that all your mappings represent REAL columns that exist in both Tables A and B.

    Explain why your mapping conforms with the provided hints and guidelines.
    Mappings are from Table B to Table A.

    EXAMPLE JSON OUTPUT:
        {
            "mappings": {
                "taxkey": "tax_account_number",
                "pin": "parcel_number",
                "num": "house_number",
                "prefix": "street_direction",
                "name": "owner_name",
                "st_type": null,
                "suffix": "street_suffix",
                "site_address": "parcel_address",
                "site_zipcode": "address_zip_code",
                "juris": "jurisdiction",
                "plss": "plss_description",
                "platname": "plat_name",
                "platlot": "plat_lot",
                "platblock": "plat_block",
                "presentuse": "land_use_code",
                "presentusedesc": "land_use_description",
                "proptype": "parcel_type",
                "sqftlot": null,
                "bathfullcount": "num_bathrooms",
                "bedrooms": "num_bedrooms",
                "nbrlivingunits": "number_of_units",
                "stories": "num_stories",
                "saledate": "last_sale_date",
                "taxablelandval": "land_value",
                "taxableimpsval": "improvement_value",
                "totalappraisedvalue": "total_value",
                "acctnbr": "tax_account_number",
                "taxpayername": "owner_name",
                "attnline": "owner_name",
                "remaining_name": null,
                "last_name": "owner_name",
                "citystate": "address_city",
                "quartersection": "plss_quarter_section",
                "section_": "plss_section",
                "township": "plss_township",
                "range": "plss_range",
                "impervious_acres": null,
                "cama_id": "parcel_number_alternate"

            },
            "mapping_explanations": {
                "parcel_number": "Mapped from 'pin' in Table B, which is a common synonym for parcel identifiers.",
                "house_number": "Derived from 'num' in Table B, representing the street number part of the address.",
                "street_direction": "Mapped from 'prefix' in Table B, indicating directionals like NE or SW.",
                "owner_name": "Combined from multiple name columns ('name', 'taxpayername', 'attnline', 'last_name') in Table B to form the full owner's name in Table A.",
                "street_suffix": "Mapped from 'st_type' and 'suffix' in Table B, providing street type abbreviations (e.g., Ave, Blvd).",
                "parcel_address": "Constructed from 'site_address' in Table B, representing the full parcel address.",
                "address_zip_code": "Directly mapped from 'site_zipcode' in Table B to the zip code part of the address.",
                "jurisdiction": "Mapped from 'juris' in Table B, indicating the governing body's area.",
                "plat_name": "Derived from 'platname' in Table B, referring to the plat name for the parcel.",
                "plat_lot": "Mapped from 'platlot' in Table B, indicating the specific lot within a plat.",
                "plat_block": "From 'platblock' in Table B, showing the block within a plat.",
                "land_use_code": "Mapped from 'presentuse' in Table B, categorizing land usage with codes.",
                "land_use_description": "Derived from 'presentusedesc' in Table B, providing descriptions for land use codes.",
                "parcel_type": "Mapped from 'proptype' in Table B, indicating the type of property (e.g., residential).",
                "main_building_sqft": "From 'sqftlot' in Table B, representing the square footage of the main building.",
                "num_bathrooms": "Directly mapped from 'bathfullcount' in Table B to the number of full bathrooms.",
                "num_bedrooms": "Mapped from 'bedrooms' in Table B, indicating the count of bedrooms.",
                "number_of_units": "Derived from 'nbrlivingunits' in Table B, showing the number of living units in the parcel.",
                "num_stories": "From 'stories' in Table B, representing the number of stories in the building.",
                "last_sale_date": "Mapped from 'saledate' in Table B to the date of the last sale.",
                "land_value": "Derived from 'taxablelandval' in Table B, indicating assessed land value.",
                "improvement_value": "From 'taxableimpsval' in Table B, showing appraised improvement value.",
                "total_value": "Mapped from 'totalappraisedvalue' in Table B to the total appraised value of the parcel.",
                "tax_account_number": "Derived from 'acctnbr' in Table B, representing a unique tax account identifier.",
                "plsss_quarter_section": "From 'quartersection' in Table B, indicating the quarter section within PLSS.",
                "plss_section": "Mapped from 'section_' in Table B to the specific section in PLSS.",
                "plss_township": "Derived from 'township' in Table B, showing the township within PLSS.",
                "plss_range": "From 'range' in Table B, indicating the range within PLSS.",
                "legal_description": "Mapped from 'legaldescnew' in Table B to the legal description of the parcel.",
                "parcel_number_alternate": "Mapped from cama_id in Table B, likely represents a unique identifier for the parcel, but parcel_number already mapped."
            }
        }
"""
