from openerp.osv import osv, fields

class solution(osv.osv):
    _name = "solution.solution"
    _description = "This table is for keeping personal data of solution"
    _columns = {
        'name': fields.char('Solution Name',size=256,required=True),
        'bom':fields.selection([('bom1','BOM1'),('bom2','BOM2')],'BOM'),
		'product_category':fields.selection([('category1','Category1'),('category2','Category2')],'Product Category'),
		'product_name':fields.selection([('product1','Product1'),('product2','Product2')],'Product'),
        'bom_create_date':fields.datetime('Create Date', readonly=True, select=True, help="Date on which sales order is created."),
		'comprobante_fname': fields.char('URL', size=64, readonly=True),
		'comprobante': fields.binary(string='URL BOM', size=256), #, filters='*.pdf'),
		'properties': fields.one2many('solution.solution_lines', 'solution_lines', 'Solution Lines'),
    }

_defaults = {
    'comprobante_fname': 'comprobante.pdf',
}

solution()

class solution_lines(osv.osv):
    _name = "solution.solution_lines"
    _description = "Solution Lines"
    _columns = {
		'product_name':fields.selection([('product1','Product1'),('product2','Product2')],'Product'),
        'bom_create_date':fields.datetime('Create Date', readonly=True, select=True, help="Date on which sales order is created."),
		'comprobante_fname': fields.char('URL', size=64, readonly=True),
		'comprobante': fields.binary(string='URL BOM', size=256), #, filters='*.pdf'),
        'solution_lines': fields.many2one('solution.solution', 'Solution Lines', select=True),
    }

solution_lines()