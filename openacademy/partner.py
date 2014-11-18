from openerp.osv import osv, fields

class res_partner(osv.osv):
    
    _name = "res.partner"
    _inherit = "res.partner"
    _columns= {
            'is_instructor': fields.boolean('Is Instructor'),
            'session_ids': fields.one2many('openacademy.session', 'instructor_id', string='Sesions'),
                        
        }
    _defaults = {
            'is_instructor': False, 
        }