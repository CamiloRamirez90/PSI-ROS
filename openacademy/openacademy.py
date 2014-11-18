from openerp.osv import osv, fields

class openacademy_course (osv.Model):
    _name= 'openacademy.course'
    _columns= {
            'name': fields.char('Name', size=32, required= True),
            'description': fields.text('Description'),
            'responsible_id': fields.many2one('res.users', string='Responsible'),
            'session_ids':fields.one2many('openacademy.session', 'course_id', string='Sessions'),
            
        }
    
    
class openacademy_session (osv.Model):
    _name= 'openacademy.session'
    _columns= {
            'name': fields.char('Name', size=32, required= True),
            'duration': fields.float('Duration'),
            'seats': fields.integer('Seats'),
            'course_id': fields.many2one('openacademy.course', string='Course'),
            'instructor_id': fields.many2one('res.partner', string='Instructor'),
        }
