from odoo import http
from odoo.http import request


class WebSaleOrderRepeat(http.Controller):
    @http.route('/order/repeat', type='http', auth="public", website=True)
    def repeat_sale_order(self, **kwargs):
        print("kw", kwargs)
        so_order_id = kwargs.get('id')
        print("orderid", so_order_id)
        repeat_so_order_id = request.env['sale.order'].sudo().browse(
            int(so_order_id))
        sale_order = request.website.sale_get_order(force_create=True)
        add_qty = 0
        set_qty = 0
        for line1 in repeat_so_order_id.order_line:
            if line1.product_id:
                if sale_order.order_line:
                    for line2 in sale_order.order_line:
                        if line2.product_id == line1.product_id:
                            add_qty = line1.product_uom_qty + line2.product_uom_qty
                            set_qty = add_qty
                            break
                        else:
                            add_qty = line1.product_uom_qty
                            set_qty = add_qty
                else:
                    add_qty = line1.product_uom_qty
                    set_qty = add_qty

                sale_order._cart_update(
                    product_id=int(line1.product_id.id),
                    add_qty=add_qty,
                    set_qty=set_qty,
                )
        return request.redirect("/shop/cart")
