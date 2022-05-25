class DHLExportLineItems:
    """
    A class for creating the Export line in the DHLInternationalDetail
    """

    def __init__(
            self, hs_code, quantity, item_description, unit_price, net_weight,
            gross_weight, manufactoring_country_code, quantity_unit='PCS'):
        self.commodity_code = hs_code
        self.quantity = quantity
        self.item_description = item_description
        self.unit_price = unit_price
        self.net_weight = net_weight
        self.gross_weight = gross_weight
        self.manufactoring_country_code = manufactoring_country_code
        self.quantity_unit = quantity_unit


class DHLOtherCharge:
    """
    A class for creating the Other Charge in the DHLInternationalDetail.
    """

    def __init__(
            self, caption, charge_value, charge_type):
        self.charge_caption = caption
        self.charge_value = charge_value
        self.charge_type = charge_type


class DHLInternationalDetail:
    """
    A class for creating the Export Declaration in the DHLShipment.
    """

    def __init__(
            self, invoice_date, invoice_reference_number, export_line_items,
            invoice_reference_type='OID', other_charge=None, remarks=None):
        self.invoice_date = invoice_date
        self.invoice_reference_number = invoice_reference_number
        self.invoice_reference_type = invoice_reference_type
        self.other_charge = other_charge
        self.export_line_items = export_line_items
        self.remarks = remarks
