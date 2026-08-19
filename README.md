# Autorización de notas de crédito

Módulo de Yagüven C.G. para Odoo 19.

Separa **cargar** una nota de crédito de venta de **confirmarla**.

- Cualquier usuario de facturación la carga en borrador, completa.
- Sólo quien tenga el permiso *Autoriza notas de crédito* puede confirmarla.
- Quien no lo tenga recibe un aviso y el comprobante queda intacto en borrador.

## Configuración

1. **Ajustes → Usuarios y compañías → Compañías**, abrir la compañía y activar
   *«Las notas de crédito de venta las confirma un autorizante»*. Nace apagado:
   mientras nadie lo prenda, nada cambia.
2. **Ajustes → Usuarios y compañías → Usuarios**, en el usuario autorizante
   elegir *Autorizaciones → Autoriza notas de crédito*.

## Alcance

Sólo notas de crédito de **venta** (`out_refund`). Las de compra, las facturas y
los asientos manuales no se tocan.

Anular una factura de venta por reversión genera una nota de crédito de venta, de
modo que esa anulación también queda bajo la misma llave.

## Verificación

- Con un usuario sin el permiso, cargar una nota de crédito de venta y apretar
  *Confirmar*: aparece el aviso y el comprobante sigue en borrador.
- Con el autorizante, abrir esa misma nota de crédito y confirmarla: postea normal.
- Con el control apagado en la compañía, cualquiera confirma como antes.
