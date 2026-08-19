from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    yaguven_exige_autoriza_nc = fields.Boolean(
        string="Las notas de crédito de venta las confirma un autorizante",
        default=False,
        help="Si está activo, cualquier usuario puede cargar la nota de crédito "
        "de venta en borrador, pero sólo la confirma quien tenga el permiso "
        "«Autoriza notas de crédito».",
    )
