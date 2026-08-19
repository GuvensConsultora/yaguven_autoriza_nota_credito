{
    "name": "Autorización de notas de crédito",
    "summary": "La nota de crédito de venta la carga cualquiera, pero sólo la confirma quien está autorizado",
    "description": """
Autorización de notas de crédito
================================

Una nota de crédito de venta anula o reduce una factura ya emitida: el
comprobante sale con CAE y el saldo del cliente cambia. En la práctica suele
cargarla quien atiende el mostrador, pero la decisión de emitirla es de quien
lleva la cuenta.

Este módulo separa las dos cosas. **Cargar** la nota de crédito en borrador sigue
siendo libre para cualquier usuario de facturación: se prepara completa, con
cliente, líneas e importes. **Confirmarla** queda reservado al grupo
*Autoriza notas de crédito*; quien no lo tenga recibe un aviso y la deja en
borrador para que el autorizante la revise.

El control se prende por compañía desde la ficha de la compañía, y nace apagado:
mientras nadie lo active, ninguna nota de crédito cambia de comportamiento.

Alcance
-------

Alcanza únicamente a las **notas de crédito de venta**. Las de compra, las
facturas y los asientos manuales no se tocan.

Tener presente que anular una factura de venta por reversión también genera una
nota de crédito de venta, de modo que esa anulación queda bajo la misma llave.
""",
    "author": "Yagüven C.G.",
    "website": "https://yaguven.com",
    "category": "Accounting/Accounting",
    "version": "19.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["account"],
    "data": [
        "security/autoriza_nota_credito_groups.xml",
        "views/res_company_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
