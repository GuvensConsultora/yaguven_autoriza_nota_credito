from odoo import _, models
from odoo.exceptions import UserError

_GRUPO_AUTORIZANTE = "yaguven_autoriza_nota_credito.group_autoriza_nota_credito"
_TIPOS_CONTROLADOS = ("out_refund",)


class AccountMove(models.Model):
    _inherit = "account.move"

    def _post(self, soft=True):
        self._yaguven_verificar_autorizacion_nc()
        return super()._post(soft=soft)

    def _yaguven_verificar_autorizacion_nc(self):
        """Frena la confirmación de notas de crédito de venta sin autorización.

        Corre antes de postear, así el comprobante queda intacto en borrador y el
        autorizante lo encuentra listo para revisar.
        """
        if self.env.su:
            return
        if self.env.user.has_group(_GRUPO_AUTORIZANTE):
            return
        bloqueadas = self.filtered(
            lambda movimiento: movimiento.move_type in _TIPOS_CONTROLADOS
            and movimiento.company_id.sudo().yaguven_exige_autoriza_nc
        )
        if not bloqueadas:
            return
        raise UserError(
            _(
                "Las notas de crédito de venta las confirma únicamente un usuario "
                "autorizado.\n\n"
                "Podés dejarla cargada en borrador y avisarle para que la revise:\n"
                "%(comprobantes)s",
                comprobantes="\n".join(
                    "· %s" % movimiento.display_name for movimiento in bloqueadas
                ),
            )
        )
