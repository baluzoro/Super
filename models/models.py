from odoo import models,fields,api,_
class statusbar(models.Model):
    _name = 'state_validate'
    name = fields.Char('Name', required=True)
    """
    This selection field contains all the possible values for the statusbar.
    The first part is the database value, the second is the string that is showed. Example:
    ('finished','Done'). 'finished' is the database key and 'Done' the value shown to the user
    """
    state = fields.Selection([
            ('concept', 'Concept'),
            ('started', 'Started'),
            ('progress', 'In progress'),
            ('finished', 'Done'),
            ])
         
#This function is triggered when the user clicks on the button 'Set to concept'
    @api.one
    def concept_progressbar1(self):
        self.write({
            'state': 'concept',
        })

#This function is triggered when the user clicks on the button 'Set to started'
    @api.one
    def started_progressbar(self):
         self.write({
	     'state': 'started'
         })

#This function is triggered when the user clicks on the button 'In progress'
    @api.one
    def progress_progressbar(self):
         self.write({
	     'state': 'progress'
         })

#This function is triggered when the user clicks on the button 'Done'
    @api.one
    def done_progressbar(self):
         self.write({
	     'state': 'finished',
         })

class Relatives(models.Model):
    _name = 'custom_employee.relatives'
    name = fields.Char(string='Name')
    gender = fields.Selection([('m', 'Male'),('f', 'Female')],default='m')
    relative_relationship = fields.Selection(selection='change_relatives')

    @api.multi
    @api.onchange('gender')

    def change_relatives(self):
        if self.gender == 'm':
          self.relative_relationship.Selection=fields.Selection([('s','Son'),('h', 'Husband'),('f','Father')], default='s',string='Relative Relationship')
        elif self.gender == 'f':
            self.relative_relationship=fields.Selection([('d','Daughter'),('w', 'Wife'),('m', 'Mother')], default='d',string='Relative Relationship')    
